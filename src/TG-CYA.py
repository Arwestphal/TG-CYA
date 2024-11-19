quickdraw = [
["Quickdraw (Enter 1 to start) (Enter 0 to leave game at any time)", 1],
["Page 1: Quickdraw - It is the year 1899, You are a cowboy who just arrived into the town Tumbleweed. You dismount your horse and enter the saloon. Do you go to the BAR (page 2) or a TABLE (page 5)", 2, 5],
["Page 2: You walk up and lean on the bar. The bartender asks if you need a drink. ACCEPT (page 3) or DECLINE (page 4)", 3, 4],
["Page 3: You decide to relax and take a few shots of whiskey. You start to feel dizzy and everything becomes blurry. A drunken man next to you begins to boast about how quickly he can draw his gun. You find him annoying and stare him down. He notices you and asks to duel. ACCEPT (page 6) or DECLINE (page 7)", 6, 7],
["Page 4: You decline the drink. A drunken man next to you begins to boast about how quickly he can draw his gun, but you ignore him. Suddenly, the saloon doors open and the room goes silent. A man in a black suit and hat is standing there, claiming to be the fastest gun. He notices you sitting at the bar and requests a duel. DECLINE (page 7) or ACCEPT (page 8)", 7, 8],
["Page 5: You decide to sit at a table where some men are playing poker. You decide to join in and the dealer gives you some cards. You have a Royal Flush and go all in, winning it all. Everyone at the table is very angry, and one of the men accuses you of cheating. He asks to duel. DECLINE (page 7) or ACCEPT (page 8)", 7, 8],
["Page 6: Confidently, you accept the duel. You both drunkenly exit the saloon and walk to the ends of the road, facing each other. You take position, both hands at your side and your feet shoulder width apart. You both begin to count down, 3, 2, 1, Draw! You somehow manage to draw your gun from your holster and you try your best to aim it at the man. F!RE (page 10) or FIR3 (page 11)", 10, 11],
["Page 7: You decline the offer to duel. The man asks the room if anyone wants to take the challenge, but no one accepts. Suddenly, a shady man sitting in the back corner slowly stands up, and accepts the duel. Both men exit the saloon. You hear a countdown, 3, 2, 1, Draw! Then a gunshot. The shady man re-enters the saloon, asking for a second round. ACCEPT (page 8) or DECLINE (page 9)", 8, 9],
["Page 8: You accept the duel and you both exit the saloon. You both walk to the ends of the street and take your position, both hands at your side and your feet shoulder width apart. You both begin to count down, 3, 2, 1, Draw! Are you QUICK (page 10) or ACCURATE (page 11)", 10, 11],
["Page 9: You decline the duel a second time and the man stares at you judgmentally. Another man confidently stands up and accepts the duel. Both men walk outside, and an excited crowd follows them. Do you WATCH (page 11) or STAY (page 12)", 11, 12],
["Page 10: BANG!!! You pull the trigger and the man falls to the ground. You won the duel! THE END. Return to title? (page 0)", 0],
["Page 11: BANG!!! You feel a bullet flying through your head and everything goes black. You are dead. THE END. Return to title? (page 0)", 0],
["Page 12: You decide to stay inside and have some whiskey from the bar. That was the best night you've ever had. The next morning, you saddle up and leave the town. THE END. Return to title? (page 0)", 0]
]

