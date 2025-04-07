def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(f'{expense}')
    print('Dinero recibido')
    print(f'{money}')
    print('Vuelto\n')
    print('Pesos:')
    print(f'{int((money-expense)//1)}')
    print('Centavos:')
    print(f'{int(((money-expense)-(money-expense)//1)*100)}')
