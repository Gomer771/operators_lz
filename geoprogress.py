a = input("Введите первый член прогрессии, множитель прогрессии и номер последнего элемента:")
a = a.split() #разделяем строку
#присваиваем целочисленное значение 
b = int(a[0])
q = int(a[1])
n = int(a[2])
S = 0 #создаём переменную для хранения суммы членов прогрессии
for i in range(1,n+1): #создаём цикл
    S += b
    b = b*q
print("Сумма геометрической прогрессии:", S)