def unlimited_arguments(*args, **kwargs):
    print(kwargs)
    for argument in kwargs:
        print(argument)

unlimited_arguments(1,2,3,4,5, name='seazlle', age=28)