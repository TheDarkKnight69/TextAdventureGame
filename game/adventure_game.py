import json
import random
import print_slow as ps

global message_history
message_history = ["You notice a shimmering portal opening before you. What do you do?"]
go_statements_outside = [
    "You find a chest hidden in the bushes. What do you do?",
    "A group of hostile bandits block your path. What do you do?",
    "You discover a forgotten diary on the ground. What do you do?",
    "A friendly stranger approaches you with a map. What do you do?",
    "There are footprints leading into a dark cave. What do you do?",
    "A pack of wild wolves emerges from the forest. What do you do?",
    "You find a torn piece of a map on the ground. What do you do?",
    "You notice a shimmering portal opening before you. What do you do?",
    "You discover a hidden underground cave. What do you do?",
    "You encounter a wise old hermit offering advice. What do you do?",
    "There are mysterious symbols etched into the ground. What do you do?",
    "You stumble upon a hidden campsite. What do you do?",
    "You notice a distant glimmer of light in the dark forest. What do you do?",
]

take_statements = [
    (
        """
You cautiously reach out to grab the sword, but a hidden trap is triggered, 
causing the sword to fall into a pit. You fail to acquire the sword.
        """,
        0.6,
    ),
    (
        """
With precise timing and agility, you deftly grab the sword before the trap 
is triggered. You pass and successfully acquire the sword!
        """,
        0.4,
    ),
    (
        """
As you attempt to snatch the key, a mechanism is triggered, and the key is 
launched into the air, just out of your reach. You fail to acquire the key.
        """,
        0.7,
    ),
    (
        """
Your keen observation pays off as you locate a hidden compartment containing 
the key. You pass and obtain the key!
        """,
        0.2,
    ),
    (
        """
You confidently grab the sword from its display, but a magical enchantment 
causes it to slip through your fingers, landing back in its original position. 
You fail to acquire the sword.
        """,
        0.4,
    ),
    (
        """
You carefully navigate the complex mechanism guarding the sword and manage 
to retrieve it without triggering any traps. You pass and acquire the sword!
        """,
        0.5,
    ),
    (
        """
You skillfully reach for the key, but it turns out to be a cleverly 
disguised decoy, leaving you empty-handed. You fail to acquire the key.
        """,
        0.4,
    ),
    (
        """
By employing your exceptional sleight of hand, you swiftly snatch the key 
without setting off any alarms. You pass and obtain the key!
        """,
        0.8,
    ),
    (
        """
Just as you are about to grab the sword, a hidden trap is triggered, causing 
the sword to fall into a pit. You fail to acquire the sword.
        """,
        0.2,
    ),
    (
        """
Your calculated approach and knowledge of ancient lore allow you to retrieve 
the sword without triggering any protective enchantments. You pass and acquire 
the sword!
        """,
        0.4,
    ),
]

words_list = ["to", "over", "the"]
global INVENTORY_PATH
INVENTORY_PATH = "/workspaces/TextAdventureGame/game/inventory.json"


def save_game():
    try:
        with open(INVENTORY_PATH, "w", encoding="utf-8") as file:
            json.dump(file)
    except Exception as e:
        print(e)


def load_inventory():
    try:
        with open(INVENTORY_PATH, "r", encoding="utf-8") as file:
            inven = json.load(file)
            return inven
    except FileNotFoundError as e:
        print(e)


global inventory
inventory = load_inventory()


def context(string):
    if "chest" in string:
        ps.print_slow("\nPossible choices: [open, leave, investigate]")
    elif "bandits" in string or "wolves" in string:
        ps.print_slow("\nPossible choices: [kill]")
    elif "map" in string or "diary" in string:
        ps.print_slow("\nPossible choices: [take]")
    elif "cave" in string or "campsite" in string:
        ps.print_slow("\nPossible choices: [enter, ignore]")
    elif "portal" in string or "light" in string or "symbols" in string:
        ps.print_slow("\nPossible choices: [investigate]")
    elif "hermit" in string:
        ps.print_slow("\nPossible choices: [talk]")


def inv():
    ps.print_slow("Your Bag: ")
    for i in inventory():
        print(i)


