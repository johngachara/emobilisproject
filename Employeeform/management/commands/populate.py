import json
import os.path
from Employeeform.models import Employee
from django.core.management import BaseCommand

from Emobilisproject3 import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR,'MOCK_DATA.json')
        self.stdout.write(
            self.style.SUCCESS("Started transferring data")
        )
        with open(path) as file:
            data = json.load(file)
            for employee in data:
                Employee.objects.create(
                    name=employee['name'],
                    email= employee['email'],
                    salary=employee['salary']
                )
        self.stdout.write(
            self.style.SUCCESS("Finished Transferring")
        )
