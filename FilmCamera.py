

from Camera import Camera


class FilmCamera(Camera):
    def __init__(self, brand, model,resolution, zoom, memory_card_type, photos_count, lens, film_type, film_ISO):
        super().__init__(model, resolution, zoom, memory_card_type, photos_count, brand, lens)
        self.film_type = film_type
        self.film_ISO = film_ISO

    def takePhotos(self):
        return f"FilmCamera:\nFilm Type: {self.film_type}\nFilm ISO: {self.film_ISO}"

    def __str__(self):
        return f"FilmCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count}))"
