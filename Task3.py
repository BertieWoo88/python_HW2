# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
#не превосходящие числа N.

n = int(input("Введите число: "))
i = 0
x = 0 
while x<n:
    x = 2**i
    if x>n:break
    print(x , end=" ")
    i+=1
