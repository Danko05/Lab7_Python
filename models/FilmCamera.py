from models.Camera import Camera


class FilmCamera(Camera):
    """
    A class that represents a film camera and inherits from the Camera class.
    """
    def __init__(self, brand, model, resolution, zoom, memory_card_type, photos_count, lens, film_type, film_ISO):
        """
        Initializes a new instance of the FilmCamera class.
        :param brand: The brand of the camera.
        :param model: The model of the camera.
        :param resolution: The resolution of the camera.
        :param zoom: The zoom of the camera.
        :param memory_card_type: The type of memory card used by the camera.
        :param photos_count: The number of photos taken by the camera.
        :param lens: The lens of the camera.
        :param film_type: The type of film used by the camera.
        :param film_ISO: The ISO of the film used by the camera.
        """
        super().__init__(model, resolution, zoom, memory_card_type, photos_count, brand, lens)
        self.film_type = film_type
        self.film_ISO = film_ISO

    def takePhotos(self):
        """
        Returns a string representation of the camera's film type and ISO.
        :return: A string representation of the camera's film type and ISO.
        """
        return f"FilmCamera:\nFilm Type: {self.film_type}\nFilm ISO: {self.film_ISO}"

    def __str__(self):
        """
        Returns a string representation of the FilmCamera instance.
        :return: A string representation of the FilmCamera instance.
        """
        return f"FilmCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count}))"
