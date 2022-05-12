from django.core.management.base import BaseCommand, CommandError
from cars.models import Car

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('car_plate', type=str)
        parser.add_argument('car_name', type=str)

    def handle(self, *args, **kwargs):
        car_values = {
            'car_plate': kwargs['car_plate'],
            'car_name': kwargs['car_name'],
            }
        car = Car(**car_values)
        car.save()
