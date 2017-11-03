#!/bin/bash

python --version
pip install -r requirements.txt

cp tester/local_settings_template.py tester/local_settings.py
sed -i -e "s/'NAME'.*/'NAME': '$DB_NAME',/g" tester/local_settings.py
sed -i -e "s/'USER'.*/'USER': '$DB_USER',/g" tester/local_settings.py
sed -i -e "s/'PASSWORD'.*/'PASSWORD': '$DB_PASSWORD',/g" tester/local_settings.py
sed -i -e "s/'HOST'.*/'HOST': '$DB_HOST',/g" tester/local_settings.py
sed -i -e "s/'PORT'.*/'PORT': '$DB_PORT',/g" tester/local_settings.py

python manage.py migrate
python manage.py loaddata blahapp
