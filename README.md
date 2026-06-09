# Age Calculator

A Python application that calculates a person's age based on their birth date. The program provides detailed age information, including years, months, days, and total time measurements.

## Features

* Calculate exact age in years, months, and days
* Calculate total months lived
* Calculate total days lived
* Calculate total hours lived
* Calculate total seconds lived
* Includes both a basic and an improved implementation
* Input validation for birth dates

## Project Versions

### 1. Basic Version

**File:** `calculate age.py`

A beginner-friendly implementation that uses manual validation and custom age calculations.

### 2. Improved Version

**File:** `calculate age(improved).py`

A cleaner and more reliable implementation that utilizes Python's built-in `datetime` module.

## Project Structure

```text
Age-Calculator/
│
├── calculate age.py
├── calculate age(improved).py
├── README.md
└── LICENSE
```

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

Run either version from the terminal:

### Basic Version

```bash
python "calculate age.py"
```

### Improved Version

```bash
python "calculate age(improved).py"
```

## Example Input

```text
Enter birth date (YYYY-MM-DD): 2000-05-15
```

## Example Output

```text
You are 25 years, 3 months, and 10 days old.
Equals to 303 months, 9240 days, 221760 hours, 13305600 seconds.
```

## How It Works

1. The user enters a birth date in `YYYY-MM-DD` format.
2. The program validates the input.
3. The current date is retrieved.
4. The age difference is calculated.
5. Results are displayed in multiple formats.

## Future Improvements

* Graphical User Interface (GUI)
* Support for multiple calendar systems
* Export results to a text file
* More detailed date validation
* Interactive command-line menu

## License

This project is licensed under the MIT License.

## Author

**Mohammad Reza Bakhshandeh**

Electrical Engineering (Electronics) Graduate

Interested in Python Development, Computer Vision, Machine Learning, and Artificial Intelligence.
