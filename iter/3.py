class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.index_stack = [(0, list_of_lists)]  # Используем стек для отслеживания индексов

    def __iter__(self):
        return self

    def __next__(self):
        while self.index_stack:
            index, current_list = self.index_stack.pop()  # Получаем текущий индекс и список
            
            if index < len(current_list):  # Если индекс в пределах текущего списка
                element = current_list[index]  # Берем элемент по индексу
                self.index_stack.append((index + 1, current_list))  # Сохраняем текущее состояние

                if isinstance(element, list):  # Если элемент - список, добавляем его в стек
                    self.index_stack.append((0, element))  # Начинаем с первого элемента этого списка
                else:
                    return element  # Если не список, возвращаем элемент

        raise StopIteration  # Если стеки пуст, остановим итерацию


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
    print("Все тесты пройдены успешно!")
