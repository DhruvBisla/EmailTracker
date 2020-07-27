# Email Tracker

Email tracker provides an automated way to track your emails.

# Installation

## Clone the Repository

Clone the respository using https:
```shell
git clone git@github.com:DhruvBisla/EmailTracker.git
```

## Using the Makefile

### Install Dependencies
Email Tracker is compatible with Python 3. To install the necessary packages and pipenv for the virtual environment execute the Makefile:
```shell
make
```
Once installation is complete, `Pipenv` will create a Pipfile which lists the packages that were successfully installed and initialize a python 3 shell in the virtual environment

## Manual Installation
Alternatively, use the virtual environment manager of your chioce and install the necessary packages using pip:
```shell
pip install -r requirements.txt
```

# Hosting the Files

## Hosting Locally
Email tracker uses `Starlette` and `Uvicorn` to host a webserver. To begin the server, run:
```shell
uvicorn main:app --reload --port ####
```
In this command, main refers to `main.py` while app refers to the instance of the Starlette webserver. The --reload flag enables auto-reload while the --port flag specifies the port at which you would like to locally host the server. If a port is not specified, `Uvicorn` will default to port 8000. For more documentation on `Uvicorn` read the documentation [here](https://www.uvicorn.org/).

If you would like, `Pipenv` allows custom script shortcuts. To add a shortcut for starting the server run:
```shell
echo '[scripts]' >> Pipfile
echo 'startserver = "uvicorn main:app --reload --port ####"' >> Pipfile
```
By running `cat Pipfile`, you should those two lines appended to the bottom.

Now, start the server using the shortcut:
```shell
pipenv run startserver
```

## Hosting on a Public Domain
In order to receive a GET request whever your email is opened by the recipient, it is necessary for the domain that the image is hosted on to be public. In order to do this, using `Ngrok` is recommended to tunnel requests from a public domain to your localhost.

### Ngrok Setup
__Note that it is not necessary to use `Ngrok`, but is the simplest to get running.__

Begin by making an account [here](https://ngrok.com). Download the appropriate package for your operating system when it prompts you. Next, move the zip file to somewhere appropriate on your computer. Unzipping the file at that location should result in an executable file with the name ngrok. 

Now, navigate to the directory in the command line. Running `./ngrok` should return a help message listing examples and commands. From your `Ngrok` dashboard, copy and run the command that looks like:
```shell
./ngrok authtoken hash
```

Next, so that it is not necessary to use `Ngrok` only when the current working directory is the location of the executable file, set up an alias:

If using bash:
Run `pwd` to get the path of the current directory where the executable file is located.
Now, add the following line to the bashrc file to make the alias
```shell
echo 'alias ngrok="path/ngrok"' >> ~/.bashrc
```
__Make sure to replace path with the path of the current working directory displayed when you ran `pwd`.__

To execture the modified bashrc file:
```shell
source ~/.bashrc
```

Finally, to initialize the http tunnel:
```shell
ngrok http port
```
__Note that the port should be the same as the one specified to uvicorn. If a port was not specified, use 8000, the default port.__

Once this has been run,`Ngrok` should open up a black window in the terminal listing the details of the tunneling. Copy the public domain that it specifies to be tunneling to your localhost

# Sending the Email
In order to send the email, exit the virtual environment shell and run `emailer.py`:
```shell
python3 emailer.py domain
```
Replace domain with the domain you copied from the `Ngrok` window.

Running the python script will prompt several fields including those of the sender's email address and password (Note that the password field is like the one displayed in the command line when running sudo commands), the recipient's email address, the subject of the email, and the message that would like to be sent.

__Note that in order to login to the sender's email, you must give access to low security apps. If you are using a gmail account, enable this [here](https://myaccount.google.com/lesssecureapps).__

Once all this is complete and all fields have been filled, the email is sent.

# Opening the Email
When the recipient of the email opens the email in their email client, the email client must send a GET request to the domain you are hosting the 1x1 transparent pixel, allowing you to know whenever the email has been opened. This information is logged in a .txt file under the logs directory with the file's name as the email recipient plus the subject of the email for uniqueness. 

# TODO
- [ ] Change dependency from Stmplib to the Gmail API
