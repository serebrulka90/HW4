from random import sample


def mylist(amount, maxnumber):
    population = range(0, maxnumber)
    return sample(population, amount)


amount = int(input("ввести количество элементов "))
maxNumber = int(input("ввести максимальный показатель "))

createdList = mylist(amount, maxNumber)
print(createdList)





