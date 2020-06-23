import logging

from django.core.management.base import BaseCommand


logger = logging.getLogger(__name__)


# Run with python manage.py hellobot
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Hello. Welcome to Dekoruma!")
