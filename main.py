import time, os
import subprocess
import resource


def scr(test):
    os.system('bat input.txt')
    os.system('bat output.txt')
    os.system(f'gnome - screenshot - a - f scr/{test}.png')
    return f'scr/{test}.png'


def time_test(file_name):
    t_start = time.perf_counter()
    p = subprocess.Popen(file_name, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    p.wait()
    return time.perf_counter() - t_start


def mem_test(file_name):
    p = subprocess.Popen(file_name, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    p.wait()
    return f'{resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss} KB'

name = input('Введите фамилию, имя и очество: ')
grNo = input('Введите номер группы: ')
labNo = input('Введите номер лабораторной: ')
theme = input('Введите тему лабораторной: ')
varik = input('Введите вариант лабораторной: ')
zadvar = list(input('Введите номера задач по вариантам: ').split())
dopzad = list(input('Введите номера дополниительных задач : ').split())


with open('{}_{}_{}_№{}.md'.format(grNo, name.split()[0], name.split()[1], labNo), 'w') as f:
    f.write('САНКТ-ПЕТЕРБУРГСКИЙ НАЦИОНАЛЬНЫЙ ИССЛЕДОВАТЕЛЬСКИЙ\n')
    f.write('УНИВЕРСИТЕТ\n')
    f.write('ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ, МЕХАНИКИ И ОПТИКИ\n')
    f.write('ФАКУЛЬТЕТ ИНФОКОММУНИКАЦИОННЫХ ТЕХНОЛОГИЙ\n')
    f.write('' + '\n')
    f.write('' + '\n')
    f.write('' + '\n')
    f.write('' + '\n')
    f.write(f'Отчет по лабораторной работе {labNo}\n')
    f.write('по курсу «Алгоритмы и структуры данных»\n')
    f.write(f'Тема: Введение {theme}\n')
    f.write(f'Вариант {varik}\n')
    f.write('' + '\n')
    f.write('Выполнил:\n')
    f.write(name + '\n')
    f.write(grNo + '\n')
    f.write('' + '\n')
    f.write('' + '\n')
    f.write('' + '\n')
    f.write('Проверила:\n')
    f.write('Артамонова В.Е.\n')
    f.write('' + '\n')
    f.write('' + '\n')
    f.write('Санкт-Петербург\n')
    f.write('2022 г.\n')
    f.write('---\n')
    f.write('##Содержание отчета\n')
    f.write('---\n')
    f.write('##Задачи по варианту')
    for n in zadvar:
        nm = input('Введи название задачи')
        f.write('Задача №' + str(n) + nm + '\n')
        txt = input('Введите текст задачи')
        f.write(txt + '\n')
        with open(f'{n}.py', 'r') as code:
            for line in code.readlines():
                f.write(line + '\n')
        f.write(input('Введите описание работы алгоритма: ') + '\n')
        tests = input('Введите минимальное, тестовые и максимальное значения через , : ').split(',')
        table_of_content = []
        for test in tests:
            open('output.txt', 'w').write(test)
            table_of_content.append([scr(n), time_test(f'{n}.py'), mem_test(f'{n}.py')])
        #скрины
        for ind in table_of_content:
            f.write(f'![screeenshot]({ind[0]})')
        #таблица
        if len(table_of_content) == 1:
            first_column=['максимальное значение',]
        elif len(table_of_content) == 2:
            first_column = ['минимальное значение', 'максимальное значение']
        else:
            first_column = ['Минимальное значение']
            for _ in range(len(table_of_content) - 2):
                first_column.append('Пример из задачи')
            first_column.append('Максимальное значение')
        f.write(' | Время выполнения | Затраты памяти')
        f.write('--- | --- | ---')
        for index, res in enumerate(table_of_content):
            f.write(f'{first_column[index]} | {res[1]} | {res[2]}')
        f.write('---\n')
        f.write('##Дополнительные задачи')
        for n in dopzad:
            nm = input('Введи название задачи')
            f.write('Задача №' + str(n) + nm + '\n')
            txt = input('Введите текст задачи')
            f.write(txt + '\n')
            with open(f'{n}.py', 'r') as code:
                for line in code.readlines():
                    f.write(line + '\n')
            f.write(input('Введите описание работы алгоритма: ') + '\n')
            tests = input('Введите минимальное, тестовые и максимальное значения через , : ').split(',')
            table_of_content = []
            for test in tests:
                open('output.txt', 'w').write(test)
                table_of_content.append([scr(n), time_test(f'{n}.py'), mem_test(f'{n}.py')])
            # скрины
            for ind in table_of_content:
                f.write(f'![screeenshot]({ind[0]})')
            # таблица
            if len(table_of_content) == 1:
                first_column = ['максимальное значение', ]
            elif len(table_of_content) == 2:
                first_column = ['минимальное значение', 'максимальное значение']
            else:
                first_column = ['Минимальное значение']
                for _ in range(len(table_of_content) - 2):
                    first_column.append('Пример из задачи')
                first_column.append('Максимальное значение')
            f.write(' | Время выполнения | Затраты памяти')
            f.write('--- | --- | ---')
            for index, res in enumerate(table_of_content):
                f.write(f'{first_column[index]} | {res[1]} | {res[2]}')
            f.write('---\n')
            f.write('##Вывод')
            f.write(input('Введите вывод по лабораторной: '))
