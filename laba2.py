ksi = int(input())
n = int(input())
step = 40

f = {
    40: [8, 6, 3, 4],
    80: [10, 9, 4, 6],
    120: [11, 11, 7, 8],
    160: [12, 13, 11, 16],
    200: [18, 15, 18, 16]
} # представляет из себя таблицу 1; 

tab_2 = [
    [ # шаги
        { # кси
            40: (4, 40), # (целевая функция, переменные) 
            80: (6, 80),
            120: (8, 120),
            160: (13, 160),
            200: (16, 120)
        }, 
    ],
    [
        {
            40: (4, 0), 
            80: (7, 40),
            120: (9, 40),
            160: (13, 0),
            200: (18, 200)
        },
    ],
    [
        {
            40: (6, 40), 
            80: (10, 40),
            120: (13, 80),
            160: (16, 80),
            200: (19, 24)
        },
    ],
    [
        {
            40: (8, 40), 
            80: (14, 40),
            120: (18, 40),
            160: (21, 40),
            200: (24, 40)
        },
    ]
] # таблица 2 с примерными данными

# tab_3 = [
#     [
#         {
#             40: {
#                     0: 4, 
#                     40: 3
#                 }, 
#             80: {
#                     0: 6, 
#                     40: 7,
#                     80: 4
#                 }
#         }
#     ],
#     [],
#     []
# ]
tab_3 = []



# Далее будет код, который заполняет таблицы 2 и 3
# Затем получаем значения из таблицы 2

# Итог:
# 2) реализовать заполнение таблиц 2 и 3;         <- Это самое сложное, наверное
# 3) реализовать получение ответа из таблицы 2;
