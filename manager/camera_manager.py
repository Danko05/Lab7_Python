"""
Class file for
"""

from models.digital_camera import DigitalCamera
from models.film_camera import FilmCamera
from models.video_camera import VideoCamera
from models.mirrorless_camera import MirrorlessCamera
import logging


class CameraManager:
    """
    A class that manages a list of cameras.
    """

    cameras = []

    def add_camera(self, camera):
        """
        Adds a camera to the list of cameras.
        :param camera: The camera to add.
        """
        self.cameras.append(camera)

    def print_cameras(self):
        """
        Prints information about all the cameras in the list.
        """
        for camera in self.cameras:
            print(camera)
            print(camera.take_photos())
            print()

    def find_camera_by_model(self):
        """
        Finds and prints cameras with the model "Canon".
        """
        find_camera = filter(lambda camera: camera.model == "Canon", self.cameras)
        print("Camera with model Canon:")
        for camera in find_camera:
            print(camera)

    def find_camera_with_photos_count_greater_than(self):
        """
        Finds and prints cameras with a photos count greater than 1000.
        """
        find_camera = filter(lambda camera: camera.photos_count > 1000, self.cameras)
        print()
        print("Camera greater 1000 photos : ")
        for camera in find_camera:
            print(camera)

    def __len__(self):
        return len(self.cameras)

    def __getitem__(self, index):
        return self.cameras[index]

    def __iter__(self):
        return iter(self.cameras)

    def save_all_photo(self):
        return [camera.take_photos() for camera in self.cameras]

    def enumerate_cameras(self):
        print(list(enumerate(self.cameras)))

    def zip_cameras(self):
        print(list(zip(self.save_all_photo(), self.cameras)))

    def check_cameras(self):

        check_cameras = [camera.memory_card_type == "SD" for camera in self.cameras]
        return {"all": all(check_cameras), "any": any(check_cameras)}


class BrandTooShortError(ValueError):
    pass


def logged(exception, mode="console"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.DEBUG)
                    logging.exception(f"{func.__name__} raised an exception")
                elif mode == "file":
                    logging.basicConfig(filename="../Lab7_Python/file/logged.txt", level=logging.DEBUG)
                    logging.exception(f"{func.__name__} raised an exception")
                raise

        return wrapper

    return decorator


@logged(BrandTooShortError, mode="file")
def validate_brand(brand):
    if len(brand) <= 3:
        raise BrandTooShortError(brand)


validate_brand("QIHE")


def main():
    """
    Creates an instance of the CameraManager class and adds several cameras to it,
    including instances of the DigitalCamera, FilmCamera, VideoCamera, and MirrorlessCamera classes.
    Finally, calls several methods on the manager instance to print information about the cameras
    and find cameras based on certain criteria.
    """
    manager = CameraManager()

    digital_camera1 = DigitalCamera("Sony", "EOS 5D Mark IV", "EF 24-105mm f/4L IS II USM",
                                    "1645x1647", 6.0, "SD", 1000)
    digital_camera2 = DigitalCamera("Canon", "EOS ", "EF 24-105mm f/4L IS II USM",
                                    "1920x1080", 2.0, "SD", 100)
    manager.add_camera(digital_camera1)
    manager.add_camera(digital_camera2)

    film_camera1 = FilmCamera("Nikon", "F6", "1234x12421", 23, "SD", 600,
                              "Nikkor 50mm f/1.8G", "35mm", 400)
    film_camera2 = FilmCamera("Canon", "F8", "1234x12421", 23, "FD", 2000,
                              "Sony 50mm f/1.8G", "55mm", 70)
    manager.add_camera(film_camera1)
    manager.add_camera(film_camera2)

    video_camera1 = VideoCamera("Canon", "1213x234", 23, "SD", 2000,
                                "Sony", "RTf", "GDyus", 24)
    video_camera2 = VideoCamera("Lumix", "3452x56584", 50, "SD", 5000,
                                "fhjd", "fhdsjk", "fhudl", 78)
    manager.add_camera(video_camera1)
    manager.add_camera(video_camera2)

    mirrorless_сamera1 = MirrorlessCamera("Canon", "1234x124", 2, "SD", 1300,
                                          "MPEG-4", "ewtre", 250, "HD")
    mirrorless_сamera2 = MirrorlessCamera("Canon", "1234x124", 2, "SD", 700,
                                          "MPEG-4", "ewtre", 250, "HD")
    manager.add_camera(mirrorless_сamera1)
    manager.add_camera(mirrorless_сamera2)

    manager.print_cameras()

    manager.find_camera_by_model()

    manager.find_camera_with_photos_count_greater_than()

    print("\n Enumerate obj :")
    (manager.enumerate_cameras())

    print("\n Obj with method takePhotos :")
    print(manager.save_all_photo())

    print("\n Obj with def 'save_all_photos':")
    (manager.zip_cameras())

    print("\n Check cameras for memory card type:")
    print(manager.check_cameras())

    print("\n All attribute by type int :")
    attribute = digital_camera2.get_attributes_by_type(int)
    print(attribute)

    print(manager[2])


if __name__ == '__main__':
    main()
