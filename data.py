import json
DICT_DATA = 'quiz_data.json'
quiz_data =[{
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения чисел c плавующей точкой?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 1
    },
    {
        'question': 'Какой тип данных используется для хранения текстовых строк?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 2
    },
    {
        'question': 'Что из перечисленного является лишним?',
        'options': ['if()', 'for()', 'while()', 'do while()'],
        'correct_option': 0
    },
    {
        'question': 'Что является типом контейнера из Python?',
        'options': ['array', 'List', 'Vector', 'Все выше перечисленное'],
        'correct_option': 1
    },
    {
        'question': 'Какие библиотеки мы не использовали на курсе?',
        'options': ['NumPy', 'Pandas', 'Keras', 'OS'],
        'correct_option': 2
    },
    {
        'question': 'Какое из приведённых объявлений функций является правильным?',
        'options': ['int a:', 'define a():', 'Function a():', 'def a():'],
        'correct_option': 3
    },
    {
        'question': 'В каком году был создан Python?',
        'options': ['1991', '2007', '1987', '1994'],
        'correct_option': 0
    },
    {
        'question': 'Кто создал Python?',
        'options': ['Гвидо ван Россум', 'Деннис Ритчи', 'Бьёрн Страуструп', 'Брендан Айк'],
        'correct_option': 0
    },]
with open(DICT_DATA, "w") as j:
    json.dump(quiz_data, j)