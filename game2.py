# This is a simple command-line adventure game
# Written in Python 2.7
# Don't Use this -- here for reference only
# Copyright 2012 Robert Greener
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
def part1():
    print "You enter a colourful room with two doors. Do you go through the door to the east or door to the west?"
    
    part1 = raw_input("> ")
    
    if part1 == "e":
        part2()
    elif part1 == "w":
        part3()
    elif part1 == "exit":
        exit()
    elif part1 == "save":
        print "41338"
        part1_restart()
    else:
        print "Doing %s was pointless. Try Again" % part1
        part1_restart()

def part2():
    print "There's a massive shark eating cheese cake"
    print "There are doors to the east and west"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    part2 = raw_input("> ")
        
    if part2 == "1":
        print "The shark eats your face off. Good job!"
    elif part2 == "2":
        print "The shark eats your legs off. Good job!"
    elif part2 == "w":
        part1()
    elif part2 == "e":
        part4()
    elif part2 == "exit":
        exit()
    elif part2 == "save":
        print "82866"
        part2_restart()
    else:
        print "Well, doing %s is pointless. Try Again." % part2
        part2_restart()

def part3():
    print "You stare into your own mind"
    print "1. Cake."
    print "2. Skinny Jeans and Mustard."
    print "3. Eating Soup of of Cellophane."
    print "The only door is to the east"
    
    part3 = raw_input("> ")
    
    if part3 == "1" or part3 == "2":
        print "Your body survives powered by a mind of pure jelly."
        part3_restart()
    elif part3 == "e":
        part1()
    elif part3 == "3":
        print "Your Crazy"
        part3_restart()
    elif part3 == "exit":
        exit()
    elif part3 == "save":
        print "24924"
        part3_restart()
    else:
        print "Doing %s is pointless. Try Again" % part3
        part3_restart()

def part4():
    print "You are in a corridor nothing of intrest appears to be here."
    print "Doors lead east and west"
    
    part4 = raw_input("> ")
    
    if part4 == "e":
        part5()
    elif part4 == "w":
        part2()
    elif part4 == "exit":
        exit()
    elif part4 == "save":
        print "69134"
        part4_restart()
    else:
        print "What does %s mean. Try Again" % part4
        part4_restart

def part5():
    print "You are in the TV room"
    print "Doors lead north, east, south and west"
    print "There is also a TV"
    print "Type 1 to inspect the tv"
    
    part5 = raw_input("> ")
    
    if part5 == "n":
        part6()
    elif part5 == "e":
        part8()
    elif part5 == "s":
        part7()
    elif part5 == "w":
        part4()
    elif part5 == "1":
        part5_ex()
    elif part5 == "exit":
        exit()
    elif part5 == "save":
        print "70965"
        part5_restart()
    else:
        print "What does %s mean. Try Again" % part5
        part5_restart()
        
def part5_ex():
    tv = raw_input("Would you like to watch the TV? (y for yes, n for no) > ")
    
    if tv == "y" or tv == "yes":
        print "The news is on. Nothing interesting has happened..."
        part5()
    elif tv == "n" or tv == "no":
        print "Okay."
        part5()
    elif tv == "exit":
        exit()
    elif tv == "save":
        print "84621"
        part5_ex_restart()
    else:
        print "What does %s mean. Try Again" % tv
        part5_ex_restart()

def part6():
    print "You are in a corridor nothing of intrest appears to be here."
    print "Doors lead north and south"
    
    part6 = raw_input("> ")
    
    if part6 == "n":
        not_ready()
    elif part6 == "s":
        part5()
    elif part6 == "exit":
        exit()
    elif part6 == "save":
        print "10168"
        part6_restart()
    else:
        print "What does %s mean. Try Again" % part6
        part6_restart()

def part7():
    print "You are in a corridor nothing of intrest appears to be here."
    print "Doors lead north and south"
    
    part7 = raw_input("> ")
    
    if part7 == "n":
        part5()
    elif part7 == "s":
        not_ready()
    elif part7 == "exit":
        exit()
    elif part7 == "save":
        print "62961"
        part7_restart()
    else:
        print "What does %s mean. Try Again" % part7
        part7_restart()

