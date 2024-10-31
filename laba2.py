ksi_0 = int(input())
n = int(input())
step = 40

f = {
    40: [8, 6, 3, 4],
    80: [10, 9, 4, 6],
    120: [11, 11, 7, 8],
    160: [12, 13, 11, 13],
    200: [18, 15, 18, 16]
} # представляет из себя таблицу 1; 

f_len = len(f[40])

tab_2 = {} # таблица 2(основная) с примерными данными

tab_3 = [] # таблица 3(вспомогательная)

x_k = []
for i in range(n + 2):
    if i > 0:
        x_k.append([])
        for i_1 in range(i + 1):
            x_k[i - 1].append(i_1 * step)

ksi_k = []
for i in range(n + 1):
    ksi_k.append(x_k[i][::-1])

for i in range(n - 1):
    tab_3.append({x: {} for x in f.keys()})

for i in range(n - 1):
    for i_1 in range(n + 1):
        a = 0
        for i_2 in range(a + 2 + i_1):
            current_x_k = x_k[len(x_k) - 1][i_2]
            current_ksi_k = ksi_k[i_1][i_2]
            
            if i_2 == 0 :
                f_x = 0
            else:
                f_x = f[current_x_k][f_len-i-2]
            
            if i_2 == a + 1 + i_1:
                Z_ksi = 0
            else:
                Z_ksi = f[current_ksi_k][i_1-i-1]
            
            tab_3[i][(i_1 + 1) * step].update({current_x_k: f_x + Z_ksi})
        a += 1

# Преобразование второй таблицы
ksi_list = [i for i in range(step, ksi_0 + 1, step)]
for i in range(n):
    for ksi in ksi_list:
        if i == 0:
            tab_2[ksi] = [(f[ksi][n - 1], ksi)]
            continue
        key = max(tab_3[i - 1][ksi], key=tab_3[i - 1][ksi].get)
        tab_2[ksi].append((tab_3[i - 1][ksi][key], key))

# Получение ответа
max_profit = tab_2[ksi_0][n - 1][0]
funds_distirbution = []

funds_remain = ksi_0
for i in range(n - 1, -1, -1):
    value = tab_2[funds_remain][i][1]
    funds_distirbution.append(value)

    funds_remain -= value
    if funds_remain == 0:
        break

print("max_profit:", max_profit)
print(funds_distirbution)

