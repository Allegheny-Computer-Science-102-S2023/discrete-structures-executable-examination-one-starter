"""Question three for an executable examination."""

from typing import List

# TODO: Question 3a. {{{

# Instructions:
# Implement a function so that it operates in the specified fashion

# Function description:
# The function compute_mean should:
# --> Accept as input a list of int values and produce a float that
#     is the arithmetic mean (i.e., the average) of the values
# --> The following examples illustrate the inputs and outputs of this function:
#     Input: [0, 0, 0]
#     Output: 0.0
#     Input: [1, 1, 1]
#     Output: 1.0
# Note that you may implement any appropriate approach for computing the
# arithmetic mean (even by using functions built-in to the Python language)


def compute_mean(numbers: List[int]) -> float:
    """Compute the mean of a list of int numbers and return it as a float."""
    mean = 0
    return mean


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    space = " "
    question_two_output_a = str((compute_mean([1, 1, 1])))
    question_two_output_a = question_two_output_a + space + str((compute_mean([0, 0, 0])))
    question_two_output_a = question_two_output_a + space + str((compute_mean([10, 10, 7])))
    return question_two_output_a

# }}}

# Question 3b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function convert_list should:
# --> Accept as input a variable called input_list that contains a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a list of all the converted int values
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output [5, 7, 9, 11]


def convert_list(input_list: List[str]) -> List[int]:
    """Convert a list of strings to a list of int values."""
    output_list_int = []
    for input_value in input_list:
        input_value_int = int(input_value)
    return output_list_int


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    question_tree_output_b = convert_list(['5', '7', '9', '11'])
    return question_tree_output_b

# }}}

# Question 3c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function sum_list should:
# --> Accept as input a list of int values
# --> Compute the sum of all of the int values in the list
# --> Return the sum of all the int values in the list
# --> For instance, if the function receives [5, 7] as
#     an input it returns the value of 12 stored in an int variable
# This function should work correctly for positive and negative int values


def sum_list(input_list: List[int]) -> int:
    """Sum all of the values inside of a list of int values."""
    return 0


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    space = " "
    question_three_output_c = str(sum_list([5, 7, 9, 11]))
    question_three_output_c = question_three_output_c + space + str((sum_list([0, 0, 0])))
    question_three_output_c = question_three_output_c + space + str((sum_list([1, 1, 1])))
    question_three_output_c = question_three_output_c + space + str((sum_list([2, -2, 2])))
    return question_three_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
