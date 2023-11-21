class Display:
    def __init__(self,
                 id,
                 message="",
                 is_on=False,
                 carpark=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.carpark = carpark

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")


