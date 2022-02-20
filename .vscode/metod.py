import matplotlib.pyplot as plt 
import networkx as nx
from sympy.simplify.simplify import simplify
from networkx.algorithms.assortativity import pairs
from numpy.ma.core import empty, power
from networkx.algorithms.components import weakly_connected
from numpy import random as rd 
import numpy as np
from sympy import symbols as sy 
import requests
from bs4 import BeautifulSoup

class play: 

    def __init__():
        pass

    #ECUACION DE RECURRENCIA LINEAL HOMOGENEA CON COEFICIENTES CONSTANTES 
    def play_RRLHCC(cof):
        if (cof is not empty) and (len(cof)>1) and (not all(n==0 for n in cof)): 
            a=np.poly1d(cof)
            r = np.roots(a)
            nconst=len(r)
            com=np.iscomplex(r)

            if True in com:
                err ="Error: No se puede solucionar"
                return (err)
            else:
                rent= [np.round(i.real, 1) for i in list(r)]
                
                rlist=[];sinr=[];ndone=[]
                for _ in range(0,nconst):
                    rlist.append("C_"+str(_)+" * "+str(rent[_])+"^n")
                
                for i in rent:
                    if i not in sinr:
                        sinr.append(i)
                
                for i in sinr:
                    nrept= list(rent).count (i)-1
                    for j in range(nrept):
                        for k in range(len(rlist)):
                            if rlist[k].find(str(i)+"^n")!=-1:
                                if (k in ndone):
                                    continue
                                break
                        rlist[k]="n"+rlist[k]
                        ndone.append(k)
                rfinal="+".join(rlist)

                fig = plt.figure(figsize=[2.1*nconst, 1], dpi=400)
                fig.text(0.5, 0.5, "F(n) = "+rfinal, horizontalalignment='center',
                    verticalalignment='center', fontsize='xx-large', wrap=True)
                fig.savefig("src/rrlhcc.png")
                plt.close()
                err=""
                return(err)
        else:
            err="Error: No existe una solución"
            return (err)
    
    #METODO PARA EL CASO BASE
    def play_CBASE(RR,CI,i0):
        n=sy('n')
        R=np.roots(RR)
        k=len(CI)
        MR=np.zeros((k,k))
        print("R: \n", R)

        for cont in range(0,k):
            MR[cont,]=(R**(i0+cont))
        print("MR: \n",MR)
        b=np.linalg.solve(MR,CI)
        print("b: \n",b)
        b1=[np.round(i,2) for i in b ]
        print(b1)
        print(R)
        sol=simplify(np.dot(b1, R**n))
        new = ((str(sol).replace("**","^")))
        fn = f"fn = {new}"
        fig = plt.figure(figsize=[((len(fn) / 2) * 0.15), 1], dpi=400)
        fig.text(0.5, 0.5, str(fn), horizontalalignment='center',
                verticalalignment='center', fontsize='xx-large', wrap=True)
        plt.savefig("src/cbase.png")
        plt.clf()
        plt.close()
        return fn 


    #METODO PARA CREAR GRAFO
    def play_graph(vert, ars, grad):
        nd = nx.Graph()
        aux = []

        for i in range (vert):
            nd.add_node(i)
            aux.append([i, 0])

        con=0
        while (con < ars):
            vin = rd.randint(vert)
            vfin = rd.randint(vert)
            
            if ( aux[vin][0] != aux[vfin][0] and aux[vin][1] < grad and aux[vfin][1] < grad):
                if (([aux[vin][0], aux[vfin][0]]) not in nd.edges()) or (([aux[vfin][0], aux[vin][0]]) not in nd.edges()):
                    nd.add_edge(aux[vin][0], aux[vfin][0])
                    aux[vin][1]=(aux[vin][1])+1
                    aux[vfin][1]=(aux[vfin][1])+1
                    con=con+1
        print("aristas: ",nd.edges())
        print(aux)
        opt= {
            'node_color' : 'black',
            'node_size' : 450,
            'width' : 3
        }
        nx.draw(nd, **opt)
        plt.savefig("src/nodo.png")
        plt.clf()
        plt.close()

    #METODO DE MARKOV Y WEB SCRAPPING 
    def play_markv(lnk):
        r = requests.get(lnk)
        htmldata = r.text
        
        soup = BeautifulSoup(htmldata, 'html.parser')
        data =''; txt=''
        for data in soup.find_all('p'):
            txt=txt+(data.get_text())
        text = txt.split()
        
        pairs = m_pairs(text)
        
        word_dic = {}
        
        for w1, w2 in pairs:
            if w1 in word_dic.keys():
                word_dic[w1].append(w2)
            else:
                word_dic[w1]=[w2]
        fword=np.random.choice(text)
        while fword.islower():
            fword=np.random.choice(text)
        
        chain= [fword]
        for i in range(len(text)): 
            chain.append(np.random.choice(word_dic[chain[-1]]))

        nchain = ' '.join(chain[0:40])        
        new='';con=0
        for i in range(len(text)):
            con+=1
            new=new+' '+chain[i]
            if con ==30:
                con=0
                new=new+'\n'
        f = open("src/gtext.txt",'w')
        f.write(new)
        f.close()
        return nchain

def m_pairs(text):
    for i in range(len(text)-1):
        yield (text[i], text[i+1])
    
    
