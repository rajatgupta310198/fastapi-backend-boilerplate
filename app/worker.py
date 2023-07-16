from celery import Celery

celery_app = Celery(broker="redis://localhost:6379")

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],  # Ignore other content
    result_serializer="json",
    timezone="Europe/Oslo",
    enable_utc=True,
)
celery_app.autodiscover_tasks(["app.users"])
