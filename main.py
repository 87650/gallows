import random
a = 0
u = 5
t = ['солон','широ','туалет']
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
               print("Вы не угадали слово и проиграли")
               break

           elif(len(val) < 2):
               try:
                   n = word.index(val)
                   te[n] = word[n]
                   test = ''.join(te)
                   print("вы угадали букву")


               except ValueError:
                   if(u > 0):
                        u =- 1
                        print("вы не угадали число, у вас осталось {0} попыток".format(u))

                   elif(u == 0):
                        print("вы не угадали букву, и проиграли")
                        break



           elif(len(val) > 1):
                    u -= 1
                    print("Вы не угадали слово у вас осталось {0} попыток".format(u))

    else:
        break






