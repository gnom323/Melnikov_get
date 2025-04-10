def calcul(numba, three_ones):
    if numba == 1:
        return 0
    else:
        if three_ones == 12:
            return 99999999
        else:
            if numba % 2 == 0 and numba % 3 == 0:
                return min(calcul(numba/2, three_ones), calcul(numba/3, three_ones), calcul(numba-1, 1 + three_ones)) + 1
            elif numba % 2 == 0:
                return min(calcul(numba/2, three_ones), calcul(numba-1, 1 + three_ones)) + 1
            elif numba % 3 == 0:
                return min(calcul(numba/3, three_ones), calcul(numba-1, 1 + three_ones)) + 1
            else:
                return calcul(numba-1, 1 + three_ones) + 1

numba = int(input())
three_ones = 0
print(calcul(numba, three_ones))