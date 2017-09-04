import time


## This file explains decorators easily
## In order to avoid repeatibility and to add necessary code
## to a function we will use a decorator

## We will write a decorator that add necessary code to a function
## when called


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs) # function results
        end = time.time()
        print(function.__name__ + "took " + str((end-start) * 1000) \
                + "mil seconds.")
        return result # return the variable containing the function  result
    return wrapper # return the function with the wrapper added


# This function calculate square of a number

@timer # decorator syntax
def calc_square(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result


# This function calculate cube of a number

@timer
def calc_cube(numbers):
    result = []
    for num in numbers:
        result.append(num * num * num)
    return result


# Create a variable with all the numbers we need to calculate
array = range(1,10000)

output_square = calc_square(array)

print("Output of the square function is " + str(output_square))
out_cube = calc_cube(array) # instanciate the output to a variable


print("Output of the cube function is " + str(output_square))


