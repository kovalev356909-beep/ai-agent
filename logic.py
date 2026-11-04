cart = []


def add_product(name: str, price_str: str) -> str:
    try:
        price = int(price_str)
        if price < 0:
            return "Ошибка: цена не может быть отрицательной."
        cart.append({"name": name, "price": price})
        return f"{name} ({price} руб.) добавлено в корзину."
    except ValueError:
        return "Ошибка: цена должна быть целым числом. Пример: add Молоко 80"


def show_cart() -> str:
    if not cart:
        return "Корзина пуста."

    result = "\n--- Ваша корзина Самокат ---\n"
    total = 0
    for i, item in enumerate(cart):
        result += f"{i + 1}. {item['name']} — {item['price']} руб.\n"
        total += item["price"]

    result += f"\nИтого к оплате: {total} руб."
    return result


def checkout() -> str:
    if not cart:
        return "Ошибка: корзина пуста, нечего заказывать."

    total = sum(item["price"] for item in cart)
    cart.clear()
    return f"Заказ на сумму {total} руб. успешно оформлен! Курьер уже в пути."