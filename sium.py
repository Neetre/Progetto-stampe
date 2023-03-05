'''
Braga Mattia 3FI
a.s. 2022/2023
'''
import csv
from icecream import ic
import pdfkit
from changer import changer
from time import time, localtime, strftime
import platform
import os.path

#ic.enable()
ic.disable()


def log(term):
    '''
    Funzione che aggiorna il file trace quando il programma
    viene eseguito e terminato.
    '''
    flog = open("./log/trace.log", "a")
    uname = platform.uname()
    name_tuple = localtime()
    time_string = strftime("%H:%M:%S del giorno %d/%m/%Y", name_tuple)
    nome_f = os.path.basename(__file__)
    line = "----------------------------------------------"

    if term == False:
        flog.write(f"{str(time())}, {uname.node}, {uname.system}, {nome_f}, Programma iniziato alle ore {time_string} \n")
    else:
        flog.write(f"{str(time())}, {uname.node}, {uname.system}, {nome_f}, Programma terminato alle ore {time_string} \n {line} \n")
    flog.close()
    
def tabella(fhtml):
	global value_table

	with open('odi_stampeA3Aule.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter = ";")
		fhtml.write("        <tr>")
		attivo = False
		i = 0 
		for row in reader:
			docente = row['docenti']

			#if docente != "BELLINI GIANNI":
				#continue

			if attivo == False:
				docente_attivo = docente
				attivo = True

			if docente != docente_attivo:
				ic(value_table)
				doc(fhtml)
				doc(fhtml)
				fhtml.write("        </tr>")
				docente_attivo = docente
				i += 1
			
			giorno = row['giorno']
			ora = row['ora']
			classe = row['classe']
			aula = row['aula']
			materia = row['materia']

			if value_table[0] != docente:
				value_table = ["" for i in range (41)]
			li(docente,  giorno, ora, classe, aula, materia)
			if i == 18:
				i = 0
				fhtml.write("<br>")
				header(fhtml)
		doc(fhtml)
		fhtml.write("        </tr>")