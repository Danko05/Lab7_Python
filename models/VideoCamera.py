from models.Camera import Camera


class VideoCamera(Camera):
    """
    A class that represents a video camera and inherits from the Camera class.
    """
    def __init__(self, model, resolution, zoom, memory_card_type, photos_count,
                 brand, lens, videoFormat, matrixSize):
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
        super().__init__(model, resolution, zoom, memory_card_type, photos_count, brand, lens)
        self.videoFormat = videoFormat
        self.matrixSize = matrixSize

    def takePhotos(self):
        """
        Returns a string representation of the camera's video format and matrix size.
        :return: A string representation of the camera's video format and matrix size.
        """
        return f"VideoCamera:\nVideoFormat:{self.videoFormat}\nMatrixSize:{self.matrixSize})"

    def __str__(self):
        """
        Returns a string representation of the VideoCamera instance.
        :return: A string representation of the VideoCamera instance.
        """
        return f"VideoCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count})"
