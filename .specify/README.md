# .specify Folder

This folder contains Spec-Kit Plus configuration and templates for the LifeStepsAI Todo Application.

## Structure

```
.specify/
├── memory/              # Project memory and constitution
│   └── constitution.md  # Core principles and standards
├── templates/           # Document templates
│   ├── phr-template.prompt.md     # Prompt History Record template
│   ├── spec-template.md           # Specification template
│   └── adr-template.md            # Architecture Decision Record template
└── README.md           # This file
```

## Memory

The `memory/` folder contains the project's foundational documents:

- **constitution.md**: Defines non-negotiable principles, code standards, and governance

## Templates

The `templates/` folder contains reusable templates for:

- **PHR (Prompt History Records)**: Document development sessions
- **Specifications**: Feature and requirement documentation
- **ADR (Architecture Decision Records)**: Document significant decisions

## Usage

Templates are used by Spec-Kit Plus and Claude Code for:

1. Creating consistent documentation
2. Recording development history
3. Maintaining spec-driven development workflow

## Constitution

The constitution (memory/constitution.md) is the **authoritative source** for:

- Development methodology (SDD + TDD)
- Code quality standards
- Testing requirements
- Project constraints
- Amendment process

All code must comply with the constitution. Violations will not be merged.

## Version

- **Spec-Kit Version**: Plus (with extended features)
- **Constitution Version**: 1.0.0
- **Last Updated**: 2025-12-07
