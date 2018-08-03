# How To Create Django Scripts Accessible From The Command Line

Note: these instructions were rephrased from [this tutorial](https://github.com/nashville-software-school/bangazon-llc/blob/master/DB_RESET_SEED_SYSTEM.md) as it was on 8/3/2018. I'm trying to make the instructions more general rather than specific to blowing up Django migrations, but keep in mind that some things might need to change.

>NOTE: anywhere in the below code where you see brackets [], replace the text inside them with your text. Do not type the brackets in your own code.

## To Create a Custom Pyman Command

1. From the command line, cd into an app folder
1. ```mg management```
1. ```touch __init__.py```
1. ```mg commands```
1. ```touch __init__.py [name of the command you want to create].py```
1. Paste the below code into the command file, adjusting as needed (this code is for faker_factory)

>NOTE: the script below would require installation of [django_seed](https://github.com/Brobin/django-seed).

```python
from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from [app_name].models import [modelnames]

class Command(BaseCommand):

    def handle(self, *args, **options):
        seeder.add_entity([model], [number of records desired])
        # [do the above for all desired models]

        inserted_pks = seeder.execute()
```

## To Create The Shell Script

1. Copy the below code into a new [filename].sh file
> NOTE: In the below code, arg1 is the name of the app and arg2 is the name of the custom pyman command.

```bash
#!/bin/bash

find . -path "/$1/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/$1/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations $1; #creates the migration and the new db file.
python manage.py migrate; #runs the migration.
python manage.py $2 #runs the custom command to generate fake data and populate your tables with it

```

## To Execute This Command

1. cd into the project root directory (wherever the manage.py file is located)
1. ```[name of shell script file].sh [arg1, the app name] [arg2, the name of the custom pyman command]```