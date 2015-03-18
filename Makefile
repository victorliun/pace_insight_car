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
	$(VIRTUALENV) && python pace_insights/manage.py test depreciation
.PHONY : test