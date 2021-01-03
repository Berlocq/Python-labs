print('''
Меню:
1. Финансовый результат
2. Прогноз на 2021 год
3. Информация о компании
''')

def check_pass_log(test):
    def wrap():
        print('Для того что бы попать в это меню, необходимо авторизоваться')
        p = input('Введите ваш логин: ')
        if p != 'admin' :      
            print('В доступе отказано')
            return
        test()
    return wrap
      
@check_pass_log
def test():
    print("""
    Финансовый результат:
    Данный год был успешный, прибыль компании составила $120 тыс.
    """)
    return

def check_log(test1):
    def wrap1():
        print('Для того что бы попать в это меню, необходимо авторизоваться')
        l = input('Введите ваш логин: ')
        if l != 'user' and l != 'admin':      
            print('В доступе отказано, не верный логин')
            return
        test1()
    return wrap1

@check_log
def test1():
    print("""
    Прогноз на 2021 год: 
    Ожидается снижение прибыли на 21%.
    """)
    return

def point3():
    print("""
    Информация о компании:
    Компания создана в 2017 году.
    """)
    return  

def menu():
    choice = input('Выберите пунк меню: ')
    if choice == '1':
        test()
    if choice == '2':
        test1() 
    if choice == '3':
        point3()
    else: 
        return
menu()
 
  



