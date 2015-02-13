# -*- coding: iso-8859-15 -*-
import os
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
            print(integer[1][i])
            print(relax[1][i])
            print(float(integer[0][i]))
            print(100*float(integer[1][i]-relax[1][i])/float(integer[1][i]))
            os.system('pause')
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
