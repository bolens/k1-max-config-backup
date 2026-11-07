# Backup delivery playbook

[Documentation](docs/README.md)

This repository is a continuously updated K1 Max configuration backup. It has
no versioned releases; immutable Git commits are recovery points.

## Prepare and validate

Capture only intended printer configuration. Exclude credentials, network
identifiers, transient logs, caches, generated jobs, and unrelated runtime
state. Review the complete diff and validate syntax with the producing firmware
and Klipper versions. Record hardware modifications and firmware assumptions.

## Review, deliver, and verify

Use a pull request and squash merge to protected `main`; do not push backups
directly. Confirm CI passes and the merged files parse independently of the live
printer. Delivery does not authorize restoring them to hardware.

## Recover

Preserve current printer files before an authorized restore. Select a commit
compatible with the exact hardware and firmware, apply through the documented
recovery path, and verify heaters, axes, endstops, macros, and safety limits
before printing.

Fleet policy: <https://github.com/bolens/.github/blob/main/RELEASING.md>.

## Branch protection

The default branch requires pull requests, resolved conversations, linear
history, and an up-to-date branch with passing required checks, including
`Development environment` and `ci/woodpecker/pr/woodpecker`. These rules also apply
to administrators;
force pushes and branch deletion are disabled. Zero approving reviews are
required because this is a solo-maintainer repository; review the complete diff
before merging.

Keep required checks available on every pull request. Filter expensive work
inside jobs or use an always-running result job that rejects failures and
cancellations. Update the protection settings when renaming required jobs.

## Source lint

Woodpecker's `development-environment` step checks maintained Markdown with the
patterns in [`scripts/check-development.sh`](scripts/check-development.sh).
Keep coverage for the scope recorded in [`.github/source-lint.json`](.github/source-lint.json)
when adding documentation. The duplicate hosted
[Source lint workflow](.github/workflows/source-lint.yml) and its required context
are retired. Keep `ci/woodpecker/pr/woodpecker` and every retained current-head
check required; the [CI index](docs/woodpecker-transition.md) maps local commands
and native ownership.

Use the CI index's local entrypoints in the locked development environment.
Review the maintained-file scope when adding documentation; generated and
imported files retain their native validation. Retained platform, artifact,
deployment and release checks keep their existing authority.

## Woodpecker validation

[The transition contract](docs/woodpecker-transition.md) runs the existing locked
Linux development check on Woodpecker. Require actual native PR and merged-main
success before retiring duplicate hosted work. Preserve platform-specific, real
Docker, and administrative checks until equivalent replacement is verified.
This automation change does not deploy printer changes or create a release.
