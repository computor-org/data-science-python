[enumerate]: <https://docs.python.org/3/library/functions.html#enumerate> "enumerate"
[here]: <https://realpython.com/python-f-strings/#doing-string-interpolation-with-f-strings-in-python> "f-strings"

# Control Structures: for Loops

## Introduction
This week you will receive an introduction to the `for` and `while` control structures in Python. So-called loops (*loops*) are among the most important components of source code in all common programming languages.
They generally serve to iterate over entries in lists, tuples, and arrays and then work with them. Proper handling therefore requires a basic understanding of Python arrays and their indexing.

In this task, you will write a program with a so-called `for-loop`. The syntax in Python looks something like this:

```python
for entry in mylist:
    do something with entry
```
It is very important that the lines to be executed during the `loop` are indented.

You can also iterate over the indices of an array or a list. For this, you can use the [enumerate] command. Here is an example:

```python
for index, entry in mylist:
    otherlist[index] = entry + 1
```

The attached py-files should serve as examples of how *for-loops* can be used.

## Task
In this task, you should read the file "climate_data_graz.csv", which contains the mean monthly temperatures of the years 2013 and 2023 in Graz (University location). It also contains the long-term monthly averages, which are calculated from the average of the years 1981-2010.
The first column contains the monthly averages for 2013, the second column the monthly averages for 2023, and the third column the long-term averages.

1. Read the file using `np.loadtxt` and name it `temp_file`. Make sure that you do not read the headers (first lines) along with it.
2. Declare the 2 variables `count_2013` and `count_2023` and assign them the value 0.
3. Now iterate with a for-loop over the rows of `temp_file` and check the following (with an if-statement):
   * If the monthly average of 2013 deviates by 2 or more degrees from the long-term average, increase the value of `count_2013` by one.
   * Proceed analogously for the monthly averages of 2023.
4. At the end, output an f-string containing the following text:
```python
f"Number of strongly deviating monthly averages in 2013: {count_2013}"
f"Number of strongly deviating monthly averages in 2023: {count_2023}"
```
Further information on using f-strings can be found [here].

## Hints
* Note that a deviation of +-2 can be smaller or larger than the monthly value.
* Pay attention to the correct indexing for the entries within the row.
* Source: <https://www.landesentwicklung.steiermark.at/>
