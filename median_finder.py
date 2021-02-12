"""
Finding Median with just a simple function
"""

# Global Variables for sampling
test_yourself = [1, 23, 45, 65, 76, 78, 87]
new_lo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Defining the function
def median(a_list):
    # Get the position of int by sub 1 from the total len of given list
    position = len(a_list) - 1
    av_pos = int(position / 2)  # Get the index of the middle No
    # Getting the median and returning it
    if position % 2 == 0:
        return a_list[av_pos]
    # Or else return average of two numbers if they are two in the middle
    else:
        return (a_list[av_pos] + a_list[av_pos + 1]) / 2
    # This would be the else statement if we want to return two integers in the middle


# Example Printing
print(median(test_yourself))  # output is 65
print(median(new_lo))  # output is 5.5

# Hope this is useful, however! Am working on a class object of this algorithm and I will update it once it is done!
# follow me here to keep updated
