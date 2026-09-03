# Animals

## Introduction

In this task, we will look at the advantage of abstract classes.

First, we start with a class `Animal` and the already known functionalities:

## Task

### 1. Animals Switch (animals_switch.py)
Fill in the open TODOs in the animals_switch.py file.

- Implement the `__init__` method of the `Animal` class.
- Implement the `make_sound` method of the `Animal` class. Distinguish between the animals `dog`, `cat`, `pig`, and `frog`, where the animals make the following sounds:
  - dog: Woof
  - cat: Miau
  - pig: Oink
  - frog: Quack
- Implement the `make_sound` method of the `Animal` class so that it outputs the sound of the respective animal. **Important:** Use the `match` statement for this.
- Override the `__repr__` method of the `Animal` class so that it outputs the name and age of the animal when printing an animal -> `print(dog)` should output `Name: Wuffi, Age: 7`.
- Implement the `create_animals_from_config(config_file)` function, which opens the config file (`animals.txt`) and creates the animals. The function should return a list of animals.

### Config File (animals.txt)
In the config file, the animals are listed with their type, name, and age, each separated by a space.

```json
dog Bernd 5
cat Mila 8
dog Dora 7
pig Josh 3
frog Fred 2
```

### 2. Animals Abstract (animals_abstract.py)
We now use the power of abstract classes to improve the `Animal` class and get rid of that annoying `match` statement (or similar `if` constructs).

Implement the `Animal` class as an abstract class and the classes `Dog`, `Cat`, `Pig`, and `Frog` as subclasses of `Animal`. The framework of the classes is already provided (with TODOs):
- Override the `__repr__` method of the `Animal` class so that it outputs the name and age of the animal when printing
- Implement the derived classes `Dog`, `Cat`, `Pig`, and `Frog` so that they output the sound of the respective animal (override make_sound)
- Write the `create_animal` method in the `AnimalFactory` class so that it creates and returns the appropriate animal.
- Implement the `create_animals_from_config` function which opens the config file and creates the animals. The function should return a list with the animals. Use the `AnimalFactory` class to create animals.

### 3. Testing the Implementation
- There is an animal of type `unicorn` which clearly does not exist. Both implementations should be able to handle this and output an appropriate error message. Run the program once with `animals.txt` and once with `exotic_animals.txt`.
- **Bonus:** Write the `create_animals_from_config` function so that it can handle non-existing animals at least for the `animals_abstract.py` implementation without terminating the program. Use a `try`-`except` statement for this (see below)

```python
try:
    # Code that might throw an error
except ValueError as e:
    # Code that is executed when an error occurs
```
