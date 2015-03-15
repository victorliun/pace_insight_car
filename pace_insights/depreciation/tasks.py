from functools import wraps
 
from pace_insights import celery_app
from .models import Job
from scraper import scrapping

 
def update_job(fn):
    """Decorator that will update Job with result of the function"""
 
    # wraps will make the name and docstring of fn available for introspection
    @wraps(fn) 
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        print job,"gggg"
        job.status = 'started'
        job.save()
        try:
            # execute the function fn
            result = fn(*args, **kwargs)
            job.result = result
            job.status = 'finished'
            job.save()
            print "result", result
            print job
        except:
            job.result = None
            job.status = 'failed'
            job.save()
            print 'job', job
    return wrapper
 
 
# two simple numerical tasks that can be computationally intensive
 
@celery_app.task
@update_job
def power(n):
    """Return 2 to the n'th power"""
    return 2 ** n
 
 
@celery_app.task
@update_job
def fib(n):
    """Return the n'th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci numbers are only defined for n >= 0.")
    return _fib(n)
 
 
def _fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return _fib(n - 1) + _fib(n - 2)
 
# mapping from names to tasks
 
TASK_MAPPING = {
    'power': power,
    'fibonacci': fib
}