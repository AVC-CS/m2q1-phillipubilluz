def getPivot(number):
    avg = sum(number) / len(number)
    pivot = number[0]
    best_diff = abs(pivot - avg)

    for x in number[1:]:
        diff = abs(x - avg)
        if diff <= best_diff:
            pivot = x
            best_diff = diff
    return pivot


def split(number):
    pivot = getPivot(number)
    left = [x for x in number if x <= pivot]
    right = [x for x in number if x > pivot]
    return left + right



def main():
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
