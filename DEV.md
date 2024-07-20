![Website logo](/documentation/screenshots/site_logo.png)

---

# Development and Deployment 

**This document covers.**

For overview information of this website, see [README.md](/README.md) <br>
For information on the development and deployment of this website, see DEV.md <br>
For information on the integrated security built into the app, see SECURITY.md <br>
For information on the testing procedure, see TESTING.md

---

## Table of Contents
1. [CI/CD](#continuous-integration--continuous-deployment)
2. [Development Environment](#development-environment-set-up)
    - [Creating a GitHub Repository](#creating-a-github-repository)
    - [Cloning the GitHub Repository Locally](#cloning-the-github-repository-locally)
    - [Setting up my IDE](#setting-up-my-ide)
    - [Building a Virtual Environment](#building-a-virtual-environment)
    - [Project Requirements](#project-requirements)
    - [Getting the Project Up and Running](#getting-the-project-up-and-running)
    - [Creating a Database](#creating-a-database)
    - [Coding in Python and PEP8](#coding-in-python-and-pep8)
3. [Local Development](#local-development)
4. [Deployment](#deployment)

## Continuous Integration / Continuous Deployment
The philosophy of continuous integration and continuous deployment was at the forefront of my mind during the development of this project.
Git has been used for the version control for the webpage and all information has been stored in a repository on GitHub. Though not strictly continuous integration, version control and continuous integration are synergistic and have a large cross over in their aims and implementation and manage the changes of the code over time. The repository was not shared with any other developers for this single developer project, so a shared repository and necessary continuous integration practices such as automated builds or automated testing were not required. That being said, the spirit and philosophy of continuous integration and continuous development can be seen in my approach to testing and implementing features.
Please see my [GitHub Project](https://github.com/users/amfairley/projects/7/views/1) for the tracking of tasks across the project. GitHub projects was used to track the development of this website, allowing tasks to be created, converted to an issue to link them to the GitHub repository and to assign a member of the team the task. As this project was completed as a single developer team, I assigned all of the tasks to myself. In a multi-developer team, this software would allow the scrum leader to assign tasks and ensure that no two developers are working on the same aspect of the project in isolation. <br>
To create a GitHub project, you will need a [GitHub](https://github.com/) account. From your profile page you can access your projects from the taskbar at the top. It is the third selection after “Overview” and “Repositories”. Help with creating a project can be found [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project). When assigning tasks in my project I used the [MoSCoW](https://www.marketing-logic.com/salesforce/the-moscow-method/) method; a way of prioritising tasks by assigning them Must, Should, Could, or Would. This allowed me to concentrate on core components of the project and build up from there.


## Development environment
Here are the steps that I took to set up my local development environment. There have been provided to highlight key philosophies in the development process and to guide unfamiliar users with how to set up their own local development environment. 

### Creating a GitHub Repository
In order to create your own repository you will also need a GitHub account. From your profile page, you can access your repositories from the taskbar at the top. It is the second selection, after “Overview”.<br>
![Github taskbar](/documentation/development/development_github_taskbar.png)<br>
From this repositories tab you can select the green “New” button to open the form for creating a new repository.<br>
![New repository button](/documentation/development/development_new_repo.png)<br>
In this form you can enter details for your own repository. The values that I used were:
-	Repository template: No template
-	Owner: I made sure that I was the owner by selecting my GitHub username from the drop down menu
-	Repository name: toytribe
-	Description: A full-stack review website for children's toys
-	Public: I toggled public so that this is available to you, however you may want to select Private if you do not wish other users to see your repository
-	Add a README file: Ticked, so that I can explain my process and code to facilitate users getting up and running with my project or create a project of their own.
-	.gitignore template: None, I will create my own .gitignore file
-	License: None
Then I clicked the green create repository button and was redirected to the new repository.<br>
![Create new repository](/documentation/development/development_create_repo.png)<br>
For any troubleshooting tips or help with creating your own repository, GitHub provides this handy [quick start guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories).

### Cloning the GitHub repository locally
My IDE of choice for this project is [Visual Studio Code](https://code.visualstudio.com/), as it has strong support for many coding and markup languages and I will be utilising HTML, CSS, JavaScript, and Python to create my website. With help setting up Git in VSCode, please see the [VSCode Git documentation](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git).
The steps that I took to clone my project to deploy it locally were:
-	Open my repository page in GitHub
-	Click the bright green “<> Code” button located below the Pin/Watch/Fork/Star toolbar and above the repository file list.
-	Selected my cloning option which was to clone from the web URL using HTTPS and clicked the copy URL to keyboard button.
-	![Repository Clone Options](/documentation/development/development_clone_options.png)
-	Other options for cloning include using a password protected SSH key using SSH, working in the official GitHub CLI with GitHub CLI, or downloading the repository in a .zip folder
-	In VSCode, I clicked on the Source Control icon located on the left hand side beneath the explorer and search button
-	![Source Control Icon](/documentation/development/development_source_control_icon.png)
-	I selected “Clone Repository”, which redirects the user to the search bar at the top of VSCode. This is where I pasted in my web URL copied from my GitHub repository and clicked enter, ensuring that the “Clone from URL” option was highlighted.
-	![Local Cloning](/documentation/development/development_local_cloning.png)
-	I then selected a folder to save the repository locally into and opened the repository when prompted

### Setting up my IDE
To set up my development IDE so that I could start coding; I required Python and PostgreSQL.<br>
Python can be downloaded and easily installed from the [Python](https://www.python.org/downloads/) website. Select the version and operating system that you want to download python for click the installer file to download. I used 3.12.4. Once the file is downloaded, open the installer and follow the python installer wizard with the following changes to the default:
- Tick “Add python.exe to PATH” on the first page of the install wizard and click on custom installation  
- On optional features, ensure that they are all ticked and click next
- On advanced options, tick the option to install python for all users if desired, and tick “Precompile standard library” and click “Install”
When the wizard displays that the setup was successful, you can close it. You can confirm its installation on windows by typing CMD into the windows search bar to open the command prompt. Here type `python --version` and it will show the currently installed version. If this does not work, please see this [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide) or [Python Documentation](https://docs.python.org/3/) for troubleshooting.<br>

My relational database will be hosted with the relational database management system; PostgreSQL. I used version 16.3. You can download PostgreSQL [here](https://www.postgresql.org/download/), just select your operating system and click "Download the installer" under the "Interactive Installer by EDB” heading. Once downloaded, go through the wizard, using default options but ensure that you choose a password that you will remember. When using PostgreSQL, the username will be postgres and the password will be the one you entered into the wizard when installing.<br>

Finally I installed the following VSCode extensions in order to have access to everything within VSCode:
- Python by Microsoft
- PostgreSQL by Chris Kolkman
- PostgreSQL by Microsoft

### Building a Virtual Environment 
I did all of my work inside a virtual environment so that I could install and work with libraries and dependencies without worrying about the greater impact of them on my system. With the repository open in VSCode, I used the terminal to create a new python virtual environment by typing: `python -m venv venv`. To see if this has worked, a folder named venv should have appeared in your root directory. This virtual environment can be activated by typing `.\venv\Scripts\activate` into the terminal on windows or `source venv/bin/activate` on MacOS. This will show a green (venv) at the start of each terminal line indicating that you are within the virtual environment.<br>
![Green venv sign](/documentation/development/green_venv.png)<br>
To leave this virtual environment when you want to close the file later, you can type `deactivate` into the terminal. Please note you will need to activate the virtual environment each time you load up the files to work on to ensure that everything is running.

### Project Requirements
This project was a flask app, so I installed the packages required for the project using pip; the python package manager.<br>
`pip3 install Flask-SQLAlchemy pyscopg2`. <br>
Flask is a lightweight Python web framework allowing me to create a web application with python. Flask-SQLAlchemy is a flask extension that adds support for SQLAlchemy; an Object Relational Mapping (ORM) library that allows us to query and manipulate data from a database in the form of an object. Psycopg2 is an adaptor for the PostgreSQL database for Python. With these three packages, you have everything you need to create a python based Flask app with a relational database backend. The full list of all libraries used can be found in my [reqirements.txt](/requirements.txt) file. Copy and pasting this into your project and typing in the terminal `pip install -r requirements.txt` will install all dependencies used in this project simply and efficiently.

### Getting the Project Up and Running
To get my project up and running I created the following files and folders:
- **env.py** in the route directory.
    * This file sets the values for connecting to the database.
    * This holds sensitive data so an example is provided as [env_example.txt](/env_example.txt). You can create your own by inserting your own secret key, PostgreSQL password, and database name.
- A new folder in the route directory named **toy_tribe**
    * This folder houses all of the app data.
- `__init__.py` in the toy_tribe folder
    * This file imports the key data from our env.py file, creates our app as an instance of the Flask class, creates our database as an instance of a SQLAlchemy class, and imports our routing (yet to be created).
- **routes.py** in the toy_tribe folder
    * This file holds all of our defined URL routes and associated view functions with each page. It also handles any request handling from forms across our website.
- **run.py** in our root directory
    * This file is the one called that will launch our app using `python3 run.py` in the terminal.
- **models.py** in the toy_tribe folder
    * Here I modelled each table in the relational database and their relationships with one another.

With these files created I set up my personal PostgreSQL server using the PostgreSQL extension (+ button at top right of the extension) with the following values:
- Host: localhost
- Database: postgres
- User: postgres
- Password: (my password from installing PostgreSQL)
- Port: 5432

Once connected to this server, you can create your database in the terminal using SQL notation through the following steps
- `psql -U postgres`
- Type in your password
- `CREATE DATABASE yourdatabasename;`
- `\c yourdatabasename` To check if it has been created
- `\q` to quit.

Double check that the values used to create your local server and database are reflected in the values you use in your env.py file.

To populate your database with your tables you can create a small python script like [I did](/update_db.py) or in the terminal type:<br>
```py
from project_name import db, app
with app.app_context():
    db.create_all()
```
To check that this has worked, you can once again access you database in as shown above and query tables using SQL notation. 

### Coding in Python and PEP8
Throughout the the project, I kept strict adherence to the Python good practices for style; [PEP8](https://peps.python.org/pep-0008/). This included:
- Line lengths less than 80 characters long
- DOCSTRINGs on all functions and classes
- Naming conventions for functions, variables, and classes
- Comments on code functionality
- 2 empty lines beneath each block of code
- 1 empty line at the bottom of the file

These were validated as show [here](/TESTING.md#python-validation) in my TESTING.md file.

## Local development
To install my project locally, you can follow my steps above in the [Development Environment](#development-environment) section, replacing file and folder names with the ones in my project.
You can also fork the GitHub repository to collaborate by once logged into GitHub by:
- Go to the repository for this project, [ToyTribe](https://github.com/amfairley/toytribe/tree/main).
- Click the Fork button in the top right corner.

## Deployment
This project was deployed remotely to [Heroku](https://www.heroku.com/), a cloud platform as a service (PaaS) that allows developers to build, run, and operate applications entirely in the cloud. The steps taken are outlined in this section:
- I created a database using the [Code Institute Database Maker](https://dbs.ci-dbs.net/) as it was available to me. Those of you without access will need to create a free or paid hosted database online and save the URL provided.
- Adding a requirements.txt file and a Procfile in order for Heroku to run this web application without errors.
    * **requirements.txt**
    * This file contains a list of all the dependencies that our project needs to run successfully.
    * This is created in the terminal with:
    * `pip3 freeze > requirements.txt`
    * **Procfile**
    * This file informs Heroku which of our files is used to run the app. In my case it is run.py, but app.py is also widely used.
    * Create it in the terminal with:
    * `echo web: python app.py > Procfile`
    * It is worth noting that there should be no extra line at the bottom and that there is no file type extension on the Procfile file.
- Log into your or create a [Heroku](https://www.heroku.com/) profile and click on Create New App, give your app a unique name and set your region and click Create App.
- As our env.py file is only stored locally, we need to transfer this information to Heroku. This can be done in the settings tab of your new app and clicking "Reveal Config Vars". Add a first setting of DATABASE_URL set to the URL you were provided with when creating a database. Then go through and add a new line for each of the values set in your env.py. It is important to remove the DEBUG variable upon final deployment. The result should look like this:
- ![Config Vars](/documentation/development/heroku_config_vars.png)
- Next connect your app to your GitHub repository on the "Deploy" tab. Select "Connect to GitHub", search for your repository and click connect. In this section I enabled automatic updates so as to push through fixes to any bugs that I encountered whilst testing the deployed site. Then click deploy branch, making sure you are deploying the correct branch (I used main).
- Finally we need to populate our database with our table models again. This is done inside the Heroku CLI, which can be accessed through the "More" button and "Run console" selection. Type python3 into the console to open a python environment. Then we can use the same code as before:
```py
from project_name import db, app
with app.app_context():
    db.create_all()
```

Congratualations, the app should now be up and running and you can click "Open App" to see the deployed project!