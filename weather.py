#Python Code to get Outside temperature for the entered location
def weather():
    weather = Weather(unit=Unit.CELSIUS)

    loc=input('Please Enter the Location:- ')

    location = weather.lookup_by_location(loc)
    #condition = location.condition.code



    print(location.description)
    print('\n')

    print("Wind Speed:-",location.wind.speed+location.units.speed)
    print("Outside Condition:-",location.condition.text)
    print("Temperature:-",location.condition.temp+location.units.temperature)
    print("Atmospheric Parameters:-",location.atmosphere)


    print("Sunrise & Sunset:-",location.astronomy)