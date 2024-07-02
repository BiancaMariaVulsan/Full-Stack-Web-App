from celery import shared_task
from time import sleep

@shared_task
def sample_task(duration):
    sleep(duration)
    return f"Task completed in {duration} seconds"
