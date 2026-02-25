nom=str(input('Ingrese su nombre: '))
apelli=str(input('Ingrese su apellido: '))
edadHM=int(input('Edad de hermano Mayor: '))
edadHN=int(input('Edad de hermano Menor: '))

a= edadHM-edadHN

print(f"Su nombre completo es {nom} {apelli} y la edad del hermano Mayor es {edadHM}, la edad del hermano Menor es {edadHN} y la diferencia de edad es {a}")