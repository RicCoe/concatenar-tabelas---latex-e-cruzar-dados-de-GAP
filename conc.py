# -*- coding: iso-8859-15 -*-

def corrige(nome):
    with open (nome,'r') as file:
        e=[]
        with open('corrigido.tex','w') as  stream:
            s=[]
            arquiv=file.read()
            for r in arquiv:
                if r=='_':
                    s.append('\\')
                    s.append('_')
                else:
                    s.append(r)
            s=''.join(s)
            stream.write(s)


def analisa(nome):
    with open(nome,'r') as file:
        instancia=[]
        sol=[]
        tempo=[]
        alg121=[]
        alg131=[]
        alg221=[]
        alg231=[]
        alg321=[]
        alg331=[]
        mbc221=[]
        mbc231=[]
        s=file.readlines()
        print(len(s))
        r=range(1,len(s)/2+1)
        for i in r:
            del s[i]
        for k in range(len(s)):
            s[k]=s[k].split('&')
            
        for i in range(len(s)):#para  arrancar o '\\ ' do final
            s[i][len(s[i])-1]=list( s[i][len(s[i])-1])
            del s[i][len(s[i])-1][len(s[i][len(s[i])-1])-1]
            del s[i][len(s[i])-1][len(s[i][len(s[i])-1])-1]
            del s[i][len(s[i])-1][len(s[i][len(s[i])-1])-1]
            s[i][len(s[i])-1]=''.join(s[i][len(s[i])-1])
            
        alg131=s[0:30]
        alg121=s[30:60]
        alg231=s[60:90]
        alg221=s[90:120]
        alg331=s[120:150]
        alg321=s[150:180]
        mbc231=s[180:210]
        mbc221=s[210:240]
        for s in range(len(mbc231)):
            del mbc231[s][3]
            del mbc231[s][3]
            del mbc221[s][3]
            del mbc221[s][3]
        analise2(alg121,mbc221,'alg121.tex')
        analise2(alg131,mbc231,'alg131.tex.')
        analise2(alg221,mbc221,'alg221.tex')
        analise2(alg231,mbc231,'alg231.tex')
        analise2(alg321,mbc221,'alg321.tex')
        analise2(alg331,mbc231,'alg331.tex')
        
def analise2(novo,mbc,nome):
    em=mbc[20:30]
    cm=mbc[0:10]
    rm=mbc[10:20]
    enovo=novo[20:30]
    rnovo=novo[10:20]
    cnovo=novo[0:10]
    gap1=[]
    gap2=[]
    gap3=[]
    for k in  range(len(em)):
        em[k][1]=float(em[k][1])
        em[k][2]=float(em[k][2])
        cm[k][1]=float(cm[k][1])
        cm[k][2]=float(cm[k][2])
        rm[k][1]=float(rm[k][1])
        rm[k][2]=float(rm[k][2])
        enovo[k][1]=float(enovo[k][1])
        enovo[k][2]=float(enovo[k][2])
        rnovo[k][1]=float(rnovo[k][1])
        rnovo[k][2]=float(rnovo[k][2])
        cnovo[k][1]=float(cnovo[k][1])
        cnovo[k][2]=float(cnovo[k][2])

    for k in range(10):
        try: 
            gap1.append((cnovo[k][1]-cm[k][1])/cnovo[k][1])
        except ZeroDivisionError:
            gap1.append(0)
        try:
            gap2.append((rnovo[k][1]-rm[k][1])/rnovo[k][1])
        except ZeroDivisionError:
            gap2.append(0)
        try:
            gap3.append((enovo[k][1]-em[k][1])/enovo[k][1])
        except ZeroDivisionError:
            gap3.append(0)
    with open (nome,'w') as file:
        file.write('\\begin{tabular}{|c|c|c|c|c|}'+'\n \\hline \\multicolumn{5}{|c|}')
        file.write('{\\textbf{Resultados do Relax And Fix (instâncias c)}}\\\\ \n')
        file.write('\\hline \n Instância &Solução MBC2 & Solução RF & Tempo RF & GAP')
        file.write('\\\\ \n \\hline \\hline \n')
        for  i in range(10):
            file.write(cnovo[i][0]+'&'+str(cm[i][1])+' & '+str(cnovo[i][1])+' & ')
            file.write(str(cnovo[i][2])+' & '+str(gap1[i])+'\\\\ \n \\hline \n')   
        file.write('\\end{tabular}'+'\n')    
        file.write('\\begin{tabular}{|c|c|c|c|c|}'+'\n \\hline \\multicolumn{5}{|c|}')
        file.write('{\\textbf{Resultados do Relax And Fix (instâncias r)}}\\\\ \n')
        file.write('\\hline \n Instância &Solução MBC2 & Solução RF & Tempo RF & GAP')
        file.write('\\\\ \n \\hline \\hline \n')
        for  i in range(10):
            file.write(rnovo[i][0]+' & '+str(rm[i][1])+' & '+str(rnovo[i][1])+' & ')
            file.write(str(rnovo[i][2])+' & '+str(gap2[i])+'\\\\ \n \\hline \n')
        file.write('\\end{tabular}'+'\n')
        file.write('\\begin{tabular}{|c|c|c|c|c|}'+'\n \\hline \\multicolumn{5}{|c|}')
        file.write('{\\textbf{Resultados do Relax And Fix (instâncias e)}}\\\\ \n')
        file.write('\\hline \n Instância &Solução MBC2 & Solução RF & Tempo RF & GAP')
        file.write('\\\\ \n \\hline \\hline \n')
        for  i in range(10):
            file.write(enovo[i][0]+' & '+str(em[i][1])+' & '+str(enovo[i][1])+' & ')
            file.write(str(enovo[i][2])+' & '+str(gap3[i])+'\\\\ \n \\hline \n')
        file.write('\\end{tabular}'+' \n')  
            
            
    
    
