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
move_counter = 0
players = []

player_turn, player_obj = drawer.start_prompt()
if player_obj == True:
    players = ["X", "O"]
else:
    players = ["O", "X"]
     

while game_status == True:
    if player_turn == "Bot":
        values = drawer.botMove(values)
        player_turn = "Player"
        # drawer.grid_Drawer(values)
        move_counter = move_counter + 1
    
    if player_turn =="Player":
        drawer.grid_Drawer(values)
        values = drawer.playerMove(values)
        player_turn = "Bot"
        drawer.grid_Drawer(values)
        move_counter = move_counter + 1
        print("\n\n")
        
    


