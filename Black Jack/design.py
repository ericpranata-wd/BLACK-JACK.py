import os
import time
import random
def menu(menu):
   if menu==0:
    return (input(f"""\033[38;2;105;105;105m

\033[38;2;105;105;105m /$$$$$$$     /$$$$$       /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
\033[38;2;105;105;105m| $$__  $$   |__  $$      | $$_____/| $$__  $$| $$_____/| $$__  $$
\033[38;2;105;105;105m| $$  \ $$      | $$      | $$      | $$  \ $$| $$      | $$  \ $$
\033[38;2;105;105;105m| $$$$$$$       | $$      | $$$$$   | $$$$$$$/| $$$$$   | $$  | $$
\033[38;2;105;105;105m| $$__  $$ /$$  | $$      | $$__/   | $$__  $$| $$__/   | $$  | $$
\033[38;2;105;105;105m| $$  \ $$| $$  | $$      | $$      | $$  \ $$| $$      | $$  | $$
\033[38;2;105;105;105m| $$$$$$$/|  $$$$$$/      | $$      | $$  | $$| $$$$$$$$| $$$$$$$/
\033[38;2;105;105;105m|_______/  \______/       |__/      |__/  |__/|________/|_______/ 
                                                                  

                  \033[38;2;105;105;105m█████████████████████████████
                  \033[38;2;105;105;105m██    1. START THE GAME    ██
                  \033[38;2;105;105;105m██    2. Option            ██
                  \033[38;2;105;105;105m██    0. EXIT              ██
                  \033[38;2;105;105;105m█████████████████████████████
\033[37m
"""))
   elif menu==1:
    return (input(f"""\033[3{random.randint(0,7)}m

\033[3{random.randint(1,7)}m /$$$$$$$     /$$$$$       /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
\033[3{random.randint(1,7)}m| $$__  $$   |__  $$      | $$_____/| $$__  $$| $$_____/| $$__  $$
\033[3{random.randint(1,7)}m| $$  \ $$      | $$      | $$      | $$  \ $$| $$      | $$  \ $$
\033[3{random.randint(1,7)}m| $$$$$$$       | $$      | $$$$$   | $$$$$$$/| $$$$$   | $$  | $$
\033[3{random.randint(1,7)}m| $$__  $$ /$$  | $$      | $$__/   | $$__  $$| $$__/   | $$  | $$
\033[3{random.randint(1,7)}m| $$  \ $$| $$  | $$      | $$      | $$  \ $$| $$      | $$  | $$
\033[3{random.randint(1,7)}m| $$$$$$$/|  $$$$$$/      | $$      | $$  | $$| $$$$$$$$| $$$$$$$/
\033[3{random.randint(1,7)}m|_______/  \______/       |__/      |__/  |__/|________/|_______/ 
                                                                  

                  \033[3{random.randint(1,7)}m█████████████████████████████
                  \033[3{random.randint(1,7)}m██    1. START THE GAME    ██
                  \033[3{random.randint(1,7)}m██    2. Option            ██
                  \033[3{random.randint(1,7)}m██    0. EXIT              ██
                  \033[3{random.randint(1,7)}m█████████████████████████████
\033[37m
"""))
def table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard):
   os.system("cls")
   count=0
   for i in (str(bet)):
      count+=1
   if count%2==0:
      lspacebet=count//2
      rspacebet=lspacebet
   else:
      lspacebet=count//2
      rspacebet=lspacebet+1
   count=0
   for i in (str(playerout)):
      count+=1
   if playerout!='🂠 🂠':
      count=count-(1*len(playercard))
   if count%2==0:
      lpospace=count//2
      rpospace=lpospace-1
   else:
      lpospace=count//2
      rpospace=lpospace
   count=0
   for i in (str(dealerout)):
      count+=1
   if dealerupcon==1:
      count=count-(1*(len(dealercard)))
   if count%2==0:
      ldospace=count//2
      rdospace=ldospace-1
   else:
      ldospace=count//2
      rdospace=ldospace
   


   print((f"""\033[40m                                      {outnilaidealer}\033[38;2;124;87;61m

                  \033[48;2;210;180;140m████████████████████████████████\033[40m
                \033[48;2;210;180;140m██\033[30m{' '*(16-ldospace)}{dealerout}{' '*(15-rdospace)}\033[38;2;124;87;61m██\033[40m
              \033[48;2;210;180;140m██                                    ██\033[40m
            \033[48;2;210;180;140m██                                        ██\033[40m
            \033[48;2;210;180;140m██\033[30m{' '*(20-lspacebet)}{bet}{' '*(20-rspacebet)}\033[38;2;124;87;61m██\033[40m
            \033[48;2;210;180;140m██                                        ██\033[40m
              \033[48;2;210;180;140m██                                    ██\033[40m
                \033[48;2;210;180;140m██\033[30m{' '*(16-lpospace)}{playerout}{' '*(15-rpospace)}\033[38;2;124;87;61m██\033[40m
                  \033[48;2;210;180;140m████████████████████████████████\033[40m
                  
                  {nilai_player}                                           {money}
                  {status}"""))
   if dealerupcon==1:
      input('Tekan enter untuk lanjut --->')


