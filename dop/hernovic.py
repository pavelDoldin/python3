list = [len([i for i in el if i.lower() in "уеёэоаыяию"]) for el in input().split()]

if all([i == list[0] for i in list]):

    print("Парам пам-пам")

else:

    print("Пам парам")

