# python_for_devops_book

This repository contains my lab work from *Python for DevOps* by Noah Gift, Kennedy Behrman, Alfredo Deza, and Grig Gheorghiu.

## DevOps scripts

The [`devops_scripts/`](./devops_scripts/) project contains command-line exercises for Chapter 3:

- `exercise_1.py` checks command-line execution with Python's `sys` module.
- `exercise_2.py` uses Click to accept and validate a name argument.
- `exercise_3.py` uses Fire to expose `greet` and `add` as command-line commands.

From the `devops_scripts/` directory, install the project dependencies and run the Fire commands with:

```shell
uv sync
uv run python ch3/exercise_3.py greet --name Brandon
uv run python ch3/exercise_3.py add 2 3
```

## Change log

- **2026-11-16** — Added the `devops_scripts` project configuration and Chapter 3 command-line exercises using `sys`, Click, and Fire. Click and Fire are declared as project dependencies.
