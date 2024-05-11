def temperature(x,y):
    # T = (T-x)/y
    # x = a, b = 0
    # ya = b = 1
    t = (-x/(y-1))
    return t

def main():
    x, y = [float(x) for x in input().split()]
    if y == 1:
        if x == 0:
            print('ALL GOOD')
        else:
            print('IMPOSSIBLE')
    else:
        print(temperature(x,y)) 
main()