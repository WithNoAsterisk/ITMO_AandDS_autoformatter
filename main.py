name = input('Введите фамилию, имя и очество: ')
grNo = input('Введите номер группы: ')
labNo = input('Введите номер лабораторной: ')
theme = input('Введите тему лабораторной: ')
varik = input('Введите вариант лабораторной: ')
zadvar = int(input('Введите колличество задач по вариантам: '))
dopzad = int(input('Введите колличество дополнительных задач: '))




def scr():
    pass




with open('{}_{}_{}_№{}.md'.format(grNo,name.split()[0],name.split()[1],labNo), 'w') as f:
    f.write('САНКТ-ПЕТЕРБУРГСКИЙ НАЦИОНАЛЬНЫЙ ИССЛЕДОВАТЕЛЬСКИЙ\n')
    f.write('УНИВЕРСИТЕТ\n')
    f.write('ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ, МЕХАНИКИ И ОПТИКИ\n')
    f.write('ФАКУЛЬТЕТ ИНФОКОММУНИКАЦИОННЫХ ТЕХНОЛОГИЙ\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write('Отчет по лабораторной работе {}\n'.format(labNo))
    f.write('по курсу «Алгоритмы и структуры данных»\n')
    f.write('Тема: Введение {}\n'.format(theme))
    f.write('Вариант {}\n'.format(varik))
    f.write(''+'\n')
    f.write('Выполнил:\n')
    f.write(name+'\n')
    f.write(grNo+'\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write('Проверила:\n')
    f.write('Артамонова В.Е.\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write('Санкт-Петербург\n')
    f.write('2022 г.\n')
    f.write('---\n')
    f.write('##Содержание отчета\n')
    f.write('---\n')
    f.write('##Задачи по варианту')
    for i in range(1, zadvar + 1):
        nm = input('Введи название задачи')
        f.write('Задача №' + str(i)+nm+'\n')
        txt = input('Введите текст задачи')
        f.write(txt+'\n')
        with open('{}.py'.format(i), 'r') as code:
            for line in code.readlines():
                f.write(line + '\n')
        tests = input('Введите минимальное, тестовые и максимальное значения').split()
        for  test in tests:
            scr()

        f.write('---\n')



