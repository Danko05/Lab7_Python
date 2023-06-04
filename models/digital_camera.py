# pylint: disable = import-error
from models.camera import Camera


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
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count
        self.the_most_popular_brands_set = {"Canon", "Sony"}

    def reset_zoom(self):
        """
        Resets the zoom level of the camera to 1.0.
        """
        self.zoom = 1.0

    def save_photo(self):
        """
        Increments the number of photos taken by the camera by 1.
        """
        self.photos_count += 1
        return self.photos_count

    def erase_memory(self):
        """
        Resets the number of photos taken by the camera to 0.
        """
        self.photos_count = 0

    def change_settings(self, resolution, zoom):
        """
        Changes the resolution and zoom level of the camera.

        Args:
        - resolution (str): The new resolution of the camera.
        - zoom (int): The new zoom level of the camera.
        """
        self.resolution = resolution
        self.zoom = zoom

    def take_photos(self):
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
        return f"DigitalCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.memory_card_type}, " \
               f"photos_count={self.photos_count})"

    def __repr__(self):
        return f"Digital_camera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.memory_card_type}, " \
               f"photos_count={self.photos_count})"

