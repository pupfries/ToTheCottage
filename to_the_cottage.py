# A text-based adventure game by me
print("To The Cottage: A Text-Based Adventure Game")

#An active flag for the game
start = input("\n\nWould you like to play 'To The Cottage'? (yes/no) ")

if start == 'yes':
    active = True
elif start == 'no':
    active = False


#The game itself
while active:
    hat = False
    flower = False
    achievements = []
    ending = ''

    print(
        "\nYou wake up in the forest. Your head hurts. You can’t remember who"
        " you are or what you’re doing here. It is dusk and your surroundings are" 
        " dead quiet. \nA heavy dread creeps over you and you aren’t sure where it’s"
        " coming from."
    )

    print("\nWhat do you do?")
    
    first_question_active = True
    while first_question_active == True:
        answer = input("\n\n(You can type 'try to remember', 'look around',"
        " or 'get up'.) ")
        if answer == 'look around':
            print("\nYou rub your eyes and sit up. There's not much light coming"
            " in through the trees but you can make out a figure in the far"  
            " distance. It’s totally motionless. That unsettles you.")
        elif answer.lower().strip() == 'try to remember':
            print("\nYou press a hand to your head. You feel fuzzy. You can" 
            " recall that you live in a small cottage somewhere near where you" 
            " are now. That’s all you can figure out. ")
        elif answer.lower().strip() == 'get up':
            first_question_active = False
        else:
            print("\nPlease type 'look around', 'try to remember', or 'get up'.")
    
    print(
        "\nYou get yourself up to your feet and as you do, you feel a weight" 
        " around your neck. You look down and see that you’re wearing a compass" 
        " necklace. You open it and see that you are facing west. "
        "\nYou can continue in the direction you're facing (west) or"
        " travel north, south or east."
    )
    answer = input("\n\nWhich direction would you like to travel in? ")

    if answer.lower().strip() == 'north':
        print(
            "\nYou begin to walk north and after a while of walking you find" 
            " a beaten path. It’s very weathered. You figure that maybe someone" 
            " lives in this forest and walks it quite often. That gives you a" 
            " bit of comfort.\n\n" 
            "You want to follow the path put you’re unsure which direction" 
            " to go."
        )
        
        answer = input("\nWhich way are you going? (left or right) ")
        if answer.lower().strip() == 'left':
            print(
                "You decide to travel left. You follow the path and keep at" 
                " it for quite some time. There’s definite evidence of human" 
                " life." 
                "\n The longer you follow, the more unsure you become. That is," 
                " until the path seems to wind out of the forest and toward a"
                " bonafide road."
                "\n\nYou pass signs the further to the edge of the woods you" 
                " go. Some are cryptic, like the X’s with eyes drawn next to" 
                " them" 
                " carved into the trees. Some simply say “Stay out, turn back.”"
                "\n\nYou hear the crunch of leaves underfoot and turn around" 
                " to find no one near you. A few yards to the road and you see" 
                " a" 
                " man standing just outside the threshold. \nThere’s a chair" 
                " beside him, as if he’d been posted up there for some time."
                "\n\nHe looks like a local townsman. He’s holding a shotgun" 
                " and as soon as you see him, he aims it at you and he shoots" 
                " you."
            )
            achievements += "Hunting Season: You met the local townsfolk!"
        elif answer.lower().strip() == 'right':
            print(
                "\nYou decide to travel left. As you travel, you see that" 
                "  about the path this way is even more worn. You begin to" 
                "  wonder who walks it. Where are they now? "
                "\n\nThe sun is fading but you notice there is still life about" 
                "  the forest. A squirrel scurries up a tree in a spiral as you" 
                "  pass. You even notice what seems like exotic plant life"
                " growing. \n\nOn one of the trees you pass, there is a flower" 
                "  growing on the branch. It’s at eye level. It’s a pretty," 
                "  pink flower and it’s fluorescent."
            )
            answer = input("\n\nTake the flower?")
            if answer.lower().strip() == 'yes':
                flower = True
                print("\n\nYou pluck the flower and pocket it.")
            elif answer.lower().strip() == 'no':
                print("\n\nYou leave it where it is and keep walking. ")
    
    elif answer.lower().strip() == 'south':
        print(
            "\n\nYou start walking south and see a hat sitting on a tree" 
            " branch. It gives you pause. \nYou wonder for a moment whose it is" 
            " and how long it has been there. It’s made of straw with a" 
            " noticeably wide brim. "
        )
        answer = input("\n\nPick up the hat? ")
        if answer.lower().strip() == 'yes':
            hat = True
            print(
                "\n\nYou take the hat off the branch and turn it over in your" 
                " hands. Other than a few leaves that you brush off of it, it" 
                " seems clean. \nOn the inside, you see the words “for the"  
                " moon” written. You have no idea what that could mean. Still,"  
                " you put the hat on and continue on your way."
            )
        elif answer.lower().strip() == 'no':
            print("\n\nYou decide to leave the hat where it is. Besides, who" 
            " knows if its owner is close by?")
        
        print(
            "\n\nYou begin to notice a persistent ambient sound that has been" 
            " on your left side. It sounds like running water. Maybe there is a" 
            " stream or river nearby, you think."
        )
        answer = input("\n\nFollow the sound? ")
        if answer.lower().strip() == 'yes':
            print("\n\nYou change direction and follow the sound of the water" 
            " until it brings you the stream.")
        elif answer.lower().strip() == 'no':
            print("\n\nYou continue through the forest, ignoring the water," 
            " until you travel so far you don’t hear it anymore at all." 
            " The trees grow denser until there is no light at all. You fumble" 
            " forward in the darkness, sure that there are bodies all around" 
            " you. You lose track of time and grow delirious. \n\n"
            "Frustrated, you try fruitlessly to circle back toward that stream" 
            " you think you heard but you never make it. Your stomach turns and" 
            " the disorientation enslaves you. You grab onto a tree to steady" 
            " yourself, wrapping your arms around it as tightly as possible." 
            " You’re sure it’s breathing."
            "\n\nFootsteps echo from seemingly every direction and you hear a" 
            " woman’s voice whisper, “I’ve got you now.” ")

            achievements += 'Frick That Noise: You did not follow the water.'
            active = False
    
    elif answer.lower().strip() == 'east':
        print("\n\nYou turn around until you are facing east and continue" 
        " forward. The trees in this direction are less sparse. There are sweet" 
        " smelling flowers along the ground as you walk."
        "\n\nThey’re pink and glowing in the dark.")
        answer = input("\n\nTake the flower or leave it? (type 'take flower'"
        " or 'leave flower') ")
        if answer.lower().strip() == 'take flower':
            flower = True
            print("\n\nYou reach down and pull the flower out of the ground." 
            " The petals are soft against your fingers." 
            "\nYou put it in your pocket.")
        elif answer.lower().strip() == 'leave flower':
            print("\n\nYou leave the mysterious glowing flower where it is.")
    
    elif answer.lower().strip() == 'west':
        print(
            "\nYou continue forward and feel a gush of cold air. You feel" 
            " even more unsettled with each step you take."
            "\nThere are voices. They sound far away but feel close.\n"
            "\nThere are narrowed eyes in the branches, watching you intensely." 
            " You begin to realize that you are prey but it’s too late. \nYou" 
            " are swallowed up by darkness and two elongated, branch-like hands" 
            " wrap around your torso. You sink to the ground and it eats you" 
            " whole."
        )
        ending = 'Westward: You died the absolute first chance you got!' 
        ending += 'But don’t beat yourself up! You can always try again 😊'
        active = False

    else:
        print("\nError: Please type 'north', 'south', 'east', or 'west'.")
    
    print(
        "\n\nYou come upon a stream. The few rays of sunlight that are still" 
        " left spill out over the water and twinkle on its surface. The sun" 
        " finally dips below the horizon and a pale glow befalls the bank."
        "\n\nThe moon is rising and it feels almost as if the forest is waking" 
        " up. You look around and see that moonlight is bathing the trees and" 
        " the stream."
    )

    if hat == True:
        print(
            "\n\nLuckily the brim of your hat shields your eyes and blocks" 
            " the moon from your vision. You find that as long as you avoid its" 
            " reflection and too much direct light, you feel safe."
        )
    elif hat == False:
        print("\n\nThe moon is coming overhead. What do you do?")
        answer = input("\n\n(You can type 'look' or 'hide') ")
        if answer.lower().strip() == 'look':
            print(
                "\n\nYou look up at the moon and feel its milky white glow" 
                "consume you. It’s blinding. You can feel it invading your mind"
                ".\n\nYou’re terrified but you can’t move or even look away." 
                " You’re fading, quickly. \n\nYou're gone." 
            )
            achievements += 'Lunatic: You were assimilated by the Moon.'
            active = False
        elif answer.lower().strip() == 'hide':
            print(
                "\n\nYou quickly duck under a tree so thick with large leaves" 
                " it might as well be a tarp. You turn your face toward the " 
                " trunk and avert you gaze from the moonlight. Something is" 
                "  definitely wrong and you won’t take chances."
                "\n\nThere is a faint buzzing and what sounds like bellows." 
                " Is it coming from the sky? No, that doesn’t make sense. That" 
                "  couldn’t be it. \n\nRight?"
                "\n\nRegardless, you shade your eyes with your hands and step" 
                " carefully under the cover of the tree."
                "\n\nThere is a bush close by that you think you can hide" 
                "  behind. Or you can try to take one of the tree’s leaves with"
                " you."
            )

            tree_question_active = True
            while tree_question_active:
                answer = input("\n\nYou can type 'hide behind bush' or 'take"
                " leaf' ")
                if answer.lower().strip() == 'take leaf':
                    print("\n\nYou reach up and feel for the lowest leaf you can" 
                    " find. It’s too thick and decidedly not coming off this" 
                    " tree.")
                elif answer.lower().strip() == 'hide behind bush':
                    print("\n\nYou will have to keep your eyes low and walk" 
                    " quickly. \n\n"
                    "Just to be safe, you cover your eyes and crouch down while" 
                    " facing it so you can go in a straight line. \nYou feel" 
                    " uneasy out in the open but you make it. Lucky you, there" 
                    " is something right next to you on the bank.")
                    tree_question_active = False
            
    print(
        "\n\nThere is a small makeshift boat near the stream." 
        " It’s made of wood with engravings on the side. It feels familiar." 
        " Somehow you know you’ll be safe in it."
    )

    answer = input("\n\nGet in the boat? ")
    if answer.lower().strip() == 'no':
        print(
            "\n\nYou decide to tough it out on this side of the" 
            " stream. Unfortunately, there is no longer any possible way" 
            " for you to make it home. \nStill amnesic, you don’t stand a" 
            " chance in these perilous woods and you don’t survive the" 
            " night."
        )
        active = False
    elif answer.lower().strip() == 'yes':
        print(
            "\n\nYou study the engravings on the outside of the boat." 
            " They seem to cover almost every spare inch. You don’t" 
            " understand them but you feel like they are some sort of spell" 
            " that will keep someone from harming you. You aren’t sure how" 
            " the knowledge comes to you but you think you made this boat."
            "\n\nIt is small, big enough for yourself and a few items. "
            "\n\nYou must keep your head down. Moonlight is rippling off" 
            " every wave of water in this stream. You just have to paddle" 
            " to the other side. You can make it. You know you can."
            "\n\nJust as you are going to paddle forward, there is a low" 
            " hum and sounds of splashing. The wind picks up considerably" 
            " and the boat rocks. It sounds like someone – or something –" 
            " is swimming towards you."
        )
        achievements += 'Lemme Drive The Boat: You got in the boat.'

        answer = input("\n\nWill you paddle harder or look and see? ")

        if answer.lower().strip() == 'look and see':
            print(
                "\n\nYou look up to see what’s pursuing you and you" 
                " are floored by what is looking back at you. It’s an evil" 
                " forest spirit, easily ten feet tall and certainly nothing" 
                " like anything you’ve ever seen in your life. \n\nIts" 
                " face – if it can be called that – is nearly featureless" 
                " except for two sunken, beady eyes. Its body is little" 
                " more than two long and grotesque legs that spin wildly" 
                " as it swims."
                "\n\nThe very sight of it shocks you and your momentary" 
                " halt is long enough for it to catch up to you." 
                " Terror-stricken, you abandon your vessel and try to swim" 
                " for it. \n\nBefore you can even be snatched out of the" 
                " water by this dreadful beast, a whirlpool materializes" 
                " beneath you and that’s the end of you."
            )
            achievements += 'Charybdis: You got sucked into a whirlpool'
            active = False

        elif answer.lower().strip() == 'paddle harder':
            print(
                "\n\nYou grip the paddle tightly and continue" 
                " forward. The splashing is coming from your left but you" 
                " know you can make it to the other side in time. You hope" 
                " you can, at least."
                "\n\nWhatever is chasing you has a voice and it’s" 
                " screaming at you now. The waters around you are churning now" 
                " and your boat sways violently from side to side. \nThe entity" 
                " throws itself against your boat, almost tipping it over" 
                " completely. You’re glad that you’re not looking at it because" 
                " it sounds terrifying."
                "\n\nIn all the commotion, you bump against something solid." 
                " You consider getting out of the boat then and there to" 
                " escape. You could also stay inside and try to dislodge" 
                " yourself from the blockage."
            )
        
        print(
            "\n\nWhatever is chasing you has a voice and it’s screaming at" 
            " you now. The waters around you are churning now and your boat sways" 
            " violently from side to side. \nThe entity throws itself against your" 
            " boat, almost tipping it over completely. You’re glad that you’re not" 
            " looking at it because it sounds terrifying."
            "\n\nIn all the commotion, you bump against something solid." 
            " You consider getting out of the boat then and there to escape. You" 
            " could also stay inside and try to dislodge yourself from the" 
            " blockage."
        )

        answer = input("\n\nStay in the boat or get out? ")

        if answer.lower().strip() == 'stay in the boat':
            print(
                "\n\nYou wedge your paddle between yourself and the solid" 
                " mass. As you push off, you hear a huge groan. Perhaps that" 
                "  wasn’t the ground at all."
            )
        elif answer.lower().strip() == 'get out':
            print(
                "\n\nYou clumsily grab hold of the solid surface your boat" 
                " has bumped into you. You stumble onto it on your hands and" 
                "  knees, careful to keep your eyes off the water."
                "\n\nYou look down and see your knees sunk into a red" 
                " substance. When you survey your surroundings, you realize" 
                "  that you are not on land. You are on the belly of..." 
                " something. It groans and shakes so violently you are almost" 
                "  flung back into the water."
                "\n\nYou look up and see a grotesque face staring back at" 
                " you. A gaping circular mouth with rows of misshapen" 
                " razor-like teeth, surrounded on all sides with a ring of" 
                " eyeballs. Its neckmust be yards long. It pokes up out of the" 
                "  water, bent and curling toward you."
            )

            monster_question_active = True
            while monster_question_active:
                answer = input("\n\nFlee or fight? ")
                if answer.lower().strip() == 'flee':
                    print(
                        "\n\nAlthough you are covered in the bodily " 
                        " secretions of this creature, you are able to scramble" 
                        " away as it attemptsto spit at you. You dodge the drool" 
                        " and slip back onto your boat."
                    )
                    monster_question_active = False
                elif answer.lower().strip() == 'fight':
                    print(
                        "\n\nYou attempt to punch the creature’s head but your" 
                        " movements are slow and it spits on you. The saliva" 
                        " quickly dissolves your skin and burns through your" 
                        " muscles in amatter of seconds. You fall into a heap," 
                        " unable to move. Its stomach opens up into another" 
                        "  mouth like a pit beneath you. It drinks you down."
                    )

        print(
            "\n\nYou’re sailing once again with the splashing right under you" 
            " now. Water and other stream items fly at you. A twig slices the" 
            " air and scratches your face. Your cheeks and forehead are" 
            " bleeding profusely."
            "\n\nYou attempt to navigate without looking up. It begins to fade" 
            " as you strike land – real land – and you tap your paddle against" 
            " the dirt to make sure. Yep, this is the real deal."
        )        

    print(
        "\n\nYou exit the boat and heave a sigh of relief. Some of the dread" 
        " you’ve been feeling since you first woke up is lifted. It’s safer on this" 
        " side of the stream. You look around and see a bonfire going. There is a" 
        " kettle, a porcelain cup, and an overturned log."
    )

    if flower == True:
        print(
            "\n\nYou pour yourself a cup of the heated water. You take the" 
            " flower out of your pocket and look over it again. Still bright," 
            " you place it in the cup of water and watch as it glows a little" 
            " brighter and some of its brilliant pink dissolves into the water" 
            " like plumes of smoke. \nThe aroma is heavenly. You bring the" 
            "  drink to your lips. Mmm, it tastes even better than it smells."
            "\n\nThe fog in your mind starts to clear and the memories rush" 
            " back. This is your bonfire. You live nearby in a cottage, in a" 
            " safer area than where you woke up. \nYou keep protections to" 
            "  stave off the malevolent spirits in these woods and you" 
            "  typically stay on this side of the stream. You look down at the" 
            "  tea and realize you crossed to collect these flowers."
            "\n\nSuddenly, the stinging in your face stops. Blood stops" 
            " dripping from your skin. You reach up to touch the cuts and they" 
            " are nonexistent. \nYou’re healed. That’s when you remember: " 
            " you went to collect these flowers for their healing properties." 
            "  You had run out of them and had to venture into a less safe part" 
            "  of the forest to get them."
            "\n\nThat’s when a spirit chased you through the trees. Your hat" 
            " caught on a branch as you ran away. \nYou went too far out and" 
            "  were hexed; it clouded your mind and made you forget, made you" 
            "  confused about who you are."
            "\n\nNow you know just the way to get home."
        )
    elif flower == False:
        print(
            "\n\nYou warm yourself at the fire and try your best to tend to" 
            " your cuts. The blood is running down your chin and onto your lap. You" 
            " pour yourself a cup of the heated water and dip your sleeve into the" 
            " cup. \nYou squeeze it out a bit and dab it onto your cuts. It helps," 
            " for the time being."
            "\n\nYou need to figure out where to go from here. It’s the dead" 
            " of night and you’re still exposed."
            "There is still quite a bit of forest to get through."
            "Aside from this campfire and the few supplies, all you can really"
            " see is more trees in each direction."
            "There is also a bridge up ahead disappearing into the tree line."
        )

        print("\n\nYou can follow the path to the trees or the bridge.")
        answer = input("\n\nPath or bridge? ")

        if answer.lower().strip() == 'path':
            print(
                "You wander deeper into the forest. You had assumed that you" 
                " were safe on this side of the stream. That’s not entirely" 
                " true. \nAlthough you know that your cottage is nearby you now"  
                " realize – all too late – that you have chosen the wrong" 
                " direction. You try to double back but you never find your way" 
                " out of the forest."
            )
        elif answer.lower().strip() == 'bridge':
            print(
                "You linger a moment near the fire. \nYou hadn’t realized just" 
                " how tired your body was, especially after that boat ride on" 
                " the way over. With a sigh, you stand up and go to the bridge."
                "\n\nWhen you cross it, it’s as if you enter a new realm." 
                " You can feel yourself crossing a threshold."
                "\n\nSoon, you happen near a tree. It’s tall with abnormally" 
                " long branches that twist upward toward the sky. They knot," 
                " intermingle, and weave in and out of each other. \nThe base" 
                " of the tree is wide and porous. Sap leaks from the bark and" 
                " pools at the roots. \nIt’s very light, almost white. "
            )

            answer = input("\n\nWill you approach or keep walking? ")
            if answer.lower().strip() == 'approach':
                print(
                    "\n\nYou approach the tree. When you get closer you can" 
                    " smell the sap and it’s very earthy. \nYou reach out and" 
                    " wipe your hand across the front of the tree as it’s very" 
                    " evident that some marking is obscured."
                    "\n\nThe sap is sticky in your hand but it doesn’t burn" 
                    " like you were expecting."
                    "\n\nYou can see what was obstructed more clearly: three" 
                    " wavy lines. They are meant to represent water. \nYou" 
                    " brush your hand over it again to gain further clarity" 
                    " and as soon as you make contact with the wood, you are" 
                    " imbued with the understanding that your way home is" 
                    " through water."
                )
            elif answer.lower().strip() == 'keep walking':
                print(
                    "\n\nYou walk past the tree. You have been through" 
                    " enough tonight and are ready to be home. \nThe last" 
                    " thing you want to do is press your luck with a" 
                    " potentially dangerous tree."
                )
        print(
            "\n\nYou continue forward to a small clearing near a cave."
            "\nYou can climb the tree to try and see if you can spot your" 
            " cottage from here, go through the cave, follow the stars, or" 
            " jump into the puddle."
        )
        answer = input(
            "\n\nHow will you proceed?"
            "(Type 'star', 'cave', 'puddle', or 'tree) "
        )
        if answer.lower().strip() == 'star':
            print(
                "\n\nYou decide to follow the stars to find your way home."
                "\n\nAs soon as you look up, your pupils expand wildly." 
                " You look up at the moon and feel its milky white glow consume" 
                " you. It’s blinding. You can feel it invading your mind. "
                "\n\nYou’re terrified but you can’t move or even look away." 
                " You’re fading, quickly."
                "\n\nYou’re gone. "
            )
            achievements += 'Lunatic: You were assimilated by the Moon.'
            ending += "So Close, Yet So Far:" 
            ending += " You made the last wrong choice in the game. " 
            ending += "One more lucky break and you’d have gotten the" 
            ending += " good ending. Oof!"
            active = False

        elif answer.lower().strip() == 'tree':
            print(
                "\n\nYou figure that you are near your cottage and climbing a" 
                " tree should help you get a better view of the surrounding" 
                " area. \nYou pat yourself on the back for the seemingly" 
                " obvious idea and begin climbing the nearest tree. "
                "\n\nLuckily, the bottom branch is at waist level and pretty" 
                " easy to get onto. \nYou climb up to the next branch and the" 
                " next and the one after until you are effortlessly ascending." 
                "\nYou aren’t even thinking about how high up you might be."
                "\n\nYour hands readily find the next branch even in the" 
                " darkness. As you climb, the moon finds you and suddenly it’s" 
                " as if a floodlight is concentrated on you. \nLuckily, you are" 
                " able to close your eyes in time and slowly maneuver to the" 
                " other side of the tree, safely out of his view."
                "\n\nJust when you think you’re out of trouble, though," 
                " you find yourself stuck. You feel around for a new branch" 
                " but your arms are stuck, glued in place. \nYour legs are" 
                " similarly immobile. You’re caught in some sort of...web."
                "\n\nA high-pitched singing rings through the trees. You can’t" 
                " tell what direction it’s coming from, can’t even turn your" 
                " head to see. \nYou feel a rush of wind as footsteps dart" 
                " toward you and there is breathing on the back of your neck."
                "\n\nWhatever is pressed against you clicks and squeals in a" 
                " language you can’t understand and then snakes its tendrils" 
                " around your body. "
                "\n\nYou begin to scream but what you can only describe as a" 
                " set of wet and cold lips set themselves at the top of your" 
                " head, slime dripping down your face and neck. \nThey slowly" 
                " slide across your head, growing wider until you realize its" 
                " mouth is engulfing you. \nIt covers your eyes, nose, mouth," 
                " and then chin. There’s no air left to breathe and all your" 
                " wild thrashing is futile as the creature wrings your body" 
                " like a wet towel."
                "\n\nOnce it has your whole head it begins to pull and suck." 
                "\nThe fleshy squelching sound is grotesque but you don’t have" 
                " to endure it long. It pulls your head clean off your body. "
            )
            ending += "So Close, Yet So Far:" 
            ending += " You made the last wrong choice in the game. " 
            ending += "One more lucky break and you’d have gotten the" 
            ending += " good ending. Oof!"
            active = False

        elif answer.lower().strip() == 'puddle':
            print(
                "\n\nYou tentatively dip the tip of your foot into the puddle." 
                " It ripples softly and seems like any old puddle. "
                "\n\nYou push your foot in deeper and find a depth that doesn’t" 
                " make sense. It goes almost up to your knee if you let it."
                "\n\nYou decide to jump in completely. Closing your eyes and" 
                " holding your breath, you dive in feet-first and quickly find"
                " yourself re-emerging from the same puddle but now in a" 
                " completely new location."
                "\n\nYou climb out, totally dry now."
            )
        elif answer.lower().strip() == 'cave':
            print(
                "\n\nIt seems reasonable to you that the cave could be a" 
                " potential shortcut so you walk right into it."
                "\n\nAs soon as you are past the entrance, the earth shifts and" 
                " rocks fall in place, blocking your way out. "
                "\n\nYou pry them free and leave the way you came, to no avail." 
                " The only way now is forward. \nYou journey deeper into the" 
                " cave while occasionally having to navigate forks in the path." 
                "\nWithin minutes you feel more disoriented than you ever have" 
                " and with the creeping feeling that you aren’t even in the"  
                " same dimension. "
                "\n\nAlthough not even an hour has passed, you feel as if" 
                " you’ve been walking for days in the pitch-black darkness." 
                "\nExhausted, you fall on your backside and sit against the" 
                " cave wall. There’s a rattling beside you."
                "\n\nYou stick your hand out and feel... a skeleton." 
                " You shriek and jump back but just as you move back you can" 
                " feel your body clacking against the ground."
                "\n\nYou’re a skeleton too. "
            )
            ending += "So Close, Yet So Far:" 
            ending += " You made the last wrong choice in the game. " 
            ending += "One more lucky break and you’d have gotten the" 
            ending += " good ending. Oof!"
            active = False
    print(
        "\n\nYou come upon a cottage. It looks quaint, earthy, and idyllic." 
        " \nA candle is lit in the window. You feel that at last, you are home."
    )

    found_cottage_question_active = True
    while found_cottage_question_active:
        answer = input(
            "\n\nWhat would you like to do?"
            "('survey yard', 'walk inside', or 'observe cottage') "
        )

        if answer.lower().strip() == 'survey yard':
            print(
                "\n\nFireflies flicker around one of the sides of the cottage." 
                " There is a wooden wheelbarrow laying on the ground."
                " \nThere are only two windows and the one with the candle is" 
                " the only window with a closed shutter."
            )
        elif answer.lower().strip() == 'observe cottage':
            print(
                "\n\nThe cottage is small. You can definitely tell only one" 
                " person lives here. \nThere are embellishments on the roof."
            )
        elif answer.lower().strip() == 'walk inside':
            print(
                "\n\nYou approach the door of the cottage. It’s made of" 
                " differently colored woods and heavily decorated. There’s a" 
                " flower wreath on the door and spells carved into the material" 
                " itself. You open it up and walk in"
            )
            found_cottage_question_active = False
    
    print(
        "\n\nAs soon as you walk in, the air is warmer. \nThe first thing that" 
        " catches your eye is a stone fireplace with a skillet sitting inside."
    )

    if hat == True:
        print(
            "\n\nYou hang your hat up on a wooden coatrack near the door where" 
            " various other garments are already hanging. You see a hooded" 
            " cloak, a blindfold, a cloth bag, and a pair of thick boots" 
            " underneath. \nYou take your shoes off and place them beside" 
            " the boots."
        )
        ending += 'Rest Easy: You got the best ending!' 
        ending += 'You remembered everything and got home in one piece.'
    elif hat == False:
        print(
            "\n\nThere’s a coatrack near the door hanging multiple items." 
            " You see a hooded cloak, a blindfold, a cloth bag, and a pair of" 
            " thick boots underneath. \nYou take your shoes off and place them" 
            " beside the boots."
        )
        ending += 'Pretty Good: Pay yourself on the back, you got home safe!' 
        ending += "You didn't recover your memory but you got home safely!"
    
    print(
        "\n\nThere isn’t much spare space inside of your cozy abode." 
        " The walls are covered in colorful and mystical plants. \nShelves" 
        " lined with books and figurines wrap around whole corners and sections" 
        " of wall. \nJars of ink and what you ascertain to be some kind of" 
        " potions are stacked underneath corner tables."
        "\n\nThe light you saw outside turns out to be a small blue flickering" 
        " candle in the window."
        "\n\nAcross the room is a curtain. When you pull it aside, you see a" 
        " small bedroom. There is a comfortable looking bed. As soon as you see" 
        " it, time catches up with you and going to bed sounds like a" 
        " great idea."
        "\n\n\nYou put out the candle and climb into bed. "
    )

    #Option to play again
    answer = input("\n\n\nPlay again? (yes/no) ")
    if answer.lower().strip() == 'yes':
        active = True
    elif answer.lower().strip() == 'no':
        active = False

#The results of the player's gameplay
if start.lower().strip() == 'no':
    print("\n\nYou chose not to play!")
elif start.lower().strip() == 'yes':
    print("\n\nThanks for playing!")

    if ending:
        print(f"\nYou got the {ending} ending!")
    
    if flower:
        print("\n And you unlocked the truth with the flower!")
    if hat:
        print("\nYou found the hat to shield you from the moon!")
    
    print("\n\nAchievements earned: ")
    if achievements:
        for achievement in achievements:
            print(f"\n\t{achievement}")
    else:
        print("None.")

