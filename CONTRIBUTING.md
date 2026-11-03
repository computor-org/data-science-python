# Contributing

Exercise texts, templates and metadata under `examples/` are generated from the
private upstream source repository and are edited there, not here; see the provenance
section of the [README](README.md). Pull requests here change the course
manifests in `courses/`, the documentation, the devcontainer, the tests or the
refresh script.

1. Create a branch from `main`.
2. Set up the environment as in [Getting started](docs/GETTING_STARTED.md) and
   run the checks:

   ```bash
   python -m pip install --require-hashes -r requirements.lock
   python -m pytest -q tests
   python scripts/refresh_from_examples.py --source <checkout> --ref <ref> --check
   ```

   The last command needs a checkout of the private source repository (so only
   maintainers with access can run it) and reports generated files that are
   out of date.
3. Open a pull request against `main`. It is merged through the merge queue,
   where the required checks run.

Contributions are licensed as described in the README: MIT ([LICENSE](LICENSE))
for everything, with course texts additionally under CC BY 4.0
([LICENSE-CC-BY-4.0.txt](LICENSE-CC-BY-4.0.txt)).
