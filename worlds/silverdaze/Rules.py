from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from .Items import party_members

if TYPE_CHECKING:
    from .World import SDWorld


def set_all_rules(world: SDWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


#Sawyer: The following are special rule helpers for easy checking.
lookup_key_from_color = {
    "red": "Red Key",
    "orange": "Orange Key",
    "yellow": "Yellow Key",
    "green": "Green Key",
    "blue": "Blue Key",
    "purple": "Purple Key",
    "black": "Black Key"
    }

def get_key_from_color(color: str) -> str:
    # Nat: This could be made to just color.lower().capitalize() then append " Key"
    # and return, but we wanna prevent user errors in this house.
    color = color.lower()
    assert (color in lookup_key_from_color.keys()), f"Input '{color}' is not a valid key color."
    return lookup_key_from_color[color]

def sd_has_key(color: str, state: CollectionState, world: SDWorld) -> bool:
    return state.has(get_key_from_color(color), world.player)

#The Discord recommended we just make one function per key. Something something performance.
def sd_has_red(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Red Key", world.player)
def sd_has_yellow(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Yellow Key", world.player)
def sd_has_blue(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Blue Key", world.player)
def sd_has_green(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Green Key", world.player)
def sd_has_purple(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Purple Key", world.player)
def sd_has_orange(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Orange Key", world.player)
def sd_has_black(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Black Key", world.player)

def sd_has_memfinder(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Memfinder", world.player)
def sd_has_glitch(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Blue_Zone()", world.player) and state.has("._locale", world.player)

def sd_has_dragon(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Dragon", world.player)
def sd_has_kappa(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Kappa", world.player)
def sd_has_unicorn(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Unicorn", world.player)
def sd_has_cyclops(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Cyclops", world.player)
def sd_has_phoenix(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Phoenix", world.player)
def sd_has_pulgasari(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Pulgasari", world.player)
def sd_has_pixie(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Pixie", world.player)

def sd_party_size_meets(state: CollectionState, world: SDWorld, size: int) -> bool:
    # party_members is all items that are party members
    # keys is just the strings, which are item names

    return state.has_from_list_unique(party_members.keys(), world.player, size)

#This is copied from vanilla, I won't bother reconfiguring the logic.
#Basic gist is that it checks every location where a Starstud could be available and adds it to the pile.
def sd_stars(state: CollectionState, world: SDWorld, size:int) -> bool:
    stars = 0
    if lambda mystate: sd_party_size_meets(state, world,1): stars += 1
    if lambda mystate: sd_has_yellow(state, world): stars += 1
    if lambda mystate: sd_has_yellow(state, world) and sd_has_green(state, world): stars += 1

    return stars >= size


def sd_can_fight_miniboss(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,2)

def sd_can_fight_warden(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,3)

def sd_can_fight_chaos_warden(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,5)

def sd_can_fight_omni(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,7)

#End of helpers


#Sawyer: Entrance time!
def set_all_entrance_rules(world: SDWorld) -> None:
    player = world.player
    multiworld = world.multiworld
    #Sawyer: Below is a var to make it so we don't have to type CollectionState every time we wanna check a function.
    mystate = CollectionState

    #begin_new_game = world.get_entrance("Begin_New_Game")
    leave_geo_room = world.get_entrance("Leave_Geo_Room")


#Sawyer: These are the location rules! Hoo boy there are many haha
def set_all_location_rules(world: SDWorld) -> None:
    player = world.player
    multiworld = world.multiworld

    #Sawyer: Don't forget to define the locations we're adding rules to here.
    add_rule(world.get_location("Red1Chest"), lambda mystate: sd_has_red( mystate, world))
    add_rule(world.get_location("RedChasm2Chest2"), lambda mystate: sd_has_red( mystate, world))
    add_rule(world.get_location("Blue3Chest"), lambda mystate: sd_party_size_meets(mystate, world,3))
    add_rule(world.get_location("BlueCaveRightStory"), lambda mystate: sd_party_size_meets(mystate, world,3))
    add_rule(world.get_location("BlueCaveLeftStory"), lambda mystate: sd_party_size_meets(mystate, world,2))
    add_rule(world.get_location("BlueCaveLeftChest"), lambda mystate: sd_has_blue(mystate, world))
    add_rule(world.get_location("Blue7Chest"), lambda mystate: sd_party_size_meets(mystate, world,4))

    #Sawyer: Put the Starstud Rules here.
    if world.options.starstuds:
        add_rule(world.get_location("StarStud1"), lambda mystate: sd_stars(mystate, world, 1))
        add_rule(world.get_location("StarStud2"), lambda mystate: sd_stars(mystate, world, 2))
        add_rule(world.get_location("StarStud3"), lambda mystate: sd_stars(mystate, world, 3))
        add_rule(world.get_location("StarStud4"), lambda mystate: sd_stars(mystate, world, 4))
        add_rule(world.get_location("StarStud5"), lambda mystate: sd_stars(mystate, world, 5))
        add_rule(world.get_location("StarStud6"), lambda mystate: sd_stars(mystate, world, 6))
        add_rule(world.get_location("StarStud7"), lambda mystate: sd_stars(mystate, world, 7))
        add_rule(world.get_location("StarStud8"), lambda mystate: sd_stars(mystate, world, 8))
        add_rule(world.get_location("StarStud9"), lambda mystate: sd_stars(mystate, world, 9))
        add_rule(world.get_location("StarStud10"), lambda mystate: sd_stars(mystate, world, 10))
        add_rule(world.get_location("StarStud11"), lambda mystate: sd_stars(mystate, world, 11))
        add_rule(world.get_location("StarStud12"), lambda mystate: sd_stars(mystate, world, 12))
        add_rule(world.get_location("StarStud13"), lambda mystate: sd_stars(mystate, world, 13))
        add_rule(world.get_location("StarStud14"), lambda mystate: sd_stars(mystate, world, 14))
        add_rule(world.get_location("StarStud15"), lambda mystate: sd_stars(mystate, world, 15))
        add_rule(world.get_location("StarStud16"), lambda mystate: sd_stars(mystate, world, 16))
        add_rule(world.get_location("StarStud17"), lambda mystate: sd_stars(mystate, world, 17))
        add_rule(world.get_location("StarStud18"), lambda mystate: sd_stars(mystate, world, 18))
        add_rule(world.get_location("StarStud19"), lambda mystate: sd_stars(mystate, world, 19))
        add_rule(world.get_location("StarStud20"), lambda mystate: sd_stars(mystate, world, 20))
        add_rule(world.get_location("StarStud21"), lambda mystate: sd_stars(mystate, world, 21))
        add_rule(world.get_location("StarStud22"), lambda mystate: sd_stars(mystate, world, 22))
        add_rule(world.get_location("StarStud23"), lambda mystate: sd_stars(mystate, world, 23))
        add_rule(world.get_location("StarStud24"), lambda mystate: sd_stars(mystate, world, 24))
        add_rule(world.get_location("StarStud25"), lambda mystate: sd_stars(mystate, world, 25))

#Sawyer: Time for the wincon! For now it'll just be three party members but once the demo works it should be Entropy
def set_completion_condition(world: SDWorld) -> None:
    player = world.player
    multiworld = world.multiworld
    mystate = CollectionState

    world.multiworld.completion_condition[world.player] = lambda mystate: sd_party_size_meets(mystate, world,3) and sd_has_red( mystate, world)

