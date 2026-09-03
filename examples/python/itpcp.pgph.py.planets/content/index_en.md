[Python-Classes]: <https://docs.python.org/3/tutorial/classes.html>
[Python-Objects]: <https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects>
[Python-Methods]: <https://docs.python.org/3/tutorial/classes.html#method-objects>
[Python-Inheritance]: <https://docs.python.org/3/tutorial/classes.html#inheritance>
[Python-Dunder-Methods]: <https://docs.python.org/3/reference/datamodel.html#special-method-names>

# Object-Oriented Programming in Python

## Introduction

In this introduction to object-oriented programming (OOP) with Python, we learn how to define simple classes, instantiate objects, and understand the basic concepts of OOP, such as method calls.

### Basics of Classes in Python

Classes are the building blocks for object-oriented programming in Python. A class is a template for objects that determines what attributes and methods the objects will have. Here is a simple example of a class in Python:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(self.value)
my_object = MyClass(10)
my_second_object = MyClass(20)
my_object.show_value()  # Outputs "10"
my_second_object.show_value()  # Outputs "20"
```

In this example, we have defined a class `MyClass` that stores a value and can output this value. The method `__init__` is a special constructor that is called when a new object of the class is created. This happens in the line `my_object = MyClass(10)`, where we create a new object `my_object` and pass it the value `10`. Then we call the method `show_value` to output the value of the object.

The `self` parameter is a reference to the object itself and is automatically passed to all methods. `self` references the attributes and methods of the object to which the method is applied. After we have created the attribute `value` in the method `__init__`, we can access it in the method `show_value` with `self.value`. `my_object.show_value()` thus returns the variable `value` of the object `my_object` and outputs `10`. `my_second_object.show_value()` returns the variable `value` of the object `my_second_object` and outputs `20`.

### Why Should I Use Classes

Classes are a powerful tool for modeling complex data structures and behaviors. They allow data and functions to be encapsulated and organized, leading to clearer and more maintainable code. Classes also enable efficient code reuse, as we will see later.

## Task

### 1. Planet Class - `planets_class.py`

We want to create a class that represents a planet and stores information such as mass, diameter, orbital period around the sun, and distance from the sun. This class should also contain methods to access this information.

Here is the specification for the problem:

1. Write a Python class named `Planet` that has the following attributes:

- `name`: Name of the planet (as a string)
- `mass`: Mass of the planet in kilograms (as a float)
- `diameter`: Diameter of the planet in kilometers (as a float)
- `orbital_period_around_sun`: Orbital period of the planet around the sun in days (as a float)
- `distance_from_sun`: Average distance of the planet from the sun in millions of kilometers (as a float)

2. The class should contain the following methods:

- `__init__(self, name, mass, diameter, orbital_period_around_sun, distance_from_sun)`: A constructor that initializes the attributes.
- `calc_avg_density(self)`: A method that calculates and returns the average density of the planet. The density of a planet is calculated by dividing the mass of the planet by its volume.

3. Use the following values for Earth as an example:

- Name: "Earth"
- Mass: 5.972 x 10^24 kg
- Diameter: 12.742 km
- Orbital period around the sun: 365.24 days
- Distance from the sun: 149.6 million km

4. Then create an object for Earth, save it in the variable `earth`.

5. Also create objects for Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune with the corresponding values.
Save the objects in the variables `mercury`, `venus`, `mars`, `jupiter`, `saturn`, `uranus`, and `neptune`.

- Mercury: 3.285 x 10^23 kg, 4.880 km, 87.97 days, 57.9 million km
- Venus: 4.867 x 10^24 kg, 12.104 km, 224.7 days, 108.2 million km
- Mars: 6.39 x 10^23 kg, 6.779 km, 686.98 days, 227.9 million km
- Jupiter: 1.898 x 10^27 kg, 139.822 km, 4,332.59 days, 778.6 million km
- Saturn: 5.683 x 10^26 kg, 116.464 km, 10,759.22 days, 1,433.5 million km
- Uranus: 8.681 x 10^25 kg, 50.724 km, 30,687.15 days, 2,872.5 million km
- Neptune: 1.024 x 10^26 kg, 49.244 km, 60,190.03 days, 4,495.1 million km

6. Which planet has the highest average density?
Save the name of the planet with the highest density in the variable `planet_with_highest_density`.

### 2. Dictionary - `planets_dict.py`

1. Write the same functionality as in the previous task, but this time use a dictionary and not a class to store the information about the planets.

Each planet should be its own dictionary and all planets should be stored in a parent dictionary `planets`.

Use the same values as in the previous task for the planets.

3. Calculate the average density of each planet and again save the name of the planet with the highest density in the variable `planet_with_highest_density`.
