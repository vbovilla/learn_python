# class Robot_Dog:
#     def __init__(self, name_val, breed_val):
#         self.name = name_val
#         self.breed = breed_val

#     def bark(self):
#         print(self.name, 'is barking')


# # Main program
# my_dog = Robot_Dog('Spot', 'Chihuaha')
# print(my_dog.name)
# print(my_dog.breed)

# my_dog.bark()


from robot import Robot


class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')

    def eat(self):
        super().eat()
        print('I like bacon!')


# Main Program
my_robot_dog = Robot_Dog('Bud')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()
