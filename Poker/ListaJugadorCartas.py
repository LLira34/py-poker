from Baraja import Baraja
from Jugador_Cartas import Jugador_Cartas
from Jugador import Jugador

class ListaJugadorCartas(Baraja,Jugador_Cartas):
    
    def __init__(self):
        self.listajugadores=[]

        Baraja.__init__(self)
        self.mezclar()
        self.listageneral=[]

    def CrearJugadores(self,NumeroJugadores):
        for x in range(NumeroJugadores):
            self.listajugadores.append(Jugador("Jugador: "+str(x+1)))
            minilista=[]    
            for i in range(5):
                minilista.append(self.RepartirCarta())
                minilista=self.ordenarcartas(minilista)
            self.listajugadores[x].lista=minilista
            self.listageneral.append(minilista)
        return self.listageneral
        
    def Ganador(self):
        niveles=[]
        listaempat=[]
        prob=[]
        jugada=[]
        nombre=[]
        nivel=[]
        wa=0
        WA2=0
        for i in self.listajugadores:
            i.jugada,i.nivel,i.prob,i.diccn=self.tipojugadas(i.lista)
        for i in self.listajugadores:
                                                                 #Probabilidad de todos los jugadores
            print(str(i.nombre)+" "+" "+str(i.nivel)+" "+str(i.jugada) + " " + str(i.prob))
            prob.append(i.prob)
            
           
            jugada.append(i.jugada)
            nombre.append(i.nombre)
            nivel.append(i.nivel)
            WA2 = WA2 + 1
            print("Jugador " + str(WA2) +"  " +  str(prob[wa]))
            wa =wa + 1

            # probabilidad
            #print("La probabilidad es: " + str(i.prob))
        print("")
        n=len(self.listajugadores)
        j=0
        i=0
        for i in range(0,n):    
            for j in range(0,n-1):
                if(self.listajugadores[j].nivel < self.listajugadores[j+1].nivel):
                    h=self.listajugadores[j]
                    k=self.listajugadores[j+1]
                    self.listajugadores[j]=k
                    self.listajugadores[j+1]=h

        for i in self.listajugadores:
            print(str(i.nombre)+" "+" "+str(i.nivel)+" "+str(i.jugada))
            print("Mi probabilidad es: " + str(i.prob))

        listplayers=[]
        for k in self.listajugadores:
            #print("list player goes here")
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            listplayers.append(k)

        num=0
        prob1=0
        porcentaje =100
        print('XXXXXXXXXXXXXXXXXXXXXXX el cardona es joto')
        

        for l in listplayers:
            if(num==0):  #Ignora el primer elemento de la lista
                num=num+1
                porcentaje = (porcentaje - (l.prob*100))
                print("Porcentaje principal " + str(porcentaje))
                prob1=round((1-l.prob)*100)
                print(prob1)
            elif (num==1):
                num=num+1
                prob1=round((porcentaje*((l.prob)*100))/100)
                porcentaje = (porcentaje - prob1)
                print("mi otro porcentaje 1: " + str(porcentaje))
                print(prob1)
            elif(num==2):
                num=num+1
                prob1=round((porcentaje*((l.prob)*100))/100)
                porcentaje = (porcentaje - prob1)
                print("mi otro porcentaje 2 " + str(porcentaje))
                print(prob1)
            else:
                #num=num+1
                #prob1=(prob1*(l.prob)*100)/100
                #porcentaje = porcentaje - prob1
                print("mi otro porcentaje " + str(porcentaje))
                print(prob1)

        print(str(listplayers[0].nombre))
        print(str(listplayers[0].nivel))
        print(str(listplayers[0].jugada))
        print(str(listplayers[0].prob))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(str(listplayers[1].nombre))
        print(str(listplayers[1].nivel))
        print(str(listplayers[1].jugada))
        print(str(listplayers[1].prob))

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(str(listplayers[3].nombre))
        print(str(listplayers[3].nivel))
        print(str(listplayers[3].jugada))
        print(str(listplayers[3].prob))

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(str(listplayers[2].nombre))
        print(str(listplayers[2].nivel))
        print(str(listplayers[2].jugada))
        print(str(listplayers[2].prob))

        va=self.listajugadores[0].nivel
        listaultimos=[]

        for i in self.listajugadores:
            if i.nivel==va:
                listaultimos.append(i)
        print("")
        for i in listaultimos:
            print("Jugador= " + str(i.nombre)+" "+"Nivel: "+str(i.nivel)+" "+ "Jugada: " +str(i.jugada))
            #print("Mi probabilidad es: " + str(i.prob))
        if va==1:
            print("NO hubo ninguna jugada")
            listaultimos=self.cartaalta(self.listajugadores)
        elif len(listaultimos)>1:
            listaultimos=self.empates(va,listaultimos)
            #print(listaultimos[0].nombre)
        return listaultimos


    # Metodo para regresar lista de probabilidades
    def all(self):
        niveles=[]
        listaempat=[]
        prob=[]
        jugada=[]
        nombre=[]
        nivel=[]
        wa=0
        WA2=0
        for i in self.listajugadores:
            i.jugada,i.nivel,i.prob,i.diccn=self.tipojugadas(i.lista)
        for i in self.listajugadores:
            #Probabilidad de todos los jugadores
            print(str(i.nombre)+" "+" "+str(i.nivel)+" "+str(i.jugada) + " " + str(i.prob))
            prob.append(i.prob)
            
            jugada.append(i.jugada)
            nombre.append(i.nombre)
            nivel.append(i.nivel)
            WA2 = WA2 + 1
            print("Jugador " + str(WA2) +"  " +  str(prob[wa]))
            wa =wa + 1

            # probabilidad
            #print("La probabilidad es: " + str(i.prob))
        print("")
        n=len(self.listajugadores)
        j=0
        i=0
        for i in range(0,n):    
            for j in range(0,n-1):
                if(self.listajugadores[j].nivel < self.listajugadores[j+1].nivel):
                    h=self.listajugadores[j]
                    k=self.listajugadores[j+1]
                    self.listajugadores[j]=k
                    self.listajugadores[j+1]=h

        listplayers=[]
        for i in self.listajugadores:
            print(str(i.nombre)+" "+" "+str(i.nivel)+" "+str(i.jugada))
            print("Mi probabilidad es: " + str(i.prob))

     #   for k in self.listajugadores:
      #      print("list player goes here")
       #     listplayers[k]=str(k.nombre)
       # print(listplayers)
       # listplayers=[]

        for k in self.listajugadores:
            #print("list player goes here")
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            listplayers.append(k)

        num=0
        prob1=0
        porcentaje =100
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx')
        
        listaProbs=[]
        for l in listplayers:
            if(num==0):  #Ignora el primer elemento de la lista
                num=num+1
                listaProbs.append([l.nombre,l.prob*100])
                #listaProbs.append(l.prob*100)
                #listaProbs={'nom':[l.nombre], 'prob':[(l.prob*100)]}
                print(listaProbs)    
                porcentaje = (porcentaje - (l.prob*100))
                #print("Porcentaje principal " + str(porcentaje))
                prob1=round((1-l.prob)*100)

                #print(prob1)
            elif (num==1):
                num=num+1
                prob1=round((porcentaje*((l.prob)*100))/100)
                #listaProbs={'nom':[l.nombre], 'prob':[prob1]}
                porcentaje = (porcentaje - prob1)
                listaProbs.append([l.nombre,prob1])
               
                print(listaProbs)    

                #print("mi otro porcentaje 1: " + str(porcentaje))
                #print(prob1)
            elif(num==2):
                num=num+1
                prob1=round((porcentaje*((l.prob)*100))/100)
                #listaProbs={'nom':[l.nombre], 'prob':[prob1]}
                porcentaje = (porcentaje - prob1)
                if (prob1 < porcentaje):       
                    listaProbs.append([l.nombre,porcentaje])
                else:
                    listaProbs.append([l.nombre,prob1])

                print(listaProbs)    

                #print("mi otro porcentaje 2 " + str(porcentaje))
                #print(prob1)
            else:
                #num=num+1
                #prob1=(prob1*(l.prob)*100)/100
                #porcentaje = porcentaje - prob1
                #listaProbs={'nom':[l.nombre], 'prob':[prob1]}
                listaProbs.append([l.nombre,prob1])
                print(listaProbs)    

                #print("mi otro porcentaje " + str(porcentaje))
                #print(prob1)
      
        print('*******************************************')
        print(str(listaProbs[0][0]))
        print listaProbs[0][1]

        print(str(listaProbs[1][0]))
        print listaProbs[1][1]

        print(str(listaProbs[2][0]))
        print listaProbs[2][1]

        print(str(listaProbs[3][0]))
        print listaProbs[3][1]
        print('*******************************************')
        #Retorna lista de las probabilidades ordenada del mayor almenor
        return listaProbs

