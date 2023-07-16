from celery.utils.log import get_task_logger

from app.models import User
from app.worker import celery_app
from app.worker import DbTask

_logger = get_task_logger(__name__)


@celery_app.task(base=DbTask, name="ping_task", bind=True)
def ping_task(self):
    user = self.db.query(User).first()
    _logger.info(user)
    return {}
