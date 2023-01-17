# домашнее задание по теме "Открытие и чтение файла, запись в файл" от 16/01/23
import os

key_list =['ingredient_name', 'quantity', 'measure']

# печать книги рецептов - словаря cook_book - форматирование по образцу в задаче №1
def print_cook_book():
   print('cook_book = {')
   last_key = list(cook_book.keys())[-1]
   for k, v in cook_book.items():
      print(f"  '{k}': [")
      [print(f'    {el}{"," * (el != v[len(v) - 1])}') for el in v]
      print(f'    ]{"," * (k != last_key)}')
   print('}')

# реализация функции по условиям задачи №2
def get_shop_list_by_dishes(dishes, person_count):
   shop_dct = {}
   for dish in dishes:
      for dct in cook_book[dish]:
         shop_dct.setdefault(dct['ingredient_name'], {}).setdefault('measure', dct['measure'])
         shop_dct[dct['ingredient_name']]['quantity'] = \
            shop_dct[dct['ingredient_name']].get('quantity', 0) + dct['quantity'] * person_count
   return shop_dct

# печать списка продуктов - форматирование по образцу в задаче №2
def print_shop_list(dishes, person_count):
   shop_dct = get_shop_list_by_dishes(dishes, person_count)
   last_key = list(shop_dct.keys())[-1]
   print(f'Для приготовления блюд: {dishes}\nколичество персон: {person_count}\nпонадобятся продукты:')
   print('{')
   for k, v in shop_dct.items():
      print(f"   '{k}':  {v}{',' * (k != last_key)}")
   print('}')

# создание объединенного файла - задача №3
def create_united_file(files):
   f_lst = []
   for fname in files:
      with open(fname, 'r', encoding='utf-8') as f:
         lst = f.readlines()
         f_lst.append({'name': fname.split('\\')[-1], 'len': len(lst), 'text': lst})
   f_lst = sorted(f_lst, key=lambda x: x['len'])
   print('в объединенный файл записаны строки из файлов:')
   for el in f_lst:
      print('файл: ' + el['name'], f"кол-во строк: {el['len']}", sep='\n')
      #print(*el['text'])
   # перед записью в файл files\united.txt удалим все старые данные из него
   if os.path.exists(r'files\united.txt'):
      f = open(r'files\united.txt', 'r+')
      f.seek(0)
      f.truncate()
      f.close()
   with open(r'files\united.txt', 'a', encoding='utf-8') as fout:
      for el in f_lst:
         fout.write(el['name'] + '\n')
         fout.write(str(el['len']) + '\n')
         [fout.write(line) for line in el['text']]
         fout.write('\n')

def react_on_kbd_command(comm):
   if comm == 'x':
      return
   if comm == '1':
      print_cook_book()
   elif comm == '2':
      print_shop_list(['Запеченный картофель', 'Омлет'], 2)
   elif comm == '3':
      print_shop_list(['Фахитос', 'Омлет'], 6)
   elif comm == '4':
      create_united_file([r'files\1.txt', r'files\2.txt', r'files\3.txt'])

def main():
   command = 'x'
   while command != '0':
      react_on_kbd_command(command)
      print('*' * 80, '\n',
            '0 - выход из программы\n1 - печать книги рецептов\n'
            '2 - список продуктов для приготовления блюд "Запеченный картофель", "Омлет" на 2 персоны\n'
            '3 - список продуктов для приготовления блюд "Фахитос", "Омлет" на 6 персон\n'
            '4 - печать результата объединения файлов 1.txt, 2.txt и 3.txt в один\n'
            'Введите команду: ', sep='')
      command = input()
   print('До свидания!')

# чтение файла и формирование словаря cook_book - задача №1
cook_book = {}
with open('files\cook_book.txt', 'r', encoding='utf-8') as fin:
   for line in fin:
      dish_name = line.strip()
      cook_book[dish_name] = []
      num = int(fin.readline())
      for i in range(num):
         ing, qty, unit = fin.readline().strip().split(' | ')
         dct = dict.fromkeys(key_list)
         dct[key_list[0]] = ing
         dct[key_list[1]] = int(qty)
         dct[key_list[2]] = unit
         cook_book[dish_name].append(dct)
      fin.readline()

main()

