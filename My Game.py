#for chance moments aka auto CPs
import random as rand

z = 0 # count of number of gameplays

#the restart function

    
restart() #needs to be run before anything

#throughout the code the different "choice points" are denoted by CPn and in different while loops of n eg n1 n2 ect. 

#Teaching the user
input ("Hello, thanks for playing my game! First some instructions, when the text ends press enter to move on, give it a try now!")
input ("Good! If you put text that is also fine, though nothing will happen. You will sometimes have an option on what to do")
CP = input ("You will then input what is in the square brackets. Do you understand [y] [n]")
#making sure people get it
n = 0
while (n == 0):
    if CP == "n":
        input("Well, you managed to get here, so let's move on")
        n = 1
    elif CP == "y":
        input("Great!")
        n = 1
    else:
        CP = input ("please only use one of the above options in the square bracket")
#getting name and pronouns, setting variables for later
input ("If you see a question mark in a square bracket please type your answer")
name = input ("What will be the name of your charecter? [?]")
print ("Hi" , name ,  "which pronouns do you prefer? He/Him/His [h] She/Her/Hers [s] or They/Them/Theirs[t]")
pronoun = input()
n = 0
while (n == 0):
    if pronoun == "h":
        p1 = "he"
        p2 = "him"
        p3 = "his"
        p4 = "lad"
        p5 = "dude"
        p6 = "sir"
        p7 = "himself"
        p8 = "man"
        n = 1
    elif pronoun == "s":
        p1 = "she"
        p2 = "her"
        p3 = "hers"
        p4 = "lass"
        p5 = "dudess"
        p6 = "ma'am"
        p7 = "herself"
        p8 = "woman"
        n = 1
    elif pronoun == "t":
        p1 = "they"
        p2 = "them"
        p3 = "theirs"
        p4 = "mate"
        p5 = "dude"
        p6 = "xir"
        p7 = "themselves"
        p8 = "person"
        n = 1
    else:
        pronoun = input ("please only use one of the above options")
