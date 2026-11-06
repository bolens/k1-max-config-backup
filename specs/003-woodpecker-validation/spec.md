# Woodpecker Linux validation

## Requirement

Run the existing locked development gate on the shared Woodpecker CI site for
pull requests, main pushes, and manual validation. This changes automation only.

## Acceptance

- Clone the complete tested source with an immutable plugin.
- Run the existing `devenv test` and committed lock in an unprivileged container.
- Do not expose publication secrets, host services, or private runtime state.
- Keep existing GitHub checks until genuine native PR and main success.
- Preserve macOS, actual Docker, distinct lint, and administrative coverage.
- Review compatible devcontainer updates together and align Node and smoke.
- Build the updated devcontainer and run its isolated post-create smoke on the
  retained hosted Linux lane, including devcontainer-only PRs.
- Record exact source and pipeline identity; recover through a corrective PR.

No hardware configuration or live printer operation is part of this work.
Synthetic plotting checks do not prove printer safety.
