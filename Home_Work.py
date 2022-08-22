import math
from pickle import TRUE

# 1. Написати програму, яка змінює значення двох цілих змінних a і b без використання додаткових змінних.
a, b = int(input("a = ")), int(input("b = "))

a, b = b, a

print("a =", a, "b =", b)

# 2. Написати програму, яка обчислює і виводить на екран:
#  • середнє арифметичне двох цілих чисел a і b
#  • середнє геометричне двох цілих чисел a і b.

print("Arithmetic mean =", (a + b) / 2, "Geometric mean =", math.sqrt(a * b))

# 3. Написати програму, яка переставляє цифри трьохзначного числа, яке задане користувачем у зворотному порядку і виводить нове число на екран.

print()

number = int(input("Number = "))

reverse_number = str(number % 10) + str(number %
                                        100 // 10) + str(number // 100)

print("Reverse number =", reverse_number)

# 4. Написати програму, яка визначає загальну кількість годин доби (змінна hour) і загальну кількість хвилин доби (змінна minute), які пройшли до
# моменту поточної секунди доби (змінна second). Наприклад, якщо second = 11111 (second = 3 * 3600 + 5 * 60 + 11), то hour = 3 і minute = 5.

print()

second = int(input("Input seconds = "))

if second < 60:
    print("0 hours and 0 minutes pass.")
elif second > 86400:
    print("Error!")
elif second < 3600:
    minute = second / 60
    print("0 hours and", int(minute), "minutes pass.")
else:
    hour = second / 3600
    minute = (second - int(hour) * 3600) / 60
    print(int(hour), "hours and", int(minute), "minutes pass.")

# 5. Написати програму яка визначає чи є натуральне число, що ввів користувач:
#   • парним
#   • таким, що закінчується на цифру 5.

print()

natural_number = int(input("Input natural number: "))

if natural_number < 0:
    print("Number isn't natural.")
else:
    if natural_number % 2 == 0:
        print("Number", natural_number, "is even and don't ends with number 5.")
    else:
        print("Number", natural_number, "is odd.")
        if natural_number % 5 == 0:
            print("Number", natural_number, "ends with number 5.")
