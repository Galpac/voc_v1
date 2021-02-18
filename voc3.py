##Step by step vocabulary so you can look up new definitions as you enter them.

# Updating things and installiing pydictionary.

##tengo que usar este https://pypi.org/project/PyDictionary/
import pip
# install PyDictionary
# pip.main(['install','--upgrade','setuptools'])
# pip.main(['install','PyDictionary',"string-color"]) #### This to install pydictionary 2.0.1

import pandas
from pydictionary  import PyDictionary

dictionary=PyDictionary() # Hacemos un diccionario con todas las palabras.
from stringcolor import *


def meaning_paired(word="word",Pydict=PyDictionary()):
    return Pydict.meaning(word) #Extraemos la lista de las definiciones de la palabra.

def meaning(word="word",Pydict=PyDictionary()):
    return list(Pydict.meaning(word).values())[0] #We get the definitions.

def gram_type(word="word",Pydict=PyDictionary()):
    return (Pydict.meaning(word).keys()) #Retrieves the categorical definitions.


# print(dictionary.meaning("increase")) #Ok, there IS a second key for Verb. Fock.
#
# print(meaning_paired("nut"))
# print (meaning("increase"))
# print (gram_type("increase"))

def voc1(lista_palabras,Pydict=PyDictionary()): #Funciona as intended. Y capitalizada además.

    ## A partir de una lista de palabras devuelve el diccionario con Palabra : Lista de definiciones de esa palabra.
    lista_palabras = capitalize_lista(lista_palabras) # capitalizamos.
    definiciones=[]

    for item in lista_palabras:
        # print(item) |
        definiciones.append(meaning2(item))


    # Now we have a list withing list that contains all definitions.
    diccionario = dict(zip(lista_palabras, definiciones))
    return diccionario


## Another one.

def ordered_definitions(word="increase",Pydict=PyDictionary()):
    word = word.capitalize()
    separator = " % "  # We could use 2. # | also valid.

    dicts = meaning_paired(word,Pydict)
    for k in dicts:  # not k.v porque entoncesharíamos mil ciento y pico cad una repetida.
            print(word + separator + k + separator + separator.join(dicts[k])   )

def ordered_definitions_inlist(word="increase",Pydict=PyDictionary()): #Also works. Retrieves a list.
    word = word.capitalize()
    separator = " % "  # We could use 2.
    list = []
    dicts = meaning_paired(word,Pydict)
    for k in dicts:  # not k.v porque entoncesharíamos mil ciento y pico cad una repetida.
            list.append(word + separator + k + separator + separator.join(dicts[k])   )
    return(list)

def ordered_definitions_indict(word="increase",Pydict=PyDictionary()): #Also works. Retrieves a dict with Key = Word (grammar type) , Value = Definitions separated by separator..
    word = word.capitalize()
    separator = " % "  # We could use 2.
    ids = []
    defs = []

    dicts = meaning_paired(word,Pydict)
    for k in dicts:  # not k.v porque entoncesharíamos mil ciento y pico cad una repetida.
            # list.append(word + separator + k + separator + separator.join(dicts[k])   )
            ids.append(word+" ("+k+")")
            defs.append(separator.join(dicts[k]))
    return(dict(zip(ids, defs)))


def capitalize_lista(lista_palabras):
    lista_cap= [x.capitalize() for x in lista_palabras]
    return lista_cap


## Now we need it to work it with lists.
def voc2(lista_palabras):  # Funciona as intended. Y capitalizada además.

    ## A partir de una lista de palabras devuelve el diccionario con Palabra : Lista de definiciones de esa palabra.
    lista_palabras = capitalize_lista(lista_palabras)  # capitalizamos.
    vocabulario = {}

    for item in lista_palabras:
        # print(item)
        vocabulario = {**vocabulario, **ordered_definitions_indict(item) }

    return (vocabulario)


# print(voc2(["increase","tomato","potato"]))
#
# print(ordered_definitions_indict("tomato"))

# print(ordered_definitions_inlist("increase"))
# print(ordered_definitions_indict("increase"))

## Now we get that to csv

def dict_to_csv(dict,separ="%",csv="./Vocabulario.csv"):
    # Recommended sep is %. Cause , or ; could appear in definitions. ANd | separates the definitions.
    df = pandas.DataFrame(data={"Word": list(dict.keys()), "Meanings": list(dict.values())})
    df.to_csv(csv, sep=separ,index=False)

### Vamos a probarlo.

# prueba=voc2(["tomato","maim","destroy","rat"])
# dict_to_csv(prueba,"./Prueba.csv") ##It works.

### Now the MAIN function.

def list_tryier(lista= ["tomato", "tonto"] ):
    elim = []
    for i in lista:

        if PyDictionary.meaning(i,disable_errors=True)==None: # Eliminamos errores porque hace un continuo print.
             elim.append(i)

        else:
            pass

    lista_limpia = [x for x in lista if x not in elim]
    print("Valores no encontrados en el diccionario: ", elim)
    return(sorted(lista_limpia))

# print(list_tryier())

## https://stackoverflow.com/questions/52563826/python-how-to-get-rid-of-pydictionary-error-messages


def verification(msg="¿Continuar?"):
    question = str(input(msg))
    if question in ["Si","si","s","Y","y","yes","Yes","True",True]:
        return(True)

    else:
        return(False)


def list_tryier2(list_prev=[]): #Funciona ya con el diccionario. Devuelve una lista de las palabras encontradas en el Pydict.
    # Hace lo del Tryier, limpiando, haciendo un set para quitar repetidas y la devuelve. Como está el tryier, tb print las que quita.
    print("Tu lista actual es: ", list_prev)
    continuation = True
    while continuation == True:
        lista = str(input(
            "Write here a list of words separated by a single space " ". \n Example: 'tomato potato' (Dont need the '')\n "))
        lista = lista.split() # any number of spaces
        lista = capitalize_lista(lista)
        print("Eliminando entradas repetidas")
        lista = list(set(lista))
        lista = list_tryier(lista)
        print("Tu lista nueva es: ", lista)
        list_prev = sorted(list(set(lista + list_prev))) #necesitamos hacer recursion. Llamamos a si misma.
        print("Tu lista completa es: ", list_prev)

        get_meanings = verification("¿Vemos los nuevos significados?")
        if get_meanings == True:
            print("Tus significados son \n")
            # print(voc2(list_prev).keys())
            for key in voc2(lista):
                print(key, ' : ', voc2(lista)[key])
        else:
            pass



        continuation= verification("¿Continuamos añadiendo (Si/s/sí/yes)? ¿O Finalizamos? (Cualquier otro valor)")

    return(list_prev)



# list_tryier2()




def main():
    print("Vocabulary Creator .01 - GPC")
    print("This creates a .csv you can import into other apps")

    print("¡Lets begin")

    the_list= list_tryier2()

    print("Tu lista final es: ", the_list )
    print("Covirtiendo a CSV")
    nombre_archivo = str(input("Deme un nombre para el archivo (sin extension) "))
    nombre_archivo = "./" + nombre_archivo +".csv"

    vocabulario = voc2(the_list)
    dict_to_csv(vocabulario,separ="%",csv=nombre_archivo)





main()
