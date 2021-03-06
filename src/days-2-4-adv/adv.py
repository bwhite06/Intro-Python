from player import Player
from room import Room
from item import Item  
     
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
done = False
start = True
result=[]
while not done:

        print("===Welcome to Adventure===")
       
    
        if start:
            r=input("enter name:")
            playerlocation = room['outside']
            print(playerlocation.name,playerlocation.description)
            start = False
            new_player = Player(str(r),100,0)
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print(" Name: " + str(new_player.name) + " Score: " + str(new_player.score) + " Health: " + str(new_player.heath))
    
        if not start:
            x = input("""MOVE PLAYER: 
                    North: 
                    South:
                    East:
                    West:
OTHER:
                    Exit:
                    Grab:
                    Drop:
                    Enter a commmand: """) 
     
        

        if x=="north":
              try:  
                    playerlocation = playerlocation.n_to 

              except:
                    print ("must go south") 
            
            

        if x=="south":
            try:
                playerlocation = playerlocation.s_to
            except:
                print("must go north")

        if x=="east":
            try:
                playerlocation = playerlocation.e_to
            except:
                 print ("must go west") 
    
        if x=="west":
            try:
              playerlocation = playerlocation.w_to
            except:
                    print ("must go east") 

        if x == "exit":
            y = input("are you sure you want to exit?:")
            if y=="y":
                     done=True
         
       

        if not playerlocation:
                    print ("must go south") 



        print("++++++++++++++++++++++++++++++++++")           
        print(playerlocation.name,playerlocation.description)
        print("++++++++++++++++++++++++++++++++++") 
        print(" Name: " + str(new_player.name) + " Score: " + str(new_player.score) + " Health: " + str(new_player.heath))
      #  if playerlocation = room['foyer']:



        if playerlocation == room['treasure']:
            print("You Win!!!")
            done = True




# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
