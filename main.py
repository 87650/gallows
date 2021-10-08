import random
import re
counter = 0
a = 0
u = 5
t = ['доктор','виселица','автобус']
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
                   values = []
                   n = word.index(val)
                   #te[n] = word[n]
                   print(n)
                   if(n == counter):
                       print("вы угадали букву")
                       #result = re.match(r'{0}'.format(val), word)
                       matches = re.compile(r'{0}'.format(val), re.MULTILINE | re.DOTALL).findall(word)
                       for inp in matches:
                           values.append(inp)

                       for i in range(len(word)):
                               if(word[i] == val and i == counter):
                                  if(len(values) == 1):
                                      te[i] = val
                                      #test = ''.join(te)
                                      print("lol")

                                  if(len(values) > 1):
                                      for s in range(len(word)):
                                          if (word[s] == val):
                                                te[s] = val
                                                print('test')


                       test = ''.join(te)
                       print(te[0])
                   else:
                       raise ValueError("t")
               except ValueError:
                   if(u > 0):
                        counter = + 1
                        u -= 1
                        print("вы не угадали букву, у вас осталось {0} попыток".format(u))

                   elif(u == 0):
                        print("вы не угадали букву, и проиграли")
                        break



           elif(len(val) > 1):
                    u -= 1
                    counter = + 1
                    print("Вы не угадали слово у вас осталось {0} попыток".format(u))

    else:
        break
    counter = + 1






