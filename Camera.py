from abc import ABC, abstractmethod


class Camera(ABC):
    """
    A class representing a camera.
    Attributes:
    - model (str): The model of the camera. Default is "Canon".
    - resolution (str): The resolution of the camera. Default is "2134x5784".
    - zoom (int): The zoom level of the camera. Default is 23.
    - memoryCardType (str): The type of memory card used by the camera. Default is "SD".
    - photosCount (int): The number of photos taken by the camera. Default is 2000.
    """

    __instance = None

    def __init__(self, model, resolution, zoom, memory_card_type, photos_count,
                 brand, lens):
        """
        Initializes a Camera instance with the given attributes.

        Args:
        - model (str): The model of the camera.
        - resolution (str): The resolution of the camera.
        - zoom (int): The zoom level of the camera.
        - memoryCardType (str): The type of memory card used by the camera.
        - photosCount (int): The number of photos taken by the camera.
        """
        self.model = model
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count
        self.brand = brand
        self.lens = lens

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

    @staticmethod
    def get_instance():
        """
        Returns a singleton instance of the Camera class.
        If an instance does not already exist, one is created.

        Returns:
        - Camera: The singleton instance of the Camera class.
        """
        if Camera.__instance is None:
            Camera.__instance = Camera()
        return Camera.__instance

    def __str__(self):
        """
        Returns a string representation of the Camera instance.

        Returns:
        - str: A string representation of the Camera instance.
        """
        return f"Camera(model={self.model}, resolution={self.resolution}, zoom={self.zoom}, " \
               f"memory_card_type={self.memory_card_type}, photosCount={self.photos_count})"

    def main(self):
        cameras = [
            Camera("Sony", "2134x5784", 50, "SD", 5000),
            Camera(),
            Camera.get_instance(),
            Camera.get_instance(),
        ]

        for camera in cameras:
            print(camera)

    @abstractmethod
    def takePhotos(self):
        pass
