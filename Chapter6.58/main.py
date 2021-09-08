import requests

my_data = {"name": "Kelvin", "email": "koh84@hotmail.com"}
r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)
