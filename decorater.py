# Decorator的有序性
def print_func_name(func):
    def warp_1():
        print("Now use function '{}'".format(func.__name__))
        func()
    return warp_1


def print_time(func):
    import time
    def warp_2():
        print("Now the Unix time is {}".format(int(time.time())))
        func()
    return warp_2


@print_func_name
@print_time
def dog_bark():
    print("Bark !!!")


@print_time
@print_func_name
def cat_miaow():
    print("Miaow !!!")


if __name__ == "__main__":
    dog_bark()
    # print_func_name(print_time(dog_bark))()

    cat_miaow()

print('----------------------------------------------------------')
print()

# Decorator帶參數
import time


def print_func_name(time):
    def decorator(func):
        def warp():
            print("Now use function '{}'".format(func.__name__))
            print("Now Unix time is {}.".format(int(time)))
            func()
        return warp
    return decorator


@print_func_name(time=(time.time()))
def dog_bark():
    print("Bark !!!")


if __name__ == "__main__":
    dog_bark()

print('----------------------------------------------------------')
print()

# Decorator example
def a(secret):
    def lover(func):
        def warp():
            print("{} is my love!".format(func.__name__))
            print("I will cherish all the memories we had!")
            func()
        return warp
    return lover

@a(secret="secret")
def Dog():
    print("Cat and dog are always best friends!")

@a(secret="secret")
def Cat():
    print("Cuteeeee~")

if __name__ == "__main__":
    Dog()
    Cat()

