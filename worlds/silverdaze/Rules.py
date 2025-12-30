from __future__ import annotations

from operator import truediv
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

import Options
from .Items import party_members, redcards, orangecards, yellowcards, greencards, bluecards, purplecards, blackcards

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

#The Discord recommended we just make one function per key.
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

def sd_has_reco(state: CollectionState, world: SDWorld, num) -> bool:
    return state.has(f"ReCollection0{num}", world.player)
def sd_has_reco10(state: CollectionState, world: SDWorld) -> bool:
    return state.has("ReCollection10", world.player)

def sd_has_chaotic(state: CollectionState, world: SDWorld) -> bool:
    return (state.has("Red Fragment", world.player) and state.has("Blue Fragment", world.player) and
            state.has("Green Fragment", world.player) and state.has("Purple Fragment", world.player) and
            state.has("Black Fragment", world.player) and state.has("Orange Fragment", world.player) and
            state.has("Yellow Fragment", world.player))

def sd_party_size_meets(state: CollectionState, world: SDWorld, size: int) -> bool:
    # party_members is all items that are party members
    # keys is just the strings, which are item names
    return state.has_from_list_unique(party_members.keys(), world.player, size)

#This is copied from vanilla, I won't bother reconfiguring the logic.
#Basic gist is that it checks every location where a Starstud could be available and adds it to the pile.
def sd_stars(state: CollectionState, world: SDWorld, size:int) -> bool:
    return state.has("Starstud", world.player, size)


def sd_can_fight_miniboss(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,2)

def sd_can_fight_warden(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,3)

def sd_can_fight_chaos_warden(state: CollectionState, world: SDWorld) -> bool:
    return sd_party_size_meets(state, world,5)

def sd_can_fight_omni(state: CollectionState, world: SDWorld) -> bool:
    if world.options.omni and not(world.options.goal == 1):
        return sd_party_size_meets(state, world,7)
    else:
        return (
                #First team to defeat Omni
                (
                    state.has("Jeff", world.player) and state.has("Kani", world.player) and state.has("Pinn", world.player)
                    and state.has("Reflect", world.player) and state.has("Shoto", world.player) and state.has("Team Player", world.player)
                    and state.has("Bubble (Foil)", world.player) and state.has("Second Chance", world.player) and state.has("Microwave", world.player)
                    and state.has("RE:Move", world.player) and state.has("Bloody Heck", world.player, 2) and state.has("FirstCut", world.player)
                    and state.has("I'm So Tired", world.player) and state.has("Mono No Aware", world.player) and state.has("Storm", world.player)
                    and state.has("Pep Talk", world.player) and state.has("Someday", world.player)
                )
                #Second team to defeat Omni
                or (
                    state.has("Kani", world.player) and state.has("Liza", world.player) and state.has("Wink", world.player)
                    and state.has("Microwave", world.player) and state.has("Voxel Generation", world.player) and state.has("FirstCut", world.player)
                    and state.has("Momentum", world.player) and state.has("SmokeBreak", world.player) and state.has("GoMode", world.player)
                    and state.has("Exception", world.player) and state.has("Bubble (Foil)", world.player) and state.has("Wall (Foil)", world.player)
                    and state.has("Revolution 1", world.player) and state.has("Footstool", world.player) and state.has("Amp Up", world.player)
                    and state.has("Chain Bolt", world.player) and state.has("Nightvision", world.player)
                )
                #Third team to defeat Omni
                or (
                    state.has("Geo", world.player) and state.has("Liza", world.player) and state.has("Pinn", world.player)
                    and state.has("Bubble (Foil)", world.player, 2) and state.has("Team Player", world.player)
                    and state.has("NoU", world.player, 2) and state.has("I'm So Tired", world.player)
                    and state.has("GoMode", world.player) and state.has("Exception", world.player) and state.has("Wall (Foil)", world.player)
                    and state.has("Revolution 1", world.player) and state.has("Mono No Aware", world.player) and state.has("Exploit", world.player)
                    and state.has("ZoneSlice", world.player) and state.has("Pep Talk", world.player) and state.has("Move Along", world.player)
                )
                #Team that defeated Omni without taking damage
                or (
                    state.has("Geo", world.player) and state.has("Kani", world.player) and state.has("Pinn", world.player)
                    and state.has("Wet Hands", world.player) and state.has("Pushbie", world.player) and state.has("Wall (Foil)", world.player)
                    and state.has("Mono No Aware", world.player) and state.has("ZoneSlice", world.player) and state.has("MOTS", world.player)
                    and state.has("Shoto", world.player) and state.has("Bubble (Foil)", world.player) and state.has("FeelingBlue", world.player)
                    and state.has("Pullbie", world.player) and state.has("NoU", world.player) and state.has("Team Player", world.player)
                    and state.has("WeirdSig", world.player) and state.has("Move Along", world.player) and state.has("Freddie Freeloader", world.player)
                )
                #Team created by SapphireJester
                or (
                     state.has("Kani", world.player) and state.has("Wink", world.player) and state.has("Shane", world.player)
                     and state.has("TobiasMoor", world.player) and state.has("Microwave", world.player) and state.has("Quick Strike", world.player)
                     and state.has("Move", world.player) and state.has("BlitzDrive", world.player) and state.has("Team Player", world.player)
                     and state.has("Underhand", world.player) and state.has("Re:PUNCH", world.player) and state.has("Due Vendetta", world.player)
                     and state.has("Re:PUNCH", world.player, 2) and state.has("Bubble (Foil)", world.player) and state.has("Softlock", world.player)
                     and state.has("Hear Me Out", world.player) and state.has("Break Free", world.player)
                )
        )

