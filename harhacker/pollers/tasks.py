from celery.task import task

@task(ignore_result=True)
def poll_har(url):
    pass
