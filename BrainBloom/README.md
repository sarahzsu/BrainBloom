## Installing Requirements

1. Activate Virtual Environment (optional)

Powershell-
.venv/Scripts/activate

2. Install Requirements

Powershell-
pip install requirements.txt

3. Deactivate Virtual Environment

Powershell-
deactivate

---
## Setting Up MySQL & PHPMyAdmin Containers

1. Install Docker Desktop
https://docs.docker.com/desktop/install/windows-install/

2. Import Data into MySQL Database
- uncomment line 13 (under 'volumes:') in 'docker-compose.yml'
- comment the line under (line 14)

3. Run Docker Compose

Powershell-
docker-compose up

4. Run PHPMyAdmin
Go to http://localhost:8080 

5. Connect to MySQL Server (from PHPMyAdmin)

- open a new terminal and enter the following command:
Powershell-
docker inspect mysql-server

- scroll up to find the line "IPAddress":
- enter that same IP address into the PHPMyAdmin 'Server' field

- user is 'root', password is 'root'

6. Stopping the Containers (suggested but optional)

Ctrl + C on the terminal where you first did 'docker-compose up'

7. Deleting the Container (CAUTION: resets the data stored)

Powershell-
docker-compose down

---
## Adding Requirements

1. Activate Virtual Environment

Powershell-
.venv/Scripts/activate

2. Install the Module

Powershell-
pip install <module>

3. Update Requirements File

Powershell-
pip freeze > requirements.txt

4. Deactivate Virtual Environment

Powershell-
deactivate

---
## Naigating Folder System

controllers:
- .py files for the backend of your application

db:
- persistant storage for the mysql container

models:
- classes for each table

routes:
- routing for each page

sql_dump:
- sql file of database (for easy import or backup)

static:
- css files
- images

templates:
- html files

app.py:
- main flask app (run this file to start app)


---
