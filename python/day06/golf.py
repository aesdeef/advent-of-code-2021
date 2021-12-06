l=[open('6').read().count(d) for d in '012345678'];x=['l=l[1:]+l[:1];l[6]+=l[8]']*258;x[80]=x[-1]='print(sum(l))';exec(';'.join(x))
