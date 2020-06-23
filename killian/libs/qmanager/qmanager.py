DEFAULT_RETRY_COUNT = 3
DEFAULT_CHANNEL = 'default'
MAX_FAILURES_META = 'max_failures'
FAILURES_META = 'failures'


class QManager():

    def __init__(self):
        import logging
        import django_rq
        self.logger = logging.getLogger(__name__)
        self.django_rq = django_rq

    def enqueue(self, *args, **kwargs):
        """ Wrapper of RQ, set maximum retry *retry_count* times """
        try:
            retry_count = kwargs.pop('retry_count', DEFAULT_RETRY_COUNT)
            channel = kwargs.pop('channel', DEFAULT_CHANNEL)
            job = self.django_rq.get_queue(channel).enqueue(*args, **kwargs)
            job.meta[MAX_FAILURES_META] = retry_count
            job.save()
        except Exception as e:
            print('Submit Django RQ FAILED', str(e))

    def requeue_failed_jobs(self, channel=DEFAULT_CHANNEL):
        self.logger.info("Re-queueing failed jobs for channel %s" % channel)
        from rq.registry import FailedJobRegistry
        failed_registry = FailedJobRegistry(
            queue=self.django_rq.get_queue(channel))

        job_ids = failed_registry.get_job_ids()
        for job_id in job_ids:
            self.logger.info('Job %s: re-queueing' % job_id)
            failed_registry.requeue(job_id)

        # fq = self.django_rq.queues.get_failed_queue()
        # jobs = fq.get_jobs()
        # for job in jobs:
        #     if MAX_FAILURES_META in job.meta:
        #         self.logger.info('%s=%s' % (MAX_FAILURES_META,
        #                                     str(job.meta[MAX_FAILURES_META])))
        #         job.meta.setdefault(FAILURES_META, 0)
        #         job.meta[FAILURES_META] += 1
        #         job.save()
        #
        #         failures = job.meta[FAILURES_META]
        #         max_failures = job.meta[MAX_FAILURES_META]
        #         if failures >= max_failures:
        #             self.logger.warn(
        #                 'Job %s: failed too many times - moving back to failed queue' % job.id)
        #         else:
        #             self.logger.info('Job %s: requeueing' % job.id)
        #             fq.requeue(job.id)


qm = QManager()

'''
How to use:
    from killian.libs.qmanager import qm
    qm.enqueue(task, arg1, arg2, ...)
'''
