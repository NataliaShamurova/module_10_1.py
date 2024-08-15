from threading import Thread
from time import sleep
from datetime import datetime


time_start = datetime.now()

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for line in range(1, word_count + 1):
            file.writelines(f'Какое-то слово № {line}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


wite = wite_words(10, 'example1.txt')
wite = wite_words(30, 'example2.txt')
wite = wite_words(200, 'example3.txt')
wite = wite_words(100, 'example4.txt')
time_end = datetime.now()
res_time_f = time_end - time_start
print(res_time_f, 'Время работы функции')


time_start_p = datetime.now()
args_first = (10, 'example5.txt')
args_second = (30, 'example6.txt')
args_third = (200, 'example7.txt')
args_fourth = (100, 'example8.txt')
thr_first = Thread(target=wite_words, args=args_first)
thr_second = Thread(target=wite_words, args=args_second)
thr_third = Thread(target=wite_words, args=args_third)
thr_fourth= Thread(target=wite_words, args=args_fourth)


thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_p = datetime.now()
res_time_p = time_end_p - time_start_p
print(res_time_p, 'Время работы потока')
