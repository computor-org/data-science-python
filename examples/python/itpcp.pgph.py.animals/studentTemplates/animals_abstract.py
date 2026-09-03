from abc import ABC, abstractmethod


class Animal(ABC):
    """Base Class for all animals

    Args:
        ABC (ABC): Abstract Base Class

    Raises:
        NotImplementedError: Is thrown when a subclass does not implement the make_sound method
    """

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("Please implement this method in a subclass")

    # TODO: overwrite __repr__ method to return the name and the age of the animal in a string


# TODO: Implement the all animal classes which are given in the Config file.


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        pass  # TODO: Implement this method


def create_animals_from_config(config_file):
    pass  # TODO: Implement this method


if __name__ == "__main__":
    # You may change this here if you want to test other config files
    # maybe you have to change this path depending on your root directory
    config_file = "animals_config.txt"
    animals = create_animals_from_config(config_file)
    for animal in animals:
        print(animal)  # introduce the animal
        print(animal.make_sound())  # make the animal sound
