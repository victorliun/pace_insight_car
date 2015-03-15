VIRTUALENV = . env/bin/activate
env:
	$(VIRTUALENV) && /bin/bash
.PHONY : env

run:
	$(VIRTUALENV) && python pace_insights/manage.py runserver
.PHONY : run