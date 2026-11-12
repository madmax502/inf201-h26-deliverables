# Deliverable 3 - Battle simulator

Authors: Max Carl Andresen and Sam Mirtaheri.

Repository: https://github.com/madmax502/inf201-h26-deliverables

A small turn-based RPG battle simulator built on the `Character` class from
lecture 08 (`game_simulator_v1.py`). Characters can carry a weapon whose
damage is decided by a dice roll, and can specialise as a `Warrior` or a
`Mage`. A `Battle` object lets two characters fight until one of them wins.

## Run the notebook

Use Python 3.12 and a separate virtual environment for this deliverable.
Run these commands from `Deliverable_3/`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open `Deliverable_3.ipynb`, select `.venv/Scripts/python.exe` as the kernel,
and run all cells from the top. The modules only use the Python standard
library. The random seed is fixed, so the results are the same every time.

## Files

- `game_simulator_v2.py`: `Character`, `Warrior` and `Mage` (Task 1, 3, 4).
- `dice.py`: `Dice` (Task 2).
- `items.py`: `Weapon` (Task 3).
- `battle.py`: `Battle` (Task 5).
- `Deliverable_3.ipynb`: presentation of each class, simulated battles and
  discussion of the results.
- `requirements.txt`: pinned notebook dependencies; Python 3.12.
- `ai_bruk.md`: description of AI use in English.

The submission also contains a PDF of the notebook, a PDF of `ai_bruk.md` and
a Git commit-log snapshot. These submission-only files are kept outside the
repository.

## Collaboration

We meet in person and write the code together on one computer. Both group
members contribute to solving the tasks. Because we use one computer and Git
account, the commits are recorded under one person even though the work is
shared.
