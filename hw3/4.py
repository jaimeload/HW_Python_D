def fill_backpack(items, max_weight, current_weight=0, index=0, selected_items={}):
    if index == len(items):
        return [selected_items] if current_weight <= max_weight else []

    item_name, item_weight = items[index]
    result = fill_backpack(items, max_weight, current_weight, index + 1, dict(selected_items))

    if current_weight + item_weight <= max_weight:
        selected_items[item_name] = item_weight
        result += fill_backpack(items, max_weight, current_weight + item_weight, index + 1, dict(selected_items))

    return result


staff = {'Палатка': 4, 'Спальник': 1, 'Пенка': 0.5, 'Котелок': 1.5, 'Горелка с баллоном': 1.5, 'Складной стул': 2,
         'Тушёнка': 1, 'Лапша': 0.5, 'Вода': 3, 'Водка': 0.7, 'Нож': 0.3, 'Топор': 2, 'Запасная обувь': 1,
         'Шерстяные носки': 0.3, 'Термос с чаем': 2, 'Орехи': 0.3, 'Конфеты': 0.3, 'Тёплая одежда': 2}
backpack = 10
combinations = fill_backpack(list(staff.items()), backpack)

print(combinations)
