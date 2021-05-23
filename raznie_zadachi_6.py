# Палиндромное число читается одинаково в обоих направлениях.
# Самый большой палиндром, составленный из двух двузначных чисел, равен 9009 = 91 × 99.
# Найдите самый большой палиндром, состоящий из произведения двух трехзначных чисел.

max = ''
i_max = 0
j_max = 0
for i in range(100,1000):
    for j in range(100,1000):
        num = str(i*j)
        if num == num[::-1]:
            if num > max:
                max = num
                i_max = i
                j_max = j
print('Произведение чисел: ',i_max,'и',j_max,'даёт полиндром: ',max)