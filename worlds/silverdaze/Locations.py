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
    #Sawyer: Now we add stuff to regions!

#Here's the main story non optional stuff.
    world.get_region("GeoRoom").add_locations(get_location_names_with_ids([
        "PinnJoin","Ultima","PinnMP3","StarterHealToken1","StarterHealToken2",
    ]),SDLocation)
#
    world.get_region("Hub1").add_locations(get_location_names_with_ids([
        "YellowKey","GeoJoin","GeoMP3","GeoWeapon1","Cotton2Chest1","Cotton3Chest1",
    ]),SDLocation)
#
    world.get_region("Hub2").add_locations(get_location_names_with_ids([
        "ReCollection08","Hub2Chest1",
    ]),SDLocation)
#
    world.get_region("QuoDefenderRoom").add_locations(get_location_names_with_ids([
        "Memo1", "Memo1A",
    ]),SDLocation)
#
    world.get_region("Red1").add_locations(get_location_names_with_ids([
        "Red1Chest", "Red3Chest",
    ]),SDLocation)
#
    world.get_region("KingooseRoom").add_locations(get_location_names_with_ids([
        "Memo2","Memo2A","Kani","KaniMP3","KaniWeapon1","KaniWeapon3","KaniWeapon2",
    ]),SDLocation)
#
    world.get_region("Red2").add_locations(get_location_names_with_ids([
        "Red4Chest1","Red4Chest2","Red4Chest3","RedTower2Chest","RedTower4Chest","RedChasm1Chest","RedChasmReunionChest",
        "ReCollection02","RedChasm2Chest1","RedChasm2Chest2"
    ]),SDLocation)
#
    world.get_region("GreyIslandGreenDoor").add_locations(get_location_names_with_ids([
        "Hub1Chest1"
    ]),SDLocation)
#
    world.get_region("YellowBackdoorIsland").add_locations(get_location_names_with_ids([
        "Yellow5_BackDoorChest"
    ]),SDLocation)
#
    world.get_region("GreyIslandBlueDoor").add_locations(get_location_names_with_ids([
        "Hub1Chest2"
    ]),SDLocation)
#
    world.get_region("GreyIslandRedDoor").add_locations(get_location_names_with_ids([
        "Hub2Chest2",
    ]),SDLocation)
#
    world.get_region("RedBackdoorIsland").add_locations(get_location_names_with_ids([
        "Red3_BackdoorChest"
    ]),SDLocation)

#
#    world.get_region("Blue1").add_locations(get_location_names_with_ids([
#   I don't think Blue1 has any locations atm
#    ]),SDLocation)
#
    world.get_region("Blue2").add_locations(get_location_names_with_ids([
        "Blue3Chest", "Blue3Chest2"
    ]),SDLocation)
#
    world.get_region("Griffin1Room").add_locations(get_location_names_with_ids([
        "Memo9","Memo9A"
    ]),SDLocation)
#
    world.get_region("BlueShaneArea").add_locations(get_location_names_with_ids([
        "Blue3Chest3"
    ]),SDLocation)
#
    world.get_region("DiggerRoom").add_locations(get_location_names_with_ids([
        "DiggerRoomChest","Memo10","Memo10A","Shane","ShaneMP3","ShaneWeapon1","ShaneWeapon2",
    ]),SDLocation)
#
    world.get_region("Blue3").add_locations(get_location_names_with_ids([
        "BlueBridgeRightChest"
    ]),SDLocation)
#
    world.get_region("Blue4").add_locations(get_location_names_with_ids([
        "WinkJoin","WinkMP3","WinkWeapon1","WinkWeapon2","Blue6Chest","Blue8Chest","ReCollection05","Blue7Chest"
    ]),SDLocation)
#
    world.get_region("Blue5").add_locations(get_location_names_with_ids([
        "BlueCaveRightChest","BlueCaveRightStory","BlueCaveLeftChest","BlueCaveLeftStory",
    ]),SDLocation)
