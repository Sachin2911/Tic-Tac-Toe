#imports
import grid as drawer

#variables
values = {
    "A1":"",
    "A2":"",
    "A3":"",
    "B1":"",
    "B2":"",
    "B3":"",
    "C1":"",
    "C2":"",
    "C3":"",
}

game_status = True

player_turn = drawer.start_prompt()
while game_status == True:
    if player_turn == "Bot":
        drawer.botMove(values)
        player_turn = "Player"
    
    if player_turn =="Player":
        drawer.playerMove(values)
        player_turn = "Bot"
    


