from random import sample

def mylist(amount, maxnumber):
    population = range(0, maxnumber)
    createdList = sample(population, amount)

    for number in createdList:
        if number > 7:
            print(number)


amount = int(input("ввести количество элементов "))
maxNumber = int(input("ввести максимальный показатель "))

mylist(amount, maxNumber)
