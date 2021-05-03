# BlandyResearchAutomation
Automated software that takes in an excel file containing raw Blandy Data and calculates the Shannon Diversity Index (H') and Pielou's Eveness Index (J') for each plot. These H' and J' values are also ranked to carry out a Kruskall Wallis test.


## How To Use the Tool

## Step 1 Installing Python

Download and run the installer for python at this link make sure to click the "Add to Path" checkbox when installing python - https://www.python.org/downloads/

## Step 2 Installing Pip

Pip is a python package manager which will allow us to install "packages" that help the code run

Open up terminal by search for "cmd" in windows or typing "Windows Key + R" and then typing "cmd" and then typing "enter"
Copy and paste this command into your terminal 

```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

If the command does not work go to this link to download pip => https://pip.pypa.io/en/stable/installing/

## Step 3 Download This Repository

Download the code you see in here by clicking the download button or look up how to download github repository
Once you have downloaded the repository save it to your desktop folder

## Step 4 Installing Dependencies

Once you have the folder downloaded, go into cmd once again and it should have somehting along the lines of "C:\Users\avyuk" once you are there type these commands

```shell
cd Desktop
cd BlandyResearchAutomation
pip install -r requirements.txt
```

## Step 5 Running the Code

Your basically done now all you need to do is run the following command(s)

```shell
python DiversityCalculator.py
```

or 

```shell
python3 DiversityCalculator.py
```

If something does not work copy and paste the error into google and look for a website called stack overflow they are more qualified than I am to help u
