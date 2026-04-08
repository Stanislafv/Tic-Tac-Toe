import random
import time

win = 0

player_1_1 = "ㅤ"
player_1_2 = "ㅤ"
player_1_3 = "ㅤ"

player_2_1 = "ㅤ"
player_2_2 = "ㅤ"
player_2_3 = "ㅤ"

player_3_1 = "ㅤ"
player_3_2 = "ㅤ"
player_3_3 = "ㅤ"

print("𝙆𝙧𝙚𝙨𝙩𝙞𝙠𝙞 𝙉𝙤𝙡𝙞𝙠𝙞")
time.sleep(1)

print("Поле:")
print("ㅤ1 2 3")
print("1",player_1_1,player_1_2,player_1_3)
print("2",player_2_1,player_2_2,player_2_3)
print("3",player_3_1,player_3_2,player_3_3)

while True:

    try:
        player_input = input("Введите координаты(Сначала цифра вертикали, затем горизонтали, через пробел):")
        player_input_y = int(player_input.split()[0])
        player_input_x = int(player_input.split()[1])
    except:
        print("Вы неправильно ввели координаты")
        continue
    if player_input_x == 1 and player_input_y == 1 and player_1_1 == "ㅤ":
        player_1_1 = "o"
    elif player_input_x == 1 and player_input_y == 1 and player_1_1 != "ㅤ":
        print("Клетка уже занята")
        continue
    elif player_input_x == 2 and player_input_y == 1 and player_1_2 == "ㅤ":
        player_1_2 = "o"
    elif player_input_x == 2 and player_input_y == 1 and player_1_2 != "ㅤ":
        print("Клетка уже занята")
        continue
    elif player_input_x == 3 and player_input_y == 1 and player_1_3 == "ㅤ":
        player_1_3 = "o"
    elif player_input_x == 3 and player_input_y == 1 and player_1_3 != "ㅤ":
        print("Клетка уже занята")
        continue
    
    elif player_input_x == 1 and player_input_y == 2 and player_2_1 == "ㅤ":
        player_2_1 = "o"
    elif player_input_x == 1 and player_input_y == 2 and player_2_1 != "ㅤ":
        print("Клетка уже занята")
        continue
    elif player_input_x == 2 and player_input_y == 2 and player_2_2 == "ㅤ":
        player_2_2 = "o"
    elif player_input_x == 2 and player_input_y == 2 and player_2_2 != "ㅤ":
        print("Клетка уже занята")
        continue
    elif player_input_x == 3 and player_input_y == 2 and player_2_3 == "ㅤ":
        player_2_3 = "o"
    elif player_input_x == 3 and player_input_y == 2 and player_2_3 != "ㅤ":
        print("Клетка уже занята")
        continue

    elif player_input_x == 1 and player_input_y == 3 and player_3_1 == "ㅤ":
        player_3_1 = "o"
    elif player_input_x == 1 and player_input_y == 3 and player_3_1 != "ㅤ":
        print("Клетка уже занята")
        continue
    elif player_input_x == 2 and player_input_y == 3 and player_3_2 == "ㅤ":
        player_3_2 = "o"
    elif player_input_x == 2 and player_input_y == 3 and player_3_2 != "ㅤ":
        print("Клетка уже занята")
        continue
    elif player_input_x == 3 and player_input_y == 3 and player_3_3 == "ㅤ":
        player_3_3 = "o"
    elif player_input_x == 3 and player_input_y == 3 and player_3_3 != "ㅤ":
        print("Клетка уже занята")
        continue

    if player_1_1 == "o" and player_1_2 == "o" and player_1_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_2_1 == "o" and player_2_2 == "o" and player_2_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_3_1 == "o" and player_3_2 == "o" and player_3_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_1 == "o" and player_2_1 == "o" and player_3_1 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_2 == "o" and player_2_2 == "o" and player_3_2 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_3 == "o" and player_2_3 == "o" and player_3_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_1 == "o" and player_2_2 == "o" and player_3_3 == "o":
        print("Вы выйграли!")
        win = 1
    elif player_1_3 == "o" and player_2_2 == "o" and player_3_1 == "o":
        print("Вы выйграли!")
        win = 1

    if player_1_1 != "ㅤ" and player_1_2 != "ㅤ" and player_1_3 != "ㅤ" and player_2_1 != "ㅤ" and player_2_2 != "ㅤ" and player_2_3 != "ㅤ" and player_3_1 != "ㅤ" and player_3_2 != "ㅤ" and player_3_3 != "ㅤ":
        print("Ничья!")
        break


    elif  player_1_1 == "x" and player_1_2 == "x" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_1_1 == "x" and player_1_3 == "x" and player_1_2 == "ㅤ":
        player_1_2 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_1_2 == "x" and player_1_3 == "x" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        print("Вы проиграли!")
        win = 2
    
    elif  player_2_1 == "x" and player_2_2 == "x" and player_2_3 == "ㅤ":
        player_2_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_1 == "x" and player_2_3 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_2_3 == "x" and player_2_1 == "ㅤ":
        player_2_1 = "x"
        print("Вы проиграли!")
        win = 2

    elif  player_3_1 == "x" and player_3_2 == "x" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_3_1 == "x" and player_3_3 == "x" and player_3_2 == "ㅤ":
        player_3_2 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_3_2 == "x" and player_3_3 == "x" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        print("Вы проиграли!")
        win = 2

    
    elif player_1_1 == "x" and player_2_1 == "x" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_1 == "x" and player_3_1 == "x" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_1_1 == "x" and player_3_1 == "x" and player_2_1 == "ㅤ":
        player_2_1 = "x"  
        print("Вы проиграли!")
        win = 2

    elif player_1_2 == "x" and player_2_2 == "x" and player_3_2 == "ㅤ":
        player_3_2 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_3_2 == "x" and player_1_2 == "ㅤ":
        player_1_2 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_1_2 == "x" and player_3_2 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x" 
        print("Вы проиграли!")
        win = 2   

    elif player_1_3 == "x" and player_2_3 == "x" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_3 == "x" and player_3_3 == "x" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_1_3 == "x" and player_3_3 == "x" and player_2_3 == "ㅤ":
        player_2_3 = "x" 
        print("Вы проиграли!")
        win = 2 

    elif player_1_1 == "x" and player_2_2 == "x" and player_3_3 == "ㅤ":
        player_3_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_3_3 == "x" and player_1_1 == "ㅤ":
        player_1_1 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_3_3 == "x" and player_1_1 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        print("Вы проиграли!")
        win = 2

    elif player_1_3 == "x" and player_2_2 == "x" and player_3_1 == "ㅤ":
        player_3_1 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_2_2 == "x" and player_3_1 == "x" and player_1_3 == "ㅤ":
        player_1_3 = "x"
        print("Вы проиграли!")
        win = 2
    elif player_3_1 == "x" and player_1_3 == "x" and player_2_2 == "ㅤ":
        player_2_2 = "x"
        print("Вы проиграли!")
        win = 2

    

    if  player_1_1 == "o" and player_1_2 == "o" and player_1_3 == "ㅤ":
        player_1_3 = "x"
    elif player_1_1 == "o" and player_1_3 == "o" and player_1_2 == "ㅤ":
        player_1_2 = "x"
    elif player_1_2 == "o" and player_1_3 == "o" and player_1_1 == "ㅤ":
        player_1_1 = "x"
    
    elif  player_2_1 == "o" and player_2_2 == "o" and player_2_3 == "ㅤ":
        player_2_3 = "x"
    elif player_2_1 == "o" and player_2_3 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"
    elif player_2_2 == "o" and player_2_3 == "o" and player_2_1 == "ㅤ":
        player_2_1 = "x"

    elif  player_3_1 == "o" and player_3_2 == "o" and player_3_3 == "ㅤ":
        player_3_3 = "x"
    elif player_3_1 == "o" and player_3_3 == "o" and player_3_2 == "ㅤ":
        player_3_2 = "x"
    elif player_3_2 == "o" and player_3_3 == "o" and player_3_1 == "ㅤ":
        player_3_1 = "x"

    
    elif player_1_1 == "o" and player_2_1 == "o" and player_3_1 == "ㅤ":
        player_3_1 = "x"
    elif player_2_1 == "o" and player_3_1 == "o" and player_1_1 == "ㅤ":
        player_1_1 = "x"
    elif player_1_1 == "o" and player_3_1 == "o" and player_2_1 == "ㅤ":
        player_2_1 = "x"    

    elif player_1_2 == "o" and player_2_2 == "o" and player_3_2 == "ㅤ":
        player_3_2 = "x"
    elif player_2_2 == "o" and player_3_2 == "o" and player_1_2 == "ㅤ":
        player_1_2 = "x"
    elif player_1_2 == "o" and player_3_2 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"    

    elif player_1_3 == "o" and player_2_3 == "o" and player_3_3 == "ㅤ":
        player_3_3 = "x"
    elif player_2_3 == "o" and player_3_3 == "o" and player_1_3 == "ㅤ":
        player_1_3 = "x"
    elif player_1_3 == "o" and player_3_3 == "o" and player_2_3 == "ㅤ":
        player_2_3 = "x"  

    elif player_1_1 == "o" and player_2_2 == "o" and player_3_3 == "ㅤ":
        player_3_3 = "x"
    elif player_2_2 == "o" and player_3_3 == "o" and player_1_1 == "ㅤ":
        player_1_1 = "x"
    elif player_3_3 == "o" and player_1_1 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"

    elif player_1_3 == "o" and player_2_2 == "o" and player_3_1 == "ㅤ":
        player_3_1 = "x"
    elif player_2_2 == "o" and player_3_1 == "o" and player_1_3 == "ㅤ":
        player_1_3 = "x"
    elif player_3_1 == "o" and player_1_3 == "o" and player_2_2 == "ㅤ":
        player_2_2 = "x"

    elif player_2_2 == "ㅤ":
        player_2_2 = "x"
    elif player_2_2 != "ㅤ":
        while win == 0:
            rand = random.randint(1,8)
            if rand == 1 and player_1_1 == "ㅤ":
                player_1_1 = "x"
                break
            if rand == 2 and player_1_2 == "ㅤ":
                player_1_2 = "x"
                break
            if rand == 3 and player_1_3 == "ㅤ":
                player_1_3 = "x"
                break
            if rand == 4 and player_2_1 == "ㅤ":
                player_2_1 = "x"   
                break
            if rand == 5 and player_2_3 == "ㅤ":
                player_2_3 = "x" 
                break
            if rand == 6 and player_3_1 == "ㅤ":
                player_3_1 = "x" 
                break
            if rand == 7 and player_3_2 == "ㅤ":
                player_3_2 = "x" 
                break
            if rand == 8 and player_3_3 == "ㅤ":
                player_3_3 = "x"  
                break   
            else:
                continue
            

    print("ㅤ1 2 3")
    print("1",player_1_1,player_1_2,player_1_3)
    print("2",player_2_1,player_2_2,player_2_3)
    print("3",player_3_1,player_3_2,player_3_3)

    if win == 1:
        print("Вы выйграли!")
        break
    elif win == 2:
        print("Вы проиграли!")
        break