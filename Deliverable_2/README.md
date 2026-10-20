# Deliverable 2 - Campus Coffee Shop

Authors: Max Carl Andresen and Sam Mirtaheri.

Repository: https://github.com/madmax502/inf201-h26-deliverables

## Run the notebook

Use Python 3.12 and a separate virtual environment for this deliverable.
Run these commands from `Deliverable_2/`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open `Deliverable_2.ipynb`, select `.venv/Scripts/python.exe` as the kernel,
and run all cells from the top. The included data can be used directly.
Running `python generate_data_for_d2.py` overwrites it with a new random dataset.
The generator comes from the course; its output path is relative to this folder.

## Files

- `Deliverable_2.ipynb`: code, executed results and discussion.
- `data/`: nine register logs and the store configuration.
- `generate_data_for_d2.py`: supplied dataset generator.
- `output/`: the four required CSV/JSON reports.
- `requirements.txt`: pinned notebook dependencies; Python 3.12.
- `ai_bruk.md`: description of AI use in English.

The submission also contains a PDF of the notebook and a Git commit-log
snapshot. These submission-only files are kept outside the repository.
The group will record and add the required video separately.
After your final commit, regenerate `git_log.txt` for submission with:

```powershell
git log --graph --pretty=format:"%h - %an, %ar : %s" > git_log.txt
```

## Collaboration

We meet in person and write the code together on one computer. Both group
members contribute to solving the tasks. Because we use one computer and Git
account, the commits are recorded under one person even though the work is shared.
