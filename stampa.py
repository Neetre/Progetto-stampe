'''
Braga Mattia 3FI - Gianni Bellini
a.s. 2022/2023
'''
import csv
from icecream import ic
import pdfkit
from changer import changer
from time import time, localtime, strftime
import platform
import os.path

ic.disable()

#tipo = "docenti"
tipo = "aule"

value_table = ["" for i in range (41)]

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
        
'''
Docenti
'''

def tabella(fhtml):
	global value_table

	with open('odi_stampeA3Docenti2.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter = ";")
		fhtml.write("        <tr>")
		attivo = False
		i = 0 
		for row in reader:
			docente = row['docenti']
			if attivo == False:
				docente_attivo = docente
				attivo = True

			if docente != docente_attivo:
				ic(value_table)
				doc()
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
		doc()
		fhtml.write("        </tr>")


def doc():
	global value_table
	for i in range(0, len(value_table)):
			if i == 0:
				fhtml.write(f"            <td colspan='8 align='center' >{value_table[i]}</td>")
			else:
				fhtml.write(f"            <td align='center'>{value_table[i]}</td>")

   
def li(docente, giorno, ora, classe, aula, materia):
    global value_table
    giorni = {"lunedi": 1, "martedi": 2, "mercoledi" : 3, "giovedi" : 4, "venerdi" : 5}
    n_giorno = giorni[giorno]
    value_table[0] = docente
    offset = ((n_giorno - 1) * 8)
    indice = offset + int(ora)
    value_table[indice] = f"{classe}<br>{aula}<br>{materia}"
    ic(value_table)


def head(fhtml):
	fhtml.write('''<!DOCTYPE html5>
	<html>
		<style>
			table, tr, td {border:1px solid black;}
		</style>''')

#table-layout:auto;  
def header(fhtml):
    fhtml.write('''
		<body>
			<table border='1'; style="width:100%; height:auto;">   
				<tr>
					<th colspan='8' align="center">Docente</th>
					<th colspan='8' align="center">Luned&igrave;</th>
					<th colspan='8' align="center">Marted&igrave;</th>
					<th colspan='8' align="center">Mercold&igrave;</th>
					<th colspan='8' align="center">Gioved&igrave;</th>
					<th colspan='8' align="center">Venerd&igrave;</th>
				</tr>
				<tr>
					<th colspan="8" align='center'></th>
					
					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>

					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>

					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>

					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>
					
					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>
				</tr>''')
 

def footer(fhtml):
	fhtml.write("    </table>")
	fhtml.write("</body>")
	fhtml.write("</html>")
	fhtml.close()


def pdf():
    options = {
    'page-size': 'A3',
	'orientation': 'Landscape',
    'margin-top': '0.50in',
    'margin-right': '0.50in',
    'margin-bottom': '0.60in',
    'margin-left': '0.50in',
}
    #Portrait

    with open('stampa.html') as f:
    	pdfkit.from_file(f, 'stampa.pdf', options = options)





'''
Aule
'''


def tabella_aula(fhtml):
	global value_table

	with open('odi_stampeA3Aule2.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter = ";")
		fhtml.write("        <tr>")
		attivo = False
		i = 0 
		for row in reader:
			docente = row['docente']
			if attivo == False:
				docente_attivo = docente
				attivo = True

			if docente != docente_attivo:
				ic(value_table)
				doc_aula()
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
			li_aula(docente,  giorno, ora, classe, aula, materia)
			if i == 18:
				i = 0
				fhtml.write("<br>")
				header_aula(fhtml)
		doc_aula()
		fhtml.write("        </tr>")


def doc_aula():
	global value_table
	for i in range(0, len(value_table)):
			if i == 0:
				fhtml.write(f"            <td colspan='8 align='center' >{value_table[i]}</td>")
			else:
				fhtml.write(f"            <td align='center'>{value_table[i]}</td>")

   
def li_aula(docente, giorno, ora, classe, aula, materia):
    global value_table
    giorni = {"lunedi": 1, "martedi": 2, "mercoledi" : 3, "giovedi" : 4, "venerdi" : 5}
    n_giorno = giorni[giorno]
    value_table[0] = docente
    offset = ((n_giorno - 1) * 8)
    indice = offset + int(ora)
    value_table[indice] = f"{classe}<br>{aula}<br>{materia}"
    ic(value_table)


def head_aula(fhtml):
	fhtml.write('''<!DOCTYPE html5>
	<html>
		<style>
			table, tr, td {border:1px solid black;}
		</style>''')

#table-layout:auto;  
def header_aula(fhtml):
    fhtml.write('''
		<body>
			<table border='1'; style="width:100%; height:auto;">   
				<tr>
					<th colspan='8' align="center">Docente</th>
					<th colspan='8' align="center">Luned&igrave;</th>
					<th colspan='8' align="center">Marted&igrave;</th>
					<th colspan='8' align="center">Mercold&igrave;</th>
					<th colspan='8' align="center">Gioved&igrave;</th>
					<th colspan='8' align="center">Venerd&igrave;</th>
				</tr>
				<tr>
					<th colspan="8" align='center'></th>
					
					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>

					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>

					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>

					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>
					
					<th align='center'>1</th>
					<th align='center'>2</th>
					<th align='center'>3</th>
					<th align='center'>4</th>
					<th align='center'>5</th>
					<th align='center'>6</th>
					<th align='center'>7</th>
					<th align='center'>8</th>
				</tr>''')
 

def footer_aula(fhtml):
	fhtml.write("    </table>")
	fhtml.write("</body>")
	fhtml.write("</html>")
	fhtml.close()


def pdf_aula():
    options = {
    'page-size': 'A3',
	'orientation': 'Landscape',
    'margin-top': '0.50in',
    'margin-right': '0.50in',
    'margin-bottom': '0.60in',
    'margin-left': '0.50in',
}
    #Portrait

    with open('stampa_aula.html') as f:
    	pdfkit.from_file(f, 'stampa_aula.pdf', options = options)


if __name__ == "__main__":
    log(term = False)
    if tipo == "docenti":
        fhtml = open("stampa.html","w")
        aula = False
        changer(aula)
        head(fhtml)
        header(fhtml)
        tabella(fhtml)
        footer(fhtml)
        ic(value_table)
        pdf()

    if tipo == "aule":
        aula = True
        fhtml = open("stampa_aula.html","w")
        changer(aula)
        head_aula(fhtml)
        header_aula(fhtml)
        tabella_aula(fhtml)
        footer_aula(fhtml)
        ic(value_table)
        pdf_aula()
    log(term = True)