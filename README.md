# uide.pinky
Asignatura de lógica de programación. 

Nombre: Domenica Fernandez Salvador

Materia: logica de programación

Universidad: UIDE

Objetivo: Desarrollar un GENERADOR SEGURO DE CONTRASENAS con python en VScode.


El objetivo de este programa es generar una contraseña más segura a partir de una palabra base ingresada por el usuario. El sistema transforma la palabra original aplicando reglas de seguridad como conversión a mayúsculas, sustitución por números y símbolos, y asegurando una longitud mínima de 12 caracteres.

Principales Funcionalidades

Solicita al usuario una palabra base.

Garantiza que la contraseña tenga al menos 12 caracteres.

Repite la palabra base si es necesario para completar la longitud mínima.

Sustituye caracteres para mejorar la seguridad:

"a" por "@"

"e" por "3"

"o" por "0"

Convierte letras minúsculas en mayúsculas.

Mantiene números existentes.

Asegura que la contraseña tenga al menos un símbolo.

Asegura que la contraseña tenga al menos un número.

Muestra la contraseña mejorada como resultado final.

Lógica Aplicada en el Código

El programa utiliza:

Estructuras repetitivas (while y for).

Estructuras condicionales (if, elif y else).

Contadores para validar criterios de seguridad.

Manipulación de cadenas.

La función len() para contar caracteres.
