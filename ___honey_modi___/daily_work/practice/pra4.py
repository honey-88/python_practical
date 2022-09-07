import random

#it will generate random number between 1 - 100
num = random.randint(1,100)
print(num)

subject_list = ["c","c++","java","python"]
print(random.choice(subject_list))

subject_list = ["c","c++","java","python"]
random.shuffle(subject_list)
print(subject_list)