def printMenu():
    print (" ")
    print ("MENU:")
    print ("1.Add number")
    print ("3.Search number")
    print ("7.Exit ")
    print (" ")

def printMenu1():
    print ("1.Add to end")
    print ("2.Add to position")
    print ("Any other value to return to the main menu")
    print (" ")

def printMenu3():
    print ("1.Print Im(z) for numbers in a given range")
    print ("2.Print all numbers with module < 10")
    print ("3.Print all numbers with module = 10")
    print ("Any other value to return to the main menu")
    print (" ")

def printNaturalMenu():
    print (" ")
    print ("NATURAL MENU:")
    print ("add - Add number")
    print ("search - Search number")
    print ("exit - Exit ")
    print (" ")    

def printNaturalMenu1():
    print ("end - Add to end")
    print ("position - Add to position")
    print ("Any other value to return to the main menu")
    print (" ")

def printNaturalMenu3():
    print ("im - Print Im(z) for numbers in a given range")
    print ("module< - Print all numbers with module < 10")
    print ("module= - Print all numbers with module = 10")
    print ("Any other value to return to the main menu")
    print (" ")



"""
Descriere: verifica daca o valoare este de tip int si afiseaza mesajul "Valoare invalida" daca valoarea nu e de tip int
Date intrare: Textul care se afiseaza la solicitarea valorii
"""
def validationInt(text):
    while True:
        try:
            cmd=int(input(text))
            return cmd
        except ValueError:
            print("Valoare invalida!!!")
            print(" ")



"""
Descriere: verifica daca o valoare este de tip float si afiseaza mesajul "Valoare invalida" daca valoarea nu e de tip float
Date intrare: Textul care se afiseaza la solicitarea valorii
"""
def validationFloat(text):
    while True:
        try:
            cmd=float(input(text))
            return cmd
        except ValueError:
            print("Valoare invalida!!!")
            print(" ")



"""
Descriere: citeste valorile pentru a-partea reala a unui nr complex
                                   b-partea imaginara a unui nr complex
"""
def createab():
    global a
    global b
    a=validationFloat("Re(z)=")
    b=validationFloat("Im(z)=")



"""
Descriere: Creeaza numar complex de forma unei liste
Date intrare: a-partea reala, b-partea imaginara
Date iesire: Returneaza lista astfel creata
"""
def createComplexNumber(a,b):
    z=[]
    z.append(a)
    z.append(b)
    return z
def testCreateComplexNumber():
    a=4
    b=5
    assert createComplexNumber(a,b)==[4,5]
    a=9
    b=6
    assert createComplexNumber(a,b)==[9,6]



"""
Descriere: Adauga numar complex la sfarsitul unei liste
Date intrare:l-lista de nr complexe, z-nr complex pe care il adaugam
"""
def addComplexNumberToEnd(l,z):
    l.append(z)
def testAddComplexNumberToEnd():
    l=[]
    addComplexNumberToEnd(l,[11,5])
    assert len(l)==1
    assert l[0][0]==11
    assert l[0][1]==5
    addComplexNumberToEnd(l,[7,4])
    assert len(l)==2
    assert l[1][0]==7
    assert l[1][1]==4



"""
Descriere: Adauga numar complex pe o pozitie din lista
Date intrare: l-lista de nr complexe, z-nr complex pe care il adaugam, pos-pozitia pe care il adaugam
"""
def addComplexNumberToPosition(l,z,pos):
    l.insert(pos,z)
def testAddComplexNumberToPosition():
    l=[]
    l.insert(0,[2,6])
    assert len(l)==1
    assert l[0]==[2,6]
    l=[[1,2],[3,4]]
    l.insert(1,[8,9])
    assert len(l)==3
    assert l[1]==[8,9]



"""
Descriere: Afiseaza partile imaginare ale tuturor nr complexe din lista care se afla intr-un interval dat
Date intrare: l-lista de nr complexe, ls-pozitia de inceput a intervalului dorit, ld-pozitia de final a intervalului dorit
"""
def printSecv(l,ls,ld):
    for i in range(ls,ld+1):
        print(l[i][1])



"""
Descriere: Returneaza -1 daca modulul unui numar complex este <10
                      0 daca modulul unui numar complex este=10
Date intrare: z-numar complex dat sub forma de lista
Date iesire: -1 si 0 cu specificatia de mai sus
"""
def module(z):
    import math
    p=0
    p=math.sqrt(z[0]*z[0]+z[1]*z[1])
    if p<10:
        return -1
    if p==10:
        return 0
