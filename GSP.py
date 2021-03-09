import re
import pandas as pd
from collections import defaultdict as de

def dell(d,na):
    for i in na:
        del d[i]
    return d #devuelvo el nuevo diccionario

def gsp_de(d,n):
    name=[]
    for k,v in d.items():
        if v<n: #revisar que aparezca en menos de dos conjuntos
            name.append(k)
    return dell(d,name) #si aparece en menos de dos conjuntos, los elimino

def gsp_cr(d):
    name=[]
    for k,v in d.items():
        name.append(k)
    name_new=[i+j[-1] for i in name for j in name if i[1:]==j[:-1]] #solo guardamos los conjuntos que cumplan con la igualdad de los valores medios
    return name_new

def gsp_crdi(name,dataset):
    r=de(int) #crear nuevo diccionario
    for i in name:
        b=''
        for j in range(len(i)-1):
            b+=i[j]+'.*'
        b+=i[-1] #creamos pares, tríos, cuartetos, etc.
        for i in dataset['elementos'].values:
            i_new=i.replace(',','')
            res=re.search(b,i_new) #buscamos en cada conjunto los pares o trios generados
            if not(res==None):
                r[b.replace('.*','')]+=1 #contamos las frecuencias de aparicion en el diccionario
    return r

with open('C:\\Users\\Janie\\Documents\\Arlette\\Minería de Datos\\gsp.csv')as archivo: #abrir archivo con la secuencia
    dataset=pd.read_csv(archivo)
    r_1=[]
    r_1_di=de(int) #crear un diccionario
    for i in dataset['elementos'].values:
        for j in set(i.split(',')):
            r_1_di[j[0]]+=1 #contar en cuantos conjuntos esta el elemento
    di=gsp_de(r_1_di,2)
    print('L1:\n',di) #primera secuencia candidata
    name=[]
    for k,v in di.items():
        name.append(k)
    name_new=[i+j for i in name for j in name]#crear parejas de datos
    r_di=gsp_crdi(name_new,dataset)
    di_3=gsp_de(r_di,2) #elimino los elementos con frecuencia menor a 2
    nuu=1
    while(len(di_3)!=0): #realizo los ciclos necesarios hasta llegar al resultado
        print('L'+str(nuu+1)+':')
        print(di_3)
        name_n=gsp_cr(di_3)
        r_di=gsp_crdi(name_n,dataset)
        di_3=gsp_de(r_di,2)
        nuu+=1
