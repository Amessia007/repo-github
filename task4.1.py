# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv

output_in_hours, rate_per_hour, premium = argv
salary = int(output_in_hours) * int(rate_per_hour) + int(premium)

print(f'salary: {salary}')