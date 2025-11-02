from base import beer_knowledge_base

def find_beer_by_name(name):
    """Вывод характеристик пива по названию."""
    beer = beer_knowledge_base.get(name)
    if beer:
        print(f"\nТип пива: {name}")
        for k, v in beer.items():
            print(f"  {k.capitalize()}: {v}")
    else:
        print("❌ Такого пива нет в базе.")

def recommend_beer(bitterness, aroma):
    """Рекомендовать пиво по вкусовым предпочтениям."""
    print(f"\n🔍 Подбор по параметрам: горечь={bitterness}, аромат={aroma}")
    matches = []
    for name, data in beer_knowledge_base.items():
        if name == "Пиво":
            continue
        if data["горечь"] == bitterness and aroma.lower() in data["аромат"]:
            matches.append(name)
    if matches:
        print("Рекомендуется:", ", ".join(matches))
    else:
        print("Не найдено подходящего типа пива.")

def find_by_ingredient(ingredient):
    """Поиск пива, где используется заданный ингредиент."""
    print(f"\n🔍 Пиво с ингредиентом: {ingredient}")
    result = [n for n, d in beer_knowledge_base.items()
              if ingredient.lower() in [i.lower() for i in d.get("ингредиенты", [])]]
    if result:
        print("Найдено:", ", ".join(result))
    else:
        print("Ингредиент не найден ни в одном типе пива.")

def find_by_strength_and_color(min_strength, color):
    """Поиск по крепости и цвету."""
    print(f"\n🔍 Пиво с крепостью >= {min_strength} и цветом '{color}'")
    result = []
    for n, d in beer_knowledge_base.items():
        if n == "Пиво":
            continue
        if d["крепость"] >= min_strength and color.lower() in d["цвет"].lower():
            result.append(n)
    if result:
        print("Подходит:", ", ".join(result))
    else:
        print("Нет пива с такими характеристиками.")

def main():
    while True:
        print("\n=== 🍺 Экспертная система: Вкусы пива ===")
        print("1. Показать характеристики пива")
        print("2. Рекомендовать по вкусу")
        print("3. Найти по ингредиенту")
        print("4. Найти по крепости и цвету")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            find_beer_by_name(input("Введите название пива: "))
        elif choice == "2":
            recommend_beer(
                input("Введите желаемую горечь (низкая/средняя/высокая): "),
                input("Введите аромат (фруктовый, цитрусовый, кофейный и т.п.): ")
            )
        elif choice == "3":
            find_by_ingredient(input("Введите ингредиент: "))
        elif choice == "4":
            find_by_strength_and_color(
                float(input("Минимальная крепость (%): ")),
                input("Цвет (светлый/тёмный/золотистый/янтарный): ")
            )
        elif choice == "0":
            print("Выход из системы. 🍻")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
