eingabe = open('schlange.txt',"r").read()
schlange=eingabe.split() #textdatei wird gelesen und in Liste eingeschrieben
p = 0 #Anfangsposition 0 gesetzt
loesung = 0 #Variable für Anzahl der Überholvorgänge 0 gesetzt

def vordraengeln(aktuelleposition, testposition, warteschlange):
    #Funktion, welche die bestmögliche neue Position nach einem Überholvorgang ermittelt
    if str(testposition) in warteschlange: #wenn aktuell überprüfte Position in Liste, also Lücke, return neue position
        return testposition
    else: #ansonsten nächst kleinere Position überprüfen, rekursion bis Lücke gefunden
        testposition -=1
        if testposition <= aktuelleposition:
            #Wenn Keine neue Lücke innerhalb der nächsten 11 gefunden wurde, abbruch
            print('Es ist nicht möglich zu wiederholen')
            exit()
        return vordraengeln(p, testposition, warteschlange)

while p < int(schlange[-1]): #solange p nicht an letzter Position
    versuche = p+11
    p = vordraengeln(p, versuche, schlange) 
    #definiere p als die neue Lücke, welches in Funktion vordrängeln gefunden wurde
    loesung += 1 #der Counter des Ergebnisses wird um eins erhöht

print('Es werden ' + str(loesung) + ' Vordrängelaktionen benötigt.') #Ergebnis ausgeben
