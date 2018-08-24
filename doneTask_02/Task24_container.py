l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
# l1+l1, wMax
l1l2 = l1 + l2
if w1 >= w2:
    wMax = w1
else:
    wMax = w2
# w2l1, w1l2Max
w2l1 = w2 + l1
if w1 >= l2:
    w1l2Max = w1
else:
    w1l2Max = l2
# w1l2, w2l1Max
w1l2 = w1 + l2
if w2 >= l1:
    w2l1Max = w2
else:
    w2l1Max = l1
# w1w2, lMax
w1w2 = w1 + w2
if l1 >= l2:
    lMax = l1
else:
    lMax = l2
# hMax
if h1 >= h2:
    hMax = h1
else:
    hMax = h2
if hMax > hc:
    print('NO')
elif h1 + h2 > hc:
    if (w1w2 <= wc and lMax <= lc) or (w1w2 <= lc and lMax <= wc):
        print('YES')
    elif (w1l2 <= wc and w2l1Max <= lc) or (w1l2 <= lc and w2l1Max <= wc):
        print('YES')
    elif (w2l1 <= wc and w1l2Max <= lc) or (w2l1 <= lc and w1l2Max <= wc):
        print('YES')
    elif (l1l2 <= wc and wMax <= lc) or (l1l2 <= lc and wMax <= wc):
        print('YES')
    else:
        print('NO')
else:
    if (wMax <= wc and lMax <= lc) or (wMax <= lc and lMax <= wc) or \
            (w2l1Max <= wc and w1l2Max <= lc) or \
            (w2l1Max <= lc and w1l2Max <= wc):
        print('YES')
    else:
        print('NO')
