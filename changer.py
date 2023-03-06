def changer(aula):
    parole = ["PALESTRA", "SOSTEGNO"]
    if aula == False:
        with open('odi_stampeA3Docenti.csv') as file:
            fil = open("odi_stampeA3Docenti2.csv", "w")
            rfile = file.readline()
            while rfile != "":
                ok = rfile
                for par in parole:
                    if par in rfile:
                        if  par == "PALESTRA":
                            ok = rfile.replace("PALESTRA", "PALE")
                        elif par == "SOSTEGNO":
                            ok = rfile.replace("SOSTEGNO", "SOST")
                rfile = file.readline()
                fil.write(ok)
    if aula == True:
        with open('odi_stampeA3Aule.csv') as file:
            fil = open("odi_stampeA3Aule2.csv", "w")
            rfile = file.readline()
            while rfile != "":
                ok = rfile
                for par in parole:
                    if par in rfile:
                        if  par == "PALESTRA":
                            ok = rfile.replace("PALESTRA", "PALE")
                        elif par == "SOSTEGNO":
                            ok = rfile.replace("SOSTEGNO", "SOST")
                rfile = file.readline()
                fil.write(ok)