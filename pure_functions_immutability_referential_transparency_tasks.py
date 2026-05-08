# -*- coding: utf-8 -*-
"""
Чисті функції, Immutability та Referential Transparency у Python

У файлі виконано 15 завдань:
- визначення чистих і нечистих функцій;
- рефакторинг у чисті функції;
- Functional Core / Imperative Shell;
- immutable update;
- pipeline без мутацій;
- referential transparency;
- memoization;
- immutable state history з undo.
"""

from datetime import datetime
from functools import lru_cache
import random
import time


def print_title(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# =============================================================================
# Завдання 1. Визначення чистоти функцій
# =============================================================================

print_title("Завдання 1. Визначення чистоти функцій")

balance = 100


def withdraw(amount):
    global balance
    balance -= amount
    return balance


def add(a, b):
    return a + b


def log_message(msg):
    print(msg)


def get_hour():
    return datetime.now().hour


print("Аналіз:")
print("withdraw(amount) — нечиста функція.")
print("Причина: змінює глобальну змінну balance, тобто має side effect.")
print()
print("add(a, b) — чиста функція.")
print("Причина: результат залежить тільки від a і b, зовнішній стан не змінюється.")
print()
print("log_message(msg) — нечиста функція.")
print("Причина: виконує print, тобто має side effect у вигляді виводу в консоль.")
print()
print("get_hour() — нечиста функція.")
print("Причина: результат залежить від поточного часу, а не тільки від аргументів.")
print()
print("Приклад add(2, 3):", add(2, 3))


# =============================================================================
# Завдання 2. Рефакторинг у чисті функції
# =============================================================================

print_title("Завдання 2. Рефакторинг у чисті функції")

tax_rate = 0.2


def calculate_price_bad(price):
    return price * (1 + tax_rate)


def calculate_price(price, tax_rate):
    return price * (1 + tax_rate)


print("Нечистіша версія залежить від глобального tax_rate:")
print("calculate_price_bad(100) =", calculate_price_bad(100))
print()
print("Чиста версія отримує всі залежності явно:")
print("calculate_price(100, 0.2) =", calculate_price(100, 0.2))
print("calculate_price(100, 0.1) =", calculate_price(100, 0.1))

print("\nПояснення:")
print("Чиста функція не використовує глобальні змінні.")
print("tax_rate передається як звичайний параметр.")


# =============================================================================
# Завдання 3. Functional Core / Imperative Shell
# =============================================================================

print_title("Завдання 3. Functional Core / Imperative Shell")

order_example = {"items": [100, 200, 300]}


# Functional Core: чиста функція
def calculate_order_total(order, tax_rate):
    items_total = sum(order["items"])
    return items_total * (1 + tax_rate)


# Imperative Shell: нечиста оболонка, яка відповідає за I/O
def process_order(order, tax_rate):
    print("Processing order...")
    return calculate_order_total(order, tax_rate)


print("Результат process_order(order_example, 0.2):", process_order(order_example, 0.2))

print("\nПояснення:")
print("calculate_order_total — functional core, бо тільки обчислює результат.")
print("process_order — imperative shell, бо виконує print.")


# =============================================================================
# Завдання 4. Заборонити мутацію
# =============================================================================

print_title("Завдання 4. Заборонити мутацію")


def add_item_bad(items, item):
    items.append(item)
    return items


def add_item(items, item):
    return items + [item]


items = ["apple", "banana"]
new_items = add_item(items, "kiwi")

print("Початковий список:", items)
print("Новий список:", new_items)
print("Початковий список після виклику не змінився:", items)

print("\nПояснення:")
print("Функція add_item не викликає append, тому не змінює вхідний список.")


# =============================================================================
# Завдання 5. Immutable update
# =============================================================================

print_title("Завдання 5. Immutable update")

user = {"name": "Alice", "age": 25}


def update_age(user, new_age):
    return {**user, "age": new_age}


updated_user = update_age(user, 30)

print("Початковий user:", user)
print("Новий user:", updated_user)

print("\nПояснення:")
print("Створюється новий словник через розпакування {**user, ...}.")
print("Оригінальний словник user не змінюється.")


# =============================================================================
# Завдання 6. Сортування без мутації
# =============================================================================

print_title("Завдання 6. Сортування без мутації")


def sort_numbers_bad(nums):
    nums.sort()
    return nums


def sort_numbers(nums):
    return sorted(nums)


nums = [5, 2, 4, 1, 3]
sorted_nums = sort_numbers(nums)

print("Початковий список:", nums)
print("Відсортований список:", sorted_nums)
print("Початковий список після sort_numbers не змінився:", nums)

print("\nПояснення:")
print("sorted(nums) повертає новий список.")
print("nums.sort() змінює список на місці, тому для immutable-підходу не підходить.")


# =============================================================================
# Завдання 7. Pipeline без мутацій
# =============================================================================

print_title("Завдання 7. Pipeline без мутацій")

data = [1, 2, 3, 4, 5, 6]


def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]


