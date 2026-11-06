# Documentation

K1 Max configuration, modular macros, and recovery ownership.

## Start here

| Need | Owning document |
| --- | --- |
| Use the project | [README.md](../README.md) |
| Change the repository | [AGENTS.md](../AGENTS.md) |
| Deliver or recover | [RELEASING.md](../RELEASING.md) |
| Plan substantial changes | [.specify/memory/project-guide.md](../.specify/memory/project-guide.md) |
| Non-negotiable constraints | [.specify/memory/constitution.md](../.specify/memory/constitution.md) |

## Architecture

[printer.cfg](../printer.cfg), [printer parameters](../printer_params.cfg), and included
[macros](../macros) describe this CoreXY machine. Dated snapshots retain recovery context. Trace the
active includes before changing motion, sensorless homing, probing, or thermal assumptions. Ender
Cartesian calibration is not a portable default.

## Deployment and recovery

[RELEASING.md](../RELEASING.md) owns backup delivery and rollback planning. Static checks do not
prove hardware safety. Keep the known-good configuration and establish an operator-controlled
verification sequence before applying changes.

## Database and state

[Moonraker configuration](../moonraker.conf) describes integration with runtime services. Their
databases, logs, and credentials are separate from the tracked configuration. Preserve snapshots
without claiming they constitute a verified restore of all printer state.

## Documentation maintenance

Keep decisions, invariants, failure modes, and recovery requirements in the owning document. Link to
commands, defaults, schemas, and generated catalogs instead of copying them. Change the owner and
affected references together. Update this index when adding or moving a guide, and verify relative
links and heading anchors. Historical specs and audits describe their recorded revision, not current
runtime proof. A topic without an implementation stays explicitly unimplemented.

## Topic guides

- [Development environments](development-environments.md)

- [Editor setup](../.vscode/README.md)
- [License scope and attribution](../THIRD_PARTY_NOTICES.md)
- [Development container](../.devcontainer/README.md)

- [Woodpecker validation transition](woodpecker-transition.md)
