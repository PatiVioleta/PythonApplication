'''
Created on Jan 22, 2018

@author: PATI
'''
from domain.jucator import Jucator

class ExceptionR(Exception):
    """
    Clasa de exceptii pentru repo
    """
    
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class RepoJ():
    '''
    repo pentru jucatori
    '''


    def __init__(self, nume):
        '''
        initializam campul nume cu numele jucatorului
        '''
        self.__nume=nume
        
    """
    Functia care citeste din fisier
    """
    def __loadFromFile(self):
        try:
            f=open(self.__nume,"r")
        except IOError:
            rez=[]
            
        line=f.readline().strip()
        rez=[]
        while line!="":
            inf=line.split(";")
            ju=Jucator(str(inf[0]),str(inf[1]),int(inf[2]),str(inf[3]))
            rez.append(ju)
            line=f.readline().strip()
        f.close()
        return rez[:]
    
    """
    Functia care scrie in fisier
    """
    def __storeToFile(self,lista):
        f=open(self.__nume,"w")
        for x in lista:
            ju=str(x.get_nume())+";"+str(x.get_prenume())+";"+str(x.get_inaltime())+";"+str(x.get_post())+"\n"
            f.write(ju)
        f.close()
        
    """
    Functia returneaza toate elementele din fisier
    """
    def getAll(self):
        alls=self.__loadFromFile()
        return alls[:]
        
    """
    Adauga un jucator in fisier
    Date intrare: ju-jucator
    """
    def add(self,ju):
        alls=self.__loadFromFile()
        for x in alls:
            if x==ju:
                raise ExceptionR("Un jucator cu acest nume exista deja!!!")
        alls.append(ju)
        self.__storeToFile(alls)
        
    """
    Adauga un jucator in fisier fara a arunca exceptii
    Date intrare: ju-jucator
    """
    def add2(self,ju):
        alls=self.__loadFromFile()
        ok=1
        for x in alls:
            if x==ju:
                ok=0
        if ok==1:
            alls.append(ju)
        self.__storeToFile(alls)
        
    """
    Modifica ianltimea unui jucator din fisier
    Date intrare: nume-nume jucator, prenume-prenume jucator,inaltime-inaltimea
    """
    def mod(self,nume,prenume,inaltime):
        alls=self.__loadFromFile()
        ju=Jucator(nume,prenume,inaltime,"Fundas")
        for x in alls:
            if x==ju:
                x.set_inaltime(inaltime)
                self.__storeToFile(alls)
                return
        raise ExceptionR("Nu exista acest jucator!!!")
    
    """
    Returneaza lista cu toti fundasii
    """
    def cautaFundas(self):
        alls=self.__loadFromFile()
        rez=[]
        for x in alls:
            if x.get_post()=="Fundas":
                rez.append(x)
        return rez[:]
         
    """
    Returneaza lista cu toti pivotii
    """       
    def cautaPivot(self):
        alls=self.__loadFromFile()
        rez=[]
        for x in alls:
            if x.get_post()=="Pivot":
                rez.append(x)
        return rez[:]
    
    """
    Returneaza lista cu toate extremele
    """
    def cautaExtrema(self):
        alls=self.__loadFromFile()
        rez=[]
        for x in alls:
            if x.get_post()=="Extrema":
                rez.append(x)
        return rez[:]
    
    """
    Sorteaza o lista
    DAte intrare: lista -lista
    Date iesire: lista sortata
    """
    def sortare(self,lista):
        sorted=False
        while not sorted:
            sorted=True
            for i in range(1,len(lista)):
                if lista[i].get_inaltime()>lista[i-1].get_inaltime():
                    aux=lista[i]
                    lista[i]=lista[i-1]
                    lista[i-1]=aux
                    sorted=False
                    
    """
    Formeaza o echipa de jucatori
    Date iesire: lista de jucatori dintr-o echipa
    """
    def echipa(self):
        fundas=self.cautaFundas()
        pivot=self.cautaPivot()
        extrema=self.cautaExtrema()
        self.sortare(fundas)
        self.sortare(pivot)
        self.sortare(extrema)
        if len(pivot)<1:
            raise ExceptionR("Nu sunt suficienti pivoti!!!")
        if len(fundas)<2:
            raise ExceptionR("Nu sunt suficienti fundasi!!!")
        if len(extrema)<2:
            raise ExceptionR("Nu sunt suficienti jucatori cu postul de extrema!!!")
        rez=[]
        rez.append(fundas[0])
        rez.append(fundas[1])
        rez.append(pivot[0])
        rez.append(extrema[0])
        rez.append(extrema[1])
        return rez[:]