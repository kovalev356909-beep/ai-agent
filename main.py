import logic


def print_help():
    print("\nДоступные команды:")
    print("  add <название> <цена> - Добавить продукт (пример: add Хлеб 50)")
    print("  list                  - Показать корзину")
    print("  checkout              - Оформить заказ")
    print("  help                  - Показать эту справку")
    print("  exit                  - Выйти из программы\n")


def main():
    print("Привет! Я твой консольный помощник по заказу продуктов Самокат.")
    print("Напиши 'help', чтобы узнать, что я умею.")

    while True:
        user_input = input("\nВведи команду > ").strip()

        if not user_input:
            print("Ошибка: пустая команда. Введи что-нибудь.")
            continue

        parts = user_input.split(" ", 2)
        command = parts[0].lower()

        if command == "exit":
            print("Пока! Хорошего дня.")
            break
        elif command == "help":
            print_help()
        elif command == "add":
            if len(parts) < 3:
                print("Ошибка: укажи название и цену. Пример: add Молоко 80")
            else:
                print(logic.add_product(parts[1], parts[2]))
        elif command == "list":
            print(logic.show_cart())
        elif command == "checkout":
            print(logic.checkout())
        else:
            print(f"Ошибка: неизвестная команда '{command}'. Напиши 'help' для списка команд.")


if __name__ == "__main__":
    main()