# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator=','):
    set_first_group = set(first_group.split(separator))
    set_second_group = set(second_group.split(separator))
    common_participants = sorted(list(set_first_group.intersection(set_second_group)))
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
