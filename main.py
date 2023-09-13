person_one=input("Введите значение: ")
person_two=input("Введите значение: ")
a = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}
for i, k in a.items():
    if person_one == i and person_two == k:
        print("Выиграл первый игрок!")
    elif person_two == i and person_one == k:
        print("Выиграл второй игрок!")
    elif person_one == person_two:
        print("Ничья")




