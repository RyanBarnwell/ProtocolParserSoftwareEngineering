# Running

From this directory, there are two options to run the parser:

Specifying the list of input values to the executable:

```
python app.py 1 2 3 4 5
```

Specifying the relative path to an examples file:

```
python app.py -f examples/example-1.txt
```

Input values in a test file are delimited by whitespace.

# Testing

The project will be graded using unit tests. After each phase, the tests used to grade the phase will be
added to your repository. You should ensure these tests continue to pass; you will be penalized if you break
previous tests in a subsequent phase.

For Python, all grading tests will be added to the file `grading_tests.py`. Do not change this file; it will
be overwritten each phase with the new grading tests. 

You are encouraged to write your own test cases. Simply follow the model in `grading_tests.py` and create a new
test suite.

To run the tests in a test file (in this example, using the provided `grading_tests.py`):
```
python grading_tests.py
```

# Notes

* Do not change any code in the `app.py` file.
* You have free rein on the rest of the application, you may create other methods, classes, or files as necessary. For simplicity, please keep new files in the same directory.
* Do not delete the existing `example-1.txt` file.
* Other test files may be added to the `examples` directory and committed to your repository.