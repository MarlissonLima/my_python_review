
def decorator(func):
    def wrapper():
        print("Hello,this is before function execution")
        func()
        print("This is after function execution")

    return wrapper

def decorated_function():
    print("This is inside the function")


decorated_function = decorator(decorated_function)

decorated_function()

#we can add any behaviour before and after the function execution