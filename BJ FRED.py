import random
import design

# design.loadscreen()

money=1000
nilai_player=0
status='?'
game=1
space=0
nilaiupcon=0
menu=0
playercard=[]
dealercard=[]
def dealertake(x,countdealer,dealerout,dealerup,nilai_dealer,acedealer,dealerupcon):
  for i in range(x):
    cardtemp=[]
    while True:
      randangka=random.randint(2,14)-2
      randgambar=random.randint(0,3)
      if kartu[randgambar][randangka]!=None:
        test=randangka+2
        if test<=10:
          num=str(test)
          value=randangka+2
        else:
          num=nonnum[randangka-9]
          value=10
        if num=='A':
          acedealer=acedealer+1
          value=11
        countdealer=countdealer+1
        dealerout='🂠 '*countdealer
        outnilaidealer='?'
        dealerup=dealerup+kartu[randgambar][randangka]+img[randgambar]+" "+(num)+" "
        cardtemp.append(randgambar)
        cardtemp.append(randangka)
        nilai_dealer=nilai_dealer+value
        while nilai_dealer>21:
          if acedealer>0:
            nilai_dealer+=-10
            acedealer+=-1
          else:
            dealerturn=0
            break
        if randangka+2 == 14:
          acedealer=acedealer+1
        dealercard.append(cardtemp)
        if len(dealercard)>=5 and nilai_dealer<=21:
          dealerturn=0
          nilai_dealer=21
        kartu[randgambar][randangka]=None
        if dealerupcon==1:
          dealerout=dealerup
          outnilaidealer=nilai_dealer
        break
  return [dealerout,nilai_dealer,countdealer,dealerup,acedealer,outnilaidealer,kartu]


def playertake(x,playerout,nilai_player,ace):
  for i in range (x):
    cardtemp=[]
    while True:
      randangka=random.randint(2,14)-2
      randgambar=random.randint(0,3)
      if kartu[randgambar][randangka]!=None:
        test=randangka+2
        if test<=10:
          num=str(test)
          value=randangka+2
        else:
          num=nonnum[randangka-9]
          value=10
        if num=='A':
          ace=ace+1
          value=11
        playerout=playerout+kartu[randgambar][randangka]+img[randgambar]+" "+(num)+" "
        cardtemp.append(randgambar)
        cardtemp.append(randangka)
        nilai_player=nilai_player+value
        bust=0
        status=''
        while nilai_player>21:
          if ace>0:
            nilai_player+=-10
            ace+=-1
          else:
            bust=1
            status='bust'
            break
        if nilai_player==21:
          status='BLACK JACK'
        playercard.append(cardtemp)
        if len(playercard)>=5 and nilai_player<=21:
          bust=1
          nilai_player=21
          status="5 card"
        kartu[randgambar][randangka]=None
        break
  return [playerout,nilai_player,ace,bust,status,kartu]

while game==1:
  if money<=0:
          turn=0
          start=0
          print("BANKRUPT")
          print()
          input('Tekan enter untuk exit --->  ')
          break
  start=(design.menu(menu))
  if start=='0':
    game=0
  elif start =='2':
    menu=input("""    MENU WARNA

    0. DEFAULT
    1. WARNA WARNI
    
    Masukan pilihan : """)
    try:
      menu=int(menu)
    except ValueError:
      pass
  while start=='1':
    if money<=0:
      break
    nilai_player='?'
    nilai_dealer='?'
    countdealer=0
    dealerupcon=0
    outnilaidealer='?'
    dealerup=''
    ace=0
    dealerout='🂠 🂠'
    playerout='🂠 🂠'
    acedealer=0
    bet=0
    design.table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
    bet = 'f'
    while bet=='f':
      bet = (input("Bet : "))
      try:
        bet=int(bet)
      except ValueError:
        bet='f'
    if bet>money:
      bet=money
    if bet<=0:
      break
    else:
      money=money-bet
      turn=1
      nilai_player = 0
      nilai_dealer = 0
      playerout=''
      dealerout=''
      diamond = [ '🃂', '🃃', '🃄', '🃅' ,'🃆',' 🃇', '🃈' ,'🃉' ,'🃊' ,'🃋' ,'🃍', '🃎','🃁' ]
      club = ['🃒', '🃓' ,'🃔' ,'🃕', '🃖' ,'🃗', '🃘' ,'🃙' ,'🃚' ,'🃛' ,'🃝', '🃞','🃑']
      heart = ["🂲", "🂳" ,"🂴" ,"🂵" ,"🂶" ,"🂷" ,"🂸" ,"🂹" ,"🂺" ,"🂻" ,"🂽" ,"🂾","🂱"]
      spade = ['🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮','🂡']
      img=['♦️','♠️','♥️','♣️']
      nonnum=['J','Q','K','A']
      button=1
      dealercard=[]
      playercard=[]
      kartu=[diamond,spade,heart,club]
      ret=playertake(2,playerout,nilai_player,ace)
      playerout=ret[0]
      nilai_player=ret[1]
      ace=ret[2]
      bust=ret[3]
      status=ret[4]
      ret=dealertake(2,countdealer,dealerout,dealerup,nilai_dealer,acedealer,dealerupcon)
      dealerout=ret[0]
      nilai_dealer=ret[1]
      countdealer=ret[2]
      dealerup=ret[3]
      acedealer=ret[4]
      outnilaidealer=ret[5]
      design.table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
      while turn!=0: #player turn
        if bust==1:
          turn=0
          print('BUSTED')
          break
        if button==1:
          design.button()
        pilihan=input("Pilih 1/2/3: ")
        if pilihan=="1":
          button=1
          design.hit(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
          ret=playertake(1,playerout,nilai_player,ace)
          playerout=ret[0]
          nilai_player=ret[1]
          ace=ret[2]
          bust=ret[3]
          status=ret[4]
          design.table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
        elif pilihan=="2":
          button=1
          design.stand(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
          # stand
          break
        elif pilihan=="3":
          button=1
          design.double(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
          # bet
          pilihan = int(input("Berapa Anda ingin bet : "))
          if pilihan<=0:
            continue
          if pilihan>money:
            print('SADAR DIRI WOI!')
          else:
            bet=pilihan+bet
            money=money-pilihan
            ret=playertake(1,playerout,nilai_player,ace)
            playerout=ret[0]
            nilai_player=ret[1]
            ace=ret[2]
            bust=ret[3]
            status=ret[4]
            design.table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
        else:
          button=0
      
      dealerturn=1
      dealerupcon=1
      dealerout=dealerup
      outnilaidealer=nilai_dealer
      design.table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
        # dealer's turn
      while dealerturn!=0:
        if nilai_dealer<21:
          while nilai_dealer<21:
            ret=dealertake(1,countdealer,dealerout,dealerup,nilai_dealer,acedealer,dealerupcon)
            dealerout=ret[0]
            nilai_dealer=ret[1]
            countdealer=ret[2]
            dealerup=ret[3]
            acedealer=ret[4]
            outnilaidealer=ret[5]
            design.table(outnilaidealer,dealerout,bet,playerout,nilai_player,money,status,dealerupcon,playercard,dealercard)
          dealerturn=0
        else:
          dealerturn=0
      if nilai_player>21:
        nilai_player=0
      if nilai_dealer>21:
        nilai_dealer=0
      if nilai_player>nilai_dealer:
        print("You win!")
        bet=bet*2
        money=money+bet
      elif nilai_player==nilai_dealer:
        print("tie!")
        money=money+bet
      else:
        print("RUNGKAD!")
      bet=0