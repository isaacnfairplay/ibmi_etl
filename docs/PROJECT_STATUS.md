# i-Series Data Warehouse Toolkit — Project Status & Roadmap

## Current Status
- **Repository maturity:** The repository only contains licensing, ignore rules, and contribution guidance—no source modules, tests, or configuration examples are present yet.
- **Architecture readiness:** High-level architecture expectations are captured in `AGENTS.md`, but no concrete package structure or scaffolding exists to implement them.
- **Documentation & automation gaps:** There is no developer onboarding documentation, CI configuration, or testing harness in place.

## Roadmap Overview (High-Level Phases)
1. **Phase 0 — Foundation & Governance:** Establish the project skeleton, baseline documentation, and automation required for safe iteration.
2. **Phase 1 — Connectivity & Credential Layer:** Implement the ODBC client and keyring adapter foundations, including expiry-aware handling and retries.
3. **Phase 2 — Incremental Load Pipeline:** Build query generation, staging, censor/cast, and partition merge flows to support incremental Parquet loads.
4. **Phase 3 — Linting & Validation Tooling:** Deliver SQL linting, expression sandboxing, and supporting documentation/test assets.

## Phase 0 Detailed Plan (Active Focus)
1. **Repository Scaffolding**
   - Create the `core/`, `lint/`, `configs/`, and `docs/` directories aligned with the architecture sketch.
   - Introduce minimal module files with docstrings describing intended responsibilities.
   - Define Python packaging metadata (e.g., `pyproject.toml`) and establish a consistent formatting/linting toolchain.
2. **Foundational Documentation**
   - Draft a contributor guide outlining coding standards, testing expectations, and safety guardrails referenced in `AGENTS.md`.
   - Author initial user-facing docs for project setup assumptions and configuration file conventions.
   - Add templates for future changelog entries and issue reporting.
3. **Testing & CI Bootstrap**
   - Configure unit-testing infrastructure (pytest) and type-checking (mypy or pyright) with placeholder tests.
   - Add GitHub Actions (or equivalent) workflows covering lint, type-check, and test jobs.
   - Establish baseline code coverage tracking and failure reporting mechanisms.

**Exit Criteria for Phase 0**
- Repository structure matches the architecture outline.
- Contributors have clear onboarding and safety documentation.
- Automated lint/test workflows run successfully on the scaffolded codebase.

## Next Detailed Steps (Plan Two Steps Ahead After Phase 0)
- **Step A — Implement the ODBC client abstraction** (Phase 1): Deliver connection management with DSN/full-string support, resilience features, and stubbed tests.
- **Step B — Build the keyring adapter with expiry enforcement** (Phase 1): Provide secure storage integration, rotation prompts, and unit tests covering expiry gating.

## Run Log
- 2025-10-31 — Initialized project status assessment, established roadmap structure, and created logging section per user guidance.
- 2025-10-31 — Documented progress on expiry-aware credential helpers to continue Phase 0 keyring groundwork.
- 2025-11-01 — Established Python package scaffolding, baseline interfaces, and contributor guidance to kick off Phase 0.
