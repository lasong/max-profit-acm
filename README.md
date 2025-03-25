# Restructuring Calculator

A Python application that calculates the maximum profit for the restructuring problem as described in problemF.pdf.

## Problem Description

The full problem description can be found in the file `problemF.pdf` included in this repository.

## Setup

1. Ensure you have Python 3.x installed
2. Clone this repository
3. No additional dependencies are required - the application uses only standard Python libraries

### Setting up a Virtual Environment (recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# When you're done, you can deactivate the virtual environment
deactivate
```

## Usage

Run the application with an input file:

```bash
python main.py <input_file>
```

### Input Format

The input file should adhere to the following format:

- Each test case starts with a line containing three integers: N, C, D
  - N: Number of machines
  - C: Initial capital
  - D: Number of days
- The next N lines each contain four integers: Di, Pi, Ri, Gi
  - Di: Day the machine becomes available
  - Pi: Price of the machine
  - Ri: Resale value
  - Gi: Daily profit generated
- A line with three zeros (0 0 0) terminates the input

### Example Input

See the provided `input.txt` file for an example input dataset.

### Output

For each test case, the application outputs the maximum possible profit achievable.

## Project Structure

- `main.py`: Entry point for the application
- `input_reader.py`: Handles reading and parsing input files
- `restructuring_calculator.py`: Contains the core logic for calculating maximum profit

## Development Notes

This project was completed in 4 hours.

