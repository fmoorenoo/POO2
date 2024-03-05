## Parámetro posicional
def tipicaFuncion(unpar:int, dospar:int)->None:
    pass

tipicaFuncion(3,6)

#unpar = 3

#dospar = 6


## Parámetro con valor por defecto
def tipicaFuncion(unpar:int, dospar = 6:int)->None:
    pass

tipicaFuncion(3)

#unpar = 3

#dospar = 6


## Parámetro arbitrario
def tipicaFuncion(unpar:int, *dospar:int, content:int)->None:
    pass

tipicaFuncion(3, 6, 6, 6, content=3)

#unpar = 3

#dospar = 6


## Parámetro nominal
def tipicaFuncion(*,unpar:int, dospar:int)->None:
    pass

tipicaFuncion(dospar = 6, unpar = 3)

#unpar = 3

#dospar = 6


## Ejercicio 3 del examen

def myDiv(id:str, *clas:str, content:str)->str:

    resultado = " "
    resultado += '<div id="' + id + '" '

    if len(clas) != 0:
        resultado += 'class = "'

        for x in clas:
            resultado += e + ','

        resultado += '"'
    
    resultado += '>' + content + '</div>'
    
    return resultado