from random import randint

class SenseHat:
    """
    Dummy implementation of the SenseHat api for showing functionality of the website
    without the necessary hardware
    """

    def get_temperature(self):
        """
        Returns a random integer between 18 and 30 simulating a temperature sensor
        """
        rand_number = randint(18, 30)
        return rand_number

    def get_humidity(self):
        """
        Returns a random integer between 25 and 50 simulation a humidity sensor
        """
        return randint(25, 50)

    def get_pressure(self):
        """
        Returns a random integer between 980 and 1050 simulation a air pressure sensor
        """
        return randint(980, 1050)
