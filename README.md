[![CircleCI](https://circleci.com/gh/ikostan/Exercism_Python_Track.svg?style=svg)](https://circleci.com/gh/ikostan/Exercism_Python_Track)
[![Build Status](https://travis-ci.org/ikostan/Exercism_Python_Track.svg?branch=master)](https://travis-ci.org/ikostan/Exercism_Python_Track)
[![codecov](https://codecov.io/gh/ikostan/Exercism_Python_Track/branch/master/graph/badge.svg)](https://codecov.io/gh/ikostan/Exercism_Python_Track)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

# Exercism Python Track

<div align="center"> 
<img width="10%" height="10%" src="https://github.com/ikostan/Exercism_Python_Track/blob/master/img/exercism-logo.png" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/Exercism_Python_Track/blob/master/img/python-track.png" hspace="20">
</div>

## Exercism exercises in Python


### What is Exercism?
Exercism is an online platform designed to help you improve your coding skills through practice and mentorship.

Exercism provides you with thousands of exercises spread across numerous language tracks. Once you start a language track you are presented with a core set of exercises to complete. Each one is a fun and interesting challenge designed to teach you a little more about the features of a language.

You complete a challenge by downloading the exercise to your computer and solving it in your normal working environment. Once you've finished you submit it online and one of our mentors will give you feedback on how you could improve it using features of the language that you may not be familiar with. After a couple of rounds of refactoring, your exercise will be complete and you will unlock both the next core exercise and also a series of related side-exercises for you to practice with.

Exercism is entirely open source and relies on the contributions of thousands of wonderful people, including our leadership team, our mentors, our track maintainers, and thousands of contributors.

Exercism is designed to be fun and friendly, and we place a strong emphasis on empathetic communication. If you have any questions or concerns about Exercism, you can browse our FAQs or contact us.

Sign up and have fun. Exercism is 100% free :)


## Getting Started
We know using a new product can be daunting, and Exercism is a little complicated. So here's a really simple set of instructions to get you started. [Click here for help](https://exercism.io/getting-started)

### [Exercism installation guide](https://exercism.io/cli-walkthrough)<br/>
This guide was created in order to help you get started learning with Exercism. Answer a few questions, follow a few instructions, and you should be ready in no time!

### [Installer for the Latest Exercism Windows CLI](https://github.com/exercism/windows-installer/releases/tag/v1.5.3)

### [Configuring the CLI](https://exercism.io/cli-walkthrough)

### Download exercise
- You should now have the CLI installed.
- Download the exercise using:<br/>
    ```exercism download --exercise=<exercise name> --track=python```

### Submit your solution
- You should now have the CLI installed and the exercise downloaded to your computer. 
- Solve the exercise and then upload it using:<br/> 
    ```exercism submit /PATH/TO/SOLUTION```
- In your web-browser, go back to the language tracks page, choose your exercise and the exercise you've just worked on. You will now see your solution online and notice that it is awaiting a mentor.

### Testing

All exercises must be compatible with Python versions 2.7 and 3.4 upwards.

To test a single exercise (e.g., with Python 2.7):
```
python2.7 test/check-exercises.py [exercise-name]
```

To test all exercises (e.g., with Python 3):
```
python3 test/check-exercises.py
```

### Code Style

The Python code in this repo is meant to follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) (a stylized version http://pep8.org).

This repo uses [flake8](http://flake8.readthedocs.org/en/latest/) with default settings to enforce the coding standard.

### Setting up Python3 virtual environment on Windows machine:

1. open CMD
2. navigate to project directory, for example:<br/> 
```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```
3. run following command:<br/> 
```bash 
pip install virtualenv
```
4. run following command:<br/> 
```bash 
virtualenv venv --python=python
```

### How to delete multiples files in Git:

- In the command-line, navigate to your local repository.
- Ensure you are in the default branch:<br/> 
```bash 
git checkout master
```
- The rm -r command will recursively remove your folder:<br/> 
```bash 
git rm -r folder-name
```
- Commit the change:<br/> 
```bash 
git commit -m "Remove duplicated directory"
```
- Push the change to your remote repository:<br/> 
```bash 
git push origin master
```

### How to fix in case .gitignore is ignored by Git:
Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 
**NOTE:** First commit your current changes, or you will lose them.<br/> 
Then run the following commands from the top folder of your Git repository:<br/> 
```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```

### More help:
[pip nstallation and upgrade](https://pip.pypa.io/en/stable/installing/)

