"""Question five for an executable examination."""


# TODO: Question 5a. {{{

# Instructions:
# Implement the requested function so that it operates in the specified fashion

# Function description:
# The function perform_subtraction should:
# --> Accept as input two floating-point values called input_one and input_two
# --> Subtract the value of the second input value from the first input value
# --> It should work correctly regardless of whether the numbers are positive or negative
# --> It should always perform the computation with floating point values, not integer values
# --> The following examples illustrate how this function should work:
#     Input: 1.0 and 1.0
#     Output: 0.0
#     Input: 2.0 and -2.0
#     Output: 4.0


def perform_subtraction(input_one: float, input_two: float) -> float:
    """Subtract the value stored in the second input from the value in the first input."""
    subtraction_output = 0
    return subtraction_output


def question_five_a():
    """Run question five-a."""
    # Do not edit this function
    space = " "
    question_five_output_a = str(perform_subtraction(1.0, 1.0))
    question_five_output_a = question_five_output_a + space + str(perform_subtraction(2.0, -2.0))
    question_five_output_a = question_five_output_a + space + str(perform_subtraction(0.0, 2.0))
    return question_five_output_a


# }}}

# TODO: Question 5b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function get_maximum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is greater than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two


def get_maximum(input_one: int, input_two: int) -> int:
    """Return the maximum value of two input values."""
    if input_one == input_two:
        return input_two
    return input_one


def question_five_b():
    """Run question five-b."""
    # Do not edit this function
    space = " "
    question_five_output_b = str(get_maximum(12, 10))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 9))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 3))
    return question_five_output_b

# }}}

# TODO: Question 5c. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function get_minimum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is less than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two


def get_minimum(input_one: int, input_two: int) -> int:
    """Return the minimum value of two input values."""
    if input_two <= 0:
        return input_one
    return 0


def question_five_c():
    """Run question five-b."""
    # Do not edit this function
    space = " "
    question_five_output_b = str(get_minimum(12, 10))
    question_five_output_b = question_five_output_b + space + str(get_minimum(3, 9))
    question_five_output_b = question_five_output_b + space + str(get_minimum(2, 2))
    return question_five_output_b

# }}}

# }}}

# Do not edit any of the source code below this line


def run_question_five():
    """Run all of the subquestions in question five."""
    # call the function for question five-a
    output = question_five_a()
    print(output)
    # call the function for question five-b
    output = question_five_b()
    print(output)
    # call the function for question five-c
    output = question_five_c()
    print(output)


if __name__ == "__main__":
    run_question_five()
