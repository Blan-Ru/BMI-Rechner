#!/usr/bin/python3
print('Content-type: text/html \n')

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name", "Unknown")
weight = float(form.getvalue("weight", 0))
height = float(form.getvalue("height", 1)) / 100 # cm to m

bmi = weight / (height ** 2)

if bmi < 18.5:
category = "Underweight"
elif bmi < 25:
category = "Normal weight"
elif bmi < 30:
category = "Overweight"
else:
category = "Obese"

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>BMI Ergebnisse</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<h1>Ergebnisse {name}</h1>
<p>Dein BMI: <strong>{bmi:.1f}</strong></p>
<p>Kategorie: <strong>{category}</strong></p>
<a href="../index.html">← Back</a><br>
<a href="https://github.com/Blun-Ru/BMI-Rechner">GitHub Repo</a>
</body>
</html>""")