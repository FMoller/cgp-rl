import numpy as np
#nome="results/random-population/sam/cm85a_seed11.txt"
#pasta="results/random-population/sam/"
#pasta="results/feasible-population/sam/"
#pasta="results/biascomp/"
#pasta="results/resultados/"
#pasta="results/resultadoswire/"
#pasta="results/resultados3/"
#pasta="results/resultadosneq/"
#pasta="results/resultadosRLN/"
#pasta="results/resultadosRLNA/"
#pasta="results/resultadosRLNA2/"
#pasta="results/resultadosRLNAp5/"
#pasta="results/resultadosRLNA1p5/"
#pasta="results/resultadosRLNAp75/"
#pasta="results/resultadosRLNA3/"
#pasta="results/teste2/"
#pasta="results/resultadosRLNA60/"
#pasta="results/resultadosRLNAE60/"
#algoritmo="problem5"
pasta=''
algoritmo = "cmb"
seeds=[1,2,3,4,5,6,7,8,9,10,11,12,13]
seeds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
"Teste de dunn"


def retira(nome):
    f=open(nome,"r")
    contents = f.read()
    val=""
    tam = len(contents)-1
    for i in range(tam,0,-1):
        if contents[i]=='t':
            if contents[i:i+11]=='transistors':
                j=i+13
                while contents[j]!='\n':
                    val=val+contents[j]
                    j+=1
                return int(val)
            


def captura(pasta,algoritmo,seeds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]):
    vetor=[]
    endereco = pasta+algoritmo
    for i in seeds:
        #print(i)
        try:
            vetor.append(retira(endereco+"_"+str(i)))
        except:
            vetor.append(retira(endereco+"_seed"+str(i)+".txt"))
        
    return vetor


a=captura(pasta,algoritmo,seeds)
while None in a:
    a.remove(None)
print(np.min(a))
print(np.median(a))
#print(len(a)/25)
print(np.mean(a))
print("{:.2e}".format(np.std(a)))
print(np.max(a))
print(len(a)/25)
print(a)
    
