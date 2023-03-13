import numpy as np
import random as rd
import matplotlib.pyplot as plt
import copy
from matrice import M
from matrice import H
class IsingModel:
    def __init__(self, n, pas, iteration,M,H,nbrsimulation):
        #n nombre de particule
        #M matrice des forces d'interactio,
        self.n = n
        self.pas = pas
        self.iteration = iteration
        self.M =M
        self.H=H
        self.nbrsimulation=nbrsimulation

    def calcule_energie(self, t):
        t1 = self.signage(t)
        return np.dot(t1, np.dot(self.M, t1))
    
    def force(self, t, i):
        def sign(x):
            criteremin=1 #on pourra changer
            if abs(x)<criteremin:
                return x/criteremin
            else:
                return int(x>0)-int(x<0)
        
        f = -sum([self.M[i,j]*sign(t[j] )for j in range(self.n)]+[self.H[i]*sign(t[i])])
        return f
    
    def nouvelle_variable(self, t, vitesse):
        # c'est pour calculer la nouvelle position de la particule
        t1 = copy.deepcopy(t)
        v = copy.deepcopy(vitesse)
        for i in range(self.n):
            v[i] = v[i] + self.pas * self.force(t, i)
            t1[i] = t1[i] + self.pas * v[i]
        return t1, v

    def signage(self, t):
        # donne le signe de chaque particule
        return [1 if t[i]>0 else -1 for i in range(self.n)]

        
    def simulate(self):
        
        
        for i in range(self.nbrsimulation):
            position=[rd.randint(0,1)*2-1 for i in range(self.n)]
            vitesse=[0]*self.n
            posparhistorique=[[k] for k in position]
            E=[]    
            for a in range(self.iteration):
                E.append(self.calcule_energie(self.signage(position)))
                position, vitesse = self.nouvelle_variable(position, vitesse)
                for j in range(len(posparhistorique)):
                    posparhistorique[j].append(position[j])
            
            Y=[i for i in range(len(E))]
            plt.plot(Y, E)
            print(self.signage(position))
            
        plt.show()

        
# Utilisation de la classe IsingModel
print("je commence")
n = 10

pas = 0.001

iteration = 10000

nbrsimulation=15
H=np.zeros(n)
I=np.eye((n))
M=np.zeros((n,n))
for i in range(n):
            for j in range(i+1):
                c = rd.randint(0,9)
                M[i,j] = c
                M[j,i] = c
                
for i in range(n):
    H[i]=rd.randint(0,1)

ising_model = IsingModel(n, pas, iteration,M,H,nbrsimulation)
ising_model.simulate()
