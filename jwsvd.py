def mystery(st):
    if (len(st)==0):
        res =0
    else:
        xx = st[1:]
        res= 3 + mystery(xx)
    return res

x = ["2","3","4"]
print(mystery(x))
