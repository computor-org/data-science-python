class Animal:
    def __init__(self, animal_type, name, age):
        # TODO
        pass

    def make_sound(self):
        # TODO use match statement to return the right sound for the animal
        pass

    # TODO overwrite __repr__ method to return the name and the age of the animal in a string


def create_animals_from_config(config_file):
    # TODO: Implement this method
    pass


if __name__ == "__main__":
    # You may change this here if you want to test other config files
    # maybe you have to change this path depending on your root directory
    config_file = "animals.txt"
    animals = create_animals_from_config(config_file)
    for animal in animals:
        print(animal)  # introduce the animal
        print(animal.make_sound())  # make the animal sound
