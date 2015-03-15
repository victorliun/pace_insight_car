from functools import wraps
 
from pace_insights import celery_app
from .models import Job
from depreciation.scraper import scrapping

 
def update_job(fn):
    """Decorator that will update Job with result of the function"""
 
    # wraps will make the name and docstring of fn available for introspection
    @wraps(fn) 
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        job.status = 'running'
        job.save()
        try:
            # execute the function fn
            result = fn(*args, **kwargs)
            job.status = 'finished'
            job.save()
        except:
            job.status = 'failed'
            job.save()
    return wrapper
 
 
# two simple numerical tasks that can be computationally intensive
 
@celery_app.task
@update_job
def run_scrapper():
    """
    running scraper.
    """
    scrapping()
 
 
# mapping from names to tasks
 
TASK_MAPPING = {
    'scrapping': run_scrapper
}