def square_numbers(numbers):
    return [x * x for x in numbers]


def pipeline_without_mutation(data):
    even_numbers = filter_even(data)
    squared_numbers = square_numbers(even_numbers)
    return squared_numbers


pipeline_result = pipeline_without_mutation(data)

print("Початкові дані:", data)
print("Результат pipeline:", pipeline_result)
print("Початкові дані після pipeline не змінились:", data)

print("\nПояснення:")
print("Кожен крок повертає новий список і не змінює попередній.")


# =============================================================================
# Завдання 8. Визначення прозорості
# =============================================================================

print_title("Завдання 8. Визначення referential transparency")


def square(x):
    return x * x


def random_value():
    return random.randint(1, 10)


counter = 0


def increment():
    global counter
    counter += 1
    return counter


print("Аналіз:")
print("square(x) — референтно прозора функція.")
print("Причина: square(5) завжди можна замінити на 25.")
print()
print("random_value() — не референтно прозора.")
print("Причина: кожен виклик може повертати різний результат.")
print()
print("increment() — не референтно прозора.")
print("Причина: змінює global counter і залежить від попередніх викликів.")
print()
print("Приклад square(5):", square(5))
print("Приклад random_value():", random_value())
print("Приклад increment():", increment())
print("Ще один increment():", increment())


# =============================================================================
# Завдання 9. Рефакторинг у referential transparency
# =============================================================================

print_title("Завдання 9. Рефакторинг у referential transparency")


def is_morning_bad():
    return datetime.now().hour < 12


def is_morning(hour):
    return hour < 12


print("is_morning(9) =", is_morning(9))
print("is_morning(15) =", is_morning(15))

print("\nПояснення:")
print("У референтно прозорій версії час передається як параметр.")
print("is_morning(9) завжди повертає True, а is_morning(15) завжди повертає False.")


# =============================================================================
# Завдання 10. Підстановка значень
# =============================================================================

print_title("Завдання 10. Підстановка значень")


def double_value(x):
    return x * 2


expression_result = double_value(5) + double_value(5)
replacement_result = 10 + 10

print("double_value(5) + double_value(5) =", expression_result)
print("Після підстановки:", replacement_result)

print("\nПояснення:")
print("double_value(5) завжди дорівнює 10.")
print("Тому вираз double_value(5) + double_value(5) можна замінити на 10 + 10.")
print("Це приклад referential transparency.")


# =============================================================================
# Завдання 11. Чистий pipeline обробки даних
# =============================================================================

print_title("Завдання 11. Чистий pipeline обробки даних")

transactions = [
    {"amount": 100, "currency": "USD"},
    {"amount": 200, "currency": "EUR"},
    {"amount": 150, "currency": "USD"},
]


def filter_usd(transactions):
    return [
        transaction
        for transaction in transactions
        if transaction["currency"] == "USD"
    ]


def convert_usd_to_uah(transactions, rate):
    return [
        {
            "amount": transaction["amount"] * rate,
            "currency": "UAH",
        }
        for transaction in transactions
    ]


def sum_amounts(transactions):
    return sum(transaction["amount"] for transaction in transactions)


def usd_transactions_total_uah(transactions, rate):
    usd_only = filter_usd(transactions)
    converted = convert_usd_to_uah(usd_only, rate)
    return sum_amounts(converted)


total_uah = usd_transactions_total_uah(transactions, 40)

print("Початкові транзакції:", transactions)
print("USD-транзакції:", filter_usd(transactions))
print("USD у гривні:", convert_usd_to_uah(filter_usd(transactions), 40))
print("Загальна сума USD у гривні:", total_uah)
print("Початкові транзакції після pipeline не змінились:", transactions)

print("\nПояснення:")
print("Усі функції чисті: вони не змінюють вхідні дані та отримують залежності явно.")


# =============================================================================
# Завдання 12. Functional transformation engine
# =============================================================================

print_title("Завдання 12. Functional transformation engine")


def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result