def part8():
    print "You are in a corridor nothing of intrest appears to be here."
    print "Doors lead east and west"
    
    part8 = raw_input("> ")
    
    if part8 == "e":
        part9()
    elif part8 == "w":
        part5()
    elif part8 == "exit":
        exit()
    elif part8 == "save":
        print "72052"
        part8_restart()
    else:
        print "What does %s mean. Try Again" % part8
        part8_restart()

def part9():
    print "You are in a room full of computers."
    print "Doors lead west and north"
    print "Type 1 to login to the computer"
    
    part9 = raw_input("> ")
    
    if part9 == "w":
        part8()
    elif part9 == "n":
        print "The door is locked try looking at the computer."
        part9()
    elif part9 == "1":
        part9_ex()
    elif part9 == "exit":
        exit()
    elif part9 == "save":
        print "34535"
        part9_restart()
    else:
        print "What does %s mean. Try Again" % part9
        part9_restart()

def part9_ex():
    print "0010010100101110110100110"
    print "Welcome to the computer."
    print "Please enter the code given at the beggining of the game."
    print "If you do not know this code, or you wish to leave the computer type leave at the prompt."
    print "If you do not know it you cannot win the game."
    
    part9_ex = raw_input("> ")
    
    if part9_ex == "uuddlrlrba":
        print "Congratulations, You got it right you have been transported past the locked door."
        part10()
    elif part9_ex == "exit":
        exit()
    elif part9_ex == "leave":
        part9()
    elif part9_ex == "save":
        print "48891"
        part9_ex_restart()
    else:
        print "Wrong. Try Again"
        part9_ex_restart()

def part10():
    print "Welcome to the futuristic room"
    print "Portals lead north, east and west."
    print "There is also a teleport to the south with a note attached"
    print "Type 1 to read the note"
    print "Type 2 to go through the teleport"
    
    part10 = raw_input("> ")
    
    if part10 == "n":
        part13()
    elif part10 == "e":
        part12()
    elif part10 == "w":
        print "Enter the Platinum Code"
        platinum = raw_input("> ")
        if platinum == "penguins":
            part11()
        else:
            part10_restart()
    elif part10 == "1":
        print "The note reads: You will need to type in the code given at the beggining of the game to go through the teleport"
        part10_restart()
    elif part10 == "2":
        print "Enter the Code"
        code24 = raw_input("> ")
        
        if code24 == "uuddlrlrba":
            part9()
        elif code24 == "exit":
            exit()
    elif part10 == "save":
        print "31015"
        part_10_restart
    elif part10 == "exit":
        exit()
    else:
        print "What does %s mean? Try Again" % part10
        part10_restart()

def part11():
    print "Welcome to the Platinum Room."
    print "Congratulations, You've Won."
    print "Type RETURN to leave."
    theend = raw_input("> ")
    if not(theend == "zabbyydfdf"):
        exit()

def part12():
    print "You are in a walk-in-wardrobe"
    print "The only door is to the west"
    print "There is a note on the floor, type 1 to read it"
    part12 = raw_input("> ")
    if part12 == "1":
        print "This is the first half of the bronze code: li"
        part12_restart()
    elif part12 == "w":
        part10()
    elif part12 == "save":
        print "82608"
        part12_restart()
    elif part12 == "exit":
        exit()
    else:
        print "I Don't Understand"
        part12_restart()

def part13():
    print "You're in a corridor with doors leading north and south"
    part13 = raw_input("> ")
    if part13 == "n":
        part14()
    elif part13 == "s":
        part10()
    elif part13 == "exit":
        exit()
    elif part13 == "save":
        print "51008"
        part13_restart()
    else:
        print "I'm sorry but I can't understand a word of what you're saying"

def part14():
    print "You're at the beggining of a very long corridor"
    print "There is a door to the south"
    print "You could also go east along the corridor"
    part14 = raw_input("> ")
    if part14 == "s":
        part13()
    elif part14 == "e":
        part15()
    elif part14 == "exit":
        exit()
    elif part14 == "save":
        print "80251"
        part14_restart()
    else:
        "What does %s mean." % part14
        part14_restart()

