# *kwargs

def student(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")

student(name = "honey",subject = "python")