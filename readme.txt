-- Workspace Setup Read Me --

Version Requirements:
  Python 3.8                  https://www.python.org/downloads/
  Visual Studio Code 1.52.1   https://code.visualstudio.com/download

If you are using Visual Studio Code to setup Python, please read through one of these guides.
https://code.visualstudio.com/docs/languages/python
https://wiki.python.org/moin/BeginnersGuide/Download


-- Python Environment Setup --
Once the IDE and Python are configured, please follow the steps:

1) Open up Command Prompt and enter the root folder of the project.
>  $ cd \\New-Pilots-Website

2) Python 3 has a virtual environment built into the version, the following command will create this virtual environment.
>  $ python -m venv dev 
If there is a virtual environment that exists, you can skip this step.

3) When the virtual environment is created, the following command will activate the virtual environment.
>  $ dev\Script\activate 
Command prompt should show (venv) stating that the virtual environment is now activated.
>  (venv) $

4) Now you'll need to download some Python packages from Python's pip command.
For now the packages we need so far are:
  flask 
  flask-sqlalchemy
  flask-login

>  (venv) $ pip install "package-name"      or
>  (venv) $ pip install flask flask-sqlalchemy flask-login

5) Besure to leave Command Prompt open as the moment you close it, it will deactivate the virtual environment.


-- Running the Flask Application --

When running the flask app for the first time, please make sure that you are running the code from the __init__.py file.
Run like you would run any other python code. Debug like you would debug any other python code.

It will run on a local server: http://127.0.0.1:5000/
Use CTRL + C to quit the session.

