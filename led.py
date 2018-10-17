
class Led:
    def __init__(self, pin):
        self.pin = pin
        self.brightness = 0
    
    def set_brightness(self, brightness):
        self.brightness = brightness

    def get_brightness(self):
        return self.brightness

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin


