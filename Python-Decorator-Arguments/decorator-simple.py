
def decorator(original_func):

    def wrapper(*args):
        print(f'Do something before: {original_func.__name__}')
        original_func(*args)
        print(f'Do something after: {original_func.__name__}\n')

    return wrapper

@decorator
def info(name, age):
    print(f'Info function runs with args: {name} {age}')

info('john', 30)
info('jane', 25)