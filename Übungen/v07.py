list = [101, 205, 310, 405, 210, 115, 320]

eingabe = int(input("wekzeug id:"))
z = 1

for i in list:
    
    if eingabe == i:
        print(f"werkzeug {eingabe} auf platz {z}")
        break
    z += 1
