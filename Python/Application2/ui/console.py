from repository.repositoryStudent import RepositoryException
from repository.repositoryMaterie import RepositoryExceptionD
from repository.repositoryNota import RepositoryExceptionN
from repository.repositoryMaterie2 import RepositoryExceptionD2
from repository.repositoryStudent2 import RepositoryException2
from repository.repositoryNota2 import RepositoryExceptionN2
from validari.validari import Validator,ValidatorException

class ConsoleValidationException(Exception):
    """
    Clasa de erori pentru console
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Comanda:
    """
    Se ocupa de preloarea si executarea comenzilor introduse de utilizator
    """
    """
    Initializeaza un camp caruia ii atribuie numele comenzii dorite si unui pentru functia care e responsabila pentru acea comanda
    Date intrare: numeCmd- numele comenzii, functcmd- functia responsabila pentru comanda
    """
    def __init__(self,numeCmd,functCmd):
        self.__numeCmd= numeCmd
        self.__functCmd =functCmd
        
    """
    Apeleaza functia responsabila pentru comanda dorita
    Date intrare: params-lista de parametrii
    """
    def executa(self,params):
        self.__functCmd(params)


class Console:
    """
    Se ocupa de interactiunea cu utilizatorul
    """
    """
    Creeaza un obiect Consola
    Date intrare: ctrl- un obiect de tip studentController, ctrlD- un obiect de tip disciplinaController, ctrlN- un obiect de tipul notaController
    """
    def __init__(self,ctrl,ctrlD,ctrlN,ctrlS):
        self.__ctrl = ctrl
        self.__ctrlD= ctrlD
        self.__ctrlN= ctrlN
        self.__ctrlS= ctrlS

    """
    Citeste o comanda de la tastatura cu split
    """
    def __citesteComanda(self):
        return input(">>").split()

    """
    Adauga un student in lista de studenti interactionand cu utilizatorul
    Date intrare: params- lista de parametrii (id, nume)
    """
    def __uiAddStudent(self,params):
        if len(params)<2:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id si un nume")
        ident = int(params[0])
        nume= params[1]
        self.__ctrl.adaugaStudent(ident,nume)  #apeleaza functia din studentController care adauga un student in lista
        print("Student adaugat cu succes!")


    """
    Permite afisarea tuturor elevilor din lista de elevi interactionand cu utilizatorul
    Date intrare: params- lista vida, folosit pt ca in apelul comenzi[cmd[0]].executa(cmd[1:]) avem un parametru, care in acest caz nu ne trebuie
    """
    def __uiPrintStudent(self,params):
        alls =self.__ctrl.getAllStudenti()     #alls primeste toate elementele din lista de elevi
        if len(alls)==0:
            print("Lista de studenti este goala!")
        for x in alls:
            print(x)
            
    """
    Permite stergerea unui student din lista de studenti interactionand cu utilizatorul
    Date intrare: params- lista de parametrii (Id student)
    """
    def __uiStergeStudent(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id")
        ident = int(params[0])
        self.__ctrl.stergeStudent(ident)        #se apeleaza functia din studentController care sterge un student cu un anumit Id       
        print("Student sters cu succes!")
        self.__uiStergeNotaS(params)            #se apeleaza stergerea notelor asociate elevului care a fost sters
        
    """
    Permite modificarea unui student din lista de studenti interactionand cu utilizatorul
    Date intrare: params- lista de parametrii (Id-ul studentului care trebuie modificat si noul nume al acestuia)
    """
    def __uiModificaStudent(self,params):
        if len(params)<2:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id si un nume")
        ident=int(params[0])
        nume=params[1]
        self.__ctrl.updateStudent(ident,nume)   #se apeleaza functia din studentController care modifica un student cu un anumit Id
        print ("Student modificat cu succes!")
        
    """
    Permite cautarea unui student din lista de studenti care are un anumit Id interactionand cu utilizatorul
    Date intrare: params- lista de parametrii necesari cautarii (Id-ul)
    """
    def __uiCautaStudentId(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id")
        ident=int(params[0])
        st=self.__ctrl.cautaStudentId(ident)    #apelam cautarea unui student dupa Id
        print (st)
        return st                               #il returnam pt a-l folosi la afisarea naturala a listei de note
    
    """
    Permite cautarea studentilor din lista de studenti care au un anumit nume interactionand cu utilizatorul
    Date intrare: params- lista de parametrii necesari cautarii (numele)
    """
    def __uiCautaStudentNume(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un nume")
        nume=params[0]
        lis=self.__ctrl.cautaStudentNume(nume)  #lis= studentii care au acelasi nume
        for x in lis:
            print(x)
        
    """
    Adauga o disciplina in lista de discipline interactionand cu utilizatorul
    Date intrare: params- lista de parametrii (id, nume, profesor)
    """
    def __uiAddDisciplina(self,params):
        if len(params)<3:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id, un nume si un profesor")
        ident = int(params[0])
        nume= params[1]
        profesor= params[2]
        self.__ctrlD.adaugaDisciplina(ident,nume,profesor)  #apeleaza functia din materieController care adauga o disciplina in lista
        print ("Disciplina adaugata cu succes!")
        
    """
    Permite afisarea tuturor disciplinelor din lista de discipline interactionand cu utilizatorul
    Date intrare: params- lista vida, folosit pt ca in apelul comenzi[cmd[0]].executa(cmd[1:]) avem un parametru, care in acest caz nu ne trebuie
    """
    def __uiPrintDisciplina(self,params):
        alls =self.__ctrlD.getAllDiscipline()     #alls primeste toate elementele din lista de discipline
        if len(alls)==0:
            print("Lista de discipline este goala!")
        for x in alls:
            print(x)
            
    """
    Permite stergerea unei discipline din lista de discipline interactionand cu utilizatorul
    Date intrare: params- lista de parametrii (Id disciplina)
    """
    def __uiStergeDisciplina(self,params):
        
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id")
        ident = int(params[0])
        
        self.__ctrlD.stergeDisciplina(ident)        #se apeleaza functia din studentController care sterge o disciplina cu un anumit Id
        print ("Disciplina stearsa cu succes!")
        self.__uiStergeNotaD(params)                #se sterg toate notele primite de studenti la disciplina respectiva
    
        
    """
    Permite modificarea unei discipline din lista de discipline interactionand cu utilizatorul
    Date intrare: params- lista de parametrii (Id-ul disciplinei care trebuie modificata, noul nume al acesteia si noul profesor)
    """
    def __uiModificaDisciplina(self,params):
        if len(params)<3:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id, un nume si un profesor")
        ident=int(params[0])
        nume=params[1]
        profesor=params[2]
        self.__ctrlD.updateDisciplina(ident,nume,profesor)   #se apeleaza functia din materieController care modifica o disciplina cu un anumit Id
        print ("Disciplina modificata cu succes!")
        
    """
    Permite cautarea unei discipline cu un anumit Id interactinand cu utilizatorul
    Date intrare: params- lista de parametrii necesari cautarii (Id)
    """
    def __uiCautaDisciplinaId(self,params):    
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id")
        ident=int(params[0])
        dis=self.__ctrlD.cautaDisciplinaId(ident)            #dis= disciplina cautata
        print (dis)
        return dis
      
    """
    Permite cautarea disciplinelor cu un anumit nume interactinand cu utilizatorul
    Date intrare: params- lista de parametrii necesari cautarii (numele)
    """  
    def __uiCautaDisciplinaNume(self,params):    
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un nume")
        nume=params[0]
        lis=self.__ctrlD.cautaDisciplinaNume(nume)            #lis= lista de discipline care au acelasi nume      
        for x in lis:
            print (x)
    
    """
    Permite cautarea disciplinelor cu un anumit profesor interactinand cu utilizatorul
    Date intrare: params- lista de parametrii necesari cautarii (profesorul)
    """        
    def __uiCautaDisciplinaProfesor(self,params):    
        if len(params)<1:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un nume")
        profesor=params[0]
        lis=self.__ctrlD.cautaDisciplinaProfesor(profesor)    #lis= lista de discipline care au acelasi profesor
        for x in lis:
            print (x)
        
    """
    Permite adaugarea unei note la lista de note interactionand cu utilizatorul
    Date intrare: params- lista de parametrii necesari adaugarii (id student, id disciplina, nota obtinuta)
    """
    def __uiAdaugaNota(self,params):
        if len(params)<3:
            raise ConsoleValidationException("Nr parametrii invalid!!! Introduceti un Id student, un Id disciplina si o nota")
        idS=int(params[0])
        idD=int(params[1])
        nota=int(params[2])        
        self.__ctrlN.adaugaNota(idS,idD,nota)                   
        print ("Nota adaugata cu succes!")
        
    """
    Sterge notele unui student interactionand cu utilizatorul
    Date intrare: params- lista de parametrii necesari (Id student)
    """
    def __uiStergeNotaS(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Lista de parametrii invalida!! Introduceti un Id de student")        
        ident=int(params[0])
        self.__ctrlN.stergeNotaS(ident)                 #apeleaza stergerea notelor unui student
        print ("Au fost sterse toate notele acestui student!")
        
    """
    Sterge notele unei discipline interactionand cu utilizatorul
    Date intrare: params- lista de parametrii necesari (Id disciplina)
    """
    def __uiStergeNotaD(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Lista de parametrii invalida!! Introduceti un Id de disciplina")        
        ident=int(params[0])
        self.__ctrlN.stergeNotaD(ident)                 #apeleaza stergerea notelor unei discipline
        print ("Au fost sterse toate notele de la aceasta disciplina!")
        
    """
    Afiseaza lista notelor
    Date intrare: params- lista vida, folosit pt ca in apelul comenzi[cmd[0]].executa(cmd[1:]) avem un parametru, care in acest caz nu ne trebuie
    """
    def __uiPrintNota(self,params):
        alls =self.__ctrlN.getAllNote()         #alls primeste toate elementele din lista de discipline
        if len(alls)==0:
            print("Lista de note este goala!")
        for x in alls:
            idStud=x.getIdstud()
            idDis=x.getIddis()
            nota=x.getNote()
            nume=self.__ctrl.cautaStudentId(idStud).getNume()
            disciplina=self.__ctrlD.cautaDisciplinaId(idDis).getNume()
            profesor=self.__ctrlD.cautaDisciplinaId(idDis).getProfesor()
            print("Studentul "+nume+" la disciplina "+disciplina+" predata de "+profesor+ " are nota/notele "+str(nota))

    """
    Ordoneaza alfabetic dupa numele de student toti studentii care au note la o disciplina cu un anumit nume
    Date intrare: params- numele disciplinei cu semnificatia de mai sus
    """      
    def __uiOrdonareAlfabetic(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Lista de parametrii invalida!! Introduceti un nume de disciplina")        
         
        numeD=params[0]                                    #numele dorit pentru discipline   
        #lis=self.__ctrlS.ordonareAlfabetic(numeD)
        lis=self.__ctrlS.shellSort(numeD,key=lambda x: self.__ctrl.cautaStudentId(x.getIdstud()).getNume())

        self.__ctrlS.printNotaL(lis)
        
    """
    Ordoneaza crescator in functie de media obtinuta de un student la o anumita disciplina toti studentii care au note la disciplina respectiva
    Date intrare: numele disciplinei cu semnificatia de mai sus
    """
    def __uiOrdonareNumeric(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Lista de parametrii invalida!! Introduceti un nume de disciplina")        
        numeD=params[0]                                    #numele dorit pentru discipline 
        #lis=self.__ctrlS.ordonareNumeric(numeD)
        lis=self.__ctrlS.bubbleSort(numeD,key=lambda x: self.__ctrlS.medie(x.getNote())    )             #apelam functia bubble sort
        self.__ctrlS.printNotaL2(lis)
        
    """
    Ordoneaza descrescator in functie de media obtinuta de un student la o anumita disciplina toti studentii care au note la disciplina respectiva
    Date intrare: numele disciplinei cu semnificatia de mai sus
    """
    def __uiOrdonareNumericDescrescator(self,params):
        if len(params)<1:
            raise ConsoleValidationException("Lista de parametrii invalida!! Introduceti un nume de disciplina")        
        numeD=params[0]                                    #numele dorit pentru discipline 
        lis=self.__ctrlS.ordonareNumericDescrescator(numeD)
        #self.__ctrlS.printNotaL2(lis)
        self.__ctrlS.printNotaL2Recursiv(lis,0)            #apelam functia recursiva pentru afisarea studentilor ordonati descrescator
            
    """
    Afiseaza primi 20% din studenti care au media anuala cea mai mare 
    Date intrare: params- lista vida
    """     
    def __uiPrimi(self,params):
        lis=self.__ctrlS.primi()
        nrStud=len(self.__ctrl.getAllStudenti())
        nr=int(20/100*nrStud)
        #self.__ctrlS.printLista(lis,nr)
        self.__ctrlS.printListaRecursiv(lis,0,nr)           #apelam functia recursiva pentru afisarea primilor 20% studenti
        
    """
    Ruleaza consola
    """
    def run(self,cond):
        comenzi = {
            "addS":Comanda("addS",self.__uiAddStudent),
            "printS":Comanda("printS",self.__uiPrintStudent),
            "delS":Comanda("delS",self.__uiStergeStudent),
            "modS":Comanda("modS",self.__uiModificaStudent),
            "getSI":Comanda("getSI",self.__uiCautaStudentId),
            "getSN":Comanda("getSN",self.__uiCautaStudentNume),
            "addD":Comanda("addD",self.__uiAddDisciplina),
            "printD":Comanda("printD",self.__uiPrintDisciplina),
            "delD":Comanda("delD",self.__uiStergeDisciplina),
            "modD":Comanda("modD",self.__uiModificaDisciplina),
            "getDI":Comanda("getDI",self.__uiCautaDisciplinaId),
            "getDN":Comanda("getDN",self.__uiCautaDisciplinaNume),
            "getDP":Comanda("getDP",self.__uiCautaDisciplinaProfesor),
            "addN":Comanda("addN",self.__uiAdaugaNota),
            "printN":Comanda("printN",self.__uiPrintNota),
            "ordAlf":Comanda("ordAlf",self.__uiOrdonareAlfabetic),
            "ordNum":Comanda("ordNum",self.__uiOrdonareNumeric),
            "ordNum2":Comanda("ordNum2",self.__uiOrdonareNumericDescrescator),
            "20%":Comanda("20%",self.__uiPrimi)
        }
        
        
        if cond==1:
            self.__ctrl.adaugaStudent(1,"ion")
            self.__ctrl.adaugaStudent(2,"ana")
            self.__ctrl.adaugaStudent(3,"alin")
            self.__ctrl.adaugaStudent(4,"maria")
            self.__ctrl.adaugaStudent(5,"andrei")
            self.__ctrl.adaugaStudent(6,"ionela")
            self.__ctrl.adaugaStudent(7,"anastasia")
            self.__ctrl.adaugaStudent(8,"dorel")
            self.__ctrl.adaugaStudent(9,"miruna")
            self.__ctrl.adaugaStudent(10,"stefan")
            
            self.__ctrlD.adaugaDisciplina(1,"mate","popescu")
            self.__ctrlD.adaugaDisciplina(2,"info","ionescu")
            self.__ctrlD.adaugaDisciplina(4,"mate","ion")
            self.__ctrlD.adaugaDisciplina(3,"logica","predescu")
            
            self.__ctrlN.adaugaNota(1,1,4)
            self.__ctrlN.adaugaNota(1,1,10)
            self.__ctrlN.adaugaNota(3,2,9)
            self.__ctrlN.adaugaNota(1,4,3)
            self.__ctrlN.adaugaNota(2,1,6)
            self.__ctrlN.adaugaNota(4,1,7)
            self.__ctrlN.adaugaNota(5,1,4)
            self.__ctrlN.adaugaNota(6,1,10)
            self.__ctrlN.adaugaNota(7,2,9)
            self.__ctrlN.adaugaNota(8,4,3)
            self.__ctrlN.adaugaNota(9,1,6)
            self.__ctrlN.adaugaNota(10,1,7)
        
        
        while True:
            print ("")
            print ("1.Gestioneaza Student")
            print ("2.Gestioneaza Disciplina")
            print ("3.Gestioneaza Nota")
            print ("4.Statistici")
            print ("")
            cmd0=Validator.validationInt("Alege o optiune: ")
            if cmd0==1:
                print ("")
                print ("Adaugare student: addS <Id> <Nume>")
                print ("Afisare lista studenti: printS")
                print ("Sterge un student: delS <Id>")
                print ("Modifica un student: modS <Id> <Noul nume>")
                print ("Cauta un student dupa Id: getSI <Id>")
                print ("Cauta un student dupa Nume: getSN <nume>")
                print ("Terminare program: exit")
                print ("")
            if cmd0==2:
                print ("")
                print ("Adaugare disciplina: addD <Id> <Nume> <Nume profesor>")
                print ("Afisare lista discipline: printD")
                print ("Sterge o disciplina: delD <Id>")
                print ("Modifica o disciplina: modD <Id> <Noul nume> <Noul profesor>")
                print ("Cauta o disciplina dupa Id: getDI <Id>")
                print ("Cauta o disciplina dupa nume: getDN <nume>")
                print ("Cauta o disciplina dupa profesor: getDP <profesor>")
                print ("Terminare program: exit")
                print ("")
            if cmd0==3:
                print ("")
                print ("Adaugare nota: addN <IdStudent> <IdDisciplina> <Nota>")
                print ("Afisare lista de note: printN")
                print ("Terminare program: exit")
                print ("")
            if cmd0==4:
                print ("")
                print ("Lista de studenti si notele lor la o disciplina data, ordonata alfabetic: ordAlf <nume disciplina>")
                print ("Lista de studenti si notele lor la o disciplina data, ordonata dupa note crescator: ordNum <nume disciplina>")
                print ("Lista de studenti si notele lor la o disciplina data, ordonata dupa note descrescator: ordNum2 <nume disciplina>")
                print ("Primi 20% din studenti ordonati dupa media notelor la toate disciplinele: 20% ")
                print ("Terminare program: exit")
                print ("")
                
            cmd = self.__citesteComanda()
            if (len(cmd)==0):
                continue
            if (len(cmd[0])==0):
                continue
            if (cmd[0]=="exit"):
                return
            if cmd[0] in comenzi:                      #daca comanda introdusa este valida
                try:
                    comenzi[cmd[0]].executa(cmd[1:])   #apelam comenzi[<comanda>].executa pentru parametrii introdusi dupa comanda
                except RepositoryException as re:
                    print("Repository:"+str(re))
                except RepositoryExceptionD as red:
                    print("RepositoryD:"+str(red))
                    
                except RepositoryExceptionD2 as red2:
                    print("RepositoryD2:"+str(red2))
                except RepositoryException2 as re2:
                    print("Repository2:"+str(re2))
                except RepositoryExceptionN2 as ren2:
                    print("RepositoryExceptionN2"+str(ren2))
                    
                except RepositoryExceptionN as ren:
                    print("RepositoryN:"+str(ren))
                except ValidatorException as ve:
                    print("Validator:"+str(ve))
                except ConsoleValidationException as cve:
                    print("Console:"+str(cve))
                except ValueError as ve:
                    print("Eroare tip de data!!!")
            else:
                print("Comanda invalida!")