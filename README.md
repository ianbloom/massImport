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


![Optional Text](https://github.com/ianbloom/massImport/blob/looper/readmeImages/DataSources.png)
