
# here we are using the decorator syntax and doing
# the same thing done in the previous program
# does'nt this look cleaner ?

def function_two(func):

    def inner():
        print("I am the decorator_function, and I am doing decoration job")
        func()

    return inner


@function_two
def function_one():
    print("I am function_one, I got decorated")

function_one()

#syntactic sugar
