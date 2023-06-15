# pylint: disable = import-error
from models.Camera import Camera


class VideoCamera(Camera):
    """
    A class that represents a video camera and inherits from the Camera class.
    """

    def __init__(self, model, resolution, zoom, memory_card_type, photos_count,
                 brand, lens, video_format, matrix_size):
        """
        Initializes a new instance of the VideoCamera class.
        :param model: The model of the camera.
        :param resolution: The resolution of the camera.
        :param zoom: The zoom of the camera.
        :param memory_card_type: The type of memory card used by the camera.
        :param photos_count: The number of photos taken by the camera.
        :param brand: The brand of the camera.
        :param lens: The lens of the camera.
        :param videoFormat: The video format used by the camera.
        :param matrixSize: The size of the matrix used by the camera.
        """
        super().__init__(brand, model, lens)
        self.video_format = video_format
        self.matrix_size = matrix_size
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count
        self.the_most_popular_brands_set = {"Olimp", "Nikon"}

    def takePhotos(self):
        """
        Returns a string representation of the camera's video format and matrix size.
        :return: A string representation of the camera's video format and matrix size.
        """
        return f"Video_camera:\nVideo_format:{self.video_format}\nMatrix_size:{self.matrix_size})"

    def __str__(self):
        """
        Returns a string representation of the VideoCamera instance.
        :return: A string representation of the VideoCamera instance.
        """
        return f"VideoCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.memory_card_type}, " \
               f"photos_count={self.photos_count})"

    def __repr__(self):
        return f"Video_camera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.memory_card_type}, " \
               f"photos_count={self.photos_count})"
