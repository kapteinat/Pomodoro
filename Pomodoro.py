import time
import playsound #biblioteca importada exlusivamente para o alarme




#converter o tempo para minutos
def conversor(t):
    return t 


#faz o minuto chegar a 0 
def contador(t,x):
    while t:
        min, sec = divmod(t,60)
        print(f"{x}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1) 
        t -=1
        
        
#funçao principal do codigo
def pomodoro(estudo, descanso):  #usa como parametro as variaveis estudo e descanso criadas logo abaixo
    pausar = 0
    estd = conversor(estudo)
    desc = conversor(descanso)
    contador(estd,"estudo")
    playsound.playsound('alarme.mp3') #toca o mp3 do alarme
    print('Hora de descansar!')
    contador(desc,"descanso")
    playsound.playsound("alarme.mp3")



#criando as variaveis
estudo = int(input("Tempo para estudo(min): " ))
descanso = int(input("Tempo para descanso(min): "))

pausar = 0
quantidade = 0
tempopausa = 1

def pausa(pausar):  #Funçao para perguntar ao usuario se quer uma pausa de 10 min após 4 pomodoros
    if pausar % 4 == 0:
        print(f"Você ja realizou 4 ou mais pomodoros em sequencia sem pausa!")
        pause = str(input("Que tal um descanso de 10 minutos? (s/n)")).lower()
        if pause == "s":
            tpp = conversor(tempopausa)
            contador (tpp, "Pausa")
            playsound.playsound("alarme.mp3")
        else:
            return 0
    else:
        return 0
        



while True:
    quantidade +=1
    pausar +=1
    print(f"Esse é seu pomodoro de número {quantidade}")
    pomodoro(estudo, descanso)
    pausa(pausar)
    restart = str(input("Voltar a estudar? (s/n)")).lower()
    if restart == "s":
        pass
    else:
        break

print(f"Parabéns, você realizou {quantidade} pomodoros !!")

