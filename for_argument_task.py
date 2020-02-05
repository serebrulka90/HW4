from random import sample

def mylist(amount, maxnumber):
    population = range(0, maxnumber)
    createdListOne = sample(population, amount)
    createdListTwo = sample(population, amount)
    print(createdListOne)
    print(createdListTwo)
    newList = []
    for number in createdListOne:
        for number2 in createdListTwo:
            if number == number2:
                newList.append(number)

    print("new list: ", newList)
    return newList



amount = int(input("ввести количество элементов "))
maxNumber = int(input("ввести максимальный показатель "))

mylist(amount, maxNumber)


