from abc import abstractmethod

from Camera import Camera


class DigitalCamera(Camera):
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type, photos_count):
        super().__init__(model, resolution, zoom, memory_card_type, photos_count, brand, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count

    def save_photo(self):
        super().save_photo()

    def erase_memory(self):
        super().erase_memory()

    def change_settings(self, resolution, zoom):
        super().change_settings(resolution, zoom)

    def takePhotos(self):
        return f"DigitalCamera:\nResolution: {self.resolution}\nZoom: {self.zoom}"

    def __str__(self):
        return f"DigitalCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count})"
