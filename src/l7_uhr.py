import datetime

def zeit_ausgeben():
    jetzt = datetime.datetime.now()
    uhrzeit = jetzt.strftime("%H:%M:%S")
    print(f"Aktuelle Uhrzeit: {uhrzeit}")
zeit_ausgeben()
