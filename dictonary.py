enter = ""
list_a = []
print(list_a)
while enter != "exit":
    enter = str(input("pleas choose A or B: "))
    alphabet = ("ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyzАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
    if enter.upper() == "A" or enter.upper() == "А":
        a = input().split(" ")
        for i in a:
            if (i not in list_a) and len(i) >=3:
                list_a.append(i)
        print(list_a)
        list_a.sort()
        for i in range(len(list_a)):
            print(list_a[i])
        print("------------------------")
    elif enter.upper() == "B" or enter.upper() == "Б":
        a = input().split()
        print(a)
        for i in range(len(alphabet)):
            number=0
            for h in a:
                number = number + h.count(alphabet[i])
            if number > 0:
                print(alphabet[i] + "-" + str(number))
        print("-----------------------------------------")
