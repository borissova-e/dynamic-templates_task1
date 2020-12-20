from django.shortcuts import render

import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        list = []
        for row in reader:
            row = {'Год': row['Год'], 'Янв': row['Янв'], 'Фев': row['Фев'], 'Мар': row['Мар'], 'Апр': row['Апр'],
                   'Май': row['Май'], 'Июн': row['Июн'], 'Июл': row['Июл'], 'Авг': row['Авг'], 'Сен': row['Сен'],
                   'Окт': row['Окт'], 'Ноя': row['Ноя'], 'Дек': row['Дек'], 'Всего': row['Суммарная']}
            for k, v in row.items():
                if v == '':
                    row.update({k: '-'})
            list.append(row)

    return render(request, template_name, context={'inflation': list})