def sd_can_status_stun(state: CollectionState, world: SDWorld) -> bool:
    return (state.has("Stungun", world.player) or state.has("FRAGSTUN", world.player) or state.has("Kappa", world.player)
            or state.has("Kappa+", world.player) or state.has("Floodgate", world.player) or state.has("Smokebreak", world.player)
            or state.has("Disruption", world.player) or (state.has("Voxel Generation", world.player) and state.has("Kani", world.player)))

def sd_can_status_depression(state: CollectionState, world: SDWorld) -> bool:
    return state.has("Irritate", world.player)

def sd_can_use_all_colors(state: CollectionState, world: SDWorld) -> bool:
    return  (state.has("Pinn", world.player) or state.has("Kani", world.player) or state.has("Wink", world.player) and
            (state.has_from_list_unique(redcards.keys(), world.player, 1) or state.has("Kani", world.player)) and
            (state.has_from_list_unique(orangecards.keys(), world.player, 1) or state.has("Shane", world.player)) and
            (state.has_from_list_unique(yellowcards.keys(), world.player, 1) or state.has("Wink", world.player)) and
            (state.has_from_list_unique(greencards.keys(), world.player, 1) or state.has("Liza", world.player)) and
            (state.has_from_list_unique(bluecards.keys(), world.player, 1) or state.has("Pinn", world.player)) and
            (state.has_from_list_unique(purplecards.keys(), world.player, 1) or state.has("Jeff", world.player)) and
            (state.has_from_list_unique(blackcards.keys(), world.player, 1) or state.has("Geo", world.player))
            )

#End of helpers


#Sawyer: Entrance time!
def set_all_entrance_rules(world: SDWorld) -> None:
    player = world.player
    multiworld = world.multiworld
    #Sawyer: Below is a var to make it so we don't have to type CollectionState every time we wanna check a function.
    mystate = CollectionState

    #begin_new_game = world.get_entrance("Begin_New_Game")


