def nombre_coureurs(lst):
    '''retourne le nombre de coureurs dans lst'''
    assert type(lst)==list
    assert all([type(obj)==str for obj in lst])
    return len(lst)

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert nombre_coureurs(classement) == 5 
print("bravo")

def nombre_coureurs(lst):
    '''retourne le nombre de coureurs dans lst'''
    assert type(lst)==list
    assert all([type(obj)==str for obj in lst])
    return 

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert nombre_coureurs(classement) == 5 
print("bravo")
