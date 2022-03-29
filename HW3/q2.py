def f(*x, **y):
    def s1(x): 
        s=0 
        if x:
            for i in x:
                s += i
        return s


    def p1(x):
        s=1
        if x:
            for i in x:
                s *= i
        return s

    def rs1(x):
        s=0 
        x = map(lambda x: 1/x,x)
        if x:
            for i in x:
                s += i
        return s
    if y["action"] == "sum":
        return s1(*x)
    elif y["action"] == "prod":
        return p1(*x)
    elif y["action"] == "rec":
        return rs1(*x)
    else:
        return f"bad argument: {y}"


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-lst', nargs='+', default = ['1'], help="List of numbers")
parser.add_argument('-op', default = 'sum', help = "sum, prod, rec")
args = parser.parse_args()
print(args.lst)
print(args.op)

if __name__ == '__main__':
    xlst = args.lst
    xlst = list(map(int,xlst))
    print(f(xlst, action = args.op))





    








