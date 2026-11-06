# Implementation plan

The repository owns the pipeline and transition/release documentation. Reuse the
pinned Nix image, pinned devenv CLI, existing lock, and actual enterTest command.
Keep fork approval and all trust flags disabled at the CI site.

Validate workflow syntax/security, documentation and native tooling checks.
Review the complete diff separately. Activate the repository, verify the
current-head native PR, squash normally, then verify genuine main. Retire only
proven duplicates through a subsequent reviewed change with aligned settings.

No product, firmware, live-host, publication-credential, or shared-workflow
interface changes are required. The existing constitution remains satisfied.

Batch the selected compatible Node and image-pin PRs into this candidate. The
retained hosted Linux lane builds the actual devcontainer and runs its setup
smoke. This evidence is distinct from the locked native Nix validation.