def text_parser(string):
    verb = string[0]
    noun = string[2] if len(string) > 2 and string[1] in words_list else string[1]

    if verb == "go" or verb == "move":
        if noun in ["north", "south", "east", "west", "forward"]:
            b = random.choice(go_statements_outside)
            if b == message_history[-1]:
                d = random.choice(go_statements_outside)
                ps.print_slow(d)
                context(d)
                message_history.append(d)
            else:
                ps.print_slow(b)
                context(b)
                message_history.append(b)
        else:
            ps.print_slow("Unknown direction. Try again.")

    elif verb == "take":
        if noun == "sword":
            tat = "hii"
            if message_history[-1] == tat:
                statement, success_rate = random.choices(take_statements)
                if random.random() < success_rate:
                    ps.print_slow(statement)
                    message_history.append(statement)
                    ps.print_slow("Sword added to inventory.")
                    inventory.append(noun)
                else:
                    ps.print_slow(statement)
            else:
                ps.print_slow("There are no swords around. What are you doing?")
        elif noun == "key":
            tat = "hii"
            if message_history[-1] == tat:
                statement, success_rate = random.choices(take_statements)
                if random.random() < success_rate:
                    ps.print_slow(statement)

                    ps.print_slow("Key added to inventory.")
                    inventory.append(noun)
                else:
                    ps.print_slow(statement)
        elif noun == "map":
            b = "A friendly stranger approaches you with a map. What do you do?"
            c = "You find a torn piece of a map on the ground. What do you do?"
            if message_history[-1] == b or message_history[-1] == c:
                a = [
                    """
You take the map. It has an X marked on it which might lead to a 
treasure. Who knows?
""",
                    """
You try reading the map but you don't understand it. 
You shake your head and move on.
""",
                ]
                ps.print_slow(random.choice(a))
            else:
                ps.print_slow("There is no map around.. ???")
        elif noun == "diary":
            b = "You discover a forgotten diary on the ground. What do you do?"
            if message_history[-1] == b:
                a = [
                    """
The diary has notes on the ancient ruins. You glance at it but 
you already know all about it.
                    """,
                    """
The diary has a huge penis drawn on it
                    """,
                    """
The diary has some spells written on it. Too bad you're not a mage.
                    """,
                    """
The diary is blank.
                    """,
                ]
                ps.print_slow(random.choice(a))
            else:
                ps.print_slow("There is no diary around.... Are you okay??")
        else:
            ps.print_slow("Unknown Item")
    elif verb == "enter":
        if noun == "cave":
            b = "You discover a hidden underground cave. What do you do?"
            c = "There are footprints leading into a dark cave. What do you do?"
            if message_history[-1] == b or message_history[-1] == c:
                ps.print_slow(
                    """
You enter the cave. It is very dim so your vision is limited.
There is nothing interesting in this cave. You exit the cave.
"""
                )
            else:
                ps.print_slow("There are no caves nearby...")
        if noun == "campsite":
            b = "You stumble upon a hidden campsite. What do you do?"
            if message_history[-1] == b:
                a = [
                    """
The campsite is dead. There is no one around, not even a 
spark of fire. You leave.                     
                    """,
                    """
The campsite is full of travellers. They look at you strangely, almost as if with pity.
You run out embarassed.
                    """,
                    """
The campsite is dead. There is no one around, not even a 
spark of fire. You go around looking at the tents and in
one of them you find a chest. You open it and you find a piece of armor.
                    """,
                ]
                c = ps.print_slow(random.choice(a))
                if c == a[2]:
                    ps.print_slow("Armor added to Inventory. ")
                    inventory.append("Armor       x1")
            else:
                ps.print_slow("There is no campsite to enter around.")
        if noun == "portal":
            a = "You notice a shimmering portal opening before you. What do you do?"
            if message_history[-1] == a:
                b = [
                    """
You enter the portal. You find yourself blinded by the pure white light around you.
You grope around and get sucked into another portal but this one leads back to where you
got sucked in.
                        """,
                    """
You enter the portal. You find yourself in a beautiful world. There are 
magical creatures everywhere. Things that you only heard in stories are now standing
infront of you. You go a bit farther and you are greeted by a dwarf who hands you a
chest. He bows and goes away. You open the chest.
                        """,
                    """
You get sucked into the portal and are spit out into a fiery world. Luckily you spot a
portal nearby and get into it. It throws you back to where you got sucked in.
                        """,
                ]
                d = random.choice(b)
                ps.print_slow(d)
                if d == b[1]:
                    t = ["Armor", "Sword"]
                    ps.print_slow(random.choice(t))
            else:
                ps.print_slow("There is no portal nearby. ")
    elif verb == "ignore":
        if noun == "cave":
            b = "You discover a hidden underground cave. What do you do?"
            c = "There are footprints leading into a dark cave. What do you do?"
            if message_history[-1] == b or message_history[-1] == c:
                ps.print_slow("You ignore the cave and move on your path.")
            else:
                ps.print_slow("There are no caves for you to ignore")
        if noun == "campsite":
            b = "You stumble upon a hidden campsite. What do you do?"
            if message_history[-1] == b:
                ps.print_slow("You ignore the campsite and move on your path.")
            else:
                ps.print_slow("There are no campsites for you to ignore")
    elif verb == "kill":
        if noun == "bandits":
            b = "A group of hostile bandits block your path. What do you do?"
            if message_history[-1] == b:
                a = [
                    "The bandits got scared and ran away!",
                    """
Most of the bandits ran away but one was foolish enough to stay. 
You slaughtered him.
                    """,
                ]
                ps.print_slow(random.choice(a))
            else:
                ps.print_slow("There are no bandits nearby.... You look so dumb.")
        elif noun == "wolf" or noun == "wolves":
            b = "A pack of wild wolves emerges from the forest. What do you do?"
            if message_history[-1] == b:
                a = [
                    """
The wolf lunges at you but you raise your sword and 
it goes through it.
                    """,
                    "The wolf runs away. ",
                    "The wolf bites you but you soldier through and stab it.",
                ]
                ps.print_slow(random.choice(a))
            else:
                ps.print_slow("There are no wolves nearby. Why are you dumb?")
        else:
            ps.print_slow("There is nothing for you to stab.")

    elif verb == "investigate":
        if noun == "light":
            b = "You notice a distant glimmer of light in the dark forest. What do you do?"
            if message_history[-1] == b:
                ps.print_slow(
                    """
Curiosity piques your interest as you approach the source of the light."""
                )
                ps.print_slow("Choose an action:\n")
                ps.print_slow("1. Investigate the light\n")
                ps.print_slow("2. Proceed with caution\n")
                ps.print_slow("3. Ignore the light and continue your path\n")

                action_choice = input(
                    "Enter the number of the action you want to take: \n"
                )

                if action_choice == "1":
                    ps.print_slow(
                        """
You cautiously make your way towards the light, drawn by its mysterious allure.\n"""
                    )
                elif action_choice == "2":
                    ps.print_slow(
                        """
Aware of potential dangers, you proceed with caution towards the glimmer of light.\n"""
                    )
                elif action_choice == "3":
                    ps.print_slow(
                        """
Deciding to focus on your original path, you ignore the distant glimmer and move on."""
                    )
                else:
                    ps.print_slow(
                        """
You stand there, contemplating the significance of the distant glimmer of light.\n"""
                    )
            else:
                ps.print_slow(
                    """
There is no distant glimmer of light in the dark forest. 
Perhaps it was just a trick of the eye."""
                )
        if noun == "symbol" or noun == "symbols":
            b = "There are mysterious symbols etched into the ground. What do you do?"
            if message_history[-1] == b:
                ps.print_slow("You closely examine the  intricate symbols.\n")
                ps.print_slow("Choose an action:\n")
                ps.print_slow("1. Decipher the symbols\n")
                ps.print_slow("2. Trace the symbols with your finger\n")
                ps.print_slow("3. Draw a sketch of the symbols\n")

                action_choice = input(
                    "Enter the number of  the action you want to take: \n"
                )

                if action_choice == "1":
                    ps.print_slow(
                        "You try to decipher the symbols, but their meaning eludes you.\n"
                    )
                elif action_choice == "2":
                    ps.print_slow(
                        """You trace the symbols with your finger, feeling a faint 
energy.\n"""
                    )
                elif action_choice == "3":
                    ps.print_slow(
                        "You sketch the symbols, hoping to study them later.\n"
                    )
                else:
                    ps.print_slow(
                        "You stand there, captivated by the enigmatic symbols.\n"
                    )
            else:
                ps.print_slow(
                    "There are no symbols around. Perhaps you imagined them.\n"
                )
    elif verb == "talk" or verb == "speak":
        if noun == "hermit":
            b = "You encounter a wise old hermit offering advice. What do you do?"

            if message_history[-1] == b:
                ps.print_slow("The hermit looks at you attentively.\n")
                ps.print_slow("Choose a topic to discuss:\n")
                ps.print_slow("1. Life's purpose\n")
                ps.print_slow("2. Finding inner peace\n")
                ps.print_slow("3. Overcoming challenges\n")
                ps.print_slow("4. Secrets of nature\n")

                topic_choice = input(
                    "Enter the number of the topic you want to discuss: \n"
                )

                if topic_choice == "1":
                    ps.print_slow(
                        "The hermit shares profound insights about the purpose of life."
                    )
                elif topic_choice == "2":
                    ps.print_slow(
                        """
The hermit imparts wisdom on finding inner peace in a 
chaotic world.\n
                        """
                    )
                elif topic_choice == "3":
                    ps.print_slow(
                        """
The hermit offers advice on overcoming challenges with resilience.\n"""
                    )
                elif topic_choice == "4":
                    ps.print_slow(
                        """
The hermit reveals ancient secrets about the interconnectedness of nature.\n"""
                    )
                else:
                    ps.print_slow(
                        """
The hermit looks at you with a gentle smile, but stays silent.\n"""
                    )

                # Update message history with the topic choice

            else:
                ps.print_slow("There is no hermit around. Are you hallucinating?")
        else:
            ps.print_slow("You can't talk to that.")

    elif verb == "open":
        if noun == "chest":
            b = "You find a chest hidden in the bushes. What do you do?"

            if message_history[-1] == b:
                ps.print_slow("You cautiously open the chest...")
                ps.print_slow("You find a shiny gem inside!")
            else:
                ps.print_slow("There is no chest around")

    elif verb == "leave":
        if noun == "chest":
            b = "You find a chest hidden in the bushes. What do you do?"

            if message_history[-1] == b:
                ps.print_slow("You decide to leave the chest untouched.")

            else:
                ps.print_slow("There is no chest around")

    elif verb == "investigate":
        if noun == "chest":
            b = "You find a chest hidden in the bushes. What do you do?"

            if message_history[-1] == b:
                ps.print_slow("You carefully examine the surroundings...")
                ps.print_slow(
                    "You notice faint footprints leading away from the chest."
                )
            else:
                ps.print_slow("There is no chest around")

        else:
            ps.print_slow("Unknown command.")
    elif string == "inventory":
        inv()
    elif verb == "save":
        if noun == "game":
            save_game()


def game():
    ps.print_slow(
        """
You open your eyes and find yourself lying on the floor in the forest.
Your sword is beside you.

Enter 'take sword' to proceed."""
    )
    while True:
        character_input = input("\n>>> ").lower()
        if character_input != "take sword":
            ps.print_slow("Wrong Input")
        else:
            ps.print_slow("Sword added to inventory.")
            inventory["weapons"] = "Sword"
            break
    ps.print_slow(
        """
You now have a sword. Use it to fight monsters and wild animals. 
You proceed further along the jungle."""
    )
    i = 0
    while i != 14:
        character_input = input("\n>>> ").lower().strip().split()
        text_parser(character_input)
        i += 1
        if i == 13:
            ps.print_slow("\nYou move along the road.")
            i += 1

    ps.print_slow(
        "\nYou stumble along a dark cave. Maybe this cave will hold some treasures.\n"
    )
    ps.print_slow("What do you do?\n")


game()
