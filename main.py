import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function()

def say_hello():
    print("Hello!")


inner_function = delay_decorator(say_hello)
