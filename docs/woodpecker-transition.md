# Woodpecker validation transition

Run the existing locked `devenv test` in a disposable Linux container on the
shared CI site. Use digest-pinned clone/runtime images and the pinned devenv
CLI with the repository lock. No publishing credentials, privileged mode, host
Docker socket, or host Nix store are provided.

## Acceptance and delivery

1. Verify the genuine current-head native PR result alongside existing checks.
2. Squash the reviewed source through a normal PR without bypassing protection.
3. Verify the genuine merged-main pipeline and its exact source revision.
4. Retire only proven duplicate Linux work after required-check settings agree.
   Preserve macOS, actual Docker and administrative workflows.

Recover through a corrective or revert PR. Re-enable a retired hosted fallback
and verify its current-head result before migrating protection during recovery.

Review the Woodpecker image pins monthly and after
security releases; existing dependency automation does not discover these YAML
image references. Updates need a reviewed PR and actual native execution.

These are offline tooling and synthetic plotting checks. They do not connect,
flash, restart, heat, home, or move a printer, and do not prove hardware safety.
No printer configuration or retained recovery archive changes in this rollout.

## Devcontainer updates

Compatible open image updates are reviewed together with their Node smoke
contract. The retained hosted Linux lane builds the actual `.devcontainer`
Dockerfile and runs its post-create smoke with a read-only root filesystem,
no network, and the runner UID. The task checkout remains writable as required
by setup. The path filter includes devcontainer changes. A native Nix gate alone
does not prove the selected devcontainer image builds or works.

## Linux check ownership

Following accepted native PR and merged-main checks, Woodpecker owns the
locked Linux `devenv test` check. The hosted matrix keeps the macOS check and
actual Docker development and VS Code devcontainer builds on Linux. Keep
the native PR context required on each current-head PR. Recover through a reviewed
revert or corrective PR if the native runner becomes unavailable.

The compatible Spec Kit update advances the managed integration to version
1.3.2. Project-owned guidance, retained specifications, CI locks and pipeline
configuration are preserved; imported managed files retain manifest validation.
The retired `taskstoissues` skill is removed after its original managed hash is
verified; the remaining generated skill and script contents match version 1.2.6.

## Nix compatibility and warning checks

Use devenv 2.4.0 at the reviewed CLI commit and the locked nix2container
revision. Keep the existing git-hooks inputs explicit when upgrading the CLI.
The disposable Nix image retains its standard `nixbld` build users; builds
must not run as root or create the `/homeless-shelter` placeholder. The container
helper places `--registry` on the `copy` subcommand, as required by this CLI.

Accept flake configuration only on the immutable CLI invocation. Its reviewed
configuration adds the two official public caches and their signing keys. Do
not enable global acceptance of arbitrary repository flake configuration.
Require real native PR and main execution, plus the retained actual Docker
image check, before accepting the upgrade; platform and cache warnings must
be absent.

## Portable workflow security

The locked native development gate now requires `actionlint` and offline
`zizmor` at medium severity and confidence. Both tools were already provided
by the development environment. Their failures propagate through
`scripts/check-development.sh` and `devenv test`; focused tests execute that
entry point with inert tools to verify both failure paths.

This replaces no printer, macOS, Docker/editor or Spec Kit update behavior.
The duplicate hosted Workflow checks and Source lint workflows and their
requirements are retired following accepted native PR/main checks. Keep
`ci/woodpecker/pr/woodpecker` and `Development environment` required; the native
gate retains actionlint, zizmor and Markdown checks.

## CI discovery index

Use the [shared CI vocabulary](https://github.com/bolens/.github/blob/main/docs/woodpecker-transition.md#ci-organization):
`validate`, `test`, `site` and `publish` identify purpose, with descriptive
subgroups. These labels preserve existing workflow and protected-status names.

| Phase / group | Local command | Current native owner |
| --- | --- | --- |
| `validate` / development | `devenv test` (`scripts/check-development.sh` is the canonical check sequence) | `woodpecker` / `development-environment` |
| `validate` / Markdown | `markdownlint-cli2` with the patterns in `scripts/check-development.sh` | Included in `development-environment` |
| `validate` / workflow security | `actionlint` and `zizmor --offline --min-severity medium --min-confidence medium .github` | Included in `development-environment` |
| `test` / fixture regressions | `python3 -m unittest discover -s tests -p test_workflow_security.py -v` | Included in `development-environment` |

The existing native PR context is `ci/woodpecker/pr/woodpecker`. Keep that name
until a coordinated fleet change updates pipeline names, required checks and
documentation together. Purpose labels describe coverage; the existing
canonical command and pipeline name remain unchanged.

The hosted development workflow still owns macOS and any actual Docker/editor
checks selected there. Forge assignment, labels and Spec Kit update automation
remain separate from these portable validation groups. The duplicate hosted
Source lint and Workflow checks producers are retired. Require fresh native PR/main
proof and coordinated settings before retiring any additional producer.
