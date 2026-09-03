# Dictionaries and JSON Files

## Introduction

When data is generated, for example in computer simulations, which subsequently needs to be
analyzed, it is advisable to store it temporarily and separate the analysis from the data
generation. One way to do this in a clear manner is to save Python dictionaries
in JSON files, which are readable as text files for humans and are syntactically
structured the same as dictionaries.

It should be noted that not all data types can be represented as text.
NumPy arrays, for example, must be converted to lists.

## Task

In this exercise unit, you write a script that exemplarily reads a JSON file with
configuration parameters and fills it with values calculated by you.

The script `generate_data.py` should read the file `data_file.json` with the [json] module as
dictionary `data`. Each entry in the dict `'sim_config'` consists of a set
of parameters for a specific calculation. In this example, these are the
means `mu`, standard deviations `sig`, and the sizes `size` of arrays of
normally distributed random numbers.

1. Generate the arrays and add them as dictionary `results` at the same
   level as `'sim_config'` and under the respective name of the simulation ('sim1',
   'sim2', ...).

1. Additionally, add the dictionary `'metadata'` with the current date and
   time (keys `'date'` and `'time'`) ([datetime]). Use the
   `"%Y-%m-%d"` and `"%H:%M"` format respectively. The resulting dict should therefore have the
   following structure:

   ```python
   {'sim_config': {...},
   'results': {'sim1': [...], 'sim2': [], ...},
   'metadata': {'date' : '...', 'time': '...'}
   }
   ```

1. Now save the nested dictionary in a file `results.json`. Writing
   works similarly to reading, where you must use the
   argument `"w"` instead of `"r"` when calling `open()` (write instead of read). Then
   use `json.dump(data, fp, indent=4)`.

[datetime]: https://docs.python.org/3/library/datetime.html
[json]: https://docs.python.org/3/library/json.html#basic-usage
