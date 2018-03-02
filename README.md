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

Next, we install requests, our only dependency.  We need requests to make HTTP requests (like the ones we will make 
to the LM API).

Type `sudo pip install requests` into the terminal.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/requestsInstall.png)

The output should look something like the below.  If you have any trouble with any of these steps, please contact me.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/requestsOutput.png)

Success!  Let's run the script!

### Script Execution

First, place whichever version of the script is relevant (or both if you'd like) into the same folder as all of the
DataSources that you would like to import into the customer account.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/folderView.png)

To run the script first right click massImport_X.py and choose copy.  Then navigate back to the terminal and type
`python ⌘v` which should paste the filepath of the script as seen in the image below.

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/exampleInput.png)

The script will prompt you for an LM Access ID, an LM Access Key, and a Trimmed Account Site.  The Access ID and Access Key
must be created prior to script execution.  It is best practice to create an API specific user and spin up credentials for
that user.

Successful script execution will look like the below.  The script prints Response Code and Response Body into the terminal.
In short, we definitely want a response code of 200.  If you see something else, [take a look at this website to learn more](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/successOutput.png)

We've done it!  Let's check in the account to make sure they've been imported correctly:

![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/DataSources.png)