def testModule():
    assert module([1,2])==-1
    assert module([6,8])==0



"""
Descriere: Daca se cer numerele complexe cu modulul <10 (op=-1) atunci le afiseaza sub forma de sir de caractere a+bi
           Daca se cer numerele complexe cu modulul=10 (op=0) atunci le afiseaza sub forma de sir de caractere a+bi
           Prin variabila ok verifica daca exista sau nu numere complexe in lista cu proprietatea ceruta si afiseaza ca nu exista numere in cazul din urma
Date intrare: l-lista de nr complexe, op-optiunea dorita (-1 pt modul<10 si 0 pt modul=10)
"""
def printModule(l,op):
    if op==-1:
        i=0
        ok=0                                 #ok va primi valoarea 1 cand se va gasi minim un numar complex cu proprietatea ceruta si 0 in caz contrar
        for i in range (0,len(l)):
            if module(l[i])==-1:
                ok=1
                print (str(l[i][0])+"+"+str(l[i][1])+"i")  #afisam in forma a+bi
        if ok==1:
            print (" ")                      #daca am gasit cel putin un nr complex cu proprietatea ceruta afisam " " pentru aspect
        else:
            print ("Nu exista numere complexe in lista cu modulul <10")
    if op==0:
        i=0
        ok=0
        for i in range (0,len(l)):
            if module(l[i])==0:
                ok=1
                print (str(l[i][0])+"+"+str(l[i][1])+"i")  #afisam in forma a+bi
        if ok==1:                            #daca am gasit cel putin un nr complex cu proprietatea ceruta afisam " " pentru aspect
            print (" ")
        else:
            print ("Nu exista numere complexe in lista cu modulul=10")


            
def test():
    testCreateComplexNumber()
    testAddComplexNumberToEnd()
    testAddComplexNumberToPosition()
    testModule()
    
def run():
    l=[]
    print ("1.Meniu normal")
    print ("2.Meniu natural")
    m=validationInt("Alegeti meniul: ")
    if m==1:
        while True:
            printMenu()
            com=validationInt("Choose an option: ")
        
            if com==7:
                print ("Exit")
                return
            if com==1:
                printMenu1()
                com2=validationInt("Choose an option: ")
                if com2==1:
                    createab()
                    addComplexNumberToEnd(l,createComplexNumber(a,b))
                if com2==2:
                    pos=validationInt("Choose a position: ")
                    if pos>=0 and pos<=len(l):
                        createab()
                        addComplexNumberToPosition(l,createComplexNumber(a,b),pos)
                    else:
                        print ("Invalid position!!")
            if com==3:
                if len(l)==0:
                    print ("Lista de numere complexe este vida!! Adaugati numere complexe in lista!")
                else:
                    printMenu3()
                    com2=validationInt("Choose an option: ")
                    if com2==1:
                        print ("Choose range:")
                        ls=validationInt("Start position= ")
                        ld=validationInt("End position= ")
                        if ls>=0 and ld<len(l) and ls<=ld:
                            printSecv(l,ls,ld)
                        else:
                            print ("Invalid range!!")
                    if com2==2:
                        printModule(l,-1)
                    if com2==3:
                        printModule(l,0)
    if m==2:
        while True:
            printNaturalMenu()
            com=str(input("Choose an option: "))
        
            if com=="exit":
                print ("Exit")
                return
            if com=="add":
                printNaturalMenu1()
                com2=str(input("Choose an option: "))
                if com2=="end":
                    createab()
                    addComplexNumberToEnd(l,createComplexNumber(a,b))
                if com2=="position":
                    pos=validationInt("Choose a position: ")
                    if pos>=0 and pos<=len(l):
                        createab()
                        addComplexNumberToPosition(l,createComplexNumber(a,b),pos)
                    else:
                        print ("Invalid position!!")
            if com=="search":
                if len(l)==0:
                    print ("Lista de numere complexe este vida!! Adaugati numere complexe in lista!")
                else:
                    printNaturalMenu3()
                    com2=str(input("Choose an option: "))
                    if com2=="im":
                        print ("Choose range:")
                        ls=validationInt("Start position= ")
                        ld=validationInt("End position= ")
                        if ls>=0 and ld<len(l) and ls<=ld:
                            printSecv(l,ls,ld)
                        else:
                            print ("Invalid range!!")
                    if com2=="module<":
                        printModule(l,-1)
                    if com2=="module=":
                        printModule(l,0)
test()
run()
