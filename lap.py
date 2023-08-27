def lapped_lap(t1, t2):
    if t1 == t2 or t1 > t2:
        return -1

    low = 1
    high = 10**12

    while low <= high:
        mid = (low + high) // 2

        if mid * t1 > (mid - 1) * t2:
            return mid
        elif mid * t1 < (mid - 1) * t2:
            high = mid - 1
        else:
            low = mid + 1

def main():
    list_answer = []
    list_Tuples = []
    while True:
        line = input().strip()
        if not line:  
            break
        numbers = [int(num) for num in line.split()]  
        tup = tuple(numbers)
        list_Tuples.append(tup)

    for tupla in list_Tuples:
        vuelta_resultado = lapped_lap(tupla[0], tupla[1])
        list_answer.append(vuelta_resultado +2)

    for i in list_answer:
        print(i)
main()
