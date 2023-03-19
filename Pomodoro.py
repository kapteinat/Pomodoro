import time
import playsound #biblioteca importada exlusivamente para o alarme
import os




#converter o tempo para minutos
def conversor(t):
    return t*60


#faz o minuto chegar a 0 
def contador(t,x):
    while t:
        min, sec = divmod(t,60)
        print(f"\033[1;31m{x}: {min:02d}:{sec:02d}", end="\r\033[m")
        time.sleep(1) 
        t -=1
        
        
#funçao principal do codigo
def pomodoro(estudo, descanso):  #usa como parametro as variaveis estudo e descanso
    estd = conversor(estudo)
    desc = conversor(descanso)
    contador(estd,"Estudo")
    playsound.playsound('alarme.mp3') #toca o mp3 do alarme
    print('\033[32mHora de descansar!\033[m')
    contador(desc,"Descanso")
    playsound.playsound("alarme.mp3")





pausar = 0
quantidade = 0
tempopausa = 10

def pausa(pausar):  #Funçao para perguntar ao usuario se quer uma pausa de 10 min após 4 pomodoros
    if pausar % 4 == 0:
        os.system("clear")
        print(f"\033[35mVocê ja realizou 4 ou mais pomodoros em sequencia sem pausa!")
        pause = str(input("Que tal um descanso de 10 minutos? (s/n)\033[m")).lower()
        if pause == "s":
            tpp = conversor(tempopausa)
            contador (tpp, "Pausa")
            playsound.playsound("alarme.mp3")
        else:
            return 0
    else:
        return 0
        

#criando as variaveis
os.system("clear")
estudo = int(input("\033[;32mTempo para estudo(min): " ))
descanso = int(input("Tempo para descanso(min):\033[m "))
os.system("clear")


#========MAIN==========


while True:
    quantidade +=1
    pausar +=1
    print(f"\033[32mEsse é seu pomodoro de número {quantidade}\033[m")
    pomodoro(estudo, descanso)
    pausa(pausar)
    restart = str(input("\033[32mVoltar a estudar? (s/n)\033[m")).lower()
    if restart == "s":
        os.system("clear")
        pass
    else:
        os.system("clear")
        break

print("==================================================================")
print(f"\033[1;32mParabéns, você realizou {quantidade} pomodoros !!\033[m")
print("==================================================================")





