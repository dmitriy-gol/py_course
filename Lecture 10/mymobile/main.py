from modile_phone_class import Phone


iphone = Phone("12345")

def main():
    print('Меню:'
          '\n1 - Включить телефон'
          '\n2 - Выключить телефон'
          '\n3 - Позвонить'
          '\n4 - Выход')
    action = input("Выберите действие: ")
    while action != "4":
        if action == "1":
            print(iphone.turn_on())
        elif action == "2":
            print(iphone.turn_off())
        elif action == "3":
            print(iphone.call('12345'))
        action = input("Выберите действие: ")


if __name__ == '__main__':
    main()
