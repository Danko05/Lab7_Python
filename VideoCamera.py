from Camera import Camera

class VideoCamera(Camera):
    def __init__(self,  model, resolution, zoom, memory_card_type, photos_count,
                 brand, lens, videoFormat, matrixSize):
        super().__init__(model, resolution, zoom, memory_card_type, photos_count, brand, lens)
        self.videoFormat = videoFormat
        self.matrixSize = matrixSize

    def takePhotos(self):
        return f"VideoCamera:\nVideoFormat:{self.videoFormat}\nMatrixSize:{self.matrixSize})"
    def __str__(self):
        return f"VideoCamera(resolution={self.resolution}, zoom={self.zoom}, memory_card_type={self.erase_memory}, " \
               f"photos_count={self.photos_count})"