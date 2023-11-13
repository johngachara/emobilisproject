from django.core.management import BaseCommand
from Employeeform.models import Employee

class Command(BaseCommand):
    def handle(self, *args, **options):
        database = Employee.objects.all()
        database.delete()
        self.stdout.write(
            self.style.SUCCESS("Deleted all data in database")
        )