def floatCastVet(vet):
    for r in range(0,len(vet)):
        vet[r]=float(vet[r])
    return vet
def read(tab):
    with open(tab,'r') as file:
        stream=file.readlines()
        for i in range(1,int(len(stream)/2)):
            del stream[i]
        del stream[len(stream)-1]
        for i in range(0,len(stream)):
            stream[i]=list(stream[i])
        instancias=[] #comecam  as  alteracoes
        for i in range(0,len(stream)):
                r=stream[i][0]
                y=1
                v=[]
                while(r!='&'):
                        v.append(r)
                        r=stream[i][y]
                        y+=1
                instancias.append(v)
        for i in range(0,len(instancias)):
                instancias[i] = ''.join(str(e) for e in instancias[i])
        for i in range(0,len(stream)):#parte antiga  do codigo
            for y in range(0,20):
                del stream[i][0]
            if(i>=10):
                del stream[i][0]
            for y in range(0,3):
                del stream[i][len(stream[i])-1]
        for i in range(0,len(stream)):
            stream[i] = ''.join(str(e) for e in stream[i])
            stream[i]=stream[i].split('&')
        file.close()
        j=[]
        k=[]
        for z in range(0,len(stream)):
            k.append(stream[z][0])
            j.append(stream[z][1])
        stream=[]
        stream.append(k)
        stream.append(j)
        stream.append(instancias)
        return stream
def gapAndStat(nome_tabela,relax,integer,instancias,nome):#usado para  as solucoes linear, inteira e integralizada pelo relax and fix
    gap=[]#nome_tabela e  uma  variavel que guarda  o nome da tabela de dados  da solucao inteira
    gap2=[]#definir  o  gap  em  termos  da  solucao inteira e  relaxada, e  inteira e relax and fix, tambem da  relax and  fix
    for i in range(0,len(relax[0])):#para  a solucao relaxada
        try:
            gap.append(100*float(integer[1][i]-relax[1][i])/float(integer[1][i]))
        except ZeroDivisionError:#se a   solucao  inteira  for  nula entao  a relaxada tambem o sera, pois todo fluxo eh positivo
            gap.append(0)
        try:
            gap2.append( 100*float(integer[0][i]-relax[0][i])/float(integer[0][i]))
        except ZeroDivisionError:
            gap2.append(0)
    with open(nome_tabela,'w')  as lat:
        lat.write('\\begin{table}\n\center\n\caption{}\n\\begin{tabular}{|l|c|c|c|c|}\n\hline\n\multicolumn{5}{|c|}{\\textbf{')
        lat.write(nome)
        lat.write('}} \n\hline\n')
        lat.write('Instância & Solução & Tempo(s) & Gap da solução & Gap de tempo')
        lat.write('\hline\n\hline\n')
        for i in range(0,len(instancias)):
            lat.write(instancias[i])
            lat.write(' &c ')
            lat.write(str(integer[1][i]))
            lat.write(' & ')
            lat.write(str(integer[0][i]))
            lat.write(' & ')
            lat.write(str(gap[i]))
            lat.write(' & ')
            lat.write(str(gap2[i]))
            lat.write(' \\\\ \n')
            lat.write('\hline\n')


a=read('int21MbcAlt.tex')
e=[]
e.append(floatCastVet(a[0]))
e.append(floatCastVet(a[1]))
u=read('tabela1.tex')
v=[]
v.append(floatCastVet(u[0]))
v.append(floatCastVet(u[1]))
print(e)
print(v)
gapAndStat('tabela.tex',v,e,u[2],'MBC alterado solução inteira para 21 nós(instâncias c)')


