# Extend the existing @logger decorator which writes logs to a file
# called log.txt instead of console


def logger(function):
    def wrapper(*args):
        with open('files/log.txt', 'w') as file:
            file.write(function(*args))
    return wrapper


@logger
def func(string: str):
    return string


func('Anything')

