# Introduction
The classical introductory exercise. Just say "Hello, World!".

"Hello, World!" is the traditional first program for beginning programming in a new language or environment.

### The objectives are simple:

- Write a function that returns the string "Hello, World!".<br/>
- Run the test suite and make sure that it succeeds.<br/>
- Submit your solution and check it at the website.<br/>
If everything goes well, you will be ready to fetch your first real exercise.

### Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")

### Running the tests
To run the tests, run the appropriate command below (why they are different):

Python 2.7: py.test hello_world_test.py
Python 3.4+: pytest hello_world_test.py
Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version): python -m pytest hello_world_test.py

### Common pytest options
-v : enable verbose output
-x : stop running tests on first failure
--ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h

### Submitting Exercises
Note that, when trying to submit an exercise, make sure the solution is in the $EXERCISM_WORKSPACE/python/hello-world directory.

You can find your Exercism workspace by running exercism debug and looking for the line that starts with Workspace.

For more detailed information about running tests, code style and linting, please see Running the Tests.

### Source
This is an exercise to introduce users to using Exercism http://en.wikipedia.org/wiki/%22Hello,_world!%22_program

### Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.

### Get started

1. Download:<br/>
exercism download --exercise=hello-world --track=python

2. Solve:<br/>
Use your code editor to solve the problem locally.

3. Submit:<br/>
exercism submit /path/to/file [/path/to/file2 ...]
Still stuck?
These guides should help you.


