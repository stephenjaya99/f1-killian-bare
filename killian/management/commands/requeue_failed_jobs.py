import logging

from django.core.management.base import BaseCommand
from redis.exceptions import ConnectionError

from config import settings
from killian.libs.qmanager import qm

logger = logging.getLogger(__name__)

RQ_QUEUES = settings.RQ_QUEUES


class Command(BaseCommand):
    help = 'For re-queueing failed jobs'

    def handle(self, *args, **options):
        try:
            for channel in RQ_QUEUES.keys():
                qm.requeue_failed_jobs(channel)
        except ConnectionError as e:
            logger.error("Connection Error: %s" % str(e))