zombie = [
["Zombie Survival (Enter 1 to start) (Enter 0 to leave game at any time)", 1],
["Page 1: It is the year 2036 and there has been an outbreak of a virus that turns people into zombies. You are in your house and hear zombies outside, so you grab your gun and sneak out the back window to escape. Do you go through the WOODS (page 2) or go through the NEIGHBORHOOD (page 3)", 2, 3],
["Page 2: You decide to sneak through the woods. You can see a hoard of zombies through the trees. Do you SNEAK PAST (page 4) or SHOOT (page 10)", 4, 10],
["Page 3: You start running through the neighborhood. As you are running, you hear a car behind you. It comes to a stop and the driver rolls his window down. The man claims to be a helicopter pilot who is driving to the airport. He claims that the airport is full of zombies but it is the best way to escape. He offers you a ride. Do you ACCEPT (page 5) or DECLINE (page 7)", 5, 7],
["Page 4: You are able to sneak past the zombies and exit the woods. You see a clear road ahead so you go in that direction. As you are running, you hear a car behind you. It comes to a stop and the driver rolls his window down. The man claims to be a helicopter pilot who is driving to the airport. He claims that the airport is full of zombies but it is the best way to escape. He offers you a ride. Do you ACCEPT (page 5) or DECLINE (page 7)", 5, 7],
["Page 5: You hop in the car and he takes you to the airport. As the man said, the airport is full of zombies, and the path to the helicopter is blocked. Do you SNEAK PAST (page 6) or SHOOT (page 10)", 6, 10],
["Page 6: You are able to sneak onto the helicopter. As you are taking off, a zombie suddenly emerges from the back seat and bites the pilot. You shoot the zombie and the pilot survives but is infected. You point your gun at him, but he begs for his life and claims he still has time to fly to safety before he is converted. Do you SPARE HIM (page 8) or KILL HIM (page 9)", 8, 9],
["Page 7: You decline the ride to the airport and continue through the neighborhood. After a while of running, you reach a highway full of zombies. As you prepare for battle, you hear a helicopter flying in the distance, moving towards your direction. You start jumping and waving your hands in the air, but the pilot doesn't seem to notice you. The zombies notice you and start moving in your direction. You realize that your only chance to escape is if you can get the pilot to notice you. Do you shoot at the AIR (page 10) or shoot at the ZOMBIES (page 12)", 10, 12],
["Page 8: You spare the pilot and he flies out of the airport. The pilot is able to fly you to a nearby military base that is safe from zombies. He talks on his radio and receives clearance to land. As you are flying over the base, the pilot starts to spasm and foam at the mouth. He points to a parachute in the back of the helicopter and tries his best to fly towards the helipad. Do you use the PARACHUTE (page 12) or let the pilot LAND (page 13)", 12, 13],
["Page 9: You shoot the pilot in the head and he falls out of the helicopter. A hoard of zombies on the runway hears the gunshot and they start charging towards your direction. Do you EXIT (page 10) or try to FLY (page 11)", 10, 11],
["Page 10: You are overrun by zombies and become infected. THE END. Return to title? (page 0)", 0],
["Page 11: You try to continue flying the helicopter. You press your foot on the pedal and the helicopter ascends. You push forward the throttle and the helicopter moves forward. You turn the wheel and begin to fly away from the airport. After a few minutes of flying, you make it to a neighboring city and notice that there are significantly fewer zombies on the ground. You keep flying and you see fewer and fewer zombies until you can no longer spot a single zombie on the ground. Suddenly, you notice a flashing light on the control panel that says low fuel. You look for a place to land, but there are too many buildings in the area. You keep flying the area looking for a spot, and the fuel continues to decrease. You see an open field about two minutes away, but the fuel gauge is nearly empty. You notice a parachute in the back of the helicopter. Do you PARACHUTE (page 12) or LAND (page 13)", 12, 13],
["Page 12: You were able to escape the zombies. THE END. Return to title? (page 0)", 0],
["Page 13: The helicopter crashes and explodes, and you burn alive. THE END. Return to title? (page 0)", 0]
]

