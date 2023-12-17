import logging
from offisync.celery import app
from django.utils import timezone
from .models import WorkHistory


logger = logging.getLogger(__name__)


@app.task
def update_work_histories_last_checked():
    try:
        logger.info("Starting to update last_checked for all active work histories.")
        WorkHistory.objects.filter(end_date__isnull=True).update(last_checked=timezone.now().date())
        logger.info("Successfully updated last_checked for all active work histories.")
    except Exception as e:
        logger.error(f"Error updating last_checked: {e}")
        raise
