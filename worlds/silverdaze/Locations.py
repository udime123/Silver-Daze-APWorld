#Sawyer: Okay we have a whole lotta locations, here's hoping for the best!


#Snagging all the below from APQuest again
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import Items

if TYPE_CHECKING:
    from .World import SDWorld

import json

#Okay, looks like everything needs an ID. Blehhh it is what it is, I'll just go in order from the default thingy.


LOCATION_NAME_TO_ID = json.load(open("./worlds/silverdaze/Location_Table.json"))

# Sawyer: Locations are now stored inside the Location_Table.json file.
# This is so they can easily be transferred to Silver Daze and given the location data.
#Sawyer: PHEW! That covers the demo stuff. It'll be fun adding more haha

class SDLocation(Location):
    game = "Silver Daze"

#Sawyer: NGL I don't really get this but APQuest said to do it.
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SDWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: SDWorld) -> None:
    #Sawyer: First up, getting regions! I kinda wanna make this a function...
    #new_game = world.get_region("New_Game")

    geo_room = world.get_region("Geo_Room")
    cotton = world.get_region("Cotton")
    greyhub2 = world.get_region("GreyHub2")

    red1 = world.get_region("Red1")
    red2 = world.get_region("Red2")

    if world.options.minibosses:
        red1_minibosses = world.get_region("Red1_Minibosses")
        red2_minibosses = world.get_region("Red2_Minibosses")
    if world.options.wardens:
        red_wardens = world.get_region("Red_Wardens")
    if world.options.shops:
        first_shop = world.get_region('Shop_One')
        second_shop = world.get_region('Shop_Two')
        third_shop = world.get_region('Shop_Three')

    #Sawyer: Now we add stuff to regions!

    #Sawyer: This is intentionally empty for easy copying!
    #new_game_locations = get_location_names_with_ids(
    #    [

    #    ]
    #)

    #Sawyer: Starting member is the only one in this region to ensure you always leave with a party member.
    geo_room_locations = get_location_names_with_ids(
        [
            "PinnJoin","Ultima","PinnMP3","StarterHealToken1","StarterHealToken2",
        ]
    )
    geo_room.add_locations(geo_room_locations, SDLocation)

    cotton_locations = get_location_names_with_ids(
        [
            "GeoJoin","GeoJoin","GeoMP3","GeoWeapon1","Cotton2Chest1","Cotton3Chest1","YellowKey",
        ]
    )
    cotton.add_locations(cotton_locations, SDLocation)
    greyhub2_locations = get_location_names_with_ids(
        [
            "Hub2Chest1",
        ]
    )
    greyhub2.add_locations(greyhub2_locations,SDLocation)
    red1_locations = get_location_names_with_ids(
        [
            "Red1Chest","Red3Chest","Red3BackdoorChest",
        ]
    )
    red1.add_locations(red1_locations,SDLocation)
    red2_locations = get_location_names_with_ids(
        [
            "Red4Chest1","Red4Chest2","Red4Chest3","RedTower2Chest","RedTower3Chest","Kani","KaniMP3",
            "KaniWeapon1","KaniWeapon2","KaniWeapon3","RedChasm1Chest","RedChasm2Chest1","RedChasm2Chest2",
            "RedChasmReunionChest","Hub2Chest2",
        ]
    )
    red2.add_locations(red2_locations,SDLocation)

    if world.options.minibosses:
        red1_minibosses_locations = get_location_names_with_ids(
            [
                "QuoDefender1","QuoDefender2","QuoDefender3",
         ]
        )
        red1_minibosses.add_locations(red1_minibosses_locations,SDLocation)
        red2_minibosses_locations = get_location_names_with_ids(
            [
                "Kingoose1","Kingoose2","Kingoose3",
            ]
        )
        red2_minibosses.add_locations(red2_minibosses_locations,SDLocation)


    if world.options.wardens:
        red_wardens_locations = get_location_names_with_ids(
            [
                "Nyx","Nyx1","Nyx2","Nyx3",
            ]
        )
        red_wardens.add_locations(red_wardens_locations,SDLocation)

    if world.options.shops:
        first_shop_locations = get_location_names_with_ids(
            [
                "Shop1", "Shop2", "Shop3", "Shop4", "Shop5", "Shop6", "Shop7", "Shop8", "Shop9", "Shop10",
                "Shop11", "Shop12", "Shop13", "Shop14", "Shop15", "Shop16", "Shop17",
            ]
        )
        second_shop_locations = get_location_names_with_ids(
            [
                "Shop18", "Shop19", "Shop20", "Shop21", "Shop22",
            ]
        )
        third_shop_locations = get_location_names_with_ids(
            [
                "Shop23", "Shop24", "Shop25", "Shop26", "Shop27", "Shop28",
            ]
        )

        first_shop.add_locations(first_shop_locations, SDLocation)
        second_shop.add_locations(second_shop_locations, SDLocation)
        third_shop.add_locations(third_shop_locations, SDLocation)



#Sawyer: Okay, the game literally has zero events because we turned all of those into items. Soooo... don't sweat it?
#Sawyer: I put the regions here just so my IDE wouldn't scream at me for leaving this empty.
def create_events(world: SDWorld) -> None:
    #new_game = world.get_region("New_Game")
    geo_room = world.get_region("Geo_Room")
    cotton = world.get_region("Cotton")
    greyhub2 = world.get_region("GreyHub2")

    red1 = world.get_region("Red1")
    red2 = world.get_region("Red2")