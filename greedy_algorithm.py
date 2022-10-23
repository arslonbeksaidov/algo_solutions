hududlar = {
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
}

binolar = {
    'B01': {10, 16, 17},
    'B02': {1, 4, 11, 30},
    'B03': {17, 18, 27, 30},
    'B04': {1, 7, 17, 19, 30},
    'B05': {7, 11, 15, 17, 20},
    'B06': {7, 6, 11},
    'B07': {23, 30},
    'B08': {10, 14, 18, 25, 29},
    'B09': {10, 16, 17, 19},
    'B10': {10, 13, 19},
    'B11': {1, 3, 6, 13, 16},
    'B12': {8, 12},
    'B13': {5, 10, 15},
    'B14': {5, 8, 17, 23, 24},
    'B15': {2, 9, 21, 22, 26, 28}
}

yakuniy_binolar = set()
while hududlar:
    bino_best = None
    qamralgan_hududlar = set()
    for bino, bino_qamrovi in binolar.items():
        qamrov = bino_qamrovi & hududlar
        print(f"{bino}:{qamrov}")
        if len(qamrov) > len(qamralgan_hududlar):
            qamralgan_hududlar = qamrov
            bino_best = bino
    hududlar -= qamralgan_hududlar
    yakuniy_binolar.add(bino_best)
    print(f"Tanlangan bino: {bino_best}")
    print(f"Qolgan hududlar: {hududlar}")
    print(f"Tanlangan binolar : {yakuniy_binolar}")
    input()
