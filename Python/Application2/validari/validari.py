
class ValidatorException(Exception):
    """
    Clasa de erori pentru Validari
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class Validator:
    """
    Permite validarea datelor
    """
    
    """
    Valideaza un obiect de tip student
    Date intrare: student- studentul pe care il validam
    """
    def valideazaStudent(self,student):
        erori = ""
        if student.getIdstud()<0:
            erori+="Id invalid!\n"
        if student.getNume()=="":
            erori+="Nume invalid!\n"
        if len(erori)>0:
            raise ValidatorException(erori)
        
    """
    Valideaza un obiect de tip disciplina
    Date intrare: disciplina- disciplina pe care o validam
    """
    def valideazaDisciplina(self,disciplina):        
        erori = ""
        if disciplina.getIddis()<0:
            erori+="Id invalid!\n"
        if disciplina.getNume()=="":
            erori+="Nume disciplina invalid!\n"
        if disciplina.getProfesor()=="":
            erori+="Nume profesor invalid!\n"
        if len(erori)>0:
            raise ValidatorException(erori)  
        
    """
    Valideaza un obiect de tip nota
    Date intrare: nota- nota pe care o validam
    """    
    def valideazaNota(self,nota):
        erori=""
        if nota.getIddis()<0:
            erori+="Id disciplina invalid!\n"
        if nota.getIdstud()<0:
            erori+="Id student invalid!\n"
        for x in nota.getNote():
            if x<0 or x>10:
                erori+="Nota invalida!\n"    
        if len(erori)>0:
            raise ValidatorException(erori)
        
    """
    Descriere: verifica daca o valoare este de tip int si afiseaza mesajul "Valoare invalida" daca valoarea nu e de tip int
    Date intrare: Textul care se afiseaza la solicitarea valorii
    """
    def validationInt(self):
        while True:
            try:
                cmd=int(input(self))
                return cmd
            except ValueError:
                print("Valoare invalida!!!")
                print(" ")