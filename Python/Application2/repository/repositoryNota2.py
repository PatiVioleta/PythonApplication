'''
Created on Dec 7, 2017

@author: PATI
'''
from repository.repositoryNota import inMemoryRepositoryN
from domain.nota import Nota

class RepositoryExceptionN2(Exception):
    """
    Clasa de erori pentru lista de discipline
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class notaFileRepository(inMemoryRepositoryN):
    """
    Clasa lista de note gestionata din fisier
    Contine o lista de obiecte de tip nota
    """

    def __init__(self):
        '''
        Initializam clasa mostenita
        '''
        inMemoryRepositoryN.__init__(self)

    """
    Extragem informatiile din fisier
    """
    def __loadFromFile(self):
        try:
            f=open("nota.txt","r")
        except IOError:
            rez=[]
        
        line=f.readline().strip()
        rez=[]
        while line!="":
            inf=line.split(";")
            
            note=inf[2:]
            
            n=[]
            
            for i in note:
                try:
                    n.append(int(i))

                except ValueError:
                    continue
            
            el= Nota(int(inf[0]),int(inf[1]),n[0])
            rez.append(el)
            line=f.readline().strip()
        f.close()
        
        return rez
    
    """
    Punem informatiile din listaD in fisier
    Date intrare: listaD-lista de discipline
    """
    def __storeToFile(self,listaN):
        f=open("nota.txt","w")
        
        for i in listaN:
            el=str(i.getIdstud())+";"+str(i.getIddis())+";"
            for j in i.getNote():
                
                el=el+str(j)
            el=el+"\n"
            f.write(el)
        f.close()
    
    
    """
    Adauga la lista de note o noua nota daca studentul curent mai are cel putin o nota la materia curenta si creeaza o noua instanta nota in caz contar
    Date de intrare: elem- noua nota asociata unui student si unei discipline
    """
    def add(self,elem):
        
        inMemoryRepositoryN.add(self,elem)
        
        self.__elems=self.__loadFromFile()
        """
        for el in self.__elems:
            if elem.eqSD(el):
                el.addNota(elem.getNote())
                return 
        """
        self.__elems.append(elem)
        
        self.__storeToFile(self.__elems)
        
        
    """
    Sterge din lista de note notele asociate unui anumit student
    Date intrare: elem-Studentul
    """
    def remS(self,elem):
        inMemoryRepositoryN.remS(self,elem)
        self.__elems=self.__loadFromFile()
        
        for el in self.__elems:    
            if elem.eqS(el):
                self.__elems.remove(el)       
    
        
        self.__storeToFile(self.__elems)
      
    """
    Sterge din lista de note notele asociate unui anumit student
    Date intrare: elem-Studentul
    """
    def remD(self,elem):
        inMemoryRepositoryN.remD(self,elem)
        self.__elems=self.__loadFromFile()
        
        for el in self.__elems:    
            if elem.eqD(el):
                self.__elems.remove(el)       
    
        
        self.__storeToFile(self.__elems)
        
        
    """
    Returneaza lista de obiecte Nota care au id-ul disciplinei egal cu id-ul disciplinei Notei elem
    Date intrare: elem- nota care are id-ul de disciplina in functie de care etragem elemente din lista de note
    """
    def getIddis(self,elem):
        #inMemoryRepositoryN.getIddis(self,elem)
        self.__elems=self.__loadFromFile()
        lis=[]
        for el in self.__elems:
            
            if el.eqD(elem): 
                                   
                ind=self.__elems.index(el)
                lis.append(self.__elems[ind])
        
        if len(lis)!=0:
            return lis[:]
        else:
            raise RepositoryExceptionN2("Nota inexistenta!")  
        
        self.__storeToFile(self.__elems)
        
    """
    Returneaza lungimea listei de note
    """
    def size(self):
        inMemoryRepositoryN.size(self)
        self.__elems=self.__loadFromFile()
        return len(self.__elems)
        
    """
    Returneaza toata lista de note
    """
    def getAll(self):
        #inMemoryRepositoryN.getAll(self)
        self.__elems=self.__loadFromFile()
        return self.__elems[:]