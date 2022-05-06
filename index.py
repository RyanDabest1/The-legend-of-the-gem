

class Room(object):
    def __init__(self, name, description):
      self.name = name
      self.description = description
      self.exits = {}
      self.items = []

class Player(object):
  def __init__(self, name, location):
   self.name = name
   self.location = location
   self.inventory = []

class Item(object):
  def __init__(self, name, description, is_movable):
    self.name = name
    self.description = description
    self.is_movable = is_movable

#bed room items
book = Item("book", "The book is heavy it's about the electro element", False)
gem = Item("gem", "Mysterious gemstone that have the use to something", True)
bedroom = Room("Your Bedroom", "You can see some books and a purple gemstone inside a glass clinder")

#Training area items
mistress = Item("mistress", "She looks disappointed", False)
dummy = Item("dummy", "A simple training dummy looking directly into your soul waiting for you to attack it", False)
guide_book = Item("book", "A guide book to awaken your element. I've been trying to follow the steps but it's insanly hard..", True)
map = Item("map", "A map which shows all geographical landmarks of your surroundings.", True)
coin = Item("coin", "A currency to buy stuff, simply everything costs only 1 coin.", True)
energy = Item("energy", "A hidden spiritual power. Can only be obtained by yourself.", True)

#Garden items
wishing_well = Item("well", "It's a wishing well. You can wish anything you want by throwing a coin down.", False)
staff = Item("staff", "A staff made out of energys from lightning. I can use it to defend myself", False)
mistress = Item("mistress", "Take the staff and go into the forest to complete your training.", False)
wishing_token = Item("token", "Wishing token, a thing you can get from wishing in the well", False)

#Old hut items
scroll = Item("scroll", "A scroll that have something written in it.", True)
clock = Item("clock", "It's a broken clock seems like it's a use for something", True)
dagger = Item("dagger", "A rusty dagger. I think I should keep it just in case.", True)
bed = Item("bed", "Looks old and broken", False)
Ruin_guardian = Item("ruin_guardian", "A destroyed ruin guardian. These robotic creatures are very menacing.", False)
guardian_core = Item("guardian_core", "A core that can power up a fighting machine.", True)

#Forest entrance items
Grass_crawler = Item("crawler", "Grass crawlers, dangerous creatures that lurk around the forest.", False)
Grass_essence = Item("essence", "Grass crawler essence that can be used later.", True)

#Bedroom 
bedroom.items.append(book)
bedroom.items.append(gem)

#Training area
Training_area = Room("Training area", "The training area where fearsome warriors trained for decades.")
Training_area.items.append(mistress)
Training_area.items.append(dummy)
Training_area.items.append(guide_book)
Training_area.items.append(map)
Training_area.items.append(coin)

#Garden
Garden = Room("Garden", "A circular shaped garden with a wishing fountain in the center and lots of flowers around it.")
Garden.items.append(wishing_well)
Garden.items.append(staff)
Garden.items.append(mistress)

#Forest entrance
Forest_entrance = Room("Forest", "An entrance part of the forest, beware you might find some creatures")
Forest_entrance.items.append(Grass_crawler)

#Old hut
Old_hut = Room("Hut", "An old, small hut in the middle of nowhere.")
Old_hut.items.append(scroll)
Old_hut.items.append(clock)
Old_hut.items.append(dagger)
Old_hut.items.append(bed)
Old_hut.items.append(Ruin_guardian)

#Small village
Small_village = Room("Village", "A small village in the middle of a forest. Well known for it's monument")

#Create exits
bedroom.exits["E"]= Training_area
Training_area.exits["W"]= bedroom
Garden.exits["S"] = Training_area
Garden.exits["E"] = Forest_entrance
Forest_entrance.exits["W"] = Garden
Forest_entrance.exits["S"] = Small_village
Forest_entrance.exits["E"] = Old_hut
Old_hut.exits["W"] = Forest_entrance
Small_village.exits["N"] = Forest_entrance

player = Player("The Player", bedroom)

#Starting game
print("THE GEMSTONE")
print("\nYou're inside your room, its 7:30am you gotta go to your training.")


while True:
  print("")
  print(player.location.name)
  print(player.location.description)
  print("\nHere are the exits: ")
  for exit  in player.location.exits :
    print(exit)
  print("\nYou see the following: ")
  for item in player.location.items:
    print(item.name)
  
  command = raw_input("\n> ")
  words = command.split()
  if len(words) > 0:
       verb = words[0]
  if len(words) > 1:
       noun = words[1]
  #Examine

  if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

  if verb in ["inv", "inventory"]:
    print("Your inventory: ")
    for item in player.inventory:
      print(item.name)
      
#getting items
  if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # Check is it movable
                if item.is_movable:
                    print("You take the {}".format(item.name))
                    # Remove from room
                    player.location.items.remove(item)
                    player.inventory.append(item)
                
                else:
                    print("I don't think its useful.")

#dropping
  if verb == "drop":
    for item in player.inventory:
      print("I dropped the {}".format(item.name))
      player.inventory.remove(item)
      player.location.items.append(item)

#moving
  if verb in ["N", "S", "E", "W", "U", "D"]:
    if verb in player.location.exits:
      player.location = player.location.exits[verb]
      print("You walked to {} and arrived somewhere".format(verb))

#Room specific 

#Training area
  if player.location == Training_area:
    if gem not in player.inventory:
      print("I feel like I need to grab the gemstone from my bedroom")
    else:
      print("Your mistress told you to practice everything that is written in the guide book 'How to awaken your element'")
    
  if player.location == Training_area:
    if verb == "train" and noun == "element":
      if guide_book in player.inventory:
       print("I sense something....\nI can feel something inside me..\nA strange sensation flows in your body.")
       Training_area.exits["N"] = Garden
       player.inventory.append(energy)
       player.inventory.remove(guide_book)

      else:
       print("I must get the guide book in order to read it...")

#Garden
  if player.location == Garden:
    if verb == "grab" and noun == "staff":
      if energy in player.inventory:
        print("You've grabbed the staff and now the staff glows and covered itself with purple lightning particles.")
        player.inventory.append(staff)
        player.location.items.remove(staff)
        
      else:
        print("Nothing happened, I think I should go train...")

  if player.location == Garden:
    if verb == "wish" and noun == "well":
      if coin in player.inventory:
        print("You threw a coin down and wish for something. You would be patience to see if its granted.")
        player.inventory.append(wishing_token)
        player.inventory.remove(coin)

      else:
        print("I don't have a coin to throw.")


#Forest Entrance
  if player.location == Forest_entrance:
    if verb == "attack" and noun == "crawler":
      if staff not in player.inventory:
        print("You tried to attack the crawler with your basic powers but it seems like you did no damage.\n The creature kills you.")
        exit()
    
      else:
        print("You killed the Grass crawler and as a result you gets {}".format(Grass_essence.name))
        player.inventory.append(Grass_essence)

#Old hut
  if player.location == Old_hut:
    if verb == "investigate" and noun == "ruin_guardian":
      print("You investigated the destroyed ruin guardian and inside it you found a glowing heart of it. Also known as the core")
      player.inventory.append(guardian_core)


        

