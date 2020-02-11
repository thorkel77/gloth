import os
from .models import Pathology, User,Molecules, Treatment_class

### Renvoie la liste de toutes les maladies
def pathologyChoices():

    temp = Pathology.query.with_entities(Pathology.id, Pathology.icd_10, Pathology.name, Pathology.other_name).all()
    other_name_temp = []

    for x in temp:
        if x[2]:
            array = x[2].split(",")

            for i in range(len(array)):
                if array[i] is not None:
                    other_name_temp.append((x[0], array[i].strip()))

    choices = [(x[0], x[1]) for x in temp] + other_name_temp

    i = 0
    l = len(choices)
    while (i < l and choices[i]):
        if choices[i][1] == '':
            del choices[i]
            l -= 1
        else:
            i += 1

    return choices

def MedicChoices():

    temp = Molecules.query.with_entities(Molecules.id, Molecules.name).all()


#renvoie la liste de tous les users
def userChoices():

    temp = User.query.with_entities(User.id, User.forename).all()
    choices = [(x[0], x[1]) for x in temp]
    return choices

def traitement_class(patho_id):
    t = Treatment_class()
    classTraitement = t.query.filter_by(icd_10=patho_id).all()
    return classTraitement

