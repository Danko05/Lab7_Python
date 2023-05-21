from models.DigitalCamera import DigitalCamera
from models.FilmCamera import FilmCamera
from models.VideoCamera import VideoCamera
from models.MirrorlessCamera import MirrorlessCamera


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
            print(camera.takePhotos())
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


def main():
    """
    Creates an instance of the CameraManager class and adds several cameras to it,
    including instances of the DigitalCamera, FilmCamera, VideoCamera, and MirrorlessCamera classes.
    Finally, calls several methods on the manager instance to print information about the cameras
    and find cameras based on certain criteria.
    """
    manager = CameraManager()

    digital_camera1 = DigitalCamera("Sony", "EOS 5D Mark IV", "EF 24-105mm f/4L IS II USM", "1645x1647", 6.0, "SD",
                                    1000)
    digital_camera2 = DigitalCamera("Canon", "EOS ", "EF 24-105mm f/4L IS II USM", "1920x1080", 2.0, "SD", 100)
    manager.add_camera(digital_camera1)
    manager.add_camera(digital_camera2)

    film_camera1 = FilmCamera("Nikon", "F6", "1234x12421", 23, "SD", 600, "Nikkor 50mm f/1.8G", "35mm", 400)
    film_camera2 = FilmCamera("Canon", "F8", "1234x12421", 23, "SD", 2000, "Sony 50mm f/1.8G", "55mm", 70)
    manager.add_camera(film_camera1)
    manager.add_camera(film_camera2)

    videocamera1 = VideoCamera("Canon", "1213x234", 23, "SD", 2000, "Sony", "RTf", "GDyus", 24)
    videocamera2 = VideoCamera("Lumix", "3452x56584", 50, "SD", 5000, "fhjd", "fhdsjk", "fhudl", 78)
    manager.add_camera(videocamera1)
    manager.add_camera(videocamera2)

    mirrorlessCameras1 = MirrorlessCamera("Canon", "1234x124", 2, "SD", 1300, "MPEG-4", "ewtre", 250, "HD")
    mirrorlessCameras2 = MirrorlessCamera("Canon", "1234x124", 2, "SD", 700, "MPEG-4", "ewtre", 250, "HD")
    manager.add_camera(mirrorlessCameras1)
    manager.add_camera(mirrorlessCameras2)

    manager.print_cameras()
    manager.find_camera_by_model()
    manager.find_camera_with_photos_count_greater_than()


if __name__ == '__main__':
    main()
