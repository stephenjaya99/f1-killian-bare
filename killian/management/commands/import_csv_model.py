import logging

from django.core.management.base import BaseCommand

from killian.apps.example.importers import ExampleCSVImporter

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    importer = dict()
    importer['Example'] = ExampleCSVImporter()

    def add_arguments(self, parser):
        parser.add_argument(
            'model',
            type=str,
            nargs=1,
            help='name of the model'
        )
        parser.add_argument(
            '--add',
            type=str,
            nargs='+',
            help='CSV filenames to be inserted (without .csv)'
        )

    def get_model_csv_importer(self, model_name):
        try:
            return self.importer[model_name]
        except Exception:
            raise ValueError("Model '%s' is not valid" % model_name)

    def handle(self, *args, **options):
        logger.info("Start Importing CSV Model")

        model_name = options['model'][0]
        filenames = options['add']
        importer = self.get_model_csv_importer(model_name)
        importer.execute(filenames=filenames)

        logger.info("End Importing CSV Model")
