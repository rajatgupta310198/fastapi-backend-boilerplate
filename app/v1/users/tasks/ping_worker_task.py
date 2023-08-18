from app.worker import celery_app


@celery_app.task(name="ping_task", bind=True)
def ping_task(self):
    return {}
