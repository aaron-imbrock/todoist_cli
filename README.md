# todoist_cli

## Prereqs

sudo mkdir -p /opt/todo && cd $_
sudo git clone git@github.com:aaron-imbrock/todoist_cli.git

If not already present install venv and then create your project's virtual environment:

sudo apt install python3.8-venv
python3 -m venv env

`pip` is automatically installed when you create the env. Use it to install the packages listed in requirements.txt 
 pip install -r requirements.txt

Rename common/template_env.py to common/env.py 

Noted in that file is the url to create and then grab your todoist api key. In env.py set `access_token` varialbe to include your API key.
On the todoist Developer console go to 'Manage App' and create your new app. Scrolling down your 'App Management' page you'll see the Test Token also referred to as 'Your Access Token'. That key gets assigned to access_token in env.py. env.py is skipped in the .gitignore file.


