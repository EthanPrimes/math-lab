---
name: move-function-to-core
description: Workflow for moving a function out of a testing environment and into the appropriate core/ file. Used when a function needs to be promoted, moved to core, or graduated from a notebook.
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, NotebookEdit
---

# Move Function To Core

The primary goal of this workflow is to take the final draft of a function and move it into the core/ file where it can be easily called. The secondary goals include sprucing up the docstring, writing tests, and validating that all doctests and pytests pass.

## Inputs

- <function_name> - Required: the user names it in the prompt.
- <module> - Required: a file in core/ (e.g. "primes" -> "core/primes.py").
- <source_location> - Optional: the source of the function to move. If not included, grep the repo to find the definition.

## Steps

1. Locate the function definition, which will likely be in a .ipynb file within notebooks/ unless otherwise specified.
2. Choose the target core module and determine where in it the function belongs.
3. Move the function to the appropriate space and verify that imports and dependencies are adjusted. Add a one-line entry for the function to the "Includes:" list in the module docstring at the top of the file.
4. Fill out any missing sections in the docstring. The following sections must be included:
  - First, a brief summary of the function.
  - Second, a more in-depth explanation of what the function does and how its implementation works.
  - An "Args:" section, unless the function has no arguments.
  - A "Returns:" section, unless the function does not return anything.
  - A "Raises:" section, unless the function does not raise anything.
  - An "Examples:" section, which should consist of at least two happy path outputs. This should be able to be run as a doctest.
5. Write tests in tests/test_<module>.py. Follow the conventions of previously written test functions.
6. Update all call sites in the repo to import the function from the core.

## Verification

- Run the doctests within the appropriate module: `python -m pytest --doctest-modules core/<module>.py -q`
- Run the unit tests: `python -m pytest tests/test_<module>.py -q`
- Report success of the tests, and report any failures of the tests before making any corrections. Wait for user input before attempting to fix broken tests.

## Conventions / Notes

- Remember that all functions should have type hints, should validate that their input is of the appropriate type, and should be written Pythonically.
- Do not modify the original function that was copied, and do not delete any other drafts of the function, unless instructed to do so.
- If any part of a function could be easily improved (e.g. a simpler or more informative name, a bug, a speedup, etc.), note the recommended changes and wait for user validation before continuing.
- As a general rule of thumb, your goal is to validate the user's function, not rewrite it from scratch. Share your suggestions, stating why you recommend each one, and default to using the function as-is when the user specifies that you should do so.
- If a core/<module>.py file is getting too long (> 1000 lines), inform the user and come up with a plan to shorten or split the file. Wait for user validation before acting on the plan.
