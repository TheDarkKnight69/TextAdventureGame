import print_slow as ps
import adventure_game

typing_speed = 75  # Adjust the typing speed (characters per second)


def help():
    ps.print_slow(
        """
----- Help -----
Basic Instructions:
- To navigate, use commands like "go north" or "move south."
- Interact with objects using commands like "take key" or "examine sword."
- Check your inventory by typing "inventory" or "i."

Type specific commands or actions to explore and progress through the game.


-----------------------------
Available Commands:
- "go [direction]" to move in a specific direction.
- "take [item]" to pick up an item.
- "examine [object]" to get more information about an object.
- "use [item]" to interact with an item or use it in a specific context.
- "talk [character]" to initiate a conversation with a character.

Use these commands creatively to progress through the game and solve puzzles!

------------------------
Additional Tips:
- Explore thoroughly and examine your surroundings. You never know what you might find!
- Keep track of clues and important information by taking notes.
- Talk to characters to gather information and uncover secrets.

Adventure awaits! Feel free to consult the help anytime you need assistance.
Good Luck!
    
    """
    )


text_adventure_intro = """
You find yourself in a mysterious world full of adventure, creatures, treasure 
and challenges. 
Your mission is to recover an ancient key stolen from your family that had been 
guarding it for centuries. It is said that it can bring peace to entire realms, if 
used by anyone worthy. No one has been able to use it for almost 400 years. Will you
be the one to bring peace to your war-stricken land? 
As you explore, you will encounter various location, interact with objects, 
and meet intriguing characters.
Are you ready to embark on this exciting journey?  (Y/N) 
  
  
Type 'help' for instructions on how to play.
"""
print("Welcome to your Text-Based Adventure Game!")
print("---------------------------------------------")
print("\n")
ps.print_slow(text_adventure_intro)

conf = input(">>> ").lower()
if conf == "y":
    print("Enter the name of your character: ")
    character_name = input(">>> ").split(" ")
    a = character_name[0].capitalize()
    b = character_name[1].capitalize()
    if len(character_name) > 2:
        c = character_name[2].capitalize()
        character_name = a + " " + b + " " + c
    else:
        character_name = a + " " + b
    print("-----------------------")
    print(
        f"""You are a brave warrior {character_name}. 
{character_name}, born to a lineage of noble knights, possesses a valiant 
spirit and an unwavering sense of honor. Trained by the legendary Sir Lancelot
himself, he embarks on a quest to recover the lost artifact that holds the key to
restoring peace to the realm."""
    )
    print("Let us start.")
    adventure_game.game()
elif conf == "help":
    help()
