#Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
with open ('input.txt','r') as f:
    a=f.readline()
    n=int(a)
with open ('output.txt','w') as f:
    f.write(str(n-2))
    f.write('  ')
    f.write(str( n-1))
    f.write('  ')
    f.write(str( n))
    f.write('  ')
    f.write(str(n+1))
    f.write('  ')
    f.write(str(n+2))
    

