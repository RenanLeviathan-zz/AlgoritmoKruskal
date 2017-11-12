'''
Created on 12 de nov de 2017

@author: Israël & Renan
'''
from plot import Plot
grafo=[
  ('0','2',5),
  ('0','3',8),
  ('1','2',16),
  ('1','4',30),
  ('1','6',26),
  ('2','3',10),
  ('2','4',3),
  ('3','4',2),
  ('3','5',18),
  ('4','5',12),
  ('4','6',14),
  ('5','6',4)
  ]
pos={
  '0':(50,100),
  '1':(200,50),
  '2':(100,50),
  '3':(100,150),
  '4':(150,100),
  '5':(200,150),
  '6':(250,100)
  }
def eAciclico(g):
  v=g[0][0]
  ini=v
  w=''
  for t in g:
    if w==t[1] or w==t[0]:
      v=w
      if v==ini:
        return False
  return True
      

#ordena as arestas em ordem decrescente
global H
grafo.sort(key=lambda a : a[2],reverse=True)
H=grafo
global T
T=[]
T.append(H[0])
global i
i=1
while len(T)<7:
  tmp=T+[H[i]]
  if eAciclico(tmp):
    T.append(H[i])
    i+=1
  tmp=[]
print(T)
g=Plot(T, pos)
g.plot("Arvore geradora mínima (Algoritmo de Kruskal)")