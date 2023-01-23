'''

'''
import csv

        
def tabella():
	with open('odi_stampeA3Docenti.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter = ";")
		fhtml.write("        <tr>")
		doc = 0
		for row in reader:
			print(row["docenti"])
			docente = row['docenti']
			if docente != "ADAMOLI PAOLO":
				continue
			giorno = row['giorno']
			ora = row['ora']
			classe = row['classe']
			aula = row['aula']
			materia = row['materia']
			if doc == 0:
				fhtml.write(f"            <td colspan='8 align='center'>{docente}</td>")
			doc += 1
			fhtml.write(f"            <td>{giorno},{ora},{materia} <br> {classe} <br> {aula}</td>")
		fhtml.write("        </tr>")
			#c = input("terminare? ")
			#if c == "y":
			#    break



fhtml = open("stampa2.html","w")
fhtml.write('''<!DOCTYPE html5>
<html>
	<style>
		table, tr, td {border:1px solid black;}
	</style>
	<body>
		<table border='1' width='400px' style="width:100%">
			<tr>
				<th colspan='8' align="center">Docente</th>
				<th colspan='8' align="center">Lunedì</th>
				<th colspan='8' align="center">Martedì</th>
				<th colspan='8' align="center">Mercoldì</th>
				<th colspan='8' align="center">Giovedì</th>
				<th colspan='8' align="center">Venerdì</th>
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
tabella()
fhtml.write("    </table>")
fhtml.write("</body>")
fhtml.write("</html>")
fhtml.close()