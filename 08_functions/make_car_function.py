
def make_car(manufacturer, model, **details):
    details['Manufacturer'] = manufacturer
    details['Model'] = model
    return details