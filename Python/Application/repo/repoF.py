'''
Created on Jan 22, 2018

@author: PATI
'''
class ExceptionRF(Exception):
    """
    Clasa exceptii pentru repo
    """
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class RepoF():
    '''
    Repo pentru fisier
    '''


    def __init__(self,nume):
        '''
        Initializam campul nume cu numele fisierului
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
            ju=[str(inf[0]),str(inf[1])]
            rez.append(ju)
            line=f.readline().strip()
        f.close()
        return rez[:]
    
    """
    Functia returneaza toate elementele din fisier
    """
    def getAll(self):
        alls=self.__loadFromFile()
        return alls[:]