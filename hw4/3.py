def main():
    balance = 0
    count = 0
    history = []
    print('Добро пожаловать в банкомат!')
    while True:
        while True:
            act = input('Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - выйти\n')
            if act not in ("1", "2", "3"):
                print("Неверный ввод")
            else:
                break
        match act:
            case "1":
                print(f'История операций: {history[::-1]}')
                balance, count, history = add_money(balance, count, history)
                print(f"Ваш баланс {balance}")
            case "2":
                print(f'История операций: {history[::-1]}')
                balance, count, history = get_money(balance, count, history)
                print(f"Ваш баланс {balance}")
            case "3":
                print(f'История операций: {history[::-1]}')
                print(f"Ваш баланс {balance}")
                print("До свидания!")
                break

def add_money(balance, count, history):
    if balance > 5_000_000:
        history.append(-balance * 0.1)
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму пополнения, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    count += 1
    history.append(summ)
    if count % 3 == 0:
        history.append(-balance * 0.03)
        balance *= 1.03
    return balance, count, history

def get_money(balance, count, history):
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму снятия, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            perc = summ * 0.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if summ + perc > balance:
                print("Недостаточно средств!")
                continue
            else:
                break
    balance -= (summ + perc)
    count += 1
    history.append(summ)
    if count % 3 == 0:
        history.append(-balance * 0.03)
        balance *= 1.03
    return balance, count, history

if __name__ == "__main__":
    main()