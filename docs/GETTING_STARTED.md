# Learn with Computor

Read the three course manifests in [the course map](../COURSE_MAP.md), then open an
example's `content/index_de.md` or `content/index_en.md`. Reading the public
material needs no account. Instructor solutions and private grading tests are
kept separately.

## Desktop VS Code

Install Python 3.12 and VS Code. Clone this repository, open its folder, and
install the **Computor** extension from publisher `computor-org`. In a Python
virtual environment, run `python -m pip install --require-hashes -r requirements.lock`.
Copy any supplied student template and input files into a working folder and run
your code locally. Some exercises begin from an empty file. Check the environment
with `python -m pytest tests`.

## GitHub Codespaces

[Create a Codespace](https://codespaces.new/computor-org/data-science-python?quickstart=1).
A GitHub account is required; GitHub's quota and billing apply. The devcontainer
installs the pinned Python dependencies and recommends the Computor extension.
Code runs in your Codespace, not on Computor's servers. No AI model is installed.

## Courses and Luna

Sign into Computor to join a course, keep progress, submit your work, and ask
Luna for hints or feedback in the course messages. A hosted workspace is optional:
you can continue in desktop VS Code or Codespaces when hosted capacity is full.
Luna processes questions using TU Graz's private model service and cannot run
code. Your account's course history contains the messages and submitted work
according to the platform privacy notice.
