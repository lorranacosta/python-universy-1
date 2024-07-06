#ej8

num = 93714
dias =  num//86400
num -= dias*86400

hs = num//36400
num -= hs*3600

min = num//60
num -= min*60

print ("{} dia, {} horas, {} minuto, {} segundos ." . format (dias, hs, min, num))