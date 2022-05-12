from django.shortcuts import render
from .models import Car
from .forms import CarsForm


# Create your views here.

def cars(request):
    """ View for search a car plate.
    when the car_plate parameter is passed in request.GET this function passes
    the value found to the template, if it did not find a value it does
    not send anything.
    """
    form = CarsForm()
    context = {}
    if request.method == "GET":
        car_plate = request.GET.get("car_plate", None) #car_plate sended
        if car_plate is not None:  #block unnecessary database queries
            car = Car.objects.filter(car_plate=car_plate)
            if car.exists():
                context['car'] = car.first()
    context['form'] = form
    return render(request, 'cars/cars.html', context)
