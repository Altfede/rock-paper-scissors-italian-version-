from random import randint


print("CARTA, SASSO, FORBICE")
premio = "500 euro"
print("\nSe vincerai avrai diritto a " + premio)

print("Come ti chiami?")
nome = input()
print("Buona fortuna " + nome + ". Che vinca il migliore!")

punteggio_Io = 0
punteggio_giocatore = 0

comando = ""
while(comando != "stop"):
  print("\nChe arma scegli?")
  armi = ["carta", "sasso", "forbice"]
  for arma in armi:
          print(arma)
  print("Premi 0 per carta, 1 per sasso, 2 per forbice")
  numero_scelto = int(input())
  arma_scelta = armi[numero_scelto]
  print("Hai scelto: " + arma_scelta)
  
  arma_gioco = ""
  numero_gioco = randint(0,2)
  arma_gioco = armi[numero_gioco]
  
  print("...anche io ho scelto!")
  
  verdetto = ""
  if(arma_scelta == "carta" and arma_gioco == "sasso"):
    verdetto = nome + "Complimenti, hai vinto!"
    punteggio_giocatore = punteggio_giocatore + 1
  if(arma_scelta == "forbice" and arma_gioco == "carta"):
    verdetto = nome + "Complimenti, hai vinto!"
    punteggio_giocatore = punteggio_giocatore + 1
  if(arma_scelta == "sasso" and arma_gioco == "forbice"):
    verdetto = nome + " Complimenti, hai vinto!"
    punteggio_giocatore = punteggio_giocatore + 1
    
  if(arma_scelta == arma_gioco):
    verdetto = "Pareggio, ritenta"
    
  if(verdetto == ""):
    verdetto = "Ti ho stracciato!"
    punteggio_Io = punteggio_Io + 1
  
  print("\nPremi invio per scoprire la mia scelta!")
  input()
  print("Io ho scelto " + arma_gioco)
  print(verdetto)
  print("\nPUNTEGGIO:")
  print(nome + " - Gioco : " + str(punteggio_giocatore) + "-" + str(punteggio_Io))
  print("\nScrivi il comando 'stop' se vuoi smettere di giocare")
  comando = input()

print("GIOCO TERMINATO")
