import time

#decorator
def calculate_duration(func):
    def wrapper():
        initial = time.time()
        func()
        final = time.time()

        print(f"{func.__name__} total execution time: {str(final-initial)}")

    return wrapper

#decorates the function with decorator
@calculate_duration
def main():
    for n in range(0,100000):
        pass

#executes the main()
main()

#the same thing:
#decorated_function = calculate_duration(main)

#decorated_function()