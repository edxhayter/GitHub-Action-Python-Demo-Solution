# Intro to GitHub Actions

**The Master Branch is arranged as a solution file - the starter file without the action set upo is available in a
[separate repository](https://github.com/edxhayter/GitHub-Action-Python-Demo-Starter).**

This repository is what I use for my intro to GitHub Actions session. Included in the documentation section is a copy
of the slides I ran the session:

- Explaining the basics of GitHub Actions in the context of CI/CD 
- The components of a GitHub Action and outlining a few example use cases for a GitHub Action. 
- The rest of the repository is for the demo part of the session - the repository should be forked by the participants and the Action built together as a group.
- The final part of the session was a quiz testing retention.

## Project Contents

- Main.py 
  - this is our simple Python script that queries the corporate buzzword API and writes the response to a text file. 
- requirements.txt
  - this is a text file that outlines all the packages that are required for the project. This will be
  used in the action to install all the script dependencies and allow it to run on a runner.
- Slides used for the training session.
- The solved update repo .yml file in the .github directory.

## Main.py

### Code:
  
```python
# Import requests package
import requests

# Send GET request to the API
url = "https://corporatebs-generator.sameerkumar.website/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the generated phrase from the JSON response
    bs_phrase = response.json()["phrase"]

    # Save the phrase to a text file
    with open("corporate_bs.txt", "w") as file:
        file.write(bs_phrase)

    print("Corporate BS phrase saved to corporate_bs.txt")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

```

## Workflow.yml

```yaml
name: Update the Repo with a new Phrase

on:
  # Manual Trigger
  workflow_dispatch:

jobs:

  # Job Name
  Refresh-Phrase:

    runs-on: ubuntu-latest

    steps:
      - name: checkout repo
        uses: actions/checkout@master
        # This checks out the master branch. This does not seem to be best practice as the master branch might be subject
        # to bugs. Best practice suggests deploying the project and assigning major version numbers and then referring
        # to the major version number in the action.

      - name: install python
        uses: actions/setup-python@v4 # 'uses:' means calling an action, and has some arguments it expects specified in the 'with' below
        with:
          python-version: '3.9.13' # installs the python version developed on


        # pipe indicates a multiline command is following. The two lines that follow first ensure that pip is installed
        # and up to date. Then says read the packages from the provided file and install them.
      - name: install requirements
        run: | 
          python -m pip install --upgrade pip
          pip install -r requirements.txt

        # Run the script
      - name: run script
        run: python Main.py

      - name: commit files
        run: |
          git config --local user.email "actions@github.com"
          git config --local user.name "GitHub Actions"
          git add corporate_bs.txt
          git commit -m 'Data updated' || echo "No changes to commit"
          git push origin || echo "No changes to commit"
```



