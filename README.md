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

Download the code you see in here by scrolling up and clicking the download button. THe button should look like the image below.

![image](https://user-images.githubusercontent.com/73862038/116841916-a7065e80-aba8-11eb-9bd7-75c44b5c78b8.png)

There should be an option called "download ZIP" click that and let it download (I promise its not a virus)
Then go into file explorer, go into your downloads folder and right click the ZIP file that you downloaded.
Then click extract all and a window should pop up. Click browse and and select your desktop as the folder you want to save the extracted files to.

## Step 4 Installing Dependencies

Once you have the folder downloaded, go into cmd once again and it should have somehting along the lines of "C:\Users\avyuk" once you are there type these commands

```shell
cd Desktop
```
```shell
cd BlandyResearchAutomation
```
```shell
python -m pip install -r requirements.txt
```

## Step 5 Running the Code

Your basically done now all you need to do is run the following command(s). Make sure to go into the downloaded folder on your desktop and into the folder that says data. The Blandy Data that was used to create this software should be in there. Delete the file and add your own if you prefer but if you do replace it rename the file you added to "Blandy_data.xlsx".

```shell
python DiversityCalculator.py
```

or 

```shell
python3 DiversityCalculator.py
```

Give the program a second to run and your command prompt (cmd) should display something that looks like this

![image](https://user-images.githubusercontent.com/73862038/116842316-23e60800-abaa-11eb-9ba0-a37d402c1cdf.png)

If something does not work and u get some sort of ambiguous error, copy and paste the error into google and look for a website called stack overflow they are more qualified than I am to help u
