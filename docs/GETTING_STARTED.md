# Learn with Computor

Read the three course manifests in [the course map](../COURSE_MAP.md), then open an
example's `content/index_de.md` or `content/index_en.md`. Reading the published
material requires no account. Public input files and student templates are
included. Instructor solutions and private grading tests are kept separately.

## Desktop VS Code

Install Python 3.12 and VS Code. Clone this repository and open its folder. Install
the **Computor** and **Hackl** extensions from publisher `computor-org`. In a Python
virtual environment, install `requirements.lock` using
`python -m pip install --require-hashes -r requirements.lock`.

Copy an example's student templates, when provided, into a working folder together
with the input files described by its assignment. Other exercises ask you to create
your own script or functions from scratch. Run your code locally. The exercises are
unfinished tasks; their templates are not expected to pass private grading tests.
The repository environment check is `python -m pytest tests`.

## GitHub Codespaces

[Create a Codespace](https://codespaces.new/computor-org/data-science-python?quickstart=1).
A GitHub account is required and GitHub's quota and billing apply. Code runs in
your Codespace rather than on Computor's servers. The devcontainer installs Python
dependencies and recommends Computor and Hackl. It disables Hackl's managed model
engine and inline completion. It never installs an inference model.

Configure Hackl with an external OpenAI-compatible **HTTPS** endpoint and model.
Use **Hackl: Set API Key** for your provider key; VS Code SecretStorage stores it.
Keep keys out of repository files, settings and commits. The external provider
receives your prompts and the selected code/context; its own usage terms apply.
Desktop learners may instead use a local model server.

## Tutor and authenticated course tools

Computor course mode uses Ask-only: hints, explanations and review of reasoning.
It disables writes, shell commands, MCP and inline completion. Independent-check
mode disables all AI assistance. Open **Computor: Open Tutor** after activating a
course. Install the current Hackl version for the course policy API.

Computor login is needed for enrolled-course progress, submissions and server
grading. These remain authenticated even though reading and local practice are
public. The current Computor Marketplace extension supports both the stable 26.10
backend and main/27.3. A full hosted workspace does not stop local practice:
**Computor: Public Courses** always offers desktop VS Code and Codespaces.

Ask-only is a teaching rule in your editor. It cannot turn a learner-controlled
editor into a secure exam environment or guarantee what an external model says.
