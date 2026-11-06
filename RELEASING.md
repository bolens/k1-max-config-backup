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
history, and an up-to-date branch with passing required checks, including `lint
/ actionlint` and `lint / zizmor`. These rules also apply to administrators;
force pushes and branch deletion are disabled. Zero approving reviews are
required because this is a solo-maintainer repository; review the complete diff
before merging.

Keep required checks available on every pull request. Filter expensive work
inside jobs or use an always-running result job that rejects failures and
cancellations. Update the protection settings when renaming required jobs.

## Source lint

The Source lint workflow checks maintained markdown files selected by
[`.github/source-lint.json`](.github/source-lint.json) on every pull request
and push to `main`. Existing native checks remain part of the merge gate.
Use the [shared local reproduction instructions](https://github.com/bolens/.github/blob/7603518f305fb76f7bb1b9979f2692521f633b82/docs/source-lint.md)
with the same tooling revision pinned in
[the workflow](.github/workflows/source-lint.yml). Review exclusions when adding
source files; generated and imported files retain their native validation.
Require the new check to pass on the current PR head before merging.

## Woodpecker validation

[The transition contract](docs/woodpecker-transition.md) runs the existing locked
Linux development check on Woodpecker. Require actual native PR and merged-main
success before retiring duplicate hosted work. Preserve platform-specific, real
Docker, and administrative checks until equivalent replacement is verified.
This automation change does not deploy printer changes or create a release.
