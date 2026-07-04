#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import shutil

SRC = Path.home() / ".agents"
OUT = SRC / "generated-codex"
CODEX_AGENTS = Path.home() / ".codex" / "agents"
STATE_FILE = OUT / ".sync-state.json"

GENERATOR_VERSION = "3"


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def toml_quote(value):
    return json.dumps(value)


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {}


def save_state(state):
    OUT.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def parse_agent(path):
    text = path.read_text(encoding="utf-8")
    name = path.stem
    description = ""
    instructions = text.strip()

    if text.startswith("---"):
        try:
            _, front, body = text.split("---", 2)
            instructions = body.strip()

            for line in front.splitlines():
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")

                if key == "name":
                    name = value
                elif key == "description":
                    description = value
        except ValueError:
            pass

    return {
        "name": name,
        "description": description,
        "developer_instructions": instructions,
        "source": path.name,
    }


def render_toml(agent):
    return f"""# Generated from {agent["source"]}. Do not edit directly.

name = {toml_quote(agent["name"])}
description = {toml_quote(agent["description"])}

developer_instructions = {toml_quote(agent["developer_instructions"])}
"""


def ensure_codex_symlink():
    CODEX_AGENTS.parent.mkdir(parents=True, exist_ok=True)

    if CODEX_AGENTS.is_symlink():
        if CODEX_AGENTS.resolve() == OUT.resolve():
            return
        CODEX_AGENTS.unlink()

    if CODEX_AGENTS.exists():
        backup = CODEX_AGENTS.with_name("agents.backup")
        if backup.exists():
            shutil.rmtree(backup)
        CODEX_AGENTS.rename(backup)
        print(f"Backed up existing Codex agents dir to {backup}")

    CODEX_AGENTS.symlink_to(OUT, target_is_directory=True)
    print(f"Linked {CODEX_AGENTS} -> {OUT}")


def output_path_for(md_path):
    return OUT / f"{md_path.stem}.toml"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ensure_codex_symlink()

    old_state = load_state()
    old_files = old_state.get("files", {})
    new_files = {}

    generated = 0
    skipped = 0

    agent_files = sorted(p for p in SRC.glob("*.md") if p.is_file())
    print(f"Found {len(agent_files)} Markdown agent file(s).")

    for md in agent_files:
        text = md.read_text(encoding="utf-8")
        agent = parse_agent(md)
        rendered = render_toml(agent)
        out_path = output_path_for(md)

        source_hash = sha256(text)
        output_hash = sha256(rendered)

        new_files[md.name] = {
            "source_hash": source_hash,
            "output_hash": output_hash,
            "output": out_path.name,
            "generator_version": GENERATOR_VERSION,
        }

        old_entry = old_files.get(md.name, {})

        unchanged = (
            old_entry.get("source_hash") == source_hash
            and old_entry.get("output_hash") == output_hash
            and old_entry.get("generator_version") == GENERATOR_VERSION
            and out_path.exists()
        )

        if unchanged:
            skipped += 1
            continue

        out_path.write_text(rendered, encoding="utf-8")
        generated += 1

    valid_outputs = {entry["output"] for entry in new_files.values()}

    removed = 0
    for toml in OUT.glob("*.toml"):
        if toml.name not in valid_outputs:
            toml.unlink()
            removed += 1

    save_state({
        "generator_version": GENERATOR_VERSION,
        "files": new_files,
    })

    print(f"Generated: {generated}")
    print(f"Skipped unchanged: {skipped}")
    print(f"Removed stale: {removed}")
    print(f"Codex agents directory: {CODEX_AGENTS}")


if __name__ == "__main__":
    main()
