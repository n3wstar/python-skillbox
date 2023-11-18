def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            if len(args) < 1:
                return "Not enough arguments"
            else:
                return "Too many arguments"

        arg = args[0]

        if not isinstance(arg, int):
            return "Wrong types"

        if arg < 0:
            return "Negative argument"

        return func(*args)

    return wrapper


@validate_args
def example_function(x):
    return x


print(example_function(1))
print(example_function())
print(example_function(1, 2))
print(example_function("string"))
print(example_function(-2))
