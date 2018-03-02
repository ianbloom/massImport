# massImport

### Introduction
I wrote this Python script as a tool for the LogicMonitor Customer Success Team to simplify the process of bulk adding
DataSources into customer accounts.

This README is designed to be followed by users of any technical ability.  After the user's Python environment is properly
configured via the steps in this guide, it is simple to run the script going forward.

When the script is run, it will prompt the user for API credentials and a trimmed account site for the desired customer
account.  After entry, the script will iterate through all .xml files in the same folder and import them into the customer
account.  After each DataSource Submission, the script will print the HTTP Response Code and Response Body.

### Python Configuration
Let's open the Terminal!  Navigate to the top right hand side of your screen and click the magnifying glass.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/magnifyingGlass.png)

Type in "terminal" and open the application.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/terminal.png)

First we need to verify if Python is installed, and if it is, what version is installed.  In the terminal type `python -V`.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/pythonVersion.png)

Your Python will either be version 2.XX or 3.XX, which will determine which version of massImport_X.py you will run.

We need to check if pip is already installed as well.  Type `pip --version` in your terminal.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/pipVersion.png)

If your output does not look like the above, then install pip by typing `sudo easy_install pip`.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/pipInstall.png)

