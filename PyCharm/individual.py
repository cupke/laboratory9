import sys
if __name__ == '__main__':
    routes = []

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            start_point = input("Начальный пункт маршрута? ")
            end_point = input("Конечный пункт маршрута? ")
            route_number = int(input("Номер маршрута? "))

            route = {
                'start_point': start_point,
                'end_point': end_point,
                'route_number': route_number,
            }

            # Добавить словарь в список маршрутов.
            routes.append(route)

            # Отсортировать список в случае необходимости.
            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('route_number', 0))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 20,
                '-' * 30,
                '-' * 20
            )
            print(line)
            print(
                '| {:^20} | {:^30} | {:^20} |'.format(
                    "Начальный пункт",
                    "Конечный пункт",
                    "Номер маршрута"
                )
            )
            print(line)

            # Вывести данные о всех маршрутах.
            for idx, route in enumerate(routes, 1):
                print(
                    '| {:<20} | {:<30} | {:>20} |'.format(
                        route.get('start_point', ''),
                        route.get('end_point', ''),
                        route.get('route_number', 0)
                    )
                )
            print(line)
        elif command.startswith('select '):
            # Разбить команду на части для выделения номера маршрута.
            parts = command.split(' ', maxsplit=1)

            try:
                # Получить требуемый номер маршрута.
                selected_route_number = int(parts[1])
                # Поиск маршрута по номеру.
                selected_route = next((route for route in routes if route['route_number'] == selected_route_number), None)

                if selected_route:
                    print(f"Информация о маршруте {selected_route_number}:")
                    print(f"Начальный пункт: {selected_route['start_point']}")
                    print(f"Конечный пункт: {selected_route['end_point']}")
                    print(f"Номер маршрута: {selected_route['route_number']}")
                else:
                    print(f"Маршрут с номером {selected_route_number} не найден.")
            except ValueError:
                print("Ошибка: введите целое число после 'select'.")
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select <номер маршрута> - запросить информацию о маршруте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
