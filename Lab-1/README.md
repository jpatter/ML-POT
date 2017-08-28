# Setting up your first DSX notebook

## Introduction:

[<img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/images/DSX.png" height="150"/>](http://datascience.ibm.com/) [<img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/images/dashdb-logo.png" height="150"/>](https://www.ibm.com/analytics/us/en/technology/cloud-data-services/dashdb/) [<img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/images/jupyter.png" height="150"/>](http://jupyter.org/index.html)

In this lab, you will use IBM's Data Science Experience (DSX) to create a Jupyter IPython notebook to connect to and query a dashDB instance running in IBM Bluemix.

## Objectives:

Upon completing the lab, you will know how to:

1. Create a Jupyter IPython notebook from a URL
1. Establish a connection to dashDB
1. Use a dataframe to read and manipulate tables
1. Use SQL to query the database
1. Explore the data using techniques from earlier in the lab
1. Close the database connection

## Instructions:

### Step 1.  Log into your [DSX](http://datascience.ibm.com/) account, then click the hamburger icon in the top left and select `My Projects`, then select the project you created at the beginning of this proof of technology.

> <img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/Lab-1/images/DSX-open-project.png"/>

### Step 2.  Click the `add notebooks` link in the top right of your project pane.

> <img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/Lab-1/images/DSX-add-notebook.png"/>

### Step 3.  Create the notebook.

> <img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/Lab-1/images/DSX-create-notebook-from-url.png"/>

1. Click the `From URL` tab under `Create Notebook`.
1. Give the notebook a name in the `Name` field, for example `Connect and Interact with dashDB` and optionally you can give it a description.
1. In the Notebook URL field, use `https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/Lab-1/dashConnectAndInteract.ipynb`.
1. Ensure that there is a `Spark Service` selected, then click the `Create Notebook` button on the bottom right of the screen.

### Step 4.  Follow the instructions in the notebook.

> <img src="https://raw.githubusercontent.com/Davin-IBM/Proof-of-Technology/master/DSX/Lab-1/images/DSX-edit-notebook-begin.png"/>
