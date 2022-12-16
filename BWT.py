def read_fasta(filename):

    f = open(filename, 'r')
    lines = f.readlines()

    if len(lines) == 2:

        stroka = str(lines[1])
        return stroka
    else:
        return []

def BWT_transforming(stroka):
    "Преобразует поданную на вход строку stroka алгоритмом BWT "
    "Возвращает первый и последний столбцы и суффиксный массив (номера)"

    words = list(stroka)
    lis, last, first, suff_list = [], [], [], []
    suff_index = len(stroka) - 1

    for i in range(len(words)):
        word = stroka[-1] + stroka[:-1]
        new = ''.join(word)
        stroka = new
        lis.append([new, str(suff_index)])
        suff_index -= 1
    sort = sorted(lis)

    for i in range(len(words)):
        element = sort[i][0]
        last.append(element[- 1])
        first.append(element[0])
        suff_list.append(sort[i][1])


    return first, last, suff_list

def Indexing(arr):
    "Для каждой буквы A, G, T, C в массиве arr проставляет индексы"
    "Cчитает количество вхождений, записывая в массив count"

    a, g, t, c = 1, 1, 1, 1
    count_A, count_C, count_G, count_T = 0, 0, 0, 0

    for i in range(len(arr)):

        if arr[i] == 'A':
            arr[i] = ["A", a]
            a += 1
            count_A += 1

        if arr[i] == "G":
            arr[i] = ["G", g]
            g += 1
            count_G += 1

        if arr[i] == "T":
            arr[i] = ["T", t]
            t += 1
            count_T += 1

        if arr[i] == "C":
            arr[i] = ["C", c]
            c += 1
            count_C += 1

    count = [count_A, count_C, count_G, count_T]
    return count, arr

def Searching(pattern, last, suff_array, count):
    "Ищет вхождения подстроки pattern в начальную строку"
    "Возвращает список из индексов вхождений"

    if not pattern or len(pattern) > len(last):
        return('Некорректный ввод подстроки')


    pattern = list(pattern)
    top, bottom = 0, 0
    ind, occur = [], []
    start = False
    flag = False

    while top <= bottom and pattern:
            symbol = pattern[-1]
            pattern.pop(-1)
            if start == False:
                if symbol == 'A':
                    top = 1
                    bottom = count[0]
                    start = True

                if symbol == 'C':
                    top = count[0] + 1
                    bottom = count[0] + count[1]
                    start = True

                if symbol == 'G':
                    top = count[0]+count[1]+1
                    bottom = count[0]+count[1]+count[2]
                    start = True

                if symbol == 'T':
                    top = count[0]+count[1]+count[2]+1
                    bottom = count[0]+count[1]+count[2]+count[3]
                    start = True

            else:
                for i in range(top, bottom+1):
                    if last[i][0] == symbol:
                        ind.append(last[i][1])
                        flag = True
                    else:
                        if flag:
                            continue

                if flag == False:
                    return 'Вхождений подстроки в строку нет.'

                sort = sorted(ind)
                top = sort[0]
                bottom = sort[-1]
                ind.clear()

                if symbol == 'A':
                    True
                if symbol == 'C':
                    top += count[0]
                    bottom += count[0]
                if symbol == 'G':
                    top += count[0]+count[1]
                    bottom += count[0] + count[1]
                if symbol == 'T':
                    top += count[0]+count[1]+count[2]
                    bottom += count[0] + count[1] + count[2]

    for suff in range(top, bottom+1):
        occur.append(int(suff_array[suff])+1)

    if occur:
        return sorted(occur)
    else:
        return 'Вхождений подстроки в строку нет.'


a = read_fasta('T.fasta')
pattern = read_fasta('P.fasta')

suff_array = BWT_transforming(a)[2]
count, last = Indexing(BWT_transforming(a)[1])
final = Searching(pattern, last, suff_array, count)
print(*final)