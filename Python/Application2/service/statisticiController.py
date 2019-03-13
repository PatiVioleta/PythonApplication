
from validari.validari import Validator
from repository.repositoryNota import RepositoryExceptionN

class StatisticiController:
    """
    Permite efectuarea unor statistici legate de studenti, note si discipline
    """
    def __init__(self,repo,repoD,repoN,ctrl,ctrlD,ctrlN):
        self.__repo=repo
        self.__repoD=repoD
        self.__repoN=repoN
        self.__ctrl = ctrl
        self.__ctrlD= ctrlD
        self.__ctrlN= ctrlN
    
    """
    Returneaza lista de note asignate unei discipline cu un id cerut
    Date intrare: idD- id-ul disciplinei
    """
    def cautaNoteIddis(self,idD):             
        lis=self.__ctrlN.cautaNoteIddis(idD)    #lis= lista de discipline care au acelasi profesor
        return lis
    
    """
    Returneaza lista de note de la disciplina cu numele dat
    Date intrare: numeD- numele disciplinei cu semnificatia de mai sus
    """
    def listaNoteIddis(self,numeD):
        
        listaD=self.__ctrlD.cautaDisciplinaNume(numeD)         #lista de discipline cu numele dorit
        
        lis=[]
        for i in listaD:                                       #luam pe rand fiecare disciplina cu numele dorit si cautam notele asignate ei
            try:
                idD=i.getIddis()                               #id-ul unei discipline cu numele dorit
                
                lis=lis+self.cautaNoteIddis(idD)               #adaugam in lista obiectele de tip Nota care au id-ul disciplinei de mai sus
                
            except RepositoryExceptionN:
                continue
        
        return lis
    
    """
    Afiseaza in mod natural elementele unei liste de obiecte Nota (nume student + nume disciplina + nume profesor + note)
    Date intrare: lis- lista de obiecte Nota
    """
    def printNotaL(self,lis):
        
        for x in lis:
                idStud=x.getIdstud()
                idDis=x.getIddis()
                nota=x.getNote()
                nume=self.__ctrl.cautaStudentId(idStud).getNume()
                disciplina=self.__ctrlD.cautaDisciplinaId(idDis).getNume()
                profesor=self.__ctrlD.cautaDisciplinaId(idDis).getProfesor()
                print("Studentul "+nume+" la disciplina "+disciplina+" predata de "+profesor+ " are nota/notele "+str(nota))
                
    """
    Afiseaza in mod natural elementele unei liste de obiecte Nota (nume student + nume disciplina + nume profesor + medie)
    Date intrare: lis- lista de obiecte Nota
    """
    def printNotaL2(self,lis):
        for x in lis:
                idStud=x.getIdstud()
                idDis=x.getIddis()
                nota=x.getNote()
                medie=self.medie(nota)
                nume=self.__ctrl.cautaStudentId(idStud).getNume()
                disciplina=self.__ctrlD.cautaDisciplinaId(idDis).getNume()
                profesor=self.__ctrlD.cautaDisciplinaId(idDis).getProfesor()
                print("Studentul "+nume+" la disciplina "+disciplina+" predata de "+profesor+ " are media "+str(medie))
                
    """
    #
    #
    #
    #
    #
    """
    """
    Functie recursiva pentru afisarea studentilor descrescator dupa mediea la o disciplina data
    Date intrare: lis- lista de studenti ce trebuie sa fie afisati, i- pozitia de pe care incepem afisarea
    -functie apelata in console (_uiOrdonareNumericDescrescator)
    """
    def printNotaL2Recursiv(self,lis,i):
        if i>=len(lis):
            return 0
        idStud=lis[i].getIdstud()
        idDis=lis[i].getIddis()
        nota=lis[i].getNote()
        medie=self.medie(nota)
        nume=self.__ctrl.cautaStudentId(idStud).getNume()
        disciplina=self.__ctrlD.cautaDisciplinaId(idDis).getNume()
        profesor=self.__ctrlD.cautaDisciplinaId(idDis).getProfesor()
        print("Studentul "+nume+" la disciplina "+disciplina+" predata de "+profesor+ " are media "+str(medie))
        return self.printNotaL2Recursiv(lis, i+1)
    
    """
    Returneaza o lista de obiecte nota ordonata alfabetic (dupa numele studentilor ) care sunt asignate unei discipline cu un nume dat
    Date intrare: numeD- numele disciplinei cu semnificatia de mai sus
    """
    def ordonareAlfabetic(self,numeD):
        lis=self.listaNoteIddis(numeD)                               #lista de note de la disciplinele cu numele numeD
        
        for i in range (0,len(lis)-1):
            for j in range (i+1,len(lis)):
                idStud1=lis[i].getIdstud()
                idStud2=lis[j].getIdstud()
                nume1=self.__ctrl.cautaStudentId(idStud1).getNume()
                nume2=self.__ctrl.cautaStudentId(idStud2).getNume()
                if(nume1>nume2):
                    aux=lis[i]
                    lis[i]=lis[j]
                    lis[j]=aux    
        return lis
    
    """
    Functie de sortare care foloseste metoda shellSort
    Date intrare: numeD- numele disciplinei pentru care trebuie ordonati studentii
    -apelata in console(_uiOrdonareAlfabetic)
    """
    def shellSort(self,numeD,key=lambda x:x , cmp=lambda x,y:x>y,reverse=False):
        alist=self.listaNoteIddis(numeD)                        #lista de obiecte
        sublistcount = len(alist)//2                            #pozitia pana la care putem considera subliste incepand de pe fiecare pozitie pana la final
        while sublistcount > 0:
            for startposition in range(sublistcount):           #startpoz de la 0 la sublistcount
                self.gapInsertionSort(alist,startposition,sublistcount,key,cmp,reverse)    #apelam functia de inserare
            sublistcount = sublistcount // 2                    #sublistcount se imparte iar la 2
            
        if reverse==True:
            alist.reverse()
            
        return alist

    """
    Functie ce face parte din shellSort, sorteaza o sublista generata de pozitiile multiplii de nr gap
    Date intrare: alist- lista completa, start- poztia de pe care consideram inceperea sublistei, gap- numarul care desemneaza pasul conform caruia alegem elementle pentru sortare
    """
    def gapInsertionSort(self,alist,start,gap,key,cmp,reverse):  #inseram fiecare element din sublista pe pozitia in care trebuie sa fie in sublista sortata
        for i in range(start+gap,len(alist),gap):                #de pe poz de start+gap pana la final din gap in gap pozitii
            currentvalue=alist[i]                                #pastram vaoarea curenta 
            position = i                                         #pozitia curenta
            while position>=gap and  cmp(key(alist[position-gap]) , key(alist[i])):    #comparam val curenta cu cele anterioare din sublista
                alist[position]=alist[position-gap]              #pozitia curenta din while primeste valoarea de pe pozitia anterioara din sublista
                position = position-gap                          #trecem la pozitia anterioara din sublista
            alist[position]=currentvalue                         #inseram pe prima pozitie din sublista
    
    """
    Sorteaza o lista crescator folosint metode bubbleSort
    -apelat in _uiOrdonareNumeric
    """
    def bubbleSort(self,numeD,key=lambda x:x , cmp=lambda x,y:x>y,reverse=False):
        l=self.listaNoteIddis(numeD)
        ok = True
        nr = len(l)-1
        while nr > 0 and ok:
            ok = False
            for i in range(nr):
            
                if cmp(key(l[i]),key(l[i+1])) :
                    ok = True
                    aux = l[i]
                    l[i] = l[i+1]
                    l[i+1] = aux
            nr = nr-1
        if reverse==True:
            l.reverse()
        return l
     
    """
    C
    C
    C
    C
    C
    """
    """
    Primeste o lista care contine mai multe note si returneaza media acestora
    Date intrare: lis- lista de note
    
    Complexitate:  O(n) teta(n) omega(n)
    """
    def medie(self,lis):
        medie=0
        k=0
        for i in lis:
            medie=medie+i
            k=k+1
        return medie/k
    
    """
    #
    #
    #
    #
    #
    """
    """
    Functia recursiva care calculeaza media numerelor dintr-o lista
    Date intrare: lis- lista de numere, i-pozitia de la care incepem calculul, suma- suma numerelor
    Date de iesire: media numerelor din lista
    -apelata in ordonareNumeric
    
    Complexitate:  O(n) teta(n) omega(n)
    """
    def medieRecursiv(self,lis,i,suma):
        if len(lis)==0:
            return 0
        if i==len(lis)-1:
            return (suma+lis[i])/len(lis)
        return self.medieRecursiv(lis, i+1, suma)+lis[i]
    
    """
    Returneaza o lista de obiecte nota (ordonata dupa medie) care sunt asignate unei discipline cu un nume dat
    Date intrare: numeD- numele disciplinei cu semnificatia de mai sus
    """
    def ordonareNumeric(self,numeD):
        lis=self.listaNoteIddis(numeD)                               #lista de note de la disciplinele cu numele numeD
                
        for i in range (0,len(lis)-1):
            for j in range (i+1,len(lis)):
                lNote1=lis[i].getNote()
                lNote2=lis[j].getNote()
                #medie1=self.medie(lNote1)
                medie1=self.medieRecursiv(lNote1, 0, 0)              #apelam functia recursiva
                #medie2=self.medie(lNote2)
                medie2=self.medieRecursiv(lNote2, 0, 0)              #apelam functia recursiva
                if(medie1>medie2):
                    aux=lis[i]
                    lis[i]=lis[j]
                    lis[j]=aux
        return lis
    
    """
    Returneaza o lista de obiecte nota (ordonata dupa medie) care sunt asignate unei discipline cu un nume dat
    Date intrare: numeD- numele disciplinei cu semnificatia de mai sus
    """
    def ordonareNumericDescrescator(self,numeD):
        lis=self.listaNoteIddis(numeD)                               #lista de note de la disciplinele cu numele numeD
                
        for i in range (0,len(lis)-1):
            for j in range (i+1,len(lis)):
                lNote1=lis[i].getNote()
                lNote2=lis[j].getNote()
                medie1=self.medie(lNote1)
                medie2=self.medie(lNote2)
                if(medie1<medie2):
                    aux=lis[i]
                    lis[i]=lis[j]
                    lis[j]=aux
        return lis
    
    """
    Returneaza o lista formata din elemente care contin un nume de student si media lor finala (media de la toate disciplinele)
    """
    def creeazaListaStudentiMedie(self):
        listaN=self.__ctrlN.getAllNote()               #lista tuturor obiectelor de tip Nota
        listaS=self.__ctrl.getAllStudenti()            #lista tuturor obiectelor de tip Student
        final=[]
        
        for i in listaS:                               #luam pe rand fiecare student
            idStud=i.getIdstud()
            nume=self.__ctrl.cautaStudentId(idStud).getNume()    #ii retinem numele 
            medie=0
            k=0
            for j in listaN:                           #parcurgem lista de note
                idi=j.getIdstud()
                if idStud==idi:                        #daca gasim note asignate studentului curent, facem media lor si o adaugam la media finala
                    lis=j.getNote()
                    med=self.medie(lis)
                    medie=medie+med
                    k=k+1
            if k!=0:
                d=[nume,medie/k]
                final.append(d)
            else:
                pass
        return final
            
        
    
    """
    Primeste o lista cu elemente care contin un nume de student si o medie finala si returneaza lista ordonata descrescator dupa media finala
    Date intrare: lis- lista cu specificatia de mai sus
    """
    def ordonareMedie(self,lis):
        for i in range (0,len(lis)-1):
            for j in range(i+1,len(lis)):
                
                medie1=lis[i][1]
                medie2=lis[j][1]
                if( medie1 < medie2 ):
                    aux=lis[i]
                    lis[i]=lis[j]
                    lis[j]=aux
        return lis
    
    """
    Afiseaza o lista cu elemente care contin un nume de student si o medie finala in mod natural
    """
    def printLista(self,lis,nr):
        for i in range(0,nr):
            print ("Studentul "+lis[i][0]+" are media finala: "+str(lis[i][1]))
            
    """
    #
    #
    #
    #
    #
    """
    """
    Functia recursiva care afiseaza primi nr (20%) studenti 
    Date intrare: lis- lista de studenti sortata, i-pozitia de pe care incepem afisarea, nr- nr de studenti ce trebuie afisat
    -functie apelata in console (_uiPrimi)
    """
    def printListaRecursiv(self,lis,i,nr):
        if i>=len(lis):
            return 0
        if i>=nr:
            return 0
        print("Studentul "+lis[i][0]+" are media finala: "+str(lis[i][1]))
        return self.printListaRecursiv(lis, i+1, nr)
        
            
    """
    Returneaza lista cu toti studentii sortati descrescator dupa media finala
    """
    def primi(self):
        final=self.creeazaListaStudentiMedie()        #creeaza o lista care contine toti studentii si mediile lor finale
        final=self.ordonareMedie(final)               #ordoneaza dupa medie toti studentii
        return final
    