# читаем файлы
def read_file(name):
    import chardet
    f = open('newsfr.txt', 'newsit.txt', 'newsafr.txt', 'newscy.txt', encoding='utf-8')
    data = f.read()
    result = chardet.detect(data)
    proper_text = data.decode(result['encoding'])
    return proper_text


# подсчитываем слова с к-вом символов > 6
def count_words(proper_text):
    split_text_to_list = proper_text.split('')
    word_set = set()
    for i in split_text_to_list:
        if len(i) > 6:
            word_set.add(i)
    word_value = {}
    for i in word_set:
        count = 0
        for j in split_text_to_list:
            if i == j:
                count += 1
        word_value[i] = count
    return word_value


# сортируем и создаем топ-10
def top_sort(word_value):
    top10_list = list()
    top_dict = str(len(word_value))
    for i in word_value.items():
        top_word = str(i[1])
        top10_list.append((len(top_dict) - len(top_word)) * '0' + str(i[1]) + ' ' + (i[0])
        top10_list.sort(reverse=True)
        finished_top10_list = list()
        top10 = {}
        count = 1
        for j in top10_list:
            top10[count] = j.split(' ')
        top10[count][0] = int(top10[count][0])
        if count == 10:
            break
        count += 1
    return top10


# основная функция
def main():
    while True:
        file_name = input('Введите имя файла: newsfr.txt или newsit.txt или newsafr.txt, или newscy.txt, или 'exit', если хотите выйти)
        if name == 'newsfr.txt' or name == 'newsit.txt' or name == 'newsafr.txt' or name == 'newscy.txt':
            print('Загрузка..')
            top10 = top_sort(count_words(read_file(name)))
            for n in top10.values():
                print(n[0], ':', n[1])
            elif file_name == 'exit':
            break
        else:
            print('Некорректный ввод информации, попробуйте еще раз')