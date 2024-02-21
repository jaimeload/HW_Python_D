def create_arguments_dict(**kwargs):
    return {str(key): value for key, value in kwargs.items()}


arguments_dict = create_arguments_dict(a=1, b="test", c=[1, 2, 3])
print(arguments_dict)