island = [
["Island Survival (Enter 1 to start) (Enter 0 to leave game at any time)", 1],
["Page 1: After your boat mysteriously crashes while traveling across the ocean, you wake up washed ashore on the beach of a large island. The island is surrounded by a beach and has a large forest in the center. You have no food or shelter so you have to act quickly. It begins to rain hard, so you need to seek shelter. You see some fallen trees along the beach that you can use to make a shelter. You also notice a cave further into the island’s forest. Do you enter the CAVE (page 2) or build on the BEACH (page 4)", 2, 4],
["Page 2: You enter the cave and take shelter. The cave is very deep and you begin to walk further inside. You suddenly hear a roar echoing from further into the cave, and you can see a black bear emerge from the shadows. You hide behind a boulder and you can hear the bear approaching. Do you PLAY DEAD (page 3) or FIGHT (page 10)", 3, 10],
["Page 3: You lay on the ground and play dead. You hear the bear sniff your body and it walks away. You slowly stand back up and take a sigh of relief. Do you return to the BEACH (page 4) or EXPLORE THE CAVE (page 11)", 4, 11],
["Page 4: You make your way along the beach. You gather logs from fallen trees to build your home. As the storm begins to settle, you are able to gather enough resources to build your home. You can hear a distant roar coming from the cave and you see a bear guarding the entrance, so entering the cave will be very difficult. As you continue to build your home, you suddenly hear a howl from the forest, and a wolf appears out of nowhere. It slowly makes its way towards you, with saliva drooling from its mouth. The only chance of survival is fighting the wolf. Do you fight with HANDS (page 5) or with a STICK (page 8)", 5, 8],
["Page 5: As the wolf lunges at you, you throw an uppercut and hit the wolf in the jaw, knocking it down. You tackle the wolf and begin punching it in the head until it stops moving. As it whimpers on the ground, you place your hands around its head and you snap its neck, killing it. You pry open its stomach and take one of its sharpest ribs to use as a knife. You also find a large chunk of meat that can be cooked for food. Do you COOK THE WOLF (page 6) or use as BAIT (page 7)", 6, 7],
["Page 6: You build a fire and cook the wolf. You take a huge bite as it's the first time eating in days. You hear something moving in the forest, so you take the bone knife and walk towards the noise. You hear a loud roar and realize the bear is right in front of you. Do you FIGHT (page 9) or RUN (page 10)", 9, 10],
["Page 7: You plant the meat outside the entrance of the cave and you hide behind a rock. Momentarily, you see the bear exit the cave and it begins to eat the meat. Do you ATTACK (page 9) or SNEAK PAST (page 10)", 9, 10],
["Page 8: You point the stick at the wolf and prepare for a fight, but instead of attacking you, the wolf begins to wag its tail and sits. You throw the stick along the beach and the wolf runs and retrieves the stick. With your new friend, you have someone who will protect you and help fight enemies. Do you ATTACK THE BEAR (page 9) or FINISH BUILDING HOME (page 12)", 9, 12],
["Page 9: You are able to kill the bear and collect its meat for food. With no more animals trying to kill you on the island, you can either explore the CAVE (page 11) or safely build your HOME (page 12)", 11, 12],
["Page 10: The bear tackles you and crushes your head, killing you instantly. THE END. Return to title? (page 0)", 0],
["Page 11: You explore deeper into the cave and you follow a tunnel underground. You are able to find a room that is illuminated by a hole in the roof that allows for sunlight to shine through. The room is connected to two tunnels, one that goes left and has the scent of food, and one that goes right and is flooded with water. Do you go LEFT (page 12) or RIGHT (page 13)", 12, 13],
["Page 12: With enough resources and shelter, you are able to survive until help arrives. THE END. Return to title? (page 0)", 0],
["Page 13: You find an inflatable raft inside the tunnel. You take it back with you to the beach and inflate it. You push it onto the water and hop on, and you begin to paddle away from the island to your freedom. THE END. Return to title? (page 0)", 0],
]

def cya():
  story = []
  running = True
  while running:
    print("\nWelcome to Choose Your Adventure. Would you like to play Quickdraw (Enter 1), Zombie Survival (Enter 2), or Island Survival (Enter 3), (0 to quit)")
    storychoice = int(input("\n1, 2, or 3?"))
    while storychoice not in [0, 1, 2, 3]:
      storychoice = int(input("\ninvalid, enter: 0, 1, 2, or 3?"))
    if storychoice == 0:
      running = False
    elif storychoice == 1:
      story = quickdraw
    elif storychoice == 2:
      story = zombie
    elif storychoice == 3:
      story = island
    if running:
      selection = story[0]
      game = True
      while game:
        text = selection[0]
        options = selection[1:]
        opt_text = ("options: " + str(options))
        print("\n" + text)
        choice = int(input("\n" + opt_text))
        while choice not in options and choice != 0:
          choice = int(input("\ninvalid, " + opt_text))
        if choice in options:
          selection = story[choice]
        elif choice == 0:
          game = False
  print("\nThank you for playing Choose Your Adventure")
cya()