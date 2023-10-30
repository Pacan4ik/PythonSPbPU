# TODO Напишите функцию для поиска индекса товара

def find(items, item):
    for i, fruit in enumerate(items):
        if fruit == item:
            return i


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for item in ['банан', 'груша', 'персик']:
    index = find(items_list, item)
    if index is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index}.")
    else:
        print(f"Товар '{item}' не найден в списке.")
