from django.test import TestCase
from cars.models import Car
from django.core.management import call_command
from io import StringIO



# Create your tests here.

class CarTestCase(TestCase):

    def call_command(self):
        """Method por call command"""
        args = ['12345', "Ford"]  # Any command line arguments go here
        out = StringIO()
        try:
            call_command('addcars', *args, stdout=out)
        except Exception as e:
            pass

    def test_create_by_model_ok(self):
        """Car created in model correctly"""
        Car.objects.create(car_plate="1234", car_name="Mustan")
        car = Car.objects.get(car_plate='1234')
        #Verify car created is correct
        self.assertEqual(car.car_plate, '1234')
        self.assertEqual(car.car_name, 'Mustan')

    def test_command_addcar(self):
        """Test create car correctly for a command"""
        self.call_command()
        car = Car.objects.get(car_plate='12345')
        #Verify car created is correct
        self.assertEqual(car.car_plate, '12345')
        self.assertEqual(car.car_name, 'Ford')

    def test_view_found_car(self):
        """Test for a view when found the car plate"""
        self.call_command()
        response = self.client.get('/?car_plate=12345')
        #Verify status code is 200 and found a car
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['car'].car_plate, '12345')

    def test_view_not_found_car(self):
        """Test for a view when not found the car plate"""
        self.call_command()
        response = self.client.get('/?car_plate=123456')
        #Verify status code is 200 and not found a car
        self.assertEqual(response.status_code, 200)
        self.assertTrue('car' not in response.context)
