print("\n🏴‍☠️ Welcome to the Treasure Hunt Challenge! 🏝️")
print("Solve riddles, avoid traps, and find the treasure!")
print("You have 3 lives. Choose wisely.\n")

lives = 3
step = 1

while step == 1 and lives > 0:
    print("""
       __________
       |  __  __  |
       | |  ||  | |
       | |  ||  | |
       | |__||__| |
       |  __  __()|
       | |  ||  | |
       | |  ||  | |
       | |  ||  | |
       | |  ||  | |
       | |__||__| |
       |__________|
    """)
    print("Step 1: You stand before four mysterious paths.")
    print("Riddle: 'I'm always in front of you, yet can’t be seen. You feel me on your skin but never hold me.'")
    print("Choose your path:")
    print("1. Path of Fire")
    print("2. Path of Wind")
    print("3. Path of Ice")
    print("4. Path of Rocks")
    choice = input("Enter 1, 2, 3, or 4: ").strip()
    if choice == '2':
        print("Correct! The answer is 'wind'. You move forward.\n")
        step = 2
    else:
        lives -= 1
        print("🚨 Trap! You triggered a net trap. Lives left:", lives)
        if lives > 0:
            print("Hint: Which path feels cool on your face?\n")

while step == 2 and lives > 0:
    print("""
     ✨✨✨ GLOWING HALLWAY ✨✨✨
     --------------------------
     |                        |
     |   *     *     *       |
     |   *     *     *       |
     |   *     *     *       |
     |________________________|
    """)
    print("Step 2: You reach a glowing hallway.")
    print("Riddle: 'I appear when light hits you, I mimic your moves but never speak. What am I?'")
    print("Choose your path:")
    print("1. Tunnel of Echoes")
    print("2. Tunnel of Light")
    print("3. Tunnel of Shadows")
    print("4. Tunnel of Mirrors")
    choice = input("Enter 1, 2, 3, or 4: ").strip()
    if choice == '3':
        print("Exactly! It's your shadow — cast to the west by the setting sun. Proceed...\n")
        step = 3
    else:
        lives -= 1
        print("💥 Arrows shoot from the walls! Lives left:", lives)
        if lives > 0:
            print("Hint: It's always behind you when the sun shines.")

while step == 3 and lives > 0:
    print("""  
      ccee88oo
  C8O8O8Q8PoOb o8oo
 dOB69QO8PdUOpugoO9bD
CgggbU8OU qOp qOdoUOdcb
    6OuU  /p u gcoUodpP
      \\\//  /douUP
        \\\////
         |||//
         |||\/
         |||||
   .....//||||\....
    """)
    print("Step 3: You face an ancient tree at the center of a spiral.")
    print("Riddle: 'I feed the world yet stay buried. Dig for my heart if you wish to be carried.'")
    print("Choose your dig spot:")
    print("1. Dig near the branches")
    print("2. Dig on the trunk")
    print("3. Dig around the roots")
    print("4. Dig near the leaves")
    choice = input("Enter 1, 2, 3, or 4: ").strip()
    if choice == '3':
        print("\n🎉 You dig at the tree's base and uncover the hidden treasure! 🎉")
        print("Congratulations, brave adventurer. The riches are yours!")
        print("""           
                         ___
                     ,-'"   "`-.
                   ,'_          `.  
                  / / \  ,-       \ 
             __   | \_0 ---        |
            /  |  |                |
            \  \  `--.______,-/    |
          ___)  \  ,--""    ,/     |
         /    _  \ \-_____,-      / 
         \__-/ \  | `.          ,'  
           \___/ <    `--------'    
            \__/\ |               
             \__//2
        """)
        exit()

    else:
        lives -= 1
        print("⚠️ Poisonous vines lash at you! Lives left:", lives)
        if lives > 0:
            print("Hint: Trees drink water through this part.\n")

if lives == 0:
    print("\n💀 You have lost all your lives. The treasure remains hidden.")
    print("Better luck next time, brave soul.")
print("""                                                             
 __     ______  _    _   _      ____   _____ ______ 
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
    | | | |__| | |__| | | |___| |__| |____) | |____ 
    |_|  \____/ \____/  |______\____/|_____/|______|

 """)
