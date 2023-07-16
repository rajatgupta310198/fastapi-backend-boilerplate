from celery.utils.log import get_task_logger

from app.worker import celery_app

_logger = get_task_logger(__name__)


@celery_app.task(name="sample_sync_task", bind=True)
def sample_sync_task(self, **kwargs):
    _logger.info(f"running every 5 seconds to sync!!!")
    return {}
