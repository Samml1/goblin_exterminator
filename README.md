# goblin_exterminator
Python project for learning all sorts

At tthe end of this project this should hopefuly be a functioning text
adventure game written in Python where the goal is to travel accross
the lands exterminating goblins.

**Game Commands:**

After entering your name the following commands are available:

- enter dungeon
- view stats
- equip weapon (this was for testing purposes)
- new game (Will reset game to enter Name screen - was for testing purposes)
- q (This will terminate the program)


When selecting enter dungeon the following option is available:
- "goblin_cave" // "goblin cave"
  - This is the only dungeon available currently

Upon entering the dungeon the following commands are available:
- view stats (displays the player objects current stats)
- describe (describes the room the player is currently in)
- location (Outputs the name of the room the player is currently in)
- exit (leaves the dungeon)
  - only usable in the dungeon entrance or other tagged room as exit
- cardinal directions (this is how you traverse the dungeon)
  - north
  - east
  - south
  - west
- q (This will terminate the program)
- pickup item (This was implemented and then not much progress made on items)
  - this will give you a sub-option to type in the item name




**TO DO:**
- ~~create yml format to create dungeons programatically~~
  - ~~read yml format using pyYaml or other lib~~
- segment and compartmentalise the codebase to prevent it from becoming too unweildy
- create more dungeons
- create enemy class
- combat function for random encounters:
  - create XP system
  - create more stats for the player and enemies
  - create different weapons to use
  - create loot system
- ~~update player class to have HP and stats~~


Reference list:
List of all sources I have taken inspiration from:
- https://gist.github.com/wynand1004/bf8b5965271687b89ab24410ce0f0fc4 - used to design exit system in room class
- https://www.youtube.com/CodeWithHuw - Used to get inspiration for how to create room class structure
