#!/bin/sh
 
cd pace_insights
# migrate db, so we have the latest db schema
su -m paceinsight -c "python manage.py migrate"
# start development server on public ip interface, on port 8000
su -m paceinsight -c "python manage.py runserver 0.0.0.0:8000"
echo "run web server"