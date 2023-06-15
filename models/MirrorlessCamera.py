from models.Camera import Camera


class MirrorlessCamera(Camera):
    """
    A class that represents a mirrorless camera and inherits from the Camera class.
    """
    def __init__(self, model, resolution, zoom, memory_card_type, photos_count,
                 brand, lens, weight, video_formats):
        """
        Initializes a new instance of the MirrorlessCamera class.
        :param model: The model of the camera.
        :param resolution: The resolution of the camera.
        :param zoom: The zoom of the camera.
        :param memory_card_type: The type of memory card used by the camera.
        :param photos_count: The number of photos taken by the camera.
        :param brand: The brand of the camera.
        :param lens: The lens of the camera.
        :param weight: The weight of the camera.
        :param video_formats: The video formats supported by the camera.
        """
        super().__init__(model, resolution, zoom, memory_card_type, photos_count,
                         brand, lens)
        self.weight = weight
        self.videoFormat = video_formats

    def takePhotos(self):
        """
        Returns a string representation of the camera's weight and video format.
        :return: A string representation of the camera's weight and video format.
        """
        return f"MirrorlessCamera:\nWeight:{self.weight}\nVideo_format:{self.videoFormat}"

    def __str__(self):
        """
        Returns a string representation of the MirrorlessCamera instance.
        :return: A string representation of the MirrorlessCamera instance.
        """
        return f"MirrorlessCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count})"
