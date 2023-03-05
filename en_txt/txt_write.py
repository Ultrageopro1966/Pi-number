import random

with open('pi.txt') as f_r:
    pi_digits = list(map(int, list(f_r.readline())))

f = open('en_txt/en_txt.txt', 'w')

pares = []
for k in range(len(pi_digits)-1):
    pares.append(str(pi_digits[k])+str(pi_digits[k+1]))

alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

for k in range(len(pares)):
    num = int(pares[k])
    letter = alph[int(num//3.84615384615)]
    f.write(letter)
