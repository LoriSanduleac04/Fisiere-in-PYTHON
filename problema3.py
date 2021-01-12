""" 
Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor
albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii.
"""
with open ('globulete.txt','r') as f:
    a=f.readline()
    na=int(a)
nr=na+3
nb=(na+nr)-2
total=na+nr+nb
with open ('bradut.txt','w') as f:
    f.write(str(total))
    
    

