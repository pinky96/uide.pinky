#Desarrollar el 50% del creador seguro de contrasenas.

usuario=(input("Ingrese una palabra para ayudarte a generar una contrasena segura"))
contador =0 

for i in usuario: 
    contador= contador +1
    
contrasena = ""
ind= 0

#Utilizo un while para asegurar que el usuario ingrese al menos 12 caracteres

while ind < 12: 
    for i in range (contador):
        if ind < 12:
            contrasena = contrasena + usuario [i]
            ind = ind+1
            
#este contador nos va a ayudar a ver simbolos numero y letras mayusculas

mayuscula = 0 
numero= 0
simbolo =0 

#Faltaria recorrer la contrasena, y transformar las letras en numeros, simbolos y mayusculas.
#y hacer la verificacion que no falten estos parametros, y mejorarla en caso de que no se cumplan
#la idea es que las contrasenas tengan una estructura similar a esta: kdiW3kd!9#2.
    
    


