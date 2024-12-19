#defining a class

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):   #initializing attributes
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def display_info(self):  #adding methods
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours"

    def make_call(self, contact):
        return f"Calling {contact} from {self.brand} {self.model}..."

# Example of using the Smartphone class
my_phone = Smartphone("Apple", "iPhone 14", 128, 20)
print(my_phone.display_info())
print(my_phone.make_call("John Doe"))

class CameraSmartphone(Smartphone):  #creating a subclass
    def __init__(self, brand, model, storage, battery_life, camera_mp):  #initializing the subclass
        super().__init__(brand, model, storage, battery_life)
        self.camera_mp = camera_mp  # in megapixels

    def take_photo(self):  #adding subclass method
        return f"Taking a photo with {self.camera_mp}MP camera!"

# Example of using the CameraSmartphone class
my_camera_phone = CameraSmartphone("Samsung", "Galaxy S22", 256, 25, 108)
print(my_camera_phone.display_info())
print(my_camera_phone.take_photo())


