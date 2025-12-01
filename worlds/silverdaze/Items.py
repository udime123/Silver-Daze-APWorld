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
    "Kappa": ItemData(230),
    "Unicorn": ItemData(187),
    "Cyclops": ItemData(292),
    "Phoenix": ItemData(86),
    "Pulgasari": ItemData(345),
    "Pixie": ItemData(137),
    "Variacut": ItemData(30),
    "Morning Ray": ItemData(7),
    "Zoner": ItemData(304),
    "Cold As Ice": ItemData(5),
    "Strife": ItemData(6),
    "RATD": ItemData(4, ItemClassification.useful, "Card", 2),
}

keys = {
    "Yellow Key": ItemData(2010, ItemClassification.progression, "Key"),
    "Green Key": ItemData(2011, ItemClassification.progression, "Key"),
    "Blue Key": ItemData(2012, ItemClassification.progression, "Key"),
    "Purple Key": ItemData(2013, ItemClassification.progression, "Key"),
    "Red Key": ItemData(2014, ItemClassification.progression, "Key"),
    "Orange Key": ItemData(2015, ItemClassification.progression, "Key"),
    "Black Key": ItemData(2016, ItemClassification.progression, "Key"),

    "Blue_Zone()": ItemData(2018, ItemClassification.progression, "Glitch"),
    "._locale": ItemData(2019, ItemClassification.progression, "Glitch"),

    ".Memfinder": ItemData(2009, ItemClassification.progression, "Memfinder"),

    "Red Fragment": ItemData(2022, ItemClassification.progression, "Fragment"),
    "Orange Fragment": ItemData(2023, ItemClassification.progression, "Fragment"),
    "Yellow Fragment": ItemData(2024, ItemClassification.progression, "Fragment"),
    "Green Fragment": ItemData(2025, ItemClassification.progression, "Fragment"),
    "Blue Fragment": ItemData(2026, ItemClassification.progression, "Fragment"),
    "Purple Fragment": ItemData(2027, ItemClassification.progression, "Fragment"),
    "Black Fragment": ItemData(2028, ItemClassification.progression, "Fragment"),
}

consumables = {
    "Heal Token": ItemData(2002, ItemClassification.filler, "Filler", 5),
    "Evade Token": ItemData(2003, ItemClassification.filler, "Filler", 1),
    "Hi-Heal Token": ItemData(2004, ItemClassification.filler, "Filler", 1),
    # Tent Token Here
    "Sneak Token": ItemData(2006, ItemClassification.filler, "Filler", 1),
}

starstuds = {
    "Starstud": ItemData(None, ItemClassification.progression, "Event", 25)
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

#Sawyer: Make a random starting member.
def get_random_member(world: SDWorld) -> SDItem:
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
    return starty_member
    #members.remove(starty_member)

def create_all_items(world: SDWorld):
    itempool = []

    for name in item_table:
        itempool.append(world.create_item(name))

    # Starting Party Member given at game start
    #if world.options.starting_party_member:
    itempool.remove(get_random_member(world))

    # other steps here maybe

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


def create_item(self, name: str) -> SDItem:
    item_data = item_table[name]
    item = SDItem(name, item_data.classification, item_data.code, self.player)
    return item