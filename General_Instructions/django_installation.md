# Django installation notes

## To start a new Django app:

It's a good idea to start by [creating a virtual environment](./set_up_venv.md).

1. cd into the project root directory
1. Run ```pip install django```
1. run the following command: ```django-admin.exe startproject mysite .```
  * "mysite" is the name of your project
  * note the period at the end of the command.

## To Run

1. Clone the repo.
2. From the command line, cd into the root directory (wherever the manage.py file is located).
3. Type ```python manage.py runserver``` into the command line.
  * Note: I've set up a ```pyman``` alias for ```python manage.py```
4. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)