import time
import playsound #biblioteca importada exlusivamente para o alarme




#converter o tempo para minutos
def conversor(t):
    return t * 60


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



#def restart():
 #   restart = str(input("Voltar a estudar? (s/n)")).lower()
  #  if restart == "s":
  #      pomodoro(estudo,descanso)
   # else:
   #     break

 


#criando as variaveis
estudo = int(input("Tempo para estudo(min): " ))
descanso = int(input("Tempo para descanso(min): "))

pausar = 0
quantidade = 0


while True:
    quantidade +=1
    pomodoro(estudo, descanso)
    restart = str(input("Voltar a estudar? (s/n)")).lower()
    if restart == "s":
        pass
    else:
        break
    

