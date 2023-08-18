from celery import Celery
from dotenv import load_dotenv

load_dotenv()

from .settings import AppConfigSettings

celery_app = Celery(broker=AppConfigSettings.CELERY_BROKER)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],  # Ignore other content
    result_serializer="json",
    timezone="Europe/Oslo",
    enable_utc=True,
)

celery_app.conf.beat_schedule = {
    "run-after-five-secs-sync": {
        "task": "sample_sync_task",
        "schedule": 5.0,
        "args": {},
    },
}

celery_app.autodiscover_tasks(["app.v1.users"])
