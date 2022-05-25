# Taylor Expansion ML Project
The goal of this project is to use Machine Learning to get the Taylor expansion of a function.

This is performed in the form of a Natural Languge Processing task.
Random functions are generated using my module [RandomFunctionGenerator](https://github.com/BoGGoG/RandomFunctionGenerator) and saved as strings.

# Prefix Notation
In `data_preparation.py` there are now functions to convert a sympy expression to 
prefix notation and back.
A notebook showing off the prefix notation is in `notebooks/2022-05-25-PrefixNotation.ipynb`.

There are also quite a few tests for this in `/tests` that can be executed as following:
- all tests: In the root folder in the terminal: `pytest`
- specific tests: In the root folder in the terminal: `pytest -k test_names`, where `test_names` can either be the name of the test file or the name of a function in one of the test files
