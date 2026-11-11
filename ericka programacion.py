nombre="Ericka"
ApellidoPaterno="Perez"
ApellidoMaterno="Colin"
fechaNacimiento="1975-01-16"
sexo="M"
entidadFederativa="DF"
final="rlr09"
Curp=ApellidoPaterno[0:2]+ApellidoMaterno[0:1]+nombre[0:1]
Curp=Curp+fechaNacimiento[2:4]+fechaNacimiento[5:7]+fechaNacimiento[8:10]
Curp=Curp+sexo+entidadFederativa+final


print(Curp.replace("DF","VZ"))
Curp=Curp.replace("DF","VZ")
print(Curp)
