def p1(max):
    def filt(x): return ((x % 3 == 0) | (x % 5 == 0))
    return list(filter(filt,range(1,max)))

print sum(p1(1000))
