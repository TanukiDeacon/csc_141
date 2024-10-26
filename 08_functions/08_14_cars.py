# this prograam will make a car

def make_car(manufacturer, model, **details):
    details['Manufacturer'] = manufacturer
    details['Model'] = model
    return details

car_details = make_car('Toyota', "Tacoma", color = 'red', tow_package = 'false')

print(car_details)