import os
import pandas as pd
import re


def process(file_path):
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path, encoding='utf-8')
        df.insert(loc=0, column='insight', value='0')
        df_merged = pd.concat([df['dlg_id'], df['role'], df['text']], ignore_index=True, sort=False, axis=1)
        df_list = df_merged.values.tolist()
        str_find = ['Добрый день', 'добрый день', 'Здравствуйте', 'здравствуйте', 'До свидания', 'до свидания',
                    'Всего доброго', 'всего доброго']
        value = 'manager'
        a = []
        for dlg_id, role, text_message in df_list:
            if role == value:
                if re.search(r'\bзовут\b', text_message):
                    print('Реплика с представлением менеджера:', text_message)
                    print('Имя: ', text_message.split()[2])
            if re.search(r'\bкомпания\b', text_message):
                if re.search(r'\bангелина\b', text_message):
                    print('Название комапнии: ', ' '.join(text_message.split()[4:6]))
                if re.search(r'\bмаксим\b', text_message):
                    print('Название комапнии: ', ' '.join(text_message.split()[5:6]))
            # __________________________________________________________________________________________________________
            list_text_start = []
            list_text_end = []
            for id in range(6):
                if dlg_id == id and role == value:
                    for string_end in str_find[4:]:
                        if text_message.find(string_end) != -1:
                            list_text_end.append(text_message)
                            df['insight'] = df['text'].str.contains('|'.join(list_text_end))
                            print('ID диалога:', dlg_id, 'Реплика с прощанием : ', list_text_end)
                    for string_start in str_find[:4]:
                        if text_message.find(string_start) != -1:
                            list_text_start.append(text_message)
                            df['insight'] = df['text'].str.contains('|'.join(list_text_start))
                            print('ID диалога:', dlg_id, 'Репликиа с приветствием: ', list_text_start)
                # __________________________________________________________________________________________________________
            if dlg_id == 5:
                a.append(text_message.split())
        print('Имя: ', a[1][2])


if __name__ == '__main__':
    file_path = r''
    process(file_path)
