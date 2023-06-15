from models.Camera import Camera


class DigitalCamera(Camera):
    """
    A class that represents a digital camera and inherits from the Camera class.
    """
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type, photos_count):
        """
        Initializes a new instance of the DigitalCamera class.
        :param brand: The brand of the camera.
        :param model: The model of the camera.
        :param lens: The lens of the camera.
        :param resolution: The resolution of the camera.
        :param zoom: The zoom of the camera.
        :param memory_card_type: The type of memory card used by the camera.
        :param photos_count: The number of photos taken by the camera.
        """
        super().__init__(model, resolution, zoom, memory_card_type, photos_count, brand, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count

    def save_photo(self):
        """
        Saves a photo taken by the camera.
        """
        super().save_photo()

    def erase_memory(self):
        """
        Erases the memory card of the camera.
        """
        super().erase_memory()

    def change_settings(self, resolution, zoom):
        """
        Changes the settings of the camera.
        :param resolution: The new resolution to set.
        :param zoom: The new zoom to set.
        """
        super().change_settings(resolution, zoom)

    def takePhotos(self):
        """
        Returns a string representation of the camera's resolution and zoom.
        :return: A string representation of the camera's resolution and zoom.
        """
        return f"DigitalCamera:\nResolution: {self.resolution}\nZoom: {self.zoom}"

    def __str__(self):
        """
        Returns a string representation of the DigitalCamera instance.
        :return: A string representation of the DigitalCamera instance.
        """
        return f"DigitalCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count})"
