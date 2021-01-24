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


print(dictionary.meaning("increase")) #Ok, there IS a second key for Verb. Fock.

print(meaning_paired("increase"))
print (meaning("increase"))
print (gram_type("increase"))

def voc1(lista_palabras,Pydict=PyDictionary()): #Funciona as intended. Y capitalizada además.

    ## A partir de una lista de palabras devuelve el diccionario con Palabra : Lista de definiciones de esa palabra.
    lista_palabras = capitalize_lista(lista_palabras) # capitalizamos.
    definiciones=[]

    for item in lista_palabras:
        # print(item)
        definiciones.append(meaning2(item))


    # Now we have a list withing list that contains all definitions.
    diccionario = dict(zip(lista_palabras, definiciones))
    return diccionario


## Another one.

def ordered_definitions(word="increase",Pydict=PyDictionary()):
    word = word.capitalize()
    separator = " | "  # We could use 2.

    dicts = meaning_paired(word,Pydict)
    for k in dicts:  # not k.v porque entoncesharíamos mil ciento y pico cad una repetida.
            print(word + separator + k + separator + separator.join(dicts[k])   )

def ordered_definitions_inlist(word="increase",Pydict=PyDictionary()): #Also works. Retrieves a list.
    word = word.capitalize()
    separator = " | "  # We could use 2.
    list = []
    dicts = meaning_paired(word,Pydict)
    for k in dicts:  # not k.v porque entoncesharíamos mil ciento y pico cad una repetida.
            list.append(word + separator + k + separator + separator.join(dicts[k])   )
    return(list)

def ordered_definitions_indict(word="increase",Pydict=PyDictionary()): #Also works. Retrieves a dict with Key = Word (grammar type) , Value = Definitions separated by separator..
    word = word.capitalize()
    separator = " | "  # We could use 2.
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


print(voc2(["increase","tomato","potato"]))

print(ordered_definitions_indict("tomato"))

# print(ordered_definitions_inlist("increase"))
# print(ordered_definitions_indict("increase"))

## Now we get that to csv


import pandas
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
    return(lista_limpia)

print(list_tryier())

## https://stackoverflow.com/questions/52563826/python-how-to-get-rid-of-pydictionary-error-messages


def verification(msg="¿Continuar?"):
    question = str(input(msg))
    if question in ["Si","si","s","Y","y","yes","Yes","True",True]:
        return(True)
    if question in ["más","+","mas","Mas","Más"]:
        return("mas")
    else:
        return(False)


def list_tryier2(list_prev=[]):
    # Hace lo del Tryier, limpiando, haciendo un set para quitar repetidas y la devuelve. Como está el tryier, tb print las que quita.
    print("Tu lista actual es: ", list_prev)
    lista = str(input(
        "Write here a list of words separated by a single space " ". \n Example: 'tomato potato' (Dont need the '')\n "))
    lista = lista.split(sep=" ")
    lista = capitalize_lista(lista)
    print("Eliminando entradas repetidas")
    lista = list(set(lista))
    lista = list_tryier(lista)
    print("Tu lista nueva es: ", lista)
    merged_list = list(set(lista + list_prev))
    print("Tu lista completa es: ", merged_list)
    # Devuelve una lista.
    return(merged_list)




def main():
    print("Vocabulary Creator .01 - GPC")
    print("This creates a .csv you can import into other apps")

    print("¡Lets begin")
    def lista_vocabulario(liste=[]):
        liste= liste
        lista = str(input("Write here a list of words separated by a single space " ". \n Example: 'tomato potato' (Dont need the '')\n "))
        lista = lista.split(sep=" ")
        lista = capitalize_lista(lista)
        print("Eliminando entradas repetidas")
        lista = list(set(lista))
        lista = list_tryier(lista)
        print("Tu lista es: ",lista)
        rpt= verification("¿Creamos el archivo ya?(Si/si/sí) ¿O añadimos más palabras?(+,más,mas)")
        if rpt =="mas":
            add_list= str(input("Write here a list of words separated by a single space " ". \n Example: 'tomato potato' (Dont need the '')\n "))
            add_list = add_list.split(sep=" ")
            add_list= capitalize_lista(add_list)
            add_list = list_tryier(add_list)
            print("Añadiendo a la lista anterior")
            mergedlist = list(set(lista + add_list))
            print("Tu lista es: ", mergedlist )
            print("Covirtiendo a CSV")
            nombre_archivo = str(input("Deme un nombre para el archivo (sin extension) "))
            nombre_archivo = "./" + nombre_archivo +".csv"

            vocabulario = voc2(mergedlist)
            dict_to_csv(vocabulario,separ="%",csv=nombre_archivo)

        elif rpt == True:
            vocabulario = voc2(lista)
            print("Covirtiendo a CSV")
            nombre_archivo = str(input("Deme un nombre para el archivo (sin extension) "))
            nombre_archivo = "./" + nombre_archivo + ".csv"

            vocabulario = voc2(lista)
            dict_to_csv(vocabulario, separ="%", csv=nombre_archivo)

        else:
            quit()



main()
# string = "tomato blonde tonto Mouse Mice door door sWoRd"
# lista = string.split(sep=" ")
# e = list_tryier(lista)
# print(e)

print(meaning("potato"))


# What do we need now. We need a list of words we want to know the definitions of, and a functiosn that take each one of those and makes a list of lists of those words.
# So we can pair them in a dictionary and get the Word : Meaning. Ideally we could do Word > Grammar Type > Meaning.
# Then we use them to construct a table-excel with that values.






# print(capitalize_lista(["agurifriski","tonto","patata"])) ## Funciona

# vocabulario = voc1(["Water","rEd","increase"]) # VA bien. Solo falla si la palabra no existe como "tonto". ## Si esta repetida no importa porque la ignora.
# print(vocabulario)
# print(list(vocabulario.keys()))
# print(list(vocabulario.values()))
#
# print(list(vocabulario.values())[1])
# print("\n\n ")
# print((list(vocabulario.values())[1])[0]) #No funcionaba antes porque puse doble uno y esa es la segunda definiciion. Ahroa bien.
#
# print("\n\n ")
# # Podemos extraer el 1, recordamos empiezan en 2.
# e= (list(vocabulario.values())[1])      # Podemos extraer el 1, recordamos empiezan en 2.
# print(e[0])

# e=meaning("word")
# print(e)
#
# e2=meaning2("word")
# print(e2)
# print(gram_type("word"))
# print (dictionary.meaning("indentation"))


# ## Now we try with verbs that are also nowns. It doent have Noun/Verb cause its not innitialy coded like that.
#
# print(meaning("increase"))
# print(gram_type("increase"))
#
#
# #enter the word you want to search here e.g. I used the word "fix"
# print(dict) # Da la localizacion del objeto.
#
# # e= str(dict.meaning("Black") )# Ironico, en pycharm estan al reves los colores porque estamos en el dark mode. Genial.1
# # print(e)