#
#    world.get_region("Scatter").add_locations(get_location_names_with_ids([
#       Scatter lacks locations as well.
#    ]),SDLocation)
#
    world.get_region("PurpleBackdoorIsland").add_locations(get_location_names_with_ids([
        "Purple2_BackdoorChest",
    ]),SDLocation)
#
    world.get_region("PurpleHippoRoom").add_locations(get_location_names_with_ids([
        "PurpleHippoChest",
    ]),SDLocation)
#
    world.get_region("BlueBackdoorIsland").add_locations(get_location_names_with_ids([
        "Blue5_BackdoorChest",
    ]),SDLocation)

#
    world.get_region("Green1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("DesmodusRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Green2").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("SquailArea").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OrangeBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("GreenBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Purple1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("SwordmoleRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Purple2").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("ScaventureRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("PurpleTower").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("GreyIslandBlackDoor").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("BlackBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OngardRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Hub3GreenSide").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Orange1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("DualistsRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Hub3PurpleSide").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Orange1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Orange2").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("GreyIslandBlackDoor").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OrangeBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("GreenBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Black1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("KisaijuRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Black2").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("GriffinRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("BlackDungeon").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("BlackBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Yellow1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("EsquireRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Yellow2").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("MothershipRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("YellowLighthouse").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("YellowBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("BlueBackdoorIsland").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("FinalLobby").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("ExanderZone").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone1").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone2").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone3").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone4").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone5").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone6").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniZone7").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("OmniRoom").add_locations(get_location_names_with_ids([

    ]),SDLocation)

#Here are the optional ones.

#Minibosses
    if world.options.minibosses:
#
        world.get_region("QuoDefenderItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("KingooseItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Griffin1Items").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("DiggerItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("DesmodusItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("SquailItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("SwordmoleItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ScaventureItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("OngardItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("DualistsItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("KisaijuItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Griffin2Items").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("EsquireItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("MothershipItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)

#Wardens
    if world.options.wardens:
#
        world.get_region("NyxItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ScatterItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("CyphonItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("EnriItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("RudaItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("RotItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("WinkItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("FinalGriffinItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)

#Chaos Wardens
    if world.options.chaoswardens:
#
        world.get_region("ChaosNyxItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ChaosScatterItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ChaosCyphonItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ChaosEnriItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ChaosRudaItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ChaosRotItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ChaosWinkItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("PurpleHippoItems").add_locations(get_location_names_with_ids([

        ]), SDLocation)

    if world.options.chaoswardens:
        world.get_region("Omni").add_locations(get_location_names_with_ids([

        ]), SDLocation)

    if world.options.starstuds:
        world.get_region("Starstuds").add_locations(get_location_names_with_ids([

        ]), SDLocation)


    if world.options.shops:
#
        world.get_region("Shop").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop1").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop2").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop3").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop4").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop5").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop6").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("Shop7").add_locations(get_location_names_with_ids([

        ]), SDLocation)

    if world.options.recollections:
#
        world.get_region("ReCollectionRed").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionBlue").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionGreen").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionPurple").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionOrange").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionBlack").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionYellow").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionGrey").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionExander").add_locations(get_location_names_with_ids([

        ]), SDLocation)
#
        world.get_region("ReCollectionWhite").add_locations(get_location_names_with_ids([

        ]), SDLocation)






#Sawyer: Okay, the game literally has zero events because we turned all of those into items. Soooo... don't sweat it?
#Sawyer: I put the regions here just so my IDE wouldn't scream at me for leaving this empty.
def create_events(world: SDWorld) -> None:
    #new_game = world.get_region("New_Game")
    geo_room = world.get_region("Geo_Room")
    cotton = world.get_region("Cotton")
    greyhub2 = world.get_region("GreyHub2")

    red1 = world.get_region("Red1")
    red2 = world.get_region("Red2")