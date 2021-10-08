# Salary with Bonus

name = str(input())
salary, sell = float(input()), float(input())
total = str(round(salary+sell*0.15, 2))

print(f'TOTAL = R$ {total+"0" if float(total[-2:]) <= 9 else total} ')

