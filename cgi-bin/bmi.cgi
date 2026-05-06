rm ~/html/cgi-bin/bmi.cgi
cat > ~/html/cgi-bin/bmi.cgi << 'EOF'
#!/usr/bin/python3
print('Content-type: text/html \n')
import cgi
form = cgi.FieldStorage()
name = form.getvalue("name", "Unbekannt")
gewicht = float(form.getvalue("Gewicht", 1))
groesse = float(form.getvalue("Groesse", 1)) / 100
bmi = gewicht / (groesse ** 2)
if bmi < 18.5:
 kategorie = "Untergewicht"
elif bmi < 25:
 kategorie = "Normalgewicht"
elif bmi < 30:
 kategorie = "Uebergewicht"
else:
 kategorie = "Stark uebergewichtig"
print("<!DOCTYPE html>")
print("<html lang='de'>")
print("<head>")
print("<meta charset='UTF-8'>")
print("<title>BMI Ergebnis</title>")
print("<link rel='stylesheet' href='../style.css'>")
print("</head>")
print("<body>")
print("<h1>Ergebnis fuer " + name + "</h1>")
print("<p>Ihr BMI: <strong>" + str(round(bmi,1)) + "</strong></p>")
print("<p>Kategorie: <strong>" + kategorie + "</strong></p>")
print("<a href='../index.html'>Zurueck</a><br>")
print("<a href='https://github.com/Blan-Ru/BMI-Rechner'>GitHub Repo</a>")
print("</body>")
print("</html>")
EOF