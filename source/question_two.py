"""Question two for an executable examination."""

from typing import Any
from typing import Callable
from typing import Tuple

# TODO: Question 2a. {{{

# Instructions:
# Repair the source code lines in this function
# so that it operates in the specified fashion.

# Function description:
# The function calculate_quadratic_equation_roots should:
# --> Compute the "roots" of a quadratic equation
# --> Return two roots even if they are the same number
# --> Perform the computation so that it accepts three inputs
#     that are of type float and returns the two roots as a float
# --> Return the root called x_one first and the root called x_two second
# --> Package both of the returned roots in a tuple using the notation (x_one, x_two)
# --> For instance,
#     -- the inputs of 1, 2, and 1 should return the output of (-1.0, -1.0)


def calculate_quadratic_equation_roots(a: float, b: float, c: float) -> Tuple[float, float]:
    """Calculate roots of quadratic equation."""
    D = (b * b - 4 * a * c) ** 5.0
    x_one = (b + D) / (2 * a)
    x_two = (b - D) / (2 * a)
    return (x_two, x_one)


def question_two_a():
    """Run question two-a."""
    # Do not edit this function
    question_two_output_a = str(calculate_quadratic_equation_roots(1, 2, 1))
    return question_two_output_a

# }}}

# TODO: Question 2b. {{{

# Instructions:
# Fix the defect(s) in one of the following functions
# Provide an implementation of one of the following functions

# Function description:
# The function compute_square should:
# --> Accept as input a variable called number of type int
# --> Compute and return the square of the number, as an int, through multiplication
# --> For instance, an input of 5 would produce the output of 25

# Function description:
# The function call_twice should:
# --> Accept as input a variable called number of type int
# --> Accept as input a function called f that is of type Callable
# --> Call the provided function f two times with the input number
# --> For instance, an input of 5 would produce the output of 625


def compute_square(number: int) -> int:
    """Compute the square of a number using multiplication."""
    return 0


def call_twice(f: Callable[[int], int], number: int) -> int:
    """Call the provided function with the input number two times."""
    return f(number)


def question_two_b():
    """Run question two-b."""
    # Do not edit this function
    space = " "
    question_two_output_b = str(call_twice(compute_square, 5))
    question_two_output_b = question_two_output_b + space + str(call_twice(compute_square, -5))
    question_two_output_b = question_two_output_b + space + str(call_twice(compute_square, 0))
    return question_two_output_b

# }}}

# TODO: Question 2c. {{{

# Instructions:
# Implement functions to produce the requested output

# Function description:
# The function convert_to_str should:
# --> Accept as input a value of any data type
# --> Convert the value to the type of string (i.e., str)
# --> Return the converted value
# --> For instance, if the function receives 5 as
#     an input it returns the value of "5"

# Function description:
# The function determine_if_str should:
# --> Accept as input a value of any data type
# --> Determine whether or not the provided value is a string
# --> If the value is a string, it should return True
# --> Otherwise, it should return False
# --> For instance, if the function receives 5 as
#     an input it returns False
# --> For instance, if the function receives "5" as
#     an input it returns True


def convert_to_str(value: Any) -> str:
    """Convert the provided value to a string."""
    return value


def determine_if_str(value) -> bool:
    """Determine whether or not a provided value is a string."""
    return False


def question_two_c():
    """Run question two-c."""
    # Do not edit this function
    space = " "
    question_two_output_c = str(determine_if_str(5))
    question_two_output_c = question_two_output_c + space + str(determine_if_str(convert_to_str(5)))
    question_two_output_c = question_two_output_c + space + str(determine_if_str(convert_to_str(5.5)))
    return question_two_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_two():
    """Run all of the subquestions in question two."""
    # call the function for question two-a
    output = question_two_a()
    print(output)
    # call the function for question two-b
    output = question_two_b()
    print(output)
    # call the function for question two-c
    output = question_two_c()
    print(output)


if __name__ == "__main__":
    run_question_two()
