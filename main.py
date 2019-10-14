map_ = []
params = input("Введите параметры (ширина, высота, кол-во бомб): ").split()
weight = int(params[0])
height = int(params[1])
count_bombs = int(params[2])
for i in range(0, height):
    map_.append({})
    for j in range(0, weight):
        map_[i][j] = 0
for n in range(1, count_bombs + 1):
    location = input("Введите координаты бомбы номер " + str(n) + ": ").split()
    x = int(location[0]) - 1
    y = int(location[1]) - 1
    if x in range(0, weight) and y in range(0, height) and map_[x][y] != "*":
        map_[x][y] = "*"
    else:
        all_not_ok = True
        while all_not_ok:
            if x < 0 or x >= weight or y < 0 or y >= height:
                location = input("Этой точки нет на карте, пожалуста, выберите другую: ").split()
            else:
                location = input("На этой точке уже есть бомба, пожалуйста, введите другую: ").split()
            x = int(location[0]) - 1
            y = int(location[1]) - 1
            if x in range(0, weight) and y in range(0, height) and map_[x][y] != "*":
                map_[x][y] = "*"
                all_not_ok = False
    for i in range(x - 1, x + 2):
        if i in range(0, height):
            for j in range(y - 1, y + 2):
                if j in range(0, weight) and map_[i][j] != "*":
                    map_[i][j] += 1
first_str = "  "
for i in range(1, weight + 1):
    first_str += str(i) + " "
print(first_str)
for i in range(0, height):
    str_ = str(i + 1) + " "
    for j in range(0, weight):
        str_ += str(map_[i][j]) + " "
    print(str_)
