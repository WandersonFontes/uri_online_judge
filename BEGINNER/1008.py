# Salary

worker, hours = int(input()), int(input())
valueHours = float(input())
salary = round(hours*valueHours, 2)
decimal = str(salary)[-2:]

print(f'NUMBER = {worker}\nSALARY = U$ {str(salary)+"0" if float(decimal) <= 9 else salary }')
