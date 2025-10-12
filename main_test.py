import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '35 5 10 20 40 15\n'
    # sys.stdin = io.StringIO(datastr)

    # main.main()
    number = [65, 15, 10, 20, 40, 55]
    number = main.split(number)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    l = number[:4]
    r = number[4:]
    print('left', l)
    print('pivot', number[3])
    print('right', r)
    assert number[0] <= 40
    assert number[1] <= 40
    assert number[2] <= 40 
    assert number[3] == 40
    assert number[4] >= 40
    assert number[5] >= 40


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '1 2 4 5 3\n'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    number = [1, 2, 4, 5, 3]
    number = main.split(number)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    l = number[:2]
    r = number[3:]
    print('left', l)
    print('pivot', number[2])
    print('right', r)
    assert number[2] == 3
    cl = [v for v in l if v > 3]
    cr = [v for v in r if v < 3]
    assert cl == []
    assert cr == []
