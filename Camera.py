class Camera:
    instance = None

    def __init__(self, model="Canon", resolution="2134x5784", zoom=23, memoryCardType="SD", photosCount=2000):
        self.model = model
        self.resolution = resolution
        self.zoom = zoom
        self.memoryCardType = memoryCardType
        self.photosCount = photosCount

    def resetZoom(self):
        self.zoom = 1.0

    def savePhoto(self):
        self.photosCount += 1

    def eraseMemory(self):
        self.photosCount = 0

    def changeSettings(self, resolution, zoom):
        self.resolution = resolution
        self.zoom = zoom

    @staticmethod
    def getInstance():
        if Camera.instance is None:
            Camera.instance = Camera()
        return Camera.instance

    def __str__(self):
        return f"Camera(model={self.model}, resolution={self.resolution}, zoom={self.zoom}, memoryCardType={self.memoryCardType}, photosCount={self.photosCount})"


camera1 = Camera("Sony", "2134x5784", 50, "SD", 5000)
camera2 = Camera()
camera3 = Camera.getInstance()
camera4 = Camera.getInstance()
cameras = [camera1, camera2, camera3, camera4]

for camera in cameras:
    print(camera)