#Get SO and get the story started
input ("Great!")
SO = input ("What is the name of your significant other? [?]")
input ("Great!")
input ("Let's get started")
def main():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global z
    global restart


    def restart():
        #all of the CPs and ns
        global n
        global n1
        global n2
        global n3
        global n4
        global n5
        global n6
        global n7 
        global n8
        global CP
        global CP1
        global CP2
        global CP3
        global CP4
        global CP5
        global CP6
        global CP7
        global CP8
        global chance
        '''
        #to get out of the while loops
        n = 1
        n2 = 1
        n3 = 1
        n4 = 1
        n5 = 1
        n6 = 1
        n7 = 1
        n8 = 1

        #to get out of the if loops
        
        CP = " "
        CP1 = " "
        CP2 = " "
        CP3 = " "
        CP4 = " "
        CP5 = " "
        CP6 = " "
        CP7 = " "
        CP8 = " "
        
        
        chance = 0 #for random chance moments
        '''

        main()
        
    while (1==1):
        #begining of the game
        print ("The universe is on the brink of war between the Inkinderins and the Greenbrights")
        input ()
        print ( name, "is on a small planet by the name of Jadesong." , name, "is at home watching the news and" , p1 , "gets a text.")
        input()
        print(SO , ": what's up?")
        input()
        #Text
        CP = input ("Do you respond yes [y] no [n]")

        n = 0
        while (n == 0):
            #conversation with SO
            if CP == "y":
                print (name, ": not much, how about you?")
                input()
                print (SO, ": Not much either... I'm just glad we're in nutrel teritory")
                input ()
                print (name , ": me too. just thinking about Jamie, he's in the center of it all")
                input ()
                print (SO, ": Right. I'm sorry about that.")
                input ()
                print (name, ": I was thinking about visiting him")
                input()
                print (SO, ":no, it's not safe")
                print ("does", name, "decide to visit Jamie? yes [y] no [n]")
                CP1 = input ()
                n1 = 0
                while (n1 == 0):
                        #in the spaceport
                    if CP1 == "y":
                        print (name, "grabs" , p3,  "phone and heads off to the spaceport")
                        input()
                        print (name, "gets to the spaceport and", p1, "looks up at the board and there are 2 trips to Jamie's home planet")
                        input()                    
                        print ("does", name, "take the cheep, fast, but a bit sketchy journey [s] or take the expensive, slow, but reputable one [r]")
                        CP2 = input ()
                        n2 = 0
                        while (n2 == 0):
                            #sketch flight
                            if CP2 == "s":
                                print ("You find your way to a freight ship and hand the man at the door cash")
                                input()
                                print('The man sitting next to you looks over at you and says "hey', p4 ,'you heading into the belly of the beast, why?')
                                input()
                                CP3 = input ('do you stay silent [s], say "whats it to you"? [w], or "im visiting my cushion [c]')
                                n3 = 0
                                while (n3 == 0):
                                    if CP3  == "s":
                                        #quiet
                                        print('The man says "well I guess we have a quiet one, I get the hint')
                                        input()
                                        n3 = n3+1
                                    elif CP3 == "w":
                                        #potential fight
                                        print ('the man says "woah woah', p5, 'just trying to make conversation')
                                        input()
                                        print ("does", name, "start a fight [f] or calm down [c]")
                                        CP4 = input()
                                        n4 = 0
                                        while (n4 == 0):
                                            if CP4 == "f":
                                                print ("You punch the man in the face and get thrown off of the ship with a broken nose")
                                                input()
                                                z = z+1
                                                print ("You have reached one of the endings")
                                                input()
                                                print("Restart [r] End [e]")
                                                CP5 = input()
                                                z = z + 1
                                                n5 = 0
                                                while (n5 == 0):
                                                    if CP5 == "r":
                                                        restart()
                                                        break                                   
                                                    elif CP5 == "e":
                                                        print ("I hope you had fun! Thanks for playing! You played through" , z, "times!")
                                                    else:
                                                        CP5 = input ("please choose one of the above options")
                                            elif CP4 == "c":
                                                print (name, "calms down and sits in silence for a while")
                                                n3 = n3 + 1
                                                n4 = n4 + 1
                                                CP5 = input ()
                                            else:
                                                CP4 = input ("please use one of the above options")
                                                n4 = 0
                                    elif CP3 == "c":
                                        print ("your cousin, eh?")
                                        input()
                                        print ("I wish the both of you luck then")
                                        n3 = n3 + 1

                                    else:
                                        CP3 = input ('Please use one of the above options')

                                    #the orphaned planet freezes

                                    print ("The ship takes off and is calm for a while")
                                    input()
                                    print ("suddenly there is a great rattle")
                                    input()
                                    print("the captin says over the PA that the ship has been shot down by a Inkinder cruiser and that we will be making an emergency landing on a plannet called Higermarsh")
                                    input () 
                                    print ("the ship lands on the surface and", name, "exit's the ship onto a strange plannet")
                                    input ()
                                    print ("there are trees surrounding the place where the ship landed")
                                    input()
                                    print("The trees have a purplish hue, and the closer" , name, "looks, the more", p1, "sees")
                                    input ()
                                    print ("The veins that run through the leaves are trembleing.", name, "Looks up and the sky went black.")
                                    input()
                                    print("The sun had been eaten for fuel")
                                    input()
                                    print("This would be the end for", name, "so", p1 , "sent a quick text off to", SO , "It wouldn't get there for a while but", SO, "needs to know...")
                                    input()
                                    print ("know how much", SO, "was loved")
                                    input ()
                                    print ("the world got colder and colder. Until eventually", name, "Fell asleep")
                                    input ()
                                    print (p1, "never wakes up")
                                    #ending procedure
                                    z = z + 1
                                    print ("you have reached one of the endings. Restart [r] and end [e]")
                                    CP4 = input ()
                                    n4 = 0
                                    z = z + 1
                                    while (n4 == 0):
                                        if CP4 == "r":                                        
                                            restart()
                                            break
                                        elif CP4 == "e":
                                            print ("Thank you for playing! I hope you had fun! You played through", z, "times!")
                                            input()
                                            quit()
                                        
                                        else:
                                            CP4 = input ("please use one of the above options")
                            #taking the safe shop
                            elif CP2 == "r":
                                print (name, "takes the safe route, buying a ticket at the check in")
                                input()
                                print(p1, "didn't have any checked bags, so at least",p1, "saved some money there")
                                input()
                                print("Boarding was in an hour,", name, "grabbed a snack and sat by the gate")
                                input()
                                print(name, "boarded the ship and after a few minutes it took off")
                                input()
                                print("once the ship had reached zero g", name, "got up and floated over to the restroom")
                                input()
                                print("The restroom was spinning to simulate a sort of gravity, otherwise things might go everywhere")
                                input()
                                print("The rest of the journey was boring, until eventually they landed")
                                input()
                                print("Jamie didn't live too far away, ", p1, "could probably walk from here")
                                input()
                                print ("Does", name, "try to walk to Jamie's neighborhood [w] or get a cab [c]?")
                                CP3 = input()
                                n3 = 0
                                while n3 == 0:
                                    if CP3 == "w":
                                        #walk's to Jamie's place
                                        print (name, "desides to try and walk to Jamie")
                                        input()
                                        print ("The road was a lonley place.")
                                        input()
                                        print ("It's strange how few cars there are")
                                        input()
                                        print ("There's a distant noise of a crash in the city")
                                        input ()
                                        print (name, "can see smoke coming from the city")
                                        input ()
                                        print ("an alarm pierces the silence following the crash.")
                                        input ()
                                        print ("does", name, "continue into the city [c] or run back [r]")
                                        CP4 = input()
                                        n4 = 0
                                        while n4 == 0:
                                            if CP4 == "c":
                                                #continues into the city
                                                print(name, "runs into the city")
                                                input()
                                                print("There is rubble all around, people trying to pull themselves out")
                                                input()
                                                print ("The musk of fear and uncertainty lay thick in the air")
                                                input()
                                                print ("but", name, "had family here,", p1, "there was no time to mess around")
                                                input()
                                                print (p1, "knew that", p3, "cousin lived on the north side.")
                                                input()
                                                print (name, "ran through the rubble and rebar.")
                                                input()
                                                print ("when", name, "makes it to the north side")
                                                input()
                                                print ("Then", name, "sees something horrible, something", p1, "can never unsee")
                                                input()
                                                print ("Jamie saw", name, "and he walked over to", p2, "then one of the bombs that didn't go off before did")
                                                input ()
                                                print (name, "turned and ran, ran as far away as possible")
                                                input()
                                                print ("does", name, "try and make", p3, "way to the spaceport [s] or hide in the city [h]?")
                                                CP5 = input()
                                                n5 = 0
                                                while n5 == 0:
                                                    #seaking safety at the spaceport
                                                    if CP5 == "s":
                                                        print(name, "set's", p3, "sights on the spaceport. It means safety")
                                                        input ()
                                                        print ("but", name, "wasn't out of the woods yet.")
                                                        input ()
                                                        print ("In the fog of the chaos no one knows what is safe")
                                                        input()
                                                        print (name, "keeps running through the city.")
                                                        input()
                                                        print("searching desprately for a scrap of safety to cling onto")
                                                        input()
                                                        print ("eventuality", p1, "found something, a place of refuge, for now at least")
                                                        input()
                                                        print ("A concrete building that had been nocked over had exposed it's basement")
                                                        input()
                                                        print  (name, "is about to get into the basement, but", p1, "hears a strange noise from inside")
                                                        input()
                                                        print ("does", name, "go into the basement anyway [b] or continue lookine elseware [e]")
                                                        CP6 = input()
                                                        n6 = 0
                                                        while n6 == 0:
                                                            #the basement in the destroyed city
                                                            if CP6 == "b":
                                                                print(name, "causiously enters the basement,", p1, "sees someone there")
                                                                input()
                                                                print ("they are huddled around a small electric heater. They look up at", name)
                                                                input()
                                                                print('"What do you want?" the strange person asks')
                                                                input()
                                                                print ('"',"I'm just looking for safety",'"')
                                                                input()
                                                                print("The person nods, and they go back to huddling around the heater")
                                                                input()
                                                                print (name, "figured that was about the best welcome", p1, "would get")
                                                                input()
                                                                print ("this was as good a place as any to wait for rescue")
                                                                input()
                                                                print (name, "reaches into", p3, "pocket and find something", p1, "frogot about")
                                                                input()
                                                                print ("a handful of candies")
                                                                input()
                                                                print ("does", name, "offer half of them to the other person? yes [y] or no [n]")
                                                                CP7 = input()
                                                                n7 = 0
                                                                while n7 == 0:
                                                                    if CP7 == "y":
                                                                        #gives friend some candy
                                                                        print(name, "decides to give", p3, "new roomate half of the candies")
                                                                        input()
                                                                        print ("how many did", name, "have with", p2,"? [?]")
                                                                        candynum = int (input ())
                                                                        tofreind = (candynum/2)-(candynum%2)
                                                                        print (name, "holds out", p3, "hand with", tofreind, "candies in it")
                                                                        input()
                                                                        print ("The person takes the candies, but still doesn't say anything")
                                                                        input()
                                                                        print ("they must be in as much shock as", name)
                                                                        input()
                                                                        print ("after an hour or so", name, "heard the sounds of sirins")
                                                                        input ()
                                                                        print ("this must me the rescue party,", name, "helps up the other person and they both leave")
                                                                        input()
                                                                        print ("It was the united planets peacekeepers. They brought", name, "along with the other survivors with them")
                                                                        input()
                                                                        print ("Everyone was being brought to a nutrel planet, ", name, "could get home from there")
                                                                        input()
                                                                        print (name, "texted", SO, "that", p1, "was okay.")
                                                                        input()
                                                                        print ('the person who was in the basement with', name, 'turned to', p2)
                                                                        input ()
                                                                        print ('"Hi, my name is John. Thanks for those sweets, that was very nice of you"')
                                                                        input()
                                                                        print (name, "brought John home with", p2, "he had no home anymore, and it was only fair")
                                                                        input()
                                                                        print ("they became good friends, and stayed in nutrel teritory for the rest of the war")
                                                                        input()                                                                
                                                                        print ("you have reached one of the endings. Restart [r] or end [e]")
                                                                        z = z + 1
                                                                        CP8 = input()
                                                                        n8 = 0
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                                input()
                                                                                quit()
                                                                            else: 
                                                                                CP8 = input ("please use one of the above options")
                                                                    elif CP7 == "n":
                                                                        #keeps the candy to yourself
                                                                        print (name, "keeps all of the candy to", p7, "and eats it in silence")
                                                                        input()
                                                                        print("after an hour or so", name, "hears the sound of sirins")
                                                                        input()
                                                                        print (name, "leaves the basement, and sees it's the united planets")
                                                                        input()
                                                                        print ("they are taking all of the survivors to a nutrel planet")
                                                                        input()
                                                                        print (name, "could get home from there")
                                                                        input()
                                                                        print (name, "sends a text to", SO, "saying that", p1, "is okay")
                                                                        input()
                                                                        print ("you have reached one of the endings, restart [r] or end [e]")
                                                                        z = z + 1
                                                                        CP8 = input ()
                                                                        n8 = 0
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print("Thank you for playing! I hope you enjoyed! You played", z, "times")
                                                                                input()
                                                                                quit()
                                                                            else:
                                                                                CP8 = input ("Please use one of the above options")
                                                                    else:
                                                                        CP7 = input("please use one of the above options")
                                                            elif CP6 == "e":
                                                                #avoiding the basement / acid rain
                                                                print(name,"is skeptical of the basement and continues to search for safety elsewhere")
                                                                input()
                                                                print (p1, "walks along the destroyed pavement of the city")
                                                                input()
                                                                print ("It starts to rain, which is strange seeing as there wasn't a cloud in the sky when", p1, "arrived")
                                                                input()
                                                                print ("Then", name, "realized something disturbing")
                                                                input()
                                                                print ("the bomber ship must have seeded a storm")
                                                                input()
                                                                print (p3, "Skin started to burn. They seeded acid rain.")
                                                                input()
                                                                print (name, "fell down, burning in the acid water")
                                                                input()
                                                                print ("you have reached one of the endings. Restart [r] or end[e]")
                                                                CP7 = input()
                                                                z = z + 1
                                                                n7 = 0
                                                                while n7 == 0:
                                                                    if CP7 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP7 == "e":
                                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP7 = input ("please use one of the above options")                                                                                                                                                                                               
                                                            else:
                                                                CP6 = input ("please use one of the above options")

                                                    elif CP5 == "h":
                                                        #hiding in the city
                                                        print (name, "looks for a place to hide around", p1)
                                                        input()
                                                        print ("in a desprate attempt to seek shelter", name, "ducks into Jamie's building")
                                                        input()
                                                        print("There was no one there.", p1, "managed to find a place to hide alone")
                                                        input()
                                                        print("there wasn't a basement, but it was safe for now")
                                                        input()
                                                        print (name, "hid there for a while before hearing someone outside")
                                                        input()
                                                        print("Does", name, "go outside and investigate [i] or continue to stay hidden [h]")
                                                        CP6 = input()
                                                        n6 = 0
                                                        while n6 == 0:
                                                            if CP6 == "i":
                                                                #investigate the strange noise / kidnapping
                                                                print(name, "peaks", p3, "head out of the door")
                                                                input()
                                                                print ("It's looters. They are smashing windows and taking things")
                                                                input()
                                                                print ("They spotted", name, "and they point a gun at", p2)
                                                                input()
                                                                print ('"Hands up" the leader shouts, "on your knees"')
                                                                input()
                                                                print (name, "does what he says. They carry", p2, "away")
                                                                input()
                                                                print ("They bring", p2, "to a recently abandoned parking garage")
                                                                input ()
                                                                print ("They tie", name, "to a concrete bar, and continue on to loot")
                                                                input()
                                                                print (name, "is left there for a while.")
                                                                input()
                                                                print ("no matter what", p1, "tries, nothing works to get", p7, "free")
                                                                input()
                                                                print ("the group comes back to get", name)
                                                                input ()
                                                                print ('"What is your name, why are you here?"')
                                                                input()
                                                                print ("does", name, 'say "I am just here to visit someone" [v], or stay silent [s]')
                                                                CP7 = input()
                                                                n7 = 0
                                                                while n7 == 0:
                                                                    if CP7 == "v":
                                                                        #honest with kidnappers
                                                                        print (name, "tells them that", p1, "are just there to visit someone")
                                                                        input()
                                                                        print ("The leader seams to  believe", p2, "and they cut", p2, "free")
                                                                        input()
                                                                        print ('"Leave, if I see your face again you are a dead', p8, ', do you understand?"')
                                                                        input()
                                                                        print (name, "nods, and leaves the garage")
                                                                        input ()
                                                                        print (name, "had survived, and", p1, "sees in the distance a rescue team")
                                                                        input()
                                                                        print ("The united planets peacekeepes were taking the survivors away")
                                                                        input()
                                                                        print (name, "flags them down, and gets on a UP ship.")
                                                                        input()
                                                                        print ("It takes", p2, "to a nutrel planet,", p2, "could get home from there")
                                                                        input()
                                                                        print ("You have reached one of the endings. Restart [r] end [e]")
                                                                        CP8 = input()
                                                                        n8 = 0
                                                                        z = z + 1
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                                input()
                                                                                quit()
                                                                    elif CP7 == "s":
                                                                        #killed by kidnappers
                                                                        print (name, "stays silent. This angers the looters. They shoot", p2, "in the head")
                                                                        input()
                                                                        print ("you have reached one of the endings. Restart [r] or end [e]")
                                                                        CP8 = input()
                                                                        n8 = 0
                                                                        z = z + 1
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                                input()
                                                                                quit()
                                                                            else: 
                                                                                CP8 = input("please use one of the above options")
                                                                        
                                                                    else:
                                                                        CP7 = input("please use one of the above options")
                                                            elif CP6 == "h":
                                                                #stay hidden in the building
                                                                print(name, "stay's hidden in the building and waits for the people to go past")
                                                                input()
                                                                print ("They stay in the area for a while.")
                                                                input()
                                                                print (name, "heard the sound of low altitude ships")
                                                                input()
                                                                print ("There was a second attack")
                                                                input()
                                                                print ("The last thing", name ,"sees is the wall collapsing in")
                                                                input()
                                                                print ("You have reached one of the endings. Restart [r] end[e]")
                                                                CP7 = input()
                                                                z = z + 1
                                                                n7 = 0
                                                                while n7 == 0:
                                                                    if CP7 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP7 == "e":
                                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP7 = input('please use one of the above options')
                                                                    
                                                            else:
                                                                CP6 = input ("please use one of the above options")

                                                                                    
                                                    else:
                                                        CP5 = input ("please use one of the above options")
                                            elif CP4 == "r":
                                                #seaking safety at the spaceport
                                                print(name, 'runs back to the Spaceport')
                                                input()
                                                print (p1, 'got there quickly.')
                                                input()
                                                print ("everything is grounded at the moment. The entire city has been bobbed")
                                                input()
                                                print ("all", name, "could do now was hope that Jamie was okay")
                                                input()
                                                print (name, "tried to call", SO, "but the lines were all jammed")
                                                input()
                                                print("Does", name, "try and smuggle", p7, "off the plannet [s] or wait [w]")
                                                CP5 = input()
                                                n5 = 0
                                                while n5 == 0:
                                                    if CP5 == "s":
                                                        #smuggleing yourself off of the planet
                                                        print (name, "finds an emergency ship about to take off, full of diplomats")
                                                        input()
                                                        print (p1, "sneaks into the cargo hold of the ship.")
                                                        input()
                                                        print ("It takes off and flies to the united planet's station")
                                                        input()
                                                        print (name, "can stay hidden while in transet")
                                                        input()
                                                        print ("After a few hours of travel at FTL they arrives at the UP")
                                                        input()
                                                        print (name, "wait's until there are no longer the sound of footsteps above")
                                                        input()
                                                        print ("Ever so slowly", name, "exits the cargo hold.")
                                                        input()
                                                        print (p1, "had to stay hidden. Ht would be found guilty of endangering diplomats")
                                                        input()
                                                        print ("a crime punishable by death")
                                                        input()
                                                        print (p1, 'hears over the PA system "envoy to Jadesong leaving from bay 7 in 10 minutes, 10 minutes"')
                                                        input()
                                                        print (name, "could get home, but", p1, "would have to get to bay 7 without being noticed")
                                                        input()
                                                        print ("does", name, "try and get to bay 7 and get home [b] or wait for a more sure opportunity [w]")
                                                        CP6 = input()
                                                        n6 = 0
                                                        while n6 == 0:
                                                            if CP6 == "b":
                                                                #trying to make it to bay 7, and home
                                                                print(name, "makes a run for it, hoping beyond hope not to be spotted")
                                                                input()
                                                                print ("There was footsteps coming from the hall ahead of ", p2)
                                                                input()
                                                                print (p1, "was just able to duck out of the way before anyone saw", p2)
                                                                input()
                                                                print ("The ship was right there. Everyone had already boarded, but there was still an opportunity")
                                                                input()
                                                                print (name, "dove for the closing cargo hatch, and just made it inside")
                                                                input ()
                                                                print ("It's unclear if anyone saw", p2, "but the ship took off anyway")
                                                                input()
                                                                print ("This journey was only an hour long, and", name, "was home again")
                                                                input()
                                                                print ("You have reached one of the endings. Restart [r] or end [e]")
                                                                CP7 = input()
                                                                z = z + 1
                                                                n7 = 0
                                                                while n7 == 0:
                                                                    if CP7 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP7 == "e":
                                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP7 = input ("please use one of the above options")
                                                            elif CP6 == "w":
                                                                #wait in the UP station
                                                                print (name, "wait's for a better opportunity to get off the station")
                                                                input()
                                                                print ("There was no way that", p1, "could make it there in time without being caught")
                                                                input()
                                                                print ("Though there was now the sound of something that", p1, "hadn't concitered.")
                                                                input()
                                                                print ("The cleaner had come to prepare the ship for it's next flight.")
                                                                input()
                                                                print ("There is nowhere to hide. The moment the door opens", name, "is seen")
                                                                input()
                                                                print ("The cleaner brings", name, "to the main office.")
                                                                input()
                                                                print (name, "is strapped into a machene. They can see", p3, "memories now")
                                                                input()
                                                                print ("They found", p2, "guilty of endangering diplomats, though they gave", p2, "one kindness")
                                                                input()
                                                                print (p1, "was sent off to spend the rest of", p3, "life in jail, not execution")
                                                                input()
                                                                print ("You have reached one of the endings restart [r] or end [e]")
                                                                CP7 = input()
                                                                n7 = 0
                                                                z = z +1
                                                                while n7 == 0:
                                                                    if CP7 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP7 == "e":
                                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP7 = input ("please use one of the above options.")

                                                            else: 
                                                                CP6 = input ("please use one of the above options")

                                                    elif CP5 == "w":
                                                        #Waiting in the spaceport for rescue
                                                        print(name, "wait's in the spaceport until rescue came. It would have to come")
                                                        input()
                                                        print (name, "is one of many people who are here, just waiting.")
                                                        input()
                                                        print (p1, "is ever so hungry.")
                                                        input()
                                                        print ("There is no where to eat that is still open")
                                                        input()
                                                        print (name, "did manage to get a hold of some water")
                                                        input()
                                                        print ("It is like the first rain after a long drought in", p3, "throat")
                                                        input()
                                                        print ("The United Planets peacekeepers eventually came")
                                                        input()
                                                        print (name, "was on the third shop to leave,", p1, "would make it home")
                                                        input()
                                                        print ("you have reached one of the endings. Restart [r] or end [e]")
                                                        CP6 = input()
                                                        n6 = 0
                                                        z = z + 1
                                                        while n6 == 0:
                                                            if CP6 == "r":
                                                                restart()
                                                                break
                                                            elif CP6 == "e":
                                                                print ("Thank you for playing! I hope you enjoyed! You played through",z,"times.")
                                                                input()
                                                                quit()
                                                            else:
                                                                CP6 = input("please use one of the above options")                                                    
                                                    else:
                                                        CP5 = input ("Please use one of the above options")                               
                                            else:
                                                CP4 = input("please use one of the above options")
                                    elif CP3 == "c":
                                        print (name, "hails a cab to bring" , p2, "to Jamie")
                                        input()
                                        print ("The cabbie takes down Jamie's address and pulls away")
                                        input()
                                        print ("Soon", p1, "was at Jamie's apartment.")
                                        input()
                                        print ("Jamie was so happy to see", name)
                                        input()
                                        print ('"It has been too long" he said')
                                        input()
                                        print ('"How have things been here?"', name, 'asked')
                                        input()
                                        print ('"There have been some scary times, not going to lie. But you just have to carry on"')
                                        input()
                                        print ("The two of them talked the afternoon away, until a siren pierced the peace")
                                        input()
                                        print ("Jamie, terrified leads", name, "to the bunker in the basement of his building")
                                        input()
                                        print ("They heard the sound of bombs from above.")
                                        input()
                                        print ("They stayed in the bunker for what felt like hours")
                                        input()
                                        print ("Eventually they left their security to peer out onto the city above")
                                        input()
                                        print ("The city had been virtually flattened.")
                                        input ()
                                        print ("Though they had survived.")
                                        input()
                                        print ("You have reached one of the endings. Restart [r] or end [e]")
                                        CP4 = input()
                                        n4 = 0
                                        z = z + 1
                                        while n4 == 0:
                                            if CP4 == "r":
                                                restart()
                                                break
                                            elif CP4 == "e":
                                                print ("Thank you for playing! I hope you enjoyed! You played", z, "times")
                                                input()
                                                quit()
                                            else:
                                                CP4 = input("please use one of the above options")

                                    else:
                                        CP3 = input ("please use one of the above options")


                            else:
                                CP2 = input ("Please use one of the above options")
                    elif CP1 == "n":
                        #doesn't visit Jamie
                        print(name, "listens to", SO, "and stays home")
                        input()
                        print (name, ": You're right. I'll stay home")
                        input()
                        print (SO, ": Good. I'll be by in a little while")
                        input()
                        print (name, ": see you soon <3")
                        input()
                        print (name, "slumps back onto the sofa, until", SO, "gets back home")
                        input()
                        print (SO, "opens the door and comes in")
                        input()
                        print (name, "and", SO, "embrace.")
                        input()
                        print ('"how was your day?"')
                        input()
                        print ('"It was alright. Glad to see you though"', SO, "kissed", name, "as they said that")
                        input()
                        print ("There was a smashing sound,", SO, "pushed", p2, "down to the ground")
                        input()
                        print (SO, "jumps out of the window and runs into the woods")
                        input()
                        print ("does", name, "follow", SO, "[f], or stay in the house [h]")
                        CP2 = input()
                        n2 = 0
                        while n2 == 0:
                            if CP2 == "f":
                                #Follows SO into the woods
                                print (name, "follows", SO, "into the woods")
                                input()
                                print ("It takes", p2, "a while to find", SO, "but when", p1, SO, "is hiding behind a tree")
                                input()
                                print ('"What are you doing here, you should not have folowed me"')
                                input()
                                print ("The tree next to them caught fire after being hit with a laze gun")
                                input()
                                print (SO, "shoots a gun back at them")
                                input()
                                print ('"What is happening?" ', name, 'yells at', SO)
                                input()
                                print ('"I told you not to come!"', SO , "yells back")
                                input()
                                print ("The sound of a in atmosphere ship filled the air from above")
                                input()
                                print ('"Shit"', SO, 'said. I need more time.')
                                input()
                                print(SO, "grabs onto a dropped rope and is hoisted up onto the ship")
                                input()
                                print ("Does", name, "try and climb the rope [c] or run away[r]")
                                CP3 = input()
                                n3 = 0
                                while n3 == 0:
                                    if CP3 == "c":
                                        #climbing the rope after SO
                                        print(name, "climbs the rope after", SO, "using all of", p3, "might.")
                                        input()
                                        print(SO, "shouts down at", name , "to get off")
                                        input()
                                        print (p1, "doesn't listen to them")
                                        input()
                                        print ("The ship takes of, leaving", name, "dangleing from the rope")
                                        input()
                                        chance=rand.randint(0,20)
                                        if chance > 15:
                                            #success at climbing the rope
                                            print (name, "manages to hold on to the rope as the ship takes off")
                                            input()
                                            print (p1, "pulls", p7, "up onto the closing ledge on the ship")  
                                            input()
                                            print (SO, "is gone by the time", name, "can climb all of the way up ")       
                                            input ()
                                            print (name, "looks around and sees that there are many computer monitors")     
                                            input()
                                            print ("They display all sorts of different diagrams and maps")
                                            input()
                                            print ("Does", name, "explore the rest of the ship [e] or look into the computers [c]")
                                            CP4 = input()
                                            n4 = 0
                                            while n4 == 0:
                                                if CP4 == "e":
                                                    #exploring SO's ship
                                                    print(name, "leaves the computers to walk around the ship")
                                                    input()
                                                    print (p1, "first comes across the mess hall, there are three people in there")
                                                    chance_1 = rand.randint (0,20)
                                                    if chance_1 > 5:
                                                        #sneaking past the mess hall
                                                        print (name, "sneaks past the door without anyone noticing", p2)
                                                        input()
                                                        print (p1, "keeps looking around and", p1, "eventually finds the bridge")
                                                        input()
                                                        print ("No one was in there! The ship must have been running on autopilot")
                                                        input()
                                                        print (name, "looks at the charts, they were going to a distant planet")
                                                        input()
                                                        print (name, "had never heard of it before")
                                                        input()
                                                        print ("Does", name, "change the course? Yes [y] No [n]")
                                                        CP5 = input()
                                                        n5 = 0
                                                        while n5 == 0:
                                                            if CP5 == "y":
                                                                #change the course of the ship
                                                                print(name, "fumbles with the controls and manages to switch the destination to home")
                                                                input()
                                                                print ("an alarm goes off the moment, and the door behind", p2, "closes")
                                                                input()
                                                                print (name, "hears footsteps of guards coming for", p2)
                                                                input ()
                                                                print ("The door opens, three guards come in, shooting", p2, "down quickly")
                                                                input()
                                                                print ("You have reached one of the endings, Restart [r] or [e]")
                                                                CP6 = input()
                                                                n6 = 0
                                                                z = z + 1
                                                                while n6 == 0:
                                                                    if CP6 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP6 == "e":
                                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP6 = input("Please choose one of the above options")

                                                            elif CP5 == "n":
                                                                #leave the ship on corse
                                                                print (name, "leaves the controls alone and moves on")
                                                                input()
                                                                print (p1, "finds a place to hide as a few guards walk by")
                                                                input()
                                                                print ("They are too deep in conversation to notice", p2)
                                                                input()
                                                                print (name, "finds the bunk rooms, and", p1, "sees that one of the beds is labled:")
                                                                input()
                                                                print ('"' , SO , '"')
                                                                input()
                                                                print ("There is soneone sleeping in the bed")
                                                                input()
                                                                print ("They suddenly wake up and", SO, "is looking right in", p3, "eyes")
                                                                input()
                                                                print ('"I told you to stay behind.', "You shouldn't be here!", 'You need to leave"')
                                                                input()
                                                                print (SO, "pushes", name, "down as someone walks by")
                                                                input()
                                                                print ('"I am taking you to an escape pod"')
                                                                input()
                                                                print (SO, "wouldn't hear any of" ,name + str("'s"), "protests")
                                                                input()
                                                                print (SO, "put's", p2, "in an escape pod bound for home")
                                                                input()
                                                                print ("You have reached one of the endings. Restart [r] or end [e]")
                                                                CP6 = input()
                                                                n6 = 0
                                                                z = z + 1
                                                                while n6 == 0:
                                                                    if CP6 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP6 == "e":
                                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP6 = input("please use one of the above options")
                                                            else:
                                                                CP5 = input("please use one of the above options")

                                                    else:
                                                        #caught by people in the mess
                                                        print("the people in the mess hall see", name, "and they call the guards")
                                                        input()
                                                        print ("The guards come, shooting", name, "down")
                                                        input()
                                                        print ("You have reached one of the endings. Restart[r] or end [e]")
                                                        CP5 = input()
                                                        n5 = 0
                                                        z = z + 1
                                                        while n5 == 0:
                                                            if CP5 == "r":
                                                                restart()
                                                                break
                                                            elif CP5 == "e":
                                                                print ("Thank you for playing! I hoped you enjoyed! You played through", z, "times.")
                                                                input()
                                                                quit()
                                                            else:
                                                                CP5 = input("please use one of the above options")

                                                elif CP4 == "c":
                                                    #looking at the computers
                                                    print (name, "looks through the computers. They are strategic plans for an attack.")
                                                    input()
                                                    print ("It couldn't be true, they were going to bomb a city.")
                                                    input()
                                                    print ("It was happening later that day")
                                                    input()
                                                    print ("But", p1, "was too engrosed in the screens and didn't hear anyone behind", p2)
                                                    input()
                                                    print ("The last thing", name , "felt was a warm wetness in", p3, "back")
                                                    input()
                                                    print ("You have reached one of the endings. Restart [r] or end [e]")
                                                    CP5 = input()
                                                    n5 = 0
                                                    z = z + 1
                                                    while n5 == 0:
                                                        if CP5 == "r":
                                                            restart()
                                                            break
                                                        elif CP5 == "e":
                                                            print ("Thank you for playing! I hope you enjoyed! You played through", z, "times")
                                                            input()
                                                            quit()
                                                        else:
                                                            CP5 = input("please use one of the above options")
                                                else:
                                                    CP4 = input ("please use one of the above options")
                                        else:
                                            print (name, "tries to hold on, but", p1, "falls")
                                            input()
                                            print (p1, "is dead the moment", p1, "hits the ground")
                                            input()
                                            print ("You have reached one of the endings. Restart [r] or end [e]")
                                            CP4 = input()
                                            n4 = 0
                                            z = z + 1
                                            while n4 == 0:
                                                if CP4 == "r":
                                                    restart()
                                                    break
                                                elif CP4 == "e":
                                                    print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                    input()
                                                    quit()
                                                else:
                                                    CP4 = input("Please use one of the above options")
                                    elif CP3 == "r":
                                        #running away
                                        chance_2 = rand.randint(0,20)
                                        if chance_2 > 10:
                                            print (name, "runs away, and escapes the laze guns")
                                            input()
                                            print ("They seem more concurned with the now escaping ship than they were with", p2)
                                            input()
                                            print (name, "keeps running, all the way home and locks", p7, "inside")
                                            input()
                                            print ("You have reached one of the endings. Restart [r] or end [e]")
                                            CP4 = input()
                                            n4 = 0
                                            z = z + 1
                                            while n4 == 0:
                                                if CP4 == "r":
                                                    restart()
                                                    break
                                                elif CP4 == "e":
                                                    print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                    input()
                                                    quit()
                                                else:
                                                    CP4 = input("Please use one of the above options")
                                        else:
                                            print (name, "tries to run away, but is struck by a laze gin in the back")
                                            input()
                                            print (p1, "doesn't even have time to think before the blackness reaches", p2)
                                            input()
                                            print ("You have reached one of the endings Restart [r] or end [e]")
                                            CP4 = input()
                                            n4 = 0
                                            z = z + 1
                                            while n4 == 0:
                                                if CP4 == "r":
                                                    restart()
                                                    break
                                                elif CP4 == "e":
                                                    print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                    input()
                                                    quit()
                                    else:
                                        CP3 = input("Please use one of the above options")
                            elif CP2 == "h":
                                #stay's behind in the house
                                print (name, "stays behind in the house and waits there")
                                input()
                                print (SO, "didn't come back for a long time")
                                input()
                                print ("In the meanwhile", name, "looks over", p3 , "phone")
                                input()
                                print (p1, "texts", SO , "and it doesn't go through. They didn't have service")
                                input()
                                print (name, "got really nervous about", SO)
                                input()
                                print (SO, "never comes home")
                                input()
                                print ("You have reached one of the endings. Restart [r] end [e]")
                                CP3 = input()
                                n3 = 0
                                z = z + 1
                                while n3 == 0:
                                    if CP3 == "r":
                                        restart()
                                        break
                                    elif CP3 == "e":
                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                        input()
                                        quit()
                                    else:
                                        CP3 = input("please use one of the above options")
                            else:
                                CP2 = input ("please use one of the above options")
                    else:
                        CP1 = input ("please use one of the above options")

                #someone familiar on the news
            elif CP == "n":
                print(name, "put's down his phone and turns", p3, "attention to the TV, the Greenbrights are moving in on the nutrel teritory")
                input()
                print("Jadesong is safe for now, but there is no telling how long that will last.")
                input()
                print ("On the TV", name, "'s friend appeared on the TV. apparently he is wanted for theft.")
                input()
                print ("does", name, "call", p3,  "friend [c] or pretend that", p1 , "didn't see anything [p]")
                CP1 = input ()
                n1 = 0
                while (n1 == 0):
                    #call the friend
                    if CP1 == "c":
                        print (name, "calls Jamie")
                        input ()
                        print("the phone rings")
                        input()
                        print("the phone rings")
                        input ()
                        print ("Jamie picks up the phone ")
                        input()
                        print ("hey", p5, "what's up?")
                        input ()
                        print ("I saw you on the news, what's going on?")
                        input()
                        print ("don't worry about that, got in a bit of trouble with the cops, you don't have to worry about that")
                        input()
                        print ("does" , name, "worry about that? yes [y] no [n]")
                        CP2 = input ()
                        n2 = 0
                        while (n2 == 0):
                            #worry
                            if CP2 == "y":
                                print ("I don't know man, seems suspicious")
                                input ()
                                print ("look", name, "I promice, everything is fine. I've got to go")
                                input ()
                                print (name, "is kept up by what", p3, "friend said and decides to go into the city")
                                input()
                                print("The hypertrains would be closed at this time.", p1, "would have to drive")
                                input ()
                                print ("does", name, "call an uber ground [u] or drive", p7, "[d]?")
                                CP3 = input()
                                n3 = 0
                                while (n3 == 0):
                                    #uber
                                    if CP3 == "u":
                                        print (name, "pulls out" , p3 , "phone and navigates to the uber app")
                                        input()
                                        print(p1, "chooses uber ground, meaning a land vehicle would come")
                                        input()
                                        print("Himpolio is coming to pick you up. He will be there in 10 minuets.")
                                        input()
                                        print (name, "grabs", p3, "coat and wallet and wait's outside for Himpolio")
                                        input()
                                        print ("after a few minuets The car shows up")
                                        input()
                                        print(name, "gets in and the car pulls off.")
                                        input()
                                        print ('"shit" Himpolio said."', "She's here.", '"hold on to your pants"')
                                        input()
                                        print("the car pulls off the road and parks in on a field")
                                        input()
                                        print ('"hey,', p6, 'you can get off here if you want to')
                                        input()
                                        print ("does", name, "leave [l] or stay with Himpolio [s]")
                                        CP4 = input()
                                        n4 = 0
                                        while (n4 == 0):
                                            #Himpolio adventure
                                            if CP4 == "s":
                                                print (name, "decides to stay with Himpolio. He shrugs and takes off.")
                                                input()
                                                print ("Another car went started folowing them", name, "notices that the person behind them has a gun")
                                                input()
                                                print('"who is that?"', name, "asked")
                                                input()
                                                print('"That is', SO, '. Incoming!"')
                                                input()
                                                print("does", name, "tell Himpolio that", p1, "is with", SO, "yes[y] no[n]")
                                                CP5 = input()
                                                n5 = 0
                                                while (n5 == 0):
                                                    if CP5 == "y":
                                                        #chased by SO
                                                        print (name, "pauses for a moment.", p1, 'looks at Himpolio')
                                                        input()
                                                        print (SO, '?')
                                                        input()
                                                        print ("Himpolio nodded", name, 'sighed and said')
                                                        input()
                                                        print ('"I am dating them"')
                                                        input()
                                                        print('"you are?" he seemed flabbergasted')
                                                        input()
                                                        print('"yeah, I am, so what are they doing trying to run us off the road?"')
                                                        input()
                                                        print ('Himpolio swerved, almost smashing into a tree')
                                                        input()
                                                        print('the sound of sirens come piercing through the air and Himpolio leans out of the window and shoots at them')
                                                        input()
                                                        print('does', name, 'grab the wheel [w] or the handbreak [h]')
                                                        CP6 = input()
                                                        n6 = 0
                                                        while (n6 == 0):
                                                            #going on with Himpolio
                                                            if CP6 == "w":
                                                                print(name, "takes control of the wheel while Himpolio is hanging out of the window")
                                                                input()
                                                                print ("the car is leaning twords the left and it was scraping along the road")
                                                                input()
                                                                print("Himpolio pulls himself back into the car and takes back over the car")
                                                                input()
                                                                print('Himpolio says "thanks for that, here we go"')
                                                                input()
                                                                print(name, "goes back to", p3, "seat and watches as the car continues to drive off")
                                                                input()
                                                                print("after about an hour of driving the fuel runs out and the car pulls into a driveway")
                                                                input()
                                                                print('Himpolio says "Well Alice',"it's into the rabbit hole now",'last chance to leave"')
                                                                input()
                                                                print("does", name, "stay [s] or leave[l]")
                                                                CP7 = input()
                                                                n7 = 0
                                                                while (n7 == 0):
                                                                    #finding the resistance
                                                                    if CP7 == "s":
                                                                        print (name, "decides to stay with Himpolio.")
                                                                        input()
                                                                        print("Himpolio pushes on the bark of a tree, which promptly opens like a door")
                                                                        input()
                                                                        print("He steps into the tree lowers himself like he is in an elevator")
                                                                        input()
                                                                        print(name, "steps into the now open tree and is lowered", p7)
                                                                        input
                                                                        print ("the roots of the tree and the earth fell away into a great concrete room")
                                                                        input()
                                                                        print("Himpolio was in the corner on a computer, looking at many video feeds")
                                                                        input()
                                                                        print('Himpolio says "welcome to the resistance, we can end the war"')
                                                                        input()
                                                                        print(name, "joins the resistance, and we will end the war")
                                                                        print ("you have reached one of the endings, or have you? restart [r] or end [e]")
                                                                        CP8 = input()
                                                                        n8 = 0
                                                                        z = z + 1
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times")
                                                                                input()
                                                                                quit()
                                                                            else:
                                                                                CP8 = input("please use one of the above options")

                                                                    elif CP7 == "l":
                                                                        print ("Himpolio noddes", name, "turns around and walks away")
                                                                        input()
                                                                        print (p1, "walks for hours until", p1, "reaches the road again.")
                                                                        input()
                                                                        print ("It was late at night", name, "gets service again and", p1, "checks the news")
                                                                        input()
                                                                        print(p3, "friend has been arrested and is set for trial")
                                                                        z = z+1 
                                                                        n7 = 0
                                                                        input()
                                                                        print ("You have reached one of the endings. Reset [r] or end [e]")
                                                                        CP8 = input()
                                                                        while n7 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thank you for playing! I hope you enjoyed! You have played through", z, "times")
                                                                                input()
                                                                                quit()
                                                                            else:
                                                                                CP8 = input ("please use one of the above options")                                                                    
                                                                    else:
                                                                        CP7 = input("Please use one of the above options")

                                                            elif CP6 =="h":
                                                                print (name, "pulls the handbreak and the car comes to a stop")
                                                                input()
                                                                print("the car stops and the poleice ram into it, causing it to flip three times")
                                                                input()
                                                                print(name, "is crushed under the weight of three cars, killing", p1, "instantly")
                                                                z = z + 1
                                                                print("you have reached one of the endings restart [r] or end [e]")
                                                                CP7 = input()
                                                                n7 = 0
                                                                while (n7 == 0):
                                                                    if CP7 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP7 == "e":
                                                                        print ("Thanks for playing! You have played through", z , "times")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        print("please use one of the above options")

                                                            else:
                                                                CP6 = input("please use one of the above options")
                                                        #shut up about SO
                                                    elif CP5 == "n":
                                                        print (name, "keeps", p3, "mouth shut about", SO)
                                                        input()
                                                        print ("The car keeps driving along the road, being chased")
                                                        input()
                                                        print ("both Himpolio and ", name, "sit in silence for a while")
                                                        input()
                                                        print ("they are keeping ahead of ", SO, "at the moment, but there is no telling how long that will last")
                                                        input()
                                                        print("...")
                                                        input()
                                                        print("...")
                                                        input()
                                                        print(SO, "is gaining on them. Does", name, "hide from", SO, "[h] or show", p7, "[s]")
                                                        CP6 = input()
                                                        n6 = 0
                                                        while n6 == 0:
                                                            if CP6 == "h":
                                                                print (name, "ducks back to avoid having", SO, "seeing", p2)
                                                                input()
                                                                print ("when", SO, "comes level with the car", SO, "shoots Himpolio.")
                                                                input()
                                                                print ("the car swerves off of the road, killing", name, "in an instant")
                                                                input()
                                                                z = z + 1
                                                                n7 = 0 
                                                                print ("You have reached one of the endings. Restart [r] or end [e]")
                                                                CP7 = input()
                                                                while n7 == 0:
                                                                    if CP7 == "r":
                                                                        restart()
                                                                        break
                                                                    elif CP7 == "e":
                                                                        print("Thank you for playing! I hope you endjoyed! You played through", z, "times")
                                                                        input()
                                                                        quit()
                                                                    else:
                                                                        CP7 = input ("please use one of the above options")
                                                            elif CP6 == "s":
                                                                print (name, "stays where", p1, "are, and let's", SO, "see", p2)
                                                                input()
                                                                print (SO, "pulls up even with the car and is about to shoot Himpolio when they see", name)
                                                                input()
                                                                print('"What are you doing here"', SO, "asks")
                                                                input()
                                                                print("what does" , name, "say? [?]")
                                                                say1 = input()
                                                                print(name, "says", say1, "after a pause, both cars going at 70 mph")
                                                                input()
                                                                print(SO, 'says "okay then... get ready to grab the wheel"')
                                                                input()
                                                                print (SO, "shoots Himpolio in the head, sending the car into a swerve")
                                                                input()
                                                                print (name, "is able to grab the wheel in time to pull the car over to the side of the road and get out")
                                                                input()
                                                                print("the car explodes seconds after", name, "gets out")
                                                                input()
                                                                print (SO, "pulls their car up next to", p2, "with significancy more grace")
                                                                input()
                                                                print ("does", name, "leave", SO, "for all of the lies [l] or get in their car [g]")
                                                                CP7 = input()
                                                                n7 = 0
                                                                while n7 == 0:
                                                                    if CP7 == "l":
                                                                        print(name, "tells", SO, "to go away. They look sad, but respect it")
                                                                        input()
                                                                        print(name, "is all alone on the side of the road, but with a bit more of the truth")
                                                                        input()
                                                                        print ("You have reached one of the endings restart [r] or end [e]")
                                                                        CP8 = input()
                                                                        n8 = 0
                                                                        z = z + 1
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thanks for playing! I hope you enjoyed! You played through", z, "times.")
                                                                                input()
                                                                                quit()
                                                                            else:
                                                                                CP8 = input("please use one of the above options")
                                                                    elif CP7 == "g":
                                                                        print(name, "gets into the car with", SO)
                                                                        input()
                                                                        print(SO, 'says "so... you are wondering what is going on"')
                                                                        input()
                                                                        print (name, "noddes.", SO, "sighs and tells" , p2, "everything")
                                                                        input()
                                                                        print (SO, "works for a government agency, trying to stay nutrel in the war")
                                                                        input()
                                                                        print("They had been supplying weapons secretly to the Greenbrights, but nobody could know")
                                                                        input()
                                                                        print("Himpolio had been a member of the resistance fighters, a terrorist organization")
                                                                        input()
                                                                        print("they think that they can end the war, and will destroy both empires if they have to")
                                                                        input()
                                                                        print("millions dead, just to say that they ended it.")
                                                                        input()
                                                                        print(name, "and", SO, "sat in silence for a while.", name, "noticed that they were headed home")
                                                                        input()
                                                                        print(SO, "pulled into the driveway, and looked at", name, '"You must not tell anyone, Do you understand?"')
                                                                        input()
                                                                        print(name, "nodded. They both went back to bed and went about their lives like nothing ever happened")
                                                                        input()
                                                                        print("they were a little bit closer. The war raged on, but it was machines destroying machines")
                                                                        input()
                                                                        print("in the end what's the harm in that?")
                                                                        input()
                                                                        print("You have reached one of the endings. restart [r], or end [e]")
                                                                        CP8 = input()
                                                                        z = z + 1
                                                                        n8 = 0
                                                                        while n8 == 0:
                                                                            if CP8 == "r":
                                                                                restart()
                                                                                break
                                                                            elif CP8 == "e":
                                                                                print ("Thank you for playing! I hope you had fun! You played through", z, "times.")
                                                                                input()
                                                                                quit()
                                                                            else:
                                                                                CP8 = input ("please use one of the above options")
                                                                            
                                                                    else:
                                                                        CP7 = input ("please use one of the above options")
                                                            else:
                                                                CP6 = input("please use one of the above options")
                                                    

                                                    else:
                                                        CP5 = input ("please use one of the above options")



                                                #stranded at the edge of a city
                                            elif CP4 == "l":

                                                print(name, "is stuck at the side of the road. Close to the city, but so far at the same time")
                                                input()
                                                print (name, "is trapped there until", p1, "can get help")
                                                input()
                                                print("does", name, "hitchhike to the city [c], hitchhike home [h], or try and walk home [w] (it's too far to walk to the city)")
                                                CP5 = input()
                                                n5 = 0 
                                                while n5 == 0:
                                                    #hitchhiking to the city, doesn't end well
                                                    if CP5 == "c":
                                                        print(name, "crosses the street and tries to flag down a car")
                                                        input()
                                                        print("most people pass", p2, "by, until eventually a car pulls over")
                                                        input()
                                                        print("The man in the car opens the door and", name, "gets in.")
                                                        input()
                                                        print("The man pulls off and drives into the city")
                                                        input()
                                                        print("when they arrive in the city the driver locks the doors")
                                                        input()
                                                        print('"Why did you do that"', name,"asks")
                                                        input()
                                                        print('"',"don't",'worry about that" the man said')
                                                        input()
                                                        print ('"we are almost there"')
                                                        input()
                                                        print("The man pulles into a parking garage and leaves", name, "in the car alone")
                                                        input()
                                                        print(name, "can't get out if the car, no matter how much", p1, "tries.")
                                                        input()
                                                        print ("the man comes back, but doesn't enter the car.")
                                                        input()
                                                        print("He leaves the garage", name, "hears a ticking sound")
                                                        input()
                                                        print ("After a few second the car explodes killing", name)
                                                        input()
                                                        print ("You have reached one of the endings. restart [r] or end [e]")
                                                        z = z + 1
                                                        n6 = 0
                                                        CP6 = input()
                                                        while n6 == 0:
                                                            if CP6 == "r":
                                                                restart()
                                                                break
                                                            elif CP6 == "e":
                                                                print("Thank you for playing! I hope you enjoyed! You played through", z, "times")
                                                                input()
                                                                quit()
                                                            else:
                                                                CP6 = input("Please use one of the above options")
                                                    #hitchhiking home
                                                    elif CP5 == "h":
                                                        print(name, "begins to flag down cars and eventually one pulls up")
                                                        input()
                                                        print ("The driver gesteres for", name, "to get in, and", p1, "does.")
                                                        input()
                                                        print ("The driver pulls off away from the city. Eventually reaching", name,"'s home")
                                                        input()
                                                        print ("The driver let's", name, "out and", p1, "heads inside")
                                                        input()
                                                        print(name, "checks the news." ,p3, "friend has been arrested")
                                                        input()
                                                        print("You have reached one og the endings. Restart [r] or end [e]")
                                                        CP6 = input()
                                                        z = z + 1
                                                        n6 = 0
                                                        while n6 == 0:
                                                            if CP6 == "r":
                                                                restart()
                                                                break
                                                            elif CP6 == "e":
                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                input()
                                                                quit()
                                                            else:
                                                                CP6 = input ("please use one of the above options")
                                                        
                                                    elif CP5 == "w":
                                                        print (name, "decides to walk home, then it starts raining")
                                                        input()
                                                        print (p1, "got almost completely soaked through by the time", p1, "gets home")
                                                        input()
                                                        print ("when", p1, "gets home takes a shower")
                                                        input()
                                                        print ("Once", name, "gets out of the shower", p1, "checks the news")
                                                        input()
                                                        print (p1, "sees that", p3, "friend has been arrested, and will probably be let out in a day or so")
                                                        input()
                                                        print ("you have reached on  of the endings. Restart [r] or end [e]")
                                                        CP6 = input()   
                                                        n6 = 0
                                                        z = z + 1
                                                        while n6 == 0:
                                                            if CP6 == "r":
                                                                restart()
                                                                break
                                                            elif CP6 == "e":
                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                input()
                                                                quit()
                                                            else:
                                                                CP6 = input("please choose one of the above endings.")
                                                    else:
                                                        CP5 = input ("please use one of the above options")

                                            else:
                                                CP4 = input("please use one of the above options")

                                    #Drive into the city
                                    elif CP3 == "d":
                                        print(name, "drives into the city")
                                        input()
                                        print (p1, "is not sure where", p3, "friend is.")
                                        input()
                                        print (p1, "text's him to try and figure it out where he is")
                                        input()
                                        print ("He doesn't get back.")
                                        input()
                                        print ("Does", name, "go back home [h] or keep looking [l]")
                                        CP4 = input()
                                        n4 = 0
                                        while n4 == 0:
                                            if CP4 == "h":
                                                #goes back home after not finding friend
                                                print (name, "turns around and goes home.", p3, "friend would be fine without", p2)
                                                input()
                                                print ("You have reached one of the endings. Restart [r] or end [e]")
                                                CP5 = input()
                                                n5 = 0
                                                z = z + 1
                                                while n5 == 0:
                                                    if CP5 == "r":
                                                        restart()
                                                        break
                                                    elif CP5 == "e":
                                                        print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                        input()
                                                        quit()
                                                    else:
                                                        CP5 = input("Please use one of the above options.")
                                            elif CP4 == "l":
                                                #keeps looking for friend
                                                print (name, "keeps looking for", p3, "friend, driving aimlessly around the city")
                                                input()
                                                print (p1, "sees him running from an exploding dumpster. That was him alright")
                                                input()
                                                print (name, "yells out of the window and shouts him down")
                                                input()
                                                print ('"Get in!"', name, "shouted at", p3, "friend")
                                                input()
                                                print ("He did, and", name, "pulled away")
                                                input()
                                                print ('"What did you do!"', name, 'asked.', p1, "got no responce")
                                                input()
                                                print ('"Fine, whatever, but I am going to take you home"')
                                                input()
                                                print (name, "takes", p3 , "friend home with", p2)
                                                input()
                                                print ('"This better not get me arrested"', name, "says")
                                                input()
                                                print (p3, "friend assures", name, "that everything will be fine")
                                                input()
                                                print ("In an hour or so, the poleice came to", p3, "house and asked about", p3, "friend")
                                                input()
                                                print ("does", name, "lie [l] or tell the truth [t]")
                                                CP5 = input()
                                                n5 = 0
                                                while n5 == 0:
                                                    if CP5 == "l":
                                                        #lie to the poleice
                                                        chance_4 = rand.randint(0,20)
                                                        if chance_4 > 15:
                                                            print ("The officer believes", name, "and leaves")
                                                            input()
                                                            print ("You have reached one of the endings. Restart [r] or end [e]")
                                                            CP6 = input()
                                                            n6 = 0
                                                            z = z + 2
                                                            while n6 == 0:
                                                                if CP6 == "r":
                                                                    restart()
                                                                    break
                                                                elif CP6 == "e":
                                                                    print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                    input()
                                                                    quit()
                                                                else:
                                                                    CP6 = input("Please use one of the above options")
                                                        else:
                                                            print ("The officer does not believed", name)
                                                            input()
                                                            print ("The officer arrests", name, "and takes", p2, "to jail")
                                                            input()
                                                            print (name, "is tried for harboring a criminal and found guilty")
                                                            input()
                                                            print ("You have reached one of the endings. Restart [r] or end [e]")
                                                            CP6 = input()
                                                            n6 = 0
                                                            z = z + 1
                                                            while n6 == 0:
                                                                if CP6 == "r":
                                                                    restart()
                                                                    break
                                                                elif CP6 == "e":
                                                                    print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                    input()
                                                                    quit()
                                                    elif CP5 == "t":
                                                        print (name, "tells the truth to the poleice officer")
                                                        input()
                                                        print ("The officer arrest's", p3, "friend, and takes him to jail.")
                                                        input()
                                                        print ("You have reached one of the endings. Restart [r] or end [e]")
                                                        CP6 = input()
                                                        n6 = 0
                                                        z = z + 1
                                                        while n6 == 0:
                                                            if CP6 == "r":
                                                                restart()
                                                                break
                                                            elif CP6 == "e":
                                                                print ("Thank you for playing! I hope you enjoyed! You played through", z, "times.")
                                                                input()
                                                                quit()
                                                            else:
                                                                CP6 = input("please use one of the above options")
                                                        else:
                                                            CP5 = input ("Please use one of the above options")
                                            else:
                                                CP4 = input("Please choose one of the above options")
                                    else:   
                                        CP3 = input ("please use one of the above options")
                                            #the neglectful ending
                            elif CP2 == "n":
                                print (name, "doesn't worry too much and hangs up the phone")
                                input()
                                print(name, "goes to sleep, and in the morning", p1, "checks the news. Jamie was arrested and his trial is set for 3 days from now")
                                input ()
                                print ("Jamie was found guilty and is serving life in prison")
                                input()
                                print ("you have reached one of the endings. restart [r] end [e]")
                                CP3 = input()
                                n3 = 0
                                z = z+1
                                while (n3 == 0):
                
                                    if CP3 == "r":
                                        restart()
                                        break
                                    elif CP3 == "e":
                                        print("I hope you had fun! Thanks for playing! You have played through", z, "times!")
                                        input()
                                        quit()
                                    else:
                                        CP3 = input ("Please use on of the options")
                    elif CP1 == "p":
                        print (name, "pretends", p1, "didn't see anything.")
                        input()
                        print(name, "goes to sleep, and in the morning", p1, "checks the news. Jamie was arrested and his trial is set for 3 days from now")
                        input ()
                        print ("Jamie was found guilty and is serving life in prison")
                        input()
                        print ("you have reached one of the endings. restart [r] end [e]")
                        z = z+1
                        CP3 = input()
                        n3 = 0
                        while (n3 == 0):
                            if CP3 == "r":
                                restart()
                                break
                            elif CP3 == "e":
                                print("I hope you had fun! Thanks for playing! You have played through", z, "times!")
                                input()
                                quit()
                            else:
                                CP3 = input ("Please use on of the options")
                    else:
                        CP1 = input ("please use one of the above options")
            else:
                CP = input ("please use one of the above options")
main()

