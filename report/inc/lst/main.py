from base import beer_knowledge_base

def find_beer_by_name(name):
    """Вывод характеристик пива по названию."""
    beer = beer_knowledge_base.get(name)
    if beer:
        print(f"\nТип пива: {name}")
        for k, v in beer.items():
            print(f"  {k.capitalize()}: {v}")
    else:
        print("Такого пива нет в базе.")

def recommend_beer():
    """Рекомендация пива по выбранной горечи и аромату."""
    bitterness_options = ["низкая", "средняя", "высокая"]
    aroma_options = ["фруктовый", "цветочный", "чистый", "нейтральный",
                     "жжёный", "кофейный", "карамельный", "цитрусовый", "хвойный", "хмелевой", "банановый", "гвоздичный"]
    
    print("\nВыберите желаемую горечь:")
    for i, b in enumerate(bitterness_options, 1):
        print(f"{i}. {b}")
    b_choice = int(input("Номер горечи: ")) - 1
    bitterness = bitterness_options[b_choice]

    print("\nВыберите желаемый аромат:")
    for i, a in enumerate(aroma_options, 1):
        print(f"{i}. {a}")
    a_choice = int(input("Номер аромата: ")) - 1
    aroma = aroma_options[a_choice]

    print(f"\n Подбор по параметрам: горечь={bitterness}, аромат={aroma}")
    matches = []
    for name, data in beer_knowledge_base.items():
        if name == "Пиво":
            continue
        if data["горечь"] == bitterness and aroma in data["аромат"]:
            matches.append(name)
    if matches:
        print("Рекомендуется:", ", ".join(matches))
    else:
        print("Не найдено подходящего типа пива.")

def find_by_country():
    """Поиск пива по стране происхождения."""
    # Собираем уникальные страны
    countries = sorted(list({data["страна"] for name, data in beer_knowledge_base.items() if name != "Пиво"}))

    print("\nВыберите страну:")
    for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")
    choice = int(input("Номер страны: ")) - 1
    if choice < 0 or choice >= len(countries):
        print(" Неверный выбор!")
        return
    country = countries[choice]

    print(f"\nПиво из страны: {country}")
    result = [name for name, data in beer_knowledge_base.items() 
              if name != "Пиво" and data["страна"] == country]
    if result:
        print("Найдено:", ", ".join(result))
    else:
        print("Пиво из этой страны не найдено.")

def find_by_strength_and_color():
    """Поиск по категории крепости и цвету."""
    strengths = ["слабая", "средняя", "сильная"]
    colors = ["светлый", "тёмный", "золотистый", "янтарный"]

    print("\nВыберите крепость:")
    for i, s in enumerate(strengths, 1):
        print(f"{i}. {s}")
    s_choice = int(input("Номер крепости: ")) - 1
    strength = strengths[s_choice]

    print("\nВыберите цвет:")
    for i, c in enumerate(colors, 1):
        print(f"{i}. {c}")
    c_choice = int(input("Номер цвета: ")) - 1
    color = colors[c_choice]

    print(f"\nПиво с крепостью '{strength}' и цветом '{color}'")
    result = []
    for n, d in beer_knowledge_base.items():
        if n == "Пиво":
            continue
        if d["крепость"] == strength and color.lower() in d["цвет"].lower():
            result.append(n)
    if result:
        print("Подходит:", ", ".join(result))
    else:
        print("Нет пива с такими характеристиками.")
def main():
    while True:
        print("\n=== Вкусы пива ===")
        print("1. Показать характеристики пива")
        print("2. Рекомендовать пиво по вкусу")
        print("3. Найти по стране происхождения")
        print("4. Найти по крепости и цвету")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            names = [n for n in beer_knowledge_base.keys() if n != "Пиво"]
            print("\nВыберите пиво:")
            for i, n in enumerate(names, 1):
                print(f"{i}. {n}")
            n_choice = int(input("Номер пива: ")) - 1
            find_beer_by_name(names[n_choice])
        elif choice == "2":
            recommend_beer()
        elif choice == "3":
            find_by_country()
        elif choice == "4":
            find_by_strength_and_color()
        elif choice == "0":
            print("Выход из системы")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
