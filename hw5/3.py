employees = ['Олег', 'Ольга', 'Игорь']
salaries = [100, 120, 170]
bonus_perc = ['10.25%', '9.5%', '11.75%']

bonus_dict = {name: salaries[i] * float(bon[:-1])/100 for i, (name, bon) in enumerate(zip(employees, bonus_perc))}
print(bonus_dict)