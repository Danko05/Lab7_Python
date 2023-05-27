# pylint: disable = import-error
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

    def __init__(self, brand, model, lens):
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
        self.brand = brand
        self.lens = lens
        self.the_most_popular_brands_set = set()

    def __iter__(self):
        return iter(self.the_most_popular_brands_set)

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

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
        return f"Camera(model={self.model})"

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
