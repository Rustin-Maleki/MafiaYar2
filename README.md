def Bazi():
    import random
    import time
    import pygame

    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\okk\\Downloads\\01) Amadea Music Productions - Forensic Enigma.mp3")
    pygame.mixer.music.play()
    #distributing_roles
    def distribute_roles(num_players, player_names):
        if num_players < 6:
            print("The number of players must be at least 6.")
            return
        else:
            mafia_count = num_players // 3 - 2
            detectives_count = max(1, num_players // 8)
    
            role_names = ["Mafia"]*mafia_count + ["Detective"] * detectives_count + ["Ordinary Citizen"] * 2  + ['God Father'] + ['Doctor'] + ['Leon'] + ['doctor L.']+['mayor']+['ravanpezeshk']+['jansakht']
            random.shuffle(role_names)
            roles = {}
            for name in player_names:
                roles[name] = role_names.pop()
            return roles
    #speaking_tools
    def speak(player):
        """Function to speak with players"""
        print(f"It's {player}'s turn.")
        time.sleep(1)
    #Voting
    def vote(player_names):
        """Function to vote for players"""
        votes = {}
        for player in player_names:
            num_votes = int(input(f"Enter the number of votes for {player}: "))
            votes[player] = num_votes
        return votes
    #second_voting
    def second_vote(guilty_players):
        """Function for second round of voting between guilty players"""
        second_votes = {}
        for player in guilty_players:
            num_votes = int(input(f"Enter the number of votes for {player}: "))
            second_votes[player] = num_votes
        return second_votes
    
    num_players = int(input("Enter the number of players: "))
    player_names = [input(f"Name of player {i+1}: ") for i in range(num_players)]
    assigned_roles = distribute_roles(num_players, player_names)

    for player in player_names:
        speak(player)

    votes = vote(player_names)
    guilty_players = [player for player, num_votes in votes.items() if num_votes >= len(player_names) / 2]
    for player in player_names:
        print(player)
    def last_words():
        cards=["beutiful mind", "insomnia", "green path", "13th lie", "red carpet", "last shoot"]
        return random.choice(cards)
    if len(guilty_players) > 1:
        for player in guilty_players:
            speak(player)
        print("Evening nap time")
        second_votes = second_vote(guilty_players)
        #بيداري شهردار
        mayor = ['mayor']
        for player in mayor:
            speak(mayor)
            mayor_decision=int(input("to Cancel the poll 1,expelled someone 2, do nothing 3: "))
            if mayor_decision==1:
                print("the poll was cancelled by the mayor")
            elif mayor_decision==2:
                mayor_deportation=input("Who will be expelled? ")
                if mayor_deportation in second_votes:
                    player_names.remove(mayor_deportation)
                    print(f"{mayor_deportation} has been expelled from the game.")
                else:
                    print("Invalid target, Please enter the target again.")
                    input("Who will be expelled? ")
                    if mayor_deportation in second_votes:
                        player_names.remove(mayor_deportation)
                        print(f"{mayor_deportation} has been expelled from the game.")
            else:
                expelled_player = max(second_votes,key=second_votes.get)
                player_names.remove(expelled_player)
                print(f"{expelled_player} has been expelled from the game.")
    elif len(guilty_players)==1:
        for player in guilty_players:
            speak(player)
        if int(input(f"Enter the number of votes for {player}: "))>= int((len(player_names))/2):
            last_words()
            player_names.remove(player)
            for player in player_names:
                print(player)

    def Night(player_names):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\okk\\Downloads\\cricket-sound-short.mp3")
        pygame.mixer.music.play()
        mafia_players = ["Mafia",'God Father','doctor L.']
        doctor_players = [player for player, role in assigned_roles.items() if role == "Doctor"]
        detective_players=[player for player, role in assigned_roles.items() if role == "Detective" ]
        leon_player=[player for player, role in assigned_roles.items() if role == 'Leon' ]
        sniper_players=["Leon"]
        jansakht=['jansakht']
        # بیداری دکتر واتسون
        for player in doctor_players:
            speak(player)
            target= input("Choose a player to save: ")
            if target in player_names:
                print(f"{target} has been saved by the Doctor.")
            else:
                print("Invalid target.")
        # بیداری مافیا
        speak('God Father')
        targetM=input("Choose a player to kill: ")
        if target in player_names:
            if targetM in target:
                print(f"{target} was targeted by the Mafia but saved by the Doctor.")
            elif targetM in jansakht:
                print("jansakht was tageted by the mafia.")
            else:
                player_names.remove(targetM)
                pygame.mixer.init()
                pygame.mixer.music.load("C:\\Users\\okk\\Desktop\\Untitled Session 21_mixdown.mp3")
                pygame.mixer.music.play()
                print(f"{targetM} has been killed by the Mafia.")
        else:
            print("Invalid target.")
        #بيداري دکتر لکتر
        speak('doctor L.')
        targetd=input("Choose a mafia player to save: ")
        if targetd in player_names:
                print(f"{targetd} has been saved by the doctor L.")
        else:
            print("Invalid target.")
        #بيداري کاراگاه
        for player in detective_players:
            speak(player)
            targetD= input("Choose a player to Inquiry: ")
            if targetD in player_names:
                if targetD in mafia_players:
                    print(f"{targetD} Is a mafia player.")
                else:
                    print(f"{targetD} Is not a mafia player.")
                    pass
        #بيداري لئون
        for player in leon_player:
            speak(player)
            targetL= input("Choose a player to shoot: ")
            if targetL in player_names:
                if targetL in mafia_players:
                    if targetL in targetd:
                        print(f"{targetL} had been shot but savedby doctor L.")
                    else:
                        player_names.remove(targetL)
                else:
                    print(f"{targetL} had been shot.")
                    player_names.remove(player)
                    
    print(assigned_roles)
    Night(player_names)
    print("Remaining players:")
    for player in player_names:
        print(player)
print(Bazi())