def button():
   print("""            \033[38;2;105;105;105m
            \033[48;2;192;192;192m██░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░██\033[40m
            \033[48;2;192;192;192m░░ \033[30m1 Hit\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;192;192m░░\033[30m 2 Stand\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;192;192m░░ \033[30m3 Bet \033[38;2;105;105;105m░░\033[40m
            \033[48;2;192;192;192m██░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░██\033[40m\033[40m
            \033[37m""")

def hit(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard):
   os.system("cls")
   table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
   print("""            \033[38;2;105;105;105m
            \033[48;2;192;20000;192m██░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░██\033[40m
            \033[48;2;192;20000;192m░░ \033[37m1 Hit\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;192;192m░░\033[30m 2 Stand\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;192;192m░░ \033[30m3 Bet \033[38;2;105;105;105m░░\033[40m
            \033[48;2;192;20000;192m██░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░██\033[40m\033[40m
            \033[37m""")
   time.sleep(0.3)
   os.system("cls")
   button()

def stand(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard):
   os.system("cls")
   table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
   print("""            \033[38;2;105;105;105m
            \033[48;2;192;192;192m██░░░░░░░██\033[40m  \033[48;2;192;2000;192m██░░░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░██\033[40m
            \033[48;2;192;192;192m░░ \033[30m1 Hit\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;2000;192m░░\033[37m 2 Stand\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;192;192m░░ \033[30m3 Bet \033[38;2;105;105;105m░░\033[40m
            \033[48;2;192;192;192m██░░░░░░░██\033[40m  \033[48;2;192;2000;192m██░░░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░██\033[40m\033[40m
            \033[37m""")
   time.sleep(0.3)
   os.system("cls")
   button()

def double(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard):
   os.system("cls")
   table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
   print("""            \033[38;2;105;105;105m
            \033[48;2;192;192;192m██░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░░░██\033[40m  \033[48;2;192;2000;192m██░░░░░░░██\033[40m
            \033[48;2;192;192;192m░░ \033[30m1 Hit\033[38;2;105;105;105m ░░\033[40m  \033[48;2;192;192;192m░░\033[30m 2 Stand\033[38;2;105;105;105m ░░\033[40m  \033[48;2;2000;192;192m░░ \033[37m3 Bet \033[38;2;105;105;105m░░\033[40m
            \033[48;2;192;192;192m██░░░░░░░██\033[40m  \033[48;2;192;192;192m██░░░░░░░░░██\033[40m  \033[48;2;192;2000;192m██░░░░░░░██\033[40m\033[40m
            \033[37m""")
   time.sleep(0.3)
   os.system("cls")
   table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
   button()

def loadscreen():
   a=['0','0','o','o',' ',' ','0','0','o','o',' ',' ','0','0','o','o',' ',' ',' ',' ',' ',' ']
   aray=[[],[],[],[],[],[]]
   array=[' ',' ',' ',' ',' ',' ']
   print("\033[48;2;105;105;105m\033[31m")
   for i in (f'       ___        _             ___    ___     ___     ___  0  0       '):
       aray[0].append(i)
   for i in (f'      | _ )    _ | |           | __|  | _ \   | __|   |   \      o     '):
       aray[1].append(i)
   for i in (f'      | _ \   | || |           | _|   |   /   | _|    | |) |      o    '):
       aray[2].append(i)
   for i in ('      |___/   _\__/   _____   _|_|_   |_|_\   |___|   |___/  [O]__ST   '):
       aray[3].append(i)
   for i in ('      |+++++|_|+++++|_|+++++|_|+++++|_|+++++|_|+++++|_|+++++|_|======} '):
       aray[4].append(i)
   for i in ("""\033[31m      `-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"'000--o\ """):
       aray[5].append(i)
   # print(aray)
   count=0
   for j in range(len(aray[0])):
      for k in range(len(array)):
         array[k]=' '
         for l in range(0,-j,-1):
             array[k]=aray[k][l]+array[k]
      for k in array:
         print(k)
      time.sleep(0.1)
      os.system('cls')
      while count>11:
         count=count-12
      if j >= len(aray[0])-3:
         a=[' ',' ','o','o',' ',' ',' ',' ','o','o',' ',' ',' ',' ','o','o',' ',' ',' ',' ',' ',' ']
      if j >= len(aray[0])-2:
         a=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      count+=1
      aray[0][60]=a[count]
      aray[0][63]=a[count+1]
      aray[1][65]=a[count+2]
      aray[2][66]=a[count+3]
   for k in array:
     print(k)
   input('\033[37mTekan enter --->   ')