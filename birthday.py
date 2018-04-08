from time import sleep
import sys
import os

r = 5

def A(r):
    for row in range(x, r):
        for col in range(4):
            if ((col == 0 or col == 3) and row > 0) or ((row == 0 or row == 2) and (col >0 and col < 3)):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def B(r):
    for row in range(x, r):
        for col in range(4):
            if col == 0 or (row%2 == 0 and col > 0 and col < 3) or (col == 3 and row%2 != 0):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def D(r):
    for row in range(x, r):
        for col in range(5):
            if col == 0 or ((row == 0 or row == 4) and (col > 0 and col < 4)) or (col == 4 and (row > 0 and row < 4)):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def H(r):
    for row in range(x, r):
        for col in range(4):
            if col == 0 or (row == 2 and col > 0 and col < 3) or col == 3:
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def I(r):
    for row in range(x, r):
        for col in range(5):
            if row == 0 or (col == 2 and row > 0 and row < 4) or row == 4:
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def L(r):
    for row in range(x, r):
        for col in range(4):
            if col == 0 or (row == 4 and col > 0):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def P(r):
    for row in range(x, r):
        for col in range(4):
            if col == 0 or ((row == 0 or row == 2) and (col > 0 and col < 3)) or (col == 3 and row == 1):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def R(r):
    for row in range(x, r):
        for col in range(5):
            if col == 0 or ((row == 0 or row == 2) and (col > 0 and col < 4)) or (col == row and col > 2) or (row == 1 and col == 4):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def T(r):
    for row in range(x, r):
        for col in range(5):
            if row == 0 or (col == 2 and row > 0):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def U(r):
    for row in range(x, r):
        for col in range(5):
            if ((col == 0 or col == 4) and row < 4) or (row == 4 and (col > 0 and col < 4)):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def V(r):
    for row in range(x, r):
        for col in range(5):
            if ((col == 0 or col == 4) and (row < 3)) or (col%2 != 0 and row == 3) or (row == 4 and col == 2):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def Y(r):
    for row in range(x, r):
        for col in range(5):
            if (col == 2 and row > 1) or (col == row and col < 2) or (row == 0 and col == 4) or (row == 1 and col == 3):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

def heart(r):
    for row in range(x, r):
        for col in range(5):
            if ((col%2 != 0) and (row == 0 and row == 3)) or (row == 1 and (col%2 == 0)):
                print '@',
                # sys.stdout.flush()
                # sleep(.1)
            else:
                print ' ',

os.system('clear')
print ' '*142,
for w in range(8):
    print '*'*143
    sleep(.5)
print ''

for k in range(1, 6):
    x = k-1 # 45
    print '-'*23, '|', ' '*17,
    H(k)
    print ' ',
    A(k)
    print ' ',
    P(k)
    print ' ',
    P(k)
    print ' ',
    Y(k)
    print ' '*23, '|', '-'*23
    sys.stdout.flush()
    sleep(.6)

print '-'*23, '|', ' '*91, '|', '-'*23
print '-'*23, '|', ' '*91, '|', '-'*23

for k in range(1, 6):
    x = k-1 
    print '-'*23, '|', ' ',
    B(k)
    print ' ',
    I(k)
    print ' ',
    R(k)
    print ' ',
    T(k)
    print ' ',
    H(k)
    print ' ',
    D(k)
    print ' ',
    A(k)
    print ' ',
    Y(k)
    print ' ', '|', '-'*23
    sys.stdout.flush()
    sleep(.6)

print '-'*23, '|', ' '*91, '|', '-'*23
print '-'*23, '|', ' '*91, '|', '-'*23

for k in range(1, 6):
    x = k-1
    print '-'*23, '|', ' '*16,
    V(k)
    print ' ',
    I(k)
    print ' ',
    P(k)
    print ' ',
    U(k)
    print ' ',
    L(k)
    print ' '*20, '|', '-'*23
    sys.stdout.flush()
    sleep(.6)

print ''
print '*'*1287
print '*'*142,
ex = input()


