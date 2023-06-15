class Camera:


    """
    A class representing a camera.
    Attributes:
    - model (str): The model of the camera. Default is "Canon".
    - resolution (str): The resolution of the camera. Default is "2134x5784".
    - zoom (int): The zoom level of the camera. Default is 23.
    - memoryCardType (str): The type of memory card used by the camera. Default is "SD".
    - photosCount (int): The number of photos taken by the camera. Default is 2000.
    """

instance = None


def __init__(self, model="Canon", resolution="2134x5784", zoom=23, memoryCardType="SD", photosCount=2000):
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
    self.resolution = resolution
    self.zoom = zoom
    self.memoryCardType = memoryCardType
    self.photosCount = photosCount


def resetZoom(self):
    """
    Resets the zoom level of the camera to 1.0.
    """
    self.zoom = 1.0


def savePhoto(self):
    """
    Increments the number of photos taken by the camera by 1.
    """
    self.photosCount += 1


def eraseMemory(self):
    """
    Resets the number of photos taken by the camera to 0.
    """
    self.photosCount = 0


def changeSettings(self, resolution, zoom):
    """
    Changes the resolution and zoom level of the camera.

    Args:
    - resolution (str): The new resolution of the camera.
    - zoom (int): The new zoom level of the camera.
    """
    self.resolution = resolution
    self.zoom = zoom


@staticmethod
def getInstance():
    """
    Returns a singleton instance of the Camera class.
    If an instance does not already exist, one is created.

    Returns:
    - Camera: The singleton instance of the Camera class.
    """
    if Camera.instance is None:
        Camera.instance = Camera()
    return Camera.instance


def __str__(self):
    """
    Returns a string representation of the Camera instance.

    Returns:
    - str: A string representation of the Camera instance.
    """
    return f"Camera(model={self.model}, resolution={self.resolution}, zoom={self.zoom}, " \
           f"memoryCardType={self.memoryCardType}, photosCount={self.photosCount})"


camera1 = Camera("Sony", "2134x5784", 50, "SD", 5000)
camera2 = Camera()
camera3 = Camera.getInstance()
camera4 = Camera.getInstance()
cameras = [camera1, camera2, camera3, camera4]

for camera in cameras:
    print(camera)
