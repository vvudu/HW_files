def load_recipes(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        if not name:
            i += 1
            continue
        i += 1
        if i < len(lines) and lines[i].strip().isdigit():
            num_ingredients = int(lines[i].strip())
            i += 1
            ingredients = []
            for _ in range(num_ingredients):
                ingredient_line = lines[i].strip()
                ingredient_parts = ingredient_line.split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_parts[0], 
                    'quantity': float(ingredient_parts[1]), 
                    'measure': ingredient_parts[2]
                }
                ingredients.append(ingredient)
                i += 1
            cook_book[name] = ingredients
        else:
            print(f"Ошибка в формате рецепта: {name}")
            break
    
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге.")
    
    return shop_list

# Пример использования
filename = 'recipes.txt'
cook_book = load_recipes(filename)
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)
