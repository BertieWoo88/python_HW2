"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
s = int(input("введите S="))
p = int(input("введите P="))

d = s**2 - 4 * p
if d<0: print("Решения нет")
else:
    x1 = (s+(d**0.5))/2
    x2 = (s-(d**0.5))/2
    print(x1, x2)
    first = False
    second = False
    if (x1 - (int(x1)) == 0) and x1<=1000:
        y1 = s- x1
        first = True
    else:         
        print(f"х1={x1} не удовлетворяет условиям задачи")
    if (x2 - (int(x2)) == 0) and x2<=1000:
        y2 = s - x2
        second = True    
    else:         
        print(f"х2={x2} не удовлетворяет условиям задачи") 
    if first and second:
        print(x1, y1, x2, y2)
    elif first:
        print (x1, y1) 
    elif second:
        print (x2, y2) 
    else:
        print("Нет решений удовлетворяющих условиям" )

# s = int(input())
# p = int(input())
# noanswer = True
# for i in range(p):
#     #print(f"i={i}")
#     for j in range(s):
#         #print(f"j={j}")
#         if s == i + j and p == i * j:
#             print(f"ответ: {i}, {j}")
#             noanswer = False    
# if noanswer: print("нет решения")






    