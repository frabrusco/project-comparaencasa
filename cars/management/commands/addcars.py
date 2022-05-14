from django.core.management.base import BaseCommand, CommandError
from cars.models import Car

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('CAR-PLATE', type=str)
        parser.add_argument('CAR-NAME', type=str)

    def handle(self, *args, **kwargs):
        car_values = {
            'car_plate': kwargs['CAR-PLATE'],
            'car_name': kwargs['CAR-NAME'],
            }
        try:
            car = Car(**car_values)
            car.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully save a new car'))
        except Exception as e:
            raise CommandError(f'{e}')
