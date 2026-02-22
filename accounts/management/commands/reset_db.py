from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Clear database"

    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR("ERROR: This command can only be used in DEBUG mode"))
            return

        self.stdout.write(self.style.WARNING("🧹 Clearing data from the database..."))

        call_command("flush", interactive=False)

        self.stdout.write(self.style.SUCCESS("✨ Database reset successfully!"))
