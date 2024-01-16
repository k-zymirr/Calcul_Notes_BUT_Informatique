"""
By @k_zymir
"""

from s1 import *

def entrerNotes():
    for competence in range(1, 7):
        print("COMPETENCE", competence)
        print("\n")
        entrerNotesResources(competence)
        print("\n")
        entrerNotesSae(competence)
        print("\n\n\n\n")

def entrerNotesResources(competence):
    for note in range(len(RESOURCES[competence])):
        print(NOMS[competence][note])
        
        notesList = []
        partnote = "None"
        while (partnote.lower()!="fin"):
            try:
                partnote = input("Entrez une note. Si toutes vos notes sont rentrées, entrez [fin] : ")
                if (partnote.lower() == "fin"):
                    pass
                elif (0<=float(partnote) and float(partnote)<=20):
                    notesList.append(float(partnote))
                else:
                    print("Entrée Invalide")
            except ValueError:
                print("Entrée Invalide")
        
        if (len(notesList)>0):
            finalNote = 0    
            for mark in notesList:
                print(mark, end=", ")
                finalNote += mark
                
            finalNote = finalNote/len(notesList)
            
            print(" ")
            if (input("Validez-vous cette saisie ? [O/N]").upper() != "N"):
                RESOURCES[competence][note] = finalNote
            else:
                note -= 1
       
        print("\n")

def entrerNotesSae(competence):
    valide = False
    note = "None"
    
    while (not valide and note != "non"):
        print(SAENOMS[competence-1], "(si vous n'avez pas eut de note, entrez [non])", end='')
        note = input(" : ")
        try:
            if (note.lower() == "non"):
                pass
            elif (0<=float(note) and float(note)<=20):
                note = float(note)
                valide = True
            else:
                print("Entrée Invalide")
        except ValueError:
            print("Entrée Invalide")
            
    if (note != "non"):
        print(note)
        if (input("Validez-vous cette note ? [O/N]").upper() == "O"):
            SAE[competence] = note
        else:
            entrerNotesSae(competence)
    

def calculComp(comp):
    Co = []
    noNote = True
    
    if SAE[comp-1] != None :
        Co.append(SAE[comp-1])
        Co.append(SAECOEF)
        noNote = False
        
    
    noteno = 0
    for note in RESOURCES[comp]:
        if note != None:
            Co.append(note)
            Co.append(COEF[comp][noteno])
            noNote = False
        noteno += 1
    
    C = 0
    div = 1
    appreciation = "SANS-RESULTAT"
    if not noNote :
        for n in range(len(Co)):
            if n%2 == 0:
                C += Co[n]*Co[n+1]
                div += Co[n+1]
                n += 1
        div -= 1        
        C = C/div
        
        if C>10:
            appreciation = "ADMIS"
        elif C>8:
            appreciation = "PASSABLE"
        else:
            appreciation = "NON-ADMIS"   
    
    return C, appreciation

def main():
    entrerNotes()
    
    C1, C1appr = calculComp(1)
    C2, C2appr = calculComp(2)
    C3, C3appr = calculComp(3)
    C4, C4appr = calculComp(4)
    C5, C5appr = calculComp(5)
    C6, C6appr = calculComp(6)
    
    print("COMPETENCE 1 :\n",
          "Note :", C1, "\n",
          C1appr,
          "\n")
    
    print("COMPETENCE 2 :\n",
          "Note :", C2, "\n",
          C2appr,
          "\n")
    
    print("COMPETENCE 3 :\n",
          "Note :", C3, "\n",
          C3appr,
          "\n")
    
    print("COMPETENCE 4 :\n",
          "Note :", C4, "\n",
          C4appr,
          "\n")
    
    print("COMPETENCE 5 :\n",
          "Note :", C5, "\n",
          C5appr,
          "\n")
    
    print("COMPETENCE 6 :\n",
          "Note :", C6, "\n",
          C6appr,
          "\n")


main()