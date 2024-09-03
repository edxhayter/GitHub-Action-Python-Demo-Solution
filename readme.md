# Intro to GitHub Actions

**The Master Branch is arranged as a starter file - created workflow.yml files will be created in a separate dev branch.**

This repository is what I use for my intro to GitHub Actions session. Included in the documentation section is a copy
of the slides I run the session with explaining the basics of GitHub Actions, the components of an action and a few
example use cases for a GitHub Action. The rest of the repository is for the demo part of the session - the repository
should be forked and then the session participants should build out the Action alongside the instructor.

## Project Contents

- Main.py 
  - this is our simple Python script that queries the corporate buzzword API and writes the response to a text file. 
- requirements.txt
  - this is a text file that outlines all the packages that are required for the project. This will be
  used in the action to install all the script dependencies and allow it to run on a runner.
- Extension.py
  - This is a more advanced Python script that queries the API and creates a Google calendar event with the title of the API response. This script is more advanced as it will involve providing secrets for the Action in a secure way.

## Main.py Workflow.yml

### Code:

### Breakdown:

## Extension.py Workflow.yml

