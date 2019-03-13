'''
Created on Jan 22, 2018

@author: PATI
'''

class Jucator(object):
    '''
    Clasa jucator retine pt un jucator un nume un prenume o inaltime si un post
    '''


    def __init__(self, nume,prenume,inaltime,post):
        '''
        initializam campul nume prenume inaltime si post cu valorile corespunzatoare
        '''
        self.__nume=nume
        self.__prenume=prenume
        self.__inaltime=inaltime
        self.__post=post
        
    """
    Functia returneaza nume
    """
    def get_nume(self):
        return self.__nume

    """
    Functia returneaza prenumele
    """
    def get_prenume(self):
        return self.__prenume

    """
    Functia returneaza inaltimea
    """
    def get_inaltime(self):
        return self.__inaltime

    """
    Functia returneaza postul
    """
    def get_post(self):
        return self.__post

    """
    Functia returneaza inaltimea
    """
    def set_inaltime(self, value):
        self.__inaltime = value

    """
    Functia returneaza daca doi jucatori sunt egali
    """
    def __eq__(self,other):
        return isinstance(self, other.__class__) and self.get_nume()==other.get_nume() and self.get_prenume()==other.get_prenume()
    
    """
    Functia returneaza stringul corespunzator unui jucator
    """
    def __str__(self):
        return str(self.get_nume())+" "+str(self.get_prenume())+" "+str(self.get_inaltime())+" "+str(self.get_post())