def part15():
    print "You are in the middle of the long corridor"
    print "There is a door towards the north."
    print "And you can go either east or west along the corridor"
    part15 = raw_input("> ")
    if part15 == "w":
        part14()
    elif part15 == "n":
        part16()
    elif part15 == "e":
        part17()
    elif part15 == "exit":
        exit()
    elif part15 == "save":
        print "83404"
        part15_restart()
    else:
        print "I Don't Understand."
        part15_restart()

def part16():
    print "You are in the room of multiplication\nThere is only one door leading to the south\nThere is also a man type 1 to speak to him"
    part16 = raw_input("> ")
    if part16 == "s":
        part15()
    elif part16 == "1":
        print "Hello, I have the first half of the copper code\nDo You Want it?\ny for yes, n for no"
        copper2 = raw_input("> ")
        if copper2 == "y":
            print "Okay Solve 127 X 4 and I will give it to you"
            q12 = raw_input("> ")
            if q12 == "508":
                print "Well Done\nThe first half of the copper code is: mo"
                part16_restart()
            elif q12 == "exit":
                exit()
            elif q12 == "save":
                print "21033"
                part16_restart()
            else:
                print "Wrong"
                part16_restart()
                
        elif copper2 == "exit":
            exit()
        elif copper2 == "save":
            print "21033"
        else:
            print "Okay Suit Yourself"
            part16_restart()
    elif part16 == "save":
        print "21033"
    elif part16 == "exit":
        exit()
    else:
        print "What?"
        part16_restart()

def part17():
    print "You are in the middle of the long corridor"
    print "There is a door towards the north."
    print "And you can go either east or west along the corridor"
    part17 = raw_input("> ")
    if part17 == "w":
        part15()
    elif part17 == "n":
        part18()
    elif part17 == "e":
        part19()
    elif part17 == "exit":
        exit()
    elif part17 == "save":
        print "13017"
        part17_restart()
    else:
        print "I Don't Understand."
        part17_restart()

def part18():
    print "You are in the room of copper\nThere is only one door leading to the south\nThere is also a man type 1 to speak to him"
    part18 = raw_input("> ")
    if part18 == "s":
        part17()
    elif part18 == "1":
        print "Hello, I have the second half of the bronze code\nDo You Want it?\ny for yes, n for no"
        bronze2 = raw_input("> ")
        if bronze2 == "y":
            print "Tell me the copper code and I will give it to you"
            q14 = raw_input("> ")
            if q14 == "mouse":
                print "Well Done\nThe second half of the bronze code is: on"
                part18_restart()
            elif q14 == "exit":
                exit()
            elif q14 == "save":
                print "21033"
                part18_restart()
            else:
                print "Wrong"
                part18_restart()
                
        elif bronze2 == "exit":
            exit()
        elif bronze2 == "save":
            print "97328"
        else:
            print "Okay. Fine."
            part18_restart()
    elif part18 == "save":
        print "97328"
    elif part18 == "exit":
        exit()
    else:
        print "What?"
        part18_restart()

def part19():
    print "You are at the end of the long corridor\nThere is a door to the south\nOr you can go west down the corridor."
    part19 = raw_input("> ")
    if part19 == "w":
        part17()
    elif part19 == "s":
        part20()
    elif part19 == "exit":
        exit()
    elif part19 == "save":
        print "73862"
        part19_restart()
    else:
        print "What does that mean ..."
        part19_restart()

def part20():
    print "You are in a dining room\nThere is lots of food on the table\nType 1 to eat it\nDoors lead north, south and west"
    part20 = raw_input("> ")
    if part20 == "n":
        part19()
    elif part20 == "w":
        part21()
    elif part20 == "s":
        part23()
    elif part20 == "1":
        print "You got food poisoning and died"
        exit()
    elif part20 == "exit":
        exit()
    elif part20 == "save":
        print "22439"
        part20_restart()
    else:
        print "I don't understand what %s means." % part20
        part20_restart()

