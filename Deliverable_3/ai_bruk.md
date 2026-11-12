# Use of Generative AI - Deliverable 3

**Max Carl Andresen and Sam Mirtaheri** - INF201, autumn 2026

We used Claude Code (Anthropic) as a support tool in Deliverable 3.

## What we used AI for
- **Virtual environment:** AI set up a separate `.venv` and a
  `requirements.txt` for this deliverable.
- **PEP 8 and small improvements to the modules:** AI fixed small PEP 8
  deviations: long lines, a missing space after `#`, whitespace on empty
  lines, blank lines and missing module docstrings. It also made some small
  changes:
    - `__repr__` and `__str__` now show the actual class name, for example
      `Warrior` instead of `Character`.
    - `Battle` has a class docstring and a `__repr__`.
    - `take_damage()` and `heal()` raise a `ValueError` for negative amounts.
      Without this check, `take_damage(-50)` could heal a character above
      `hp_max`.

  The notebook was run again from the top after these changes, and the
  battle results were the same as before.
- **Submission:** AI exported the notebook and this file to PDF, wrote the
  README for Deliverable 3.

## Collaboration

We meet in person and write the code together on one computer. Both group
members contribute to solving the tasks. Because we use one computer and Git
account, the commits are recorded under one person even though the work is
shared.
