#!/bin/sh
 
cd pace_insights
# run Celery worker for our project pace insight with Celery configuration stored in Celeryconf
su -m paceinsight -c "celery worker -A pace_insights.celeryconf -Q default -n default@%h"