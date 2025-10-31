# Contributing Guidelines

## Safety & Data Hygiene
- Never commit production credentials or personally identifiable information.
- Scrub example values so they are clearly synthetic.

## Code Style
- Prefer small, composable functions and explicit naming over clever abstractions.
- Keep modules importable without side effects.
- Document interfaces with docstrings, including rationale for design decisions.

## Testing Expectations
- Add or update unit tests for every functional change.
- Run `pytest` locally before opening a pull request.
- Include smoke tests that exercise new public interfaces.

## Documentation
- Update `docs/PROJECT_STATUS.md` with roadmap adjustments or run log entries.
- Provide user-facing documentation whenever behavior changes.

## Pull Requests
- Summarize context, plan, acceptance criteria, and references in the PR body following the template in `AGENTS.md`.
- Ensure automated checks pass and link to relevant issues or discussions when applicable.
