from Camera import Camera


class MirrorlessCamera(Camera):
    def __init__(self, model, resolution, zoom, memory_card_type, photos_count,
                 brand, lens, weight, video_formats):
        super().__init__(model, resolution, zoom, memory_card_type, photos_count,
                         brand, lens, )
        self.weight = weight
        self.videoFormat = video_formats

    def takePhotos(self):
        return f"MirrorlessCamera:\nWeight:{self.weight}\nVideo_format:{self.videoFormat}"

    def __str__(self):
        return f"MirrorlessCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count})"
