from django.core.management.base import BaseCommand

from services import CounterService


class Command(BaseCommand):
    """Initialize counter in DB before running the server."""

    help = "Initializes the database counter sequence."

    def handle(self, *args, **options):
        CounterService.create_counter(name="url_shortner")
        self.stdout.write(self.style.SUCCESS("✅ Counter sequence initialized."))
