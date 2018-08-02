# Setting up Venv in Windows

**If you have not set up a virtual environment, do this stuff the first time you want to run this app:**

1. From the command line cd into the project directory
2. Run the following command: ```python -m venv myvenv```
  * Note: the gitignore will automatically exclude any directory ending with "venv".
3. CD into the myvenv directory
4. Run the following command: ```. Scripts/activate```
  * You will know the virtual environment is running when the command prompt is preceded with ```(myvenv)```
5. CD into the project root directory (should be the parent of the myvenv directory)
6. [Install Django and create a Django app](./django_installation.md)
7. Run the following command: ```python manage.py runserver```
8. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**If you've already installed Django, etc. inside your virtual environment**

1. From the command line, cd into your myvenv directory
1. Run the following command: ```. Scripts/activate```
1. CD into the root directory (wherever the manage.py file is located).
1. Type ```python manage.py runserver``` into the command line.
1. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
