'''
Braga Mattia 3FI
a.s. 2022/2023
'''
import csv

value_table = ["" for i in range (41)]
        
def tabella(fhtml):
	global value_table

	with open('odi_stampeA3Docenti.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter = ";")
		fhtml.write("        <tr>")
		attivo = False
		for row in reader:
			docente = row['docenti']
			#if docente != "BELLINI GIANNI":
				#continue
			if attivo == False:
				docente_attivo = docente
				attivo = True
			if docente != docente_attivo:
				#print(value_table)
				doc()
				fhtml.write("        </tr>")
				docente_attivo = docente
			
			giorno = row['giorno']
			ora = row['ora']
			classe = row['classe']
			aula = row['aula']
			materia = row['materia']

			if value_table[0] != docente:
				value_table = ["" for i in range (41)]
			li(docente,  giorno, ora, classe, aula, materia)


def doc():
	global value_table
	for i in range(0, len(value_table)):
			if i == 0:
				fhtml.write(f"            <td colspan='8 align='center'>{value_table[i]}</td>")
			else:
				fhtml.write(f"            <td align='center'>{value_table[i]}</td>")

   
def li(docente, giorno, ora, classe, aula, materia):
    global value_table
    giorni = {"lunedi": 1, "martedi": 2, "mercoledi" : 3, "giovedi" : 4, "venerdi" : 5}
    n_giorno = giorni[giorno]
    value_table[0] = docente
    offset = ((n_giorno - 1) * 8)
    indice = offset + int(ora)
    value_table[indice] = f"{classe} <br> {aula} <br> {materia}"
    #print(value_table)


def header(fhtml):
	fhtml.write('''<!DOCTYPE html5>
	<html>
		<style>
			table, tr, td {border:1px solid black;}
		</style>
		<body>
			<table border='1' width='400px' style="width:100%">
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

if __name__ == "__main__":
    fhtml = open("stampa.html","w")
    header(fhtml)
    tabella(fhtml)
    footer(fhtml)

print(value_table)