from django.core.management.base import BaseCommand, CommandError
from depreciation.scraper import scrapping

class Command(BaseCommand):
    help = 'scrapping whatcar site to get car depreciation data'

    def handle(self, *args, **options):
        self.stdout.write('Start crawlling...')
        scrapping()
        self.stdout.write('Successfully finish crawlling.')
