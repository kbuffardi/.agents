---
name: infra-setup
description: Sets up the infrastructure for a new project according to a documented plan in README.md and verifies its internal compatibility.
---

# Infrastructure Setup

## Purpose

Help a developer create the foundational infrastructure for a greenfield project. This skill will read the `README.md` at the repository root, extract the infrastructure plan, and implement it in a new project. It will also verify that the selected technologies are compatible with each other and with the platform, connectivity, storage, testing, and analysis decisions made in the plan.

## Guardrails

This skill is a setup tool only. It must install, configure, containerize, test, check, and deploy the infrastructure described in the `README.md` plan. It must not make any infrastructure decisions that changes the plan. It must not implement any application features, business logic, or user interface. It must not perform any actions that are not explicitly described in the plan.

## Setup Steps

1. Read the `README.md` at the repository root and extract the infrastructure plan from the `## Infrastructure` section, including its subsections (`### Development Tools` and `### CI/CD`).
2. Create or update a `.gitignore` file to exclude any files or directories that should not be committed to the repository, such as local development artifacts, temporary files, and sensitive credentials. The `.gitignore` file should be consistent with the selected technologies and tools in the plan.
3. Create a containerized development environment that includes all required technologies, tools, and services described in the plan.
4. Verify that the selected technologies are compatible with each other within the containerized environment and with the platform, connectivity, storage, testing, and analysis decisions made in the plan.
5. Document any incompatibilities or missing technologies in response to the developer, and provide guidance on how to resolve them. For example, if unnamed dependencies are required for a selected technology, notify the developer of a list of the dependencies inferred. If a selected technology is incompatible with another selected technology, provide a brief explanation of the conflict and suggest alternative technologies that would be compatible with the rest of the plan.
6. Create GitHub Actions workflows for pull requests and releases that implement the CI/CD plan described in the `README.md` plan.
7. Verify that the workflows run successfully locally (e.g., using `act`) and that they perform the required checks, tests, and deployment. If checks, tests, or deployment involves communicating with a third-party service such as a web host or requires secrets that are not yet set, do not require them to succeed before proceeding; in those cases, advise to the developer that manual configuration is necessary to get the workflow to function. Create smoke tests to verify that the major components of the infrastructure are integrating correctly, such as the database connection, endpoints, and frontend rendering.
8. Update the `README.md` with a section `## Getting Started` that provides concise instructions for developers to set up the development environment, including any manual installation steps for required technologies not supplied by Docker and any configuration steps for the containerized environment and GitHub Actions workflows. For steps that involve installing third-party software, provide links to the official documentation or download pages. For steps that involve configuring the containerized environment or GitHub Actions workflows, provide example commands or configuration files that developers can use as a starting point.
9. Update the `README.md` with a section `## Commands` after the Getting Started section that describes commands for building, testing, and running the application in the containerized environment, as well as any commands for interacting with the GitHub Actions workflows.


## Guiding principles

- Assume the project is a greenfield project with no existing infrastructure or configuration. Refuse to begin if the repository already contains infrastructure or configuration files that conflict with the plan.
- Assume the project will be managed with Git and hosted on GitHub as a monorepo. Refuse to begin if the repository is not a Git repository or is not hosted on GitHub.
- The Infrastructure plan in the `README.md` must be complete, accurate, and the source of truth for this skill. Refuse to begin setup if the plan is missing.
- When choosing versions of technologies, assume that the latest stable versions are preferred unless the plan specifies otherwise or if version incompatibilities are discovered during verification.
- Make incremental git commits for each step of the setup process that makes any file changes, with clear commit messages that describe the purpose of the changes made.