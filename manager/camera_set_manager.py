from models.digital_camera import DigitalCamera
from models.film_camera import FilmCamera
from models.video_camera import VideoCamera
from models.mirrorless_camera import MirrorlessCamera
from manager.camera_manager import CameraManager, logged
import re
import datetime


class CameraSetManager:
    def __init__(self, camera_manager):
        self.cameras = camera_manager
        self.index = 0

    def __len__(self):
        return len(list(iter(self)))

    def __iter__(self):
        self.camera_set_list = []
        for camera in self.cameras:
            for words in camera.the_most_popular_brands_set:
                self.camera_set_list.append(words)
        return iter(self.camera_set_list)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        return self.camera_set_list[index]

    def __next__(self):
        if self.index >= len(self.camera_set_list):
            raise StopIteration
        s_d = self.camera_set_list[self.index]
        self.index += 1
        return s_d

    @staticmethod
    def snake_case(self):
        """
        Decorator to check if a method name follows the snake_case style.

        :param self: method to check
        :return: wrapper around the method to check
        :raises ValueError: if the method name does not follow the snake_case style
        """

        def wrapper(*args, **kwargs):
            if re.match(r'^[a-z]+(_[a-z]+)*$', self.__name__):
                return self(*args, **kwargs)
            else:
                raise ValueError

        return wrapper

    @snake_case
    def check_method_by_snake_case(self):
        """
        Prints "Method snake_case" if the method name follows the snake_case style.
        """
        print("Method snake_case")
    def save_history(self):
        """
        Decorator to save the history of method calls.

        :return: wrapper around the method to save its history
        """

        def wrapper(*args, **kwargs):
            result = self(*args, **kwargs)
            with open("../manager/history.txt", "a") as d:
                d.write(f'{self.__name__} was called at {datetime.datetime.now()}\n')
            return result

        return wrapper

    @save_history
    def history_and_time(self):
        """
        Prints "Method called" and saves its history.
        """
        print("Method called")


def main():
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

    set_manager = CameraSetManager(manager)

    print("The length of the new list:")
    print(len(set_manager))
    print()
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    manager.add_camera(digital_camera2)
    print(len(set_manager))
    print("getitem:")
    print(set_manager[0])

    set_manager.check_method_by_snake_case()
    set_manager.history_and_time()


if __name__ == '__main__':
    main()