steps = [
    lambda xs: [x for x in xs if x > 2],
    lambda xs: [x * 10 for x in xs],
    lambda xs: sum(xs),
]

engine_result = pipeline([1, 2, 3, 4, 5], steps)

print("pipeline([1, 2, 3, 4, 5], steps) =", engine_result)

print("\nПояснення:")
print("pipeline не мутує дані.")
print("Кожен step приймає результат попереднього кроку і повертає нове значення.")


# =============================================================================
# Завдання 13. Обробка замовлення
# =============================================================================

print_title("Завдання 13. Обробка замовлення")

order = {
    "items": [100, 200, 300],
    "discount": 0.1,
}


def calculate_items_sum(order):
    return sum(order["items"])


def apply_order_discount(total, discount):
    return total * (1 - discount)


def apply_order_tax(total, tax_rate):
    return total * (1 + tax_rate)


def calculate_final_order_price(order, tax_rate):
    items_sum = calculate_items_sum(order)
    after_discount = apply_order_discount(items_sum, order["discount"])
    after_tax = apply_order_tax(after_discount, tax_rate)
    return after_tax


final_order_price = calculate_final_order_price(order, 0.2)

print("Замовлення:", order)
print("Сума товарів:", calculate_items_sum(order))
print("Після знижки:", apply_order_discount(calculate_items_sum(order), order["discount"]))
print("Фінальна ціна з податком:", final_order_price)
print("Замовлення після обробки не змінилось:", order)

print("\nПояснення:")
print("Функції не змінюють order.")
print("За однакових аргументів вони завжди повертають однаковий результат.")


# =============================================================================
# Завдання 14. Memoization
# =============================================================================

print_title("Завдання 14. Memoization")


def slow_function_without_cache(x):
    time.sleep(0.1)
    return x * x


@lru_cache(maxsize=None)
def slow_function(x):
    time.sleep(0.1)
    return x * x


print("Перший виклик slow_function(10):", slow_function(10))
print("Другий виклик slow_function(10):", slow_function(10))
print("slow_function(20):", slow_function(20))

print("\nІнформація про кеш:")
print(slow_function.cache_info())

print("\nПояснення:")
print("Memoization — це кешування результатів функції.")
print("Воно безпечне для чистих функцій, бо однаковий аргумент завжди дає однаковий результат.")
print("Тому результат slow_function(10) можна зберегти й повторно використати.")


# =============================================================================
# Завдання 15. Immutable state history
# =============================================================================

print_title("Завдання 15. Immutable state history")


def create_state(value):
    return {"value": value}


def update_state(state, new_value):
    return {**state, "value": new_value}


def add_state(history, state):
    return history + [state]


def undo(history):
    if len(history) <= 1:
        return history, history[-1] if history else None

    new_history = history[:-1]
    current_state = new_history[-1]
    return new_history, current_state


state0 = create_state(0)
history = [state0]

state1 = update_state(state0, 10)
history = add_state(history, state1)

state2 = update_state(state1, 20)
history = add_state(history, state2)

state3 = update_state(state2, 30)
history = add_state(history, state3)

print("state0:", state0)
print("state1:", state1)
print("state2:", state2)
print("state3:", state3)
print("Історія:", history)

history_after_undo, current_after_undo = undo(history)

print("Історія після undo:", history_after_undo)
print("Поточний стан після undo:", current_after_undo)

history_after_second_undo, current_after_second_undo = undo(history_after_undo)

print("Історія після другого undo:", history_after_second_undo)
print("Поточний стан після другого undo:", current_after_second_undo)

print("\nПояснення:")
print("Кожен стан створюється як новий словник.")
print("Старі стани не змінюються, тому їх можна зберігати в історії.")
print("undo просто повертає попередню версію history без мутації початкового списку.")


# =============================================================================
# Загальний висновок
# =============================================================================

print_title("Загальний висновок")

print("Чиста функція — це функція, результат якої залежить тільки від її аргументів,")
print("і яка не має side effects: не змінює глобальний стан, не мутує вхідні дані,")
print("не виконує I/O всередині обчислювального ядра.")
print()
print("Immutability — це підхід, за якого дані не змінюються на місці.")
print("Замість цього створюються нові списки, словники або інші структури.")
print()
print("Referential Transparency означає, що виклик функції можна замінити його")
print("результатом без зміни поведінки програми.")
print()
print("Ці принципи допомагають писати код, який легше тестувати, кешувати,")
print("відлагоджувати та комбінувати у pipeline.")