#Sawyer: These are the location rules! Hoo boy there are many haha
def set_all_location_rules(world: SDWorld) -> None:
    player = world.player
    multiworld = world.multiworld

    #Sawyer: Don't forget to define the locations we're adding rules to here.
    add_rule(world.get_location("Blue Zone - Glitch Bridge 1 Silver Chest"), lambda mystate: sd_party_size_meets(mystate, world,3))
    add_rule(world.get_location("Blue Cavern - Right Side Glitch Chest"), lambda mystate: sd_party_size_meets(mystate, world,3))
    add_rule(world.get_location("Blue Cavern - Left Side Glitch Chest"), lambda mystate: sd_party_size_meets(mystate, world,2))
    add_rule(world.get_location("Blue Zone - Wink Area Silver Chest"), lambda mystate: sd_party_size_meets(mystate, world,4))
    add_rule(world.get_location("Blue Cavern - Left Side Silver Chest"), lambda mystate: sd_has_blue(mystate, world))
    add_rule(world.get_location("Green Zone - Cyphon's Debut Silver Chest"), lambda mystate: sd_has_green(mystate, world))
    add_rule(world.get_location("Red Zone - Green Chest Behind Key Bridge"), lambda mystate: sd_has_red( mystate, world))
    add_rule(world.get_location("Red Zone Chasm - Silver Chest Behind Key Bridge"), lambda mystate: sd_has_red( mystate, world))
    add_rule(world.get_location("Green Zone - Squail Theatre Chest"), lambda mystate: sd_has_green( mystate, world))
    add_rule(world.get_location("Purple Zone - First Room Silver Chest"), lambda mystate: sd_has_purple( mystate, world))
    add_rule(world.get_location("Purple Zone - Left Path Silver Chest"), lambda mystate: sd_has_purple( mystate, world))
    add_rule(world.get_location("Purple Zone - Before Scaventure Gold Chest"), lambda mystate: sd_has_purple(mystate, world))
    add_rule(world.get_location("Orange Zone - Center Room Silver Chest"), lambda mystate: sd_has_orange( mystate, world))
    add_rule(world.get_location("Black Zone - First Room Chest Behind Key Bridge"), lambda mystate: sd_has_black( mystate, world))
    add_rule(world.get_location("Black Zone - Rot Passageway 1 Gold Chest"), lambda mystate: sd_has_black( mystate, world))
    add_rule(world.get_location("Black Zone - Second Elevator Room Behind Key Bridge"), lambda mystate: sd_has_black( mystate, world))
    add_rule(world.get_location("Black Zone - Rot Passageway 2 Gold Chest"), lambda mystate: sd_has_black( mystate, world))
    add_rule(world.get_location("Yellow Zone - Green Chest Behind Early Key Bridge"), lambda mystate: sd_has_yellow( mystate, world))
    add_rule(world.get_location("Yellow Zone - ReCollection Room Chest"), lambda mystate: sd_has_yellow( mystate, world))
    add_rule(world.get_location("Forge Chaotic Dance"), lambda mystate: sd_has_chaotic( mystate, world))
    add_rule(world.get_location("Yellow Zone - ReCollection 06 Unlock"), lambda mystate: sd_has_yellow( mystate, world))


    #Sawyer: Put the Starstud Rules here.
    if world.options.starstuds:
        add_rule(world.get_location("Starstud 1"), lambda mystate: sd_stars(mystate, world, 1))
        add_rule(world.get_location("Starstud 2"), lambda mystate: sd_stars(mystate, world, 2))
        add_rule(world.get_location("Starstud 3"), lambda mystate: sd_stars(mystate, world, 3))
        add_rule(world.get_location("Starstud 4"), lambda mystate: sd_stars(mystate, world, 4))
        add_rule(world.get_location("Starstud 5"), lambda mystate: sd_stars(mystate, world, 5))
        add_rule(world.get_location("Starstud 6"), lambda mystate: sd_stars(mystate, world, 6))
        add_rule(world.get_location("Starstud 7"), lambda mystate: sd_stars(mystate, world, 7))
        add_rule(world.get_location("Starstud 8"), lambda mystate: sd_stars(mystate, world, 8))
        add_rule(world.get_location("Starstud 9"), lambda mystate: sd_stars(mystate, world, 9))
        add_rule(world.get_location("Starstud 10"), lambda mystate: sd_stars(mystate, world, 10))
        add_rule(world.get_location("Starstud 11"), lambda mystate: sd_stars(mystate, world, 11))
        add_rule(world.get_location("Starstud 12"), lambda mystate: sd_stars(mystate, world, 12))
        add_rule(world.get_location("Starstud 13"), lambda mystate: sd_stars(mystate, world, 13))
        add_rule(world.get_location("Starstud 14"), lambda mystate: sd_stars(mystate, world, 14))
        add_rule(world.get_location("Starstud 15"), lambda mystate: sd_stars(mystate, world, 15))
        add_rule(world.get_location("Starstud 16"), lambda mystate: sd_stars(mystate, world, 16))
        add_rule(world.get_location("Starstud 17"), lambda mystate: sd_stars(mystate, world, 17))
        add_rule(world.get_location("Starstud 18"), lambda mystate: sd_stars(mystate, world, 18))
        add_rule(world.get_location("Starstud 19"), lambda mystate: sd_stars(mystate, world, 19))
        add_rule(world.get_location("Starstud 20"), lambda mystate: sd_stars(mystate, world, 20))
        add_rule(world.get_location("Starstud 21"), lambda mystate: sd_stars(mystate, world, 21))
        add_rule(world.get_location("Starstud 22"), lambda mystate: sd_stars(mystate, world, 22))
        add_rule(world.get_location("Starstud 23"), lambda mystate: sd_stars(mystate, world, 23))
        add_rule(world.get_location("Starstud 24"), lambda mystate: sd_stars(mystate, world, 24))
        add_rule(world.get_location("Starstud 25"), lambda mystate: sd_stars(mystate, world, 25))

#Sawyer: Time for the wincon! For now, it'll just be three party members but once the demo works it should be Entropy
def set_completion_condition(world: SDWorld) -> None:
    player = world.player
    multiworld = world.multiworld
    mystate = CollectionState

    if world.options.goal == 0:
        world.multiworld.completion_condition[world.player] = lambda mystate: sd_party_size_meets(mystate, world,7) and sd_has_black( mystate, world)
    elif world.options.goal == 1:
        world.multiworld.completion_condition[world.player] = lambda mystate: sd_can_fight_omni(mystate, world) and mystate.can_reach_region('OmniItems', player)
