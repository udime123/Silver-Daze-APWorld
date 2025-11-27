from __future__ import annotations

from typing import TYPE_CHECKING
import typing

from BaseClasses import Item, ItemClassification

from worlds.AutoWorld import World, WebWorld

if TYPE_CHECKING:
    from .World import SDWorld

#Sawyer: This time I said screwit and went with the old system we already had, hopefully it works.
#Sawyer: The APQuest version looked mean and scary but we can do it if we must.

class SDItem(Item):
    game = "Silver Daze"


class ItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.filler
    category: str = 'Card'
    max_quantity: int = 1
    weight: int = 1


# Item groups for easy management

party_members = {
    "Pinn": ItemData(3001, ItemClassification.progression, "Party"),
    "Geo": ItemData(3002, ItemClassification.progression, "Party"),
    "Kani": ItemData(3003, ItemClassification.progression, "Party"),
}

mp3s = {
    "Freddie Freeloader": ItemData(1063, ItemClassification.useful, "MP3"),
    "Flossophy": ItemData(1044, ItemClassification.useful, "MP3"),
    "Big Shot": ItemData(1003, ItemClassification.useful, "MP3"),
    "Triage": ItemData(1065, ItemClassification.useful, "MP3"),
    "The Sign": ItemData(1045, ItemClassification.useful, "MP3"),
    "Wet Hands": ItemData(1010, ItemClassification.useful, "MP3"),
    "Move": ItemData(1001, ItemClassification.useful, "MP3"),
    "Low Ride": ItemData(1042, ItemClassification.useful, "MP3"),
    "Lost In Thought": ItemData(1062, ItemClassification.useful, "MP3"),
}

# In Visual Studio Code or another IDE you can collapse the dict to hide the cards
cards = {
    "Ultima": ItemData(352),
    "Finish Touch": ItemData(42),
    "Valor Drive": ItemData(25),
    "Sonic Boom": ItemData(29),
    "Hopscotch": ItemData(154),
    "CoffeBrek": ItemData(155),
    "Fine Tune": ItemData(256),
    "SmokeBreak": ItemData(311),
    "PowerNap": ItemData(72),
    "Flatten": ItemData(18),
    "Dragon": ItemData(31),
    "Variacut": ItemData(30),
    "Morning Ray": ItemData(7),
    "Zoner": ItemData(304),
    "Cold As Ice": ItemData(5),
    "Strife": ItemData(6),
    "RATD": ItemData(4, ItemClassification.useful, "Card", 2),
}

keys = {
    "Yellow Key": ItemData(2010, ItemClassification.progression, "Key"),
    "Red Key": ItemData(2014, ItemClassification.progression, "Key"),
}

consumables = {
    "Heal Token": ItemData(2002, ItemClassification.filler, "Filler", 5),
    "Evade Token": ItemData(2003, ItemClassification.filler, "Filler", 1),
    "Hi-Heal Token": ItemData(2004, ItemClassification.filler, "Filler", 1),
    # Tent Token Here
    "Sneak Token": ItemData(2006, ItemClassification.filler, "Filler", 1),
}

#Sawyer: This should give us some random fillers. Let's look into adding traps later.
def get_random_filler_item_name(world: SDWorld) -> str:
    fillers = ["Evade Token", "Sneak Token"]
    randomResult = world.random.randint(0, len(fillers) - 1)
    return fillers[randomResult]

item_table = {
    # This includes all entries in those other dicts in this one
    **party_members,
    **cards,
    **mp3s,
    **keys,
    **consumables,

    # Events - Note that these are items!

    # Other Items
    #  "Sneak Token":          ItemData(2006,       ItemClassification.filler, "Filler",   1),
}

# def create_item_with_correct_classification(world: SDWorld, name: str) -> SDItem:
#     item_data = item_table[name]
#     return SDItem(name, item_data.classification, item_data.code, self.player)


#Sawyer: Make a random starting member.
def get_random_member(world: SDWorld):
    #Sawyer: First we get the keys (names of the values) from the party member list.
    members = [key for key, val in party_members.items()]
    #Sawyer: Then we get a random number from the length of that list.
    randomResult = world.random.randint(0, len(members) - 1)
    #Sawyer: Then we get the member belonging to that random number we picked.
    member_name = members[randomResult]
    starty_member = world.create_item(member_name)
    #Next we grab the PinnJoin location which is where the first party member is always given.
    location = world.multiworld.get_location("PinnJoin", world.player)
    #Finally, add it to the location.
    location.place_locked_item(starty_member)

def create_all_items(world: SDWorld):
    itempool = []

    for name in item_table:
    #for name, max_quantity in item_table:
    #    itempool += world.create_item(name)
    #    itempool += [name] * max_quantity
        itempool.append(world.create_item(name))

    # Starting Party Member given at game start

    #Sawyer: I commented this out so we can just give you a random party member.
    #starter_member = "Pinn"
    #if (world.options.starting_party_member == "geo"):
    #    starter_member = "Geo"
    #if (world.options.starting_party_member == "kani"):
    #    starter_member = "Kani"

    #starter_member = get_random_member(world)
    get_random_member(world)

    #itempool.remove(starter_member)
    # Sawyer: Add starter party member at the end.
    #starting_party_member = world.create_item(starter_member)
    #world.multiworld.push_precollected(starting_party_member)


    # other steps here maybe

    # Create Items
    # itempool = [item for item in map(lambda name: world.create_item(name), itempool)]
    # # Fill remaining items with randomly generated junk
    # while len(itempool) < len(world.multiworld.get_unfilled_locations(world.player)):
    #     itempool.append(world.get_random_filler_item_name())

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
    #world.multiworld.itempool += [world.create_item(itemname) for itemname in itempool]


def create_item(self, name: str) -> SDItem:
    item_data = item_table[name]
    item = SDItem(name, item_data.classification, item_data.code, self.player)
    return item