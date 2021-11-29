def delete_empty_lines(file):
    final_str = ""
    for row in file:
        if row == "\n":
            continue
        final_str += row

    print(final_str)  # Это надо вставить в твой виджет текстовый


file = open('test.txt', 'r').readlines()  # тут файл который ты открываешь

delete_empty_lines(file)
