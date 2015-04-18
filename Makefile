VIRTUALENV = . env/bin/activate
env:
	$(VIRTUALENV) && /bin/bash
.PHONY : env

run:
	$(VIRTUALENV) && python pace_insights/manage.py runserver
.PHONY : run

run-celery-worker:
	$(VIRTUALENV) && cd pace_insights && celery -A \
		pace_insights worker --app=pace_insights.celeryconf:app --loglevel=info
.PHONY : run-celery-worker

shell:
	$(VIRTUALENV) && python pace_insights/manage.py shell
.PHONY : shell

test:
	$(VIRTUALENV) && python pace_insights/manage.py test $(ARGS) depreciation
.PHONY : test

setup:
	$(VIRTUALENV) && pip install -r requirements.txt
.PHONY : setup

migrate:
	$(VIRTUALENV) && python pace_insights/manage.py migrate
.PHONY : migrate

make-migrates:
	$(VIRTUALENV) && python pace_insights/manage.py makemigrations
.PHONY : make-migrates