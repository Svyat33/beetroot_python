# Lesson 10
# Task 2. Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age. Then create a
# method `human_age` which returns the dog’s age in human equivalent.
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.age = dog_age

    def human_age(self, coefficient=age_factor):
        comparison = self.age * coefficient
        return f"By human standards, your dog is {comparison} years old"


if __name__ == '__main__':
    dog_age = 10
    doggy_12 = Dog(dog_age)
    print(doggy_12.human_age())
