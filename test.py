import random
a = 0
u = 5
t = ['слон','широ','туалет']
flag = False
flag1 = False

num = random.randint(0, 2)
word = t[num]
te = []
for m in word:
    te.append(m)

print("Начало игры виселица")
for i in range(len(te)):
    te[i] = "_"
test = ''.join(te)
print(word)

while True:
    flag1 = False
    if(flag == False):
        if(u > 0):
           print(test)
           print("введите правильное слово или букву слова")
           val = input()
           if(val == word):
               print("Вы угадали слово поздравляю!")
               break
           elif(test == word):
               print("Вы угадали слово поздравляю!")
               break

           elif(u == 0):
               print("Вы не угадали букву и проиграли")
               break
           elif(len(val) < 2):

                    for y in range(len(word)):
                        if(flag1 == False):
                            print(word[y])
                            if word[y] == val:
                                for n in range(len(te)):
                                    te[y] = val
                                    test = ''.join(te)
                                    flag1 = True
                                    break

                            elif(u > 0):
                                u -= 1
                                print(word[y])
                                print("Вы не угадали букву у вас осталось {0} попыток".format(u))
                                break

                            elif(u == 0):
                                print("Вы не угадали букву и проиграли ")
                                flag = True
                                break
                        else:
                            break

           elif(len(val) > 1):
                    u -= 1
                    print("Вы не угадали слово у вас осталось {0} попыток".format(u))

    else:
        break