def part21():
    print "You are in a room with nothing but a sign on the wall\nIt reads to the west is the puzzle room\nAnd to the east is the dining room"
    part21 = raw_input("> ")
    if part21 == "e":
        part20()
    elif part21 == "w":
        part22()
    elif part21 == "exit":
        exit()
    elif part21 == "save":
        print "59584"
        part20_restart()
    else:
        print "Huh?"
        part20_restart()

def part22():
    print "Welcome to the puzzle room\nDoors Lead to the west\nSolve this puzzle and I will give you the second half of the copper code"
    print "Using the numbers 2, 4, 6 and 8, the\nmultiply sign, the add sign and the equals\nsign, what is the largest number you can\nmake?\nYou may press each digit and sign only once,\nbut you don't have to press all the signs"
    part22 = raw_input("> ")
    if part22 == "5248" or part22 == "8642":
        print "Well Done,\nThe second half of the copper code is: use"
        part22_restart()
    elif part22 == "74684164":
        print ":O *AMAZING* for that answer I will give you the platinum code\nThe code is: penguin"
        part22_restart()
    elif part22 == "exit":
        exit()
    elif part22 == "save":
        print "25934"
        part22_restart()
    else:
        print "What?"
        part22_restart()
    

def part1_restart():
    part1()

def part2_restart():
    part2()

def part3_restart():
    part3()

def part4_restart():
    part4()

def part5_restart():
    part5()

def part5_ex_restart():
    part5_ex()

def part6_restart():
    part6()

def part7_restart():
    part7()

def part8_restart():
    part8()

def part9_restart():
    part9()

def part9_ex_restart():
    part9_ex()

def part10_restart():
    part10()

def part11_restart():
    part11()

def part12_restart():
    part12()

def part13_restart():
    part13()

def part14_restart():
    part14()

def part15_restart():
    part15()

def part16_restart():
    part16()

def part17_restart():
    part17()

def part18_restart():
    part18()

def part19_restart():
    part19()

def part20_restart():
    part20()

def part21_restart():
    part21()

def part22_restart():
    part22()

def exit():
    print "Goodbye."

def not_ready():
    print "This Feature Has Not Yet Been Implemented. Sorry"

def load():
    print """
    CHARLIE'S ADVENTURE
    This is a short adventure game created by Robert Greener.
    in this game n is north e is east s is south and w is west.
    You can exit by typing exit at the prompt.
    Remember uuddlrlrba it will be needed during the game.
    To find out a save code type save at the prompt.
    The aim of the game is to get to the sacred Platinum Room
    and retrieve the treasure.
    
    -----------------------------------------------------------
    """
    part1()

def load_restart():
    load()

def savecodes():
    print "Enter your 5 digit save code now."
    
    code = raw_input("> ")
    
    if code == "41338":
        part1()
    elif code == "82866":
        part2()
    elif code == "24924":
        part3()
    elif code == "69134":
        part4()
    elif code == "70965":
        part5()
    elif code == "84621":
        part5_ex()
    elif code == "10168":
        part6()
    elif code == "62961":
        part7()
    elif code == "72052":
        part8()
    elif code == "34535":
        part9()
    elif code == "48891":
        part9_ex()
    elif code == "31015":
        part10()
    elif code == "39937":
        part11()
    elif code == "82608":
        part12()
    elif code == "51008":
        part13()
    elif code == "80251":
        part14()
    elif code == "83404":
        part15()
    elif code == "21033":
        part16()
    elif code == "13017":
        part17()
    elif code == "97328":
        part18()
    elif code == "73862":
        part19()
    elif code == "22439":
        part20()
    elif code == "59584":
        part21()
    elif code == "25934":
        part22()
    else:
        print "Wrong"
        savecodes_restart()

def savecodes_restart():
    savecodes()

print "Do you have a save code? y for yes n for no"

q26 = raw_input("> ")

if q26 == "y" or q26 == "yes":
    savecodes()

elif q26 == "n" or q26 == "no":
    load()

elif q26 == "exit":
    exit()
else:
    print "ERROR - YOU BROKE IT ANSWER YES OR NO NEXT TIME"
