inputs = [
'13, 8\n',
'17,16\n',
'1416,8\n'
]

def process(left, right):
    left = int(left)
    right = int(right)
    tmp = right
    while (left > right):
        right += tmp
    return right

for i in inputs:
    left, right = i.strip().split(',')
    print process(left, right)


# import sys
# def process(left, right):
#     left = int(left)
#     right = int(right)
#     while (left > right):
#         right *=2
#     return right
# test_cases = open(sys.argv[1], 'r')
# for test in test_cases:
#     left, right = test.strip().split(',')
#     print process()
# test_cases.close()
