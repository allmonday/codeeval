def fizz_buzz(line):
    args = line.strip().split(' ')
    a = int(args[0])
    b = int(args[1])
    group = int(args[2])
    ret = []
    for i in xrange(1, group + 1):
        if i % a == 0 and i % b == 0:
            ret.append('FB')
        elif i % a == 0:
            ret.append('F')
        elif i % b == 0:
            ret.append('B')
        else:
            ret.append(str(i))
    return ' '.join(ret)

def fizz_buzz_design(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()
        for line in lines:
            print fizz_buzz(line)

fizz_buzz_design('fbinput.txt')
