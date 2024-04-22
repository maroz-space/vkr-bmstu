def config_app():
    return {
        'fields': [
            {'name': 'Соотношение матрица-наполнитель'},                        # 0
            {'name': 'Плотность, кг/м3'},                                       # 1
            {'name': 'Модуль упругости, ГПа'},                                  # 2
            {'name': 'Количество отвердителя, м.%'},                            # 3
            {'name': 'Содержание эпоксидных групп, %_2'},                       # 4
            {'name': 'Температура вспышки, С_2'},                               # 5
            {'name': 'Поверхностная плотность, г/м2'},                          # 6
            {'name': 'Модуль упругости при растяжении, ГПа'},                   # 7
            {'name': 'Прочность при растяжении, МПа'},                          # 8
            {'name': 'Потребление смолы, г/м2'},                                # 9
            {'name': 'Угол нашивки, град', 'ref': {'0': '0', '90': '90'}},      # 10
            {'name': 'Шаг нашивки'},                                            # 11
            {'name': 'Плотность нашивки'}                                       # 12
        ],
        'form': [{
            'button': 'Модуль упругости и прочность при растяжении',
            'title': '''
                Прогнозирование характеристик композитного материала: 
                модуль упругости при растяжении, прочность при растяжении
            ''',
            'fields': {
                '0': '1',
                '1': '1',
                '2': '1',
                '3': '1',
                '4': '1',
                '9': '1',
                '11': '1',
                '12': '1',
                '10': '0'
            },
            'model': ['M1', 'M2'],
            'answer': {
                'Модуль упругости при растяжении, ГПа': '',
                'Прочность при растяжении, МПа': ''
            }
        },{
            'button': 'Матрица-наполнитель',
            'title': '''
                Рекомендация соотношения матрицы-наполнителеля 
                для технологического процесса изготовления 
                композитных материалов
            ''',
            'fields': {
                '1': '1',
                '2': '1',
                '3': '1',
                '4': '1',
                '5': '1',
                '6': '1',
                '7': '1',
                '8': '1',
                '9': '1',
                '11': '1',
                '12': '1',
                '10': '0'
            },
            'model': ['M3'],
            'answer': {
                'Матрица-наполнитель': ''
            }
        }]
    }