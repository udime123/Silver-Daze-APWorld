# Silver Daze APWorld
Welcome to the Silver Daze APWorld! This will allow you to create a multiworld with Silver Daze.
To play it, [you'll need your own copy of Silver Daze.](https://store.steampowered.com/app/2912770/Silver_Daze/)

# Quick Install Instructions
-Place the ArchipelagoSilverDaze.json file in the www folder of your Silver Daze install path.
-open the game, select New Game, then Archipelago.
-It'll ask you to enter your host, room number, and player name.
-Give it a couple seconds, and you're in!



# In Depth Install Instructions
Silver Daze Archipelago only works on Silver Daze version GOLD 1.4.1 or later. If your game isn't up to date, please update it before installing this APWorld.
This APWorld was created for Archipelago version 0.6.4 and may not be compatible with earlier versions. [Click here to install the latest version of Archipelago.](https://github.com/ArchipelagoMW/Archipelago/releases)

To begin, download the ArchipelagoSilverDaze.json file.
Open up your install directory for Silver Daze and place this file into the WWW folder.
This file doesn't do anything on its own, except inform the game that it can play Archipelago.
Now that the game is set up, we can install your APWorld.

Download the silverdaze.apworld file and open your Archipelago install.
Select "Install APWorld", then navigate to the location of your silverdaze.apworld and select it.
To create a yaml, select Generate Template Options, then navigate to the "Players/Templates" folder in your Archipelago install.
Finally, open up the Silver Daze.yaml file and edit your settings to suit your preferences.

### How To Generate A Game
Collect the .yaml files for each player and place them in the Players folder in your Archipelago install.
Then, open the launcher and select "Generate". This will open a terminal which will begin generating your game.
If nothing went wrong, the terminal will close on its own, and a .zip file will appear in your Output folder.

### Hosting A Game
To host a game, go to the [Archipelago Hosting Page](https://archipelago.gg/uploads) and click "Upload File".
Navigate to your Output folder and select the .zip file you generated. When given the option, select "Create Room".
This will bring you to a room where you can connect to the server to play the generated game. Share the room's link with all players.

### Connecting Your Game
Open up Silver Daze and select New Game.
The game will give you a few options. Select "Archipelago".
Now, the game will ask you to enter the host name. If you are hosting your game on the Archipelago server, simply press Enter to skip to the next step.
Next, you'll be asked your room number. This is the five digit number at the end of the server address.
Finally, you'll be asked your player name. Simply enter the name associated with your slot in the room.

# Options
### Minibosses
This option prevents important items from being associated with the card drops for minibosses. Some runs may require you still defeat certain minibosses to progress if they're blocking your path.

### Wardens
This option prevents important items from being associated with the Key and Card drops from Wardens. Since all Wardens are completely optional, you can choose not to fight them at all if this setting is false.
This setting treats the final battle against Griffin as a Warden.

### Chaos Wardens
This option prevents important items from being associated with the Fragment and Card drops from Wardens. Since all Chaos Wardens are completely optional, you can choose not to fight them at all if this setting is false.
This setting treats the Purple Hippo as a Chaos Warden.

### Omni
This option prevents important items from being associated with the FCard drops from Omni. Since Omni is completely optional, you can choose not to fight them at all if this setting is false.

### Shops
This option prevents important items from being associated with shops.

### ReCollections
This options prevents important items from being associated with the rewards at the end of ReCollections. The checks for unlocking ReCollections are sitll included in the pool.

### Starstuds
This option prevents important items from being associated with Starstuds.

# FAQ
### How do I get hints?
-At the moment, it is recommended that you play this game alongside the Generic Client, as Silver Daze currently does not have a native way to send messages or request hints.

### What happens if I disconnect?
-The game will remember your room number when you save. As long as your room number doesn't change, you can use these settings to quickly connect.

### What happens to the locations I exclude in my options?
-Excluded locations from your options will cause those slots to be filled with random cards.

### The item I need is in the shop but I can't find it.
-Shops in the randomizer obtain new stock every time you get a new party member. All 59 shop items will only be available if you have seven party members.

### I haven't gotten my item yet while I'm in a battle.
-Items will not be given to you during battle. Leaving combat will cause items to be delivered to you.

### Are enemy drops shuffled?
-Enemy drops are not currently included in the multiworld pool, but they are randomized.

### Is there Deathlink support?
-Deathlink is in development.




# Archipelago Information

# [Archipelago](https://archipelago.gg) ![Discord Shield](https://discordapp.com/api/guilds/731205301247803413/widget.png?style=shield) | [Install](https://github.com/ArchipelagoMW/Archipelago/releases)

Archipelago provides a generic framework for developing multiworld capability for game randomizers. In all cases,
presently, Archipelago is also the randomizer itself.

Currently, the following games are supported:

* The Legend of Zelda: A Link to the Past
* Factorio
* Subnautica
* Risk of Rain 2
* The Legend of Zelda: Ocarina of Time
* Timespinner
* Super Metroid
* Secret of Evermore
* Final Fantasy
* VVVVVV
* Raft
* Super Mario 64
* Meritous
* Super Metroid/Link to the Past combo randomizer (SMZ3)
* ChecksFinder
* Hollow Knight
* The Witness
* Sonic Adventure 2: Battle
* Starcraft 2
* Donkey Kong Country 3
* Dark Souls 3
* Super Mario World
* Pokémon Red and Blue
* Hylics 2
* Overcooked! 2
* Zillion
* Lufia II Ancient Cave
* Blasphemous
* Wargroove
* Stardew Valley
* The Legend of Zelda
* The Messenger
* Kingdom Hearts 2
* The Legend of Zelda: Link's Awakening DX
* Adventure
* DLC Quest
* Noita
* Undertale
* Bumper Stickers
* Mega Man Battle Network 3: Blue Version
* Muse Dash
* DOOM 1993
* Terraria
* Lingo
* Pokémon Emerald
* DOOM II
* Shivers
* Heretic
* Landstalker: The Treasures of King Nole
* Final Fantasy Mystic Quest
* TUNIC
* Kirby's Dream Land 3
* Celeste 64
* Castlevania 64
* A Short Hike
* Yoshi's Island
* Mario & Luigi: Superstar Saga
* Bomb Rush Cyberfunk
* Aquaria
* Yu-Gi-Oh! Ultimate Masters: World Championship Tournament 2006
* A Hat in Time
* Old School Runescape
* Kingdom Hearts 1
* Mega Man 2
* Yacht Dice
* Faxanadu
* Saving Princess
* Castlevania: Circle of the Moon
* Inscryption
* Civilization VI
* The Legend of Zelda: The Wind Waker
* Jak and Daxter: The Precursor Legacy
* Super Mario Land 2: 6 Golden Coins
* shapez
* Paint
* Celeste (Open World)
* Choo-Choo Charles
* APQuest

For setup and instructions check out our [tutorials page](https://archipelago.gg/tutorial/).
Downloads can be found at [Releases](https://github.com/ArchipelagoMW/Archipelago/releases), including compiled
windows binaries.

## History

Archipelago is built upon a strong legacy of brilliant hobbyists. We want to honor that legacy by showing it here.
The repositories which Archipelago is built upon, inspired by, or otherwise owes its gratitude to are:

* [bonta0's MultiWorld](https://github.com/Bonta0/ALttPEntranceRandomizer/tree/multiworld_31)
* [AmazingAmpharos' Entrance Randomizer](https://github.com/AmazingAmpharos/ALttPEntranceRandomizer)
* [VT Web Randomizer](https://github.com/sporchia/alttp_vt_randomizer)
* [Dessyreqt's alttprandomizer](https://github.com/Dessyreqt/alttprandomizer)
* [Zarby89's](https://github.com/Ijwu/Enemizer/commits?author=Zarby89)
  and [sosuke3's](https://github.com/Ijwu/Enemizer/commits?author=sosuke3) contributions to Enemizer, which make up the
  vast majority of Enemizer contributions.

We recognize that there is a strong community of incredibly smart people that have come before us and helped pave the
path. Just because one person's name may be in a repository title does not mean that only one person made that project
happen. We can't hope to perfectly cover every single contribution that lead up to Archipelago, but we hope to honor
them fairly.

### Path to the Archipelago

Archipelago was directly forked from bonta0's `multiworld_31` branch of ALttPEntranceRandomizer (this project has a
long legacy of its own, please check it out linked above) on January 12, 2020. The repository was then named to
_MultiWorld-Utilities_ to better encompass its intended function. As Archipelago matured, then known as
"Berserker's MultiWorld" by some, we found it necessary to transform our repository into a root level repository
(as opposed to a 'forked repo') and change the name (which came later) to better reflect our project.

## Running Archipelago

For most people, all you need to do is head over to
the [releases page](https://github.com/ArchipelagoMW/Archipelago/releases), then download and run the appropriate
installer, or AppImage for Linux-based systems.

If you are a developer or are running on a platform with no compiled releases available, please see our doc on
[running Archipelago from source](docs/running%20from%20source.md).

## Related Repositories

This project makes use of multiple other projects. We wouldn't be here without these other repositories and the
contributions of their developers, past and present.

* [z3randomizer](https://github.com/ArchipelagoMW/z3randomizer)
* [Enemizer](https://github.com/Ijwu/Enemizer)
* [Ocarina of Time Randomizer](https://github.com/TestRunnerSRL/OoT-Randomizer)

## Contributing

To contribute to Archipelago, including the WebHost, core program, or by adding a new game, see our
[Contributing guidelines](/docs/contributing.md).

## FAQ

For Frequently asked questions, please see the website's [FAQ Page](https://archipelago.gg/faq/en/).

## Code of Conduct

Please refer to our [code of conduct](/docs/code_of_conduct.md).
