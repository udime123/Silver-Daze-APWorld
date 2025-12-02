#Sawyer: Okay we have a whole lotta locations, here's hoping for the best!


#Snagging all the below from APQuest again
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import Items
from ..factorio import location_pools

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
        "Green1Chest","GreenCyphonDebutChest","Jeff","JeffMP3","JeffWeapon1","JeffWeapon2","JeffWeapon3","ReCollection03",
    ]),SDLocation)
#
    world.get_region("DesmodusRoom").add_locations(get_location_names_with_ids([
        "Memo7","Memo7A",
    ]),SDLocation)
#
    world.get_region("Green2").add_locations(get_location_names_with_ids([
        "CyphonHallChest","GreenLeftUpChest","GreenRightChest",
    ]),SDLocation)
#
    world.get_region("SquailArea").add_locations(get_location_names_with_ids([
        "Memo8","Memo8A","GreenTheatreChest",
    ]),SDLocation)
#
    world.get_region("Purple1").add_locations(get_location_names_with_ids([
        "Purple1Chest2","Purple1Chest1",
    ]),SDLocation)
#
    world.get_region("SwordmoleRoom").add_locations(get_location_names_with_ids([
        "Memo11","Memo11A",
    ]),SDLocation)
#
    world.get_region("Purple2").add_locations(get_location_names_with_ids([
        "Purple4Chest1","Purple4Chest2","PurpleSniper2Chest","Purple7Chest2","Purple7Chest1","Liza","LizaMP3","LizaWeapon1",
        "LizaWeapon2","LizaWeapon3",
    ]),SDLocation)
#
    world.get_region("ScaventureRoom").add_locations(get_location_names_with_ids([
        "Memo12","Memo12A",
    ]),SDLocation)
#
    world.get_region("PurpleTower").add_locations(get_location_names_with_ids([
        "PurpleTowerEntranceChest","PurpleLeftChest","ReCollection04","PurpleTower7Chest",
    ]),SDLocation)

#
    world.get_region("GreyIslandBlackDoor").add_locations(get_location_names_with_ids([
        "Cotton3Chest2"
    ]),SDLocation)
#
    world.get_region("BlackBackdoorIsland").add_locations(get_location_names_with_ids([
        "BlackChase1_BackdoorChest"
    ]),SDLocation)


#
    world.get_region("OngardRoom").add_locations(get_location_names_with_ids([
        "Memo4","Memo4A",
    ]),SDLocation)
#
    world.get_region("Hub3GreenSide").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Orange1").add_locations(get_location_names_with_ids([
        "Orange1Chest1","Orange1Chest2","OrangeLeftChest1","OrangeRightChest1"
    ]),SDLocation)
#
    world.get_region("DualistsRoom").add_locations(get_location_names_with_ids([
        "Memo3","Memo3A",
    ]),SDLocation)
#
    world.get_region("Hub3PurpleSide").add_locations(get_location_names_with_ids([
        "Hub3Chest1",
    ]),SDLocation)
#
    world.get_region("Orange2").add_locations(get_location_names_with_ids([
        "OrangeKeyAreaChest1","OrangeKeyAreaChest2","ReCollection07",
    ]),SDLocation)
#
    world.get_region("OrangeBackdoorIsland").add_locations(get_location_names_with_ids([
        "OrangeRight_BackdoorChest",
    ]),SDLocation)
#
    world.get_region("GreenBackdoorIsland").add_locations(get_location_names_with_ids([
        "Green3_BackdoorChest"
    ]),SDLocation)
#
    world.get_region("Black1").add_locations(get_location_names_with_ids([
        "Black1Chest","BlackBetween1Chest","Black3Chest","Black4Chest",
    ]),SDLocation)
#
    world.get_region("KisaijuRoom").add_locations(get_location_names_with_ids([
        "Memo13","Memo13A",
    ]),SDLocation)
#
    world.get_region("Black2").add_locations(get_location_names_with_ids([
        "Black7Chest","BlackBetween2Chest",
    ]),SDLocation)
#
    world.get_region("Griffin2Room").add_locations(get_location_names_with_ids([
        "Memo14","Memo14A","ReCollection01",
    ]),SDLocation)
#
#    world.get_region("BlackDungeon").add_locations(get_location_names_with_ids([
#Doesn't seem to have any items.
#    ]),SDLocation)
#
    world.get_region("Yellow1").add_locations(get_location_names_with_ids([
        "Yellow3Chest","Yellow5Chest",
    ]),SDLocation)
#
    world.get_region("EsquireRoom").add_locations(get_location_names_with_ids([
        "Memo5","Memo5A"
    ]),SDLocation)
#
    world.get_region("Yellow2").add_locations(get_location_names_with_ids([
        "Yellow6Chest1","Yellow6Chest2","Yellow8Chest",
    ]),SDLocation)
#
    world.get_region("MothershipRoom").add_locations(get_location_names_with_ids([
        "Memo6","Memo6A"
    ]),SDLocation)
#
    world.get_region("YellowLighthouse").add_locations(get_location_names_with_ids([
        "Yellow12Chest","Yellow14Chest1","Yellow14Chest2","Yellow14Chest3","YellowTower5Chest1","YellowTower5Chest2",
    ]),SDLocation)
#
    world.get_region("FinalLobby").add_locations(get_location_names_with_ids([
        "ChaoticDance","ReCollection10",
    ]),SDLocation)
#
    world.get_region("ExanderZone").add_locations(get_location_names_with_ids([
        "Final1Chest","Final2Chest","Final3Chest1","Fair1Chest3","Fair1Chest1","Fair1Chest2","ReCollection09",
        "BeforeExanderChest","ExanderMerge",
    ]),SDLocation)
#
    world.get_region("OmniZone1").add_locations(get_location_names_with_ids([
        "White1Chest","White2Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone2").add_locations(get_location_names_with_ids([
        "White3Chest2","White3Chest1"
    ]),SDLocation)
#
    world.get_region("OmniZone3").add_locations(get_location_names_with_ids([
        "White4Chest2", "White4Chest1"
    ]),SDLocation)
#
    world.get_region("OmniZone4").add_locations(get_location_names_with_ids([
        "White5Chest1"
    ]),SDLocation)
#
    world.get_region("OmniZone5").add_locations(get_location_names_with_ids([
        "White6Chest1"
    ]),SDLocation)
#
    world.get_region("OmniZone6").add_locations(get_location_names_with_ids([
        "White7Chest1"
    ]),SDLocation)
#
    world.get_region("OmniZone7").add_locations(get_location_names_with_ids([
        "White8Chest1"
    ]),SDLocation)
#
    world.get_region("OmniRoom").add_locations(get_location_names_with_ids([
        "White9Chest1"
    ]),SDLocation)

#Here are the optional ones.

#Minibosses
    if world.options.minibosses:
#
        world.get_region("QuoDefenderItems").add_locations(get_location_names_with_ids([
            "QuoDefender1","QuoDefender2","QuoDefender3",
        ]), SDLocation)
#
        world.get_region("KingooseItems").add_locations(get_location_names_with_ids([
            "Kingoose1","Kingoose2","Kingoose3",
        ]), SDLocation)
#
        world.get_region("Griffin1Items").add_locations(get_location_names_with_ids([
            "GriffinBlue1","GriffinBlue2","GriffinBlue3",
        ]), SDLocation)
#
        world.get_region("DiggerItems").add_locations(get_location_names_with_ids([
            "Digger1","Digger2","Digger3",
        ]), SDLocation)
#
        world.get_region("DesmodusItems").add_locations(get_location_names_with_ids([
            "Desmodus1","Desmodus2","Desmodus3",
        ]), SDLocation)
#
        world.get_region("SquailItems").add_locations(get_location_names_with_ids([
            "Squail1","Squail2","Squail3",
        ]), SDLocation)
#
        world.get_region("SwordmoleItems").add_locations(get_location_names_with_ids([
            "Swordmole1","Swordmole2","Swordmole3"
        ]), SDLocation)
#
        world.get_region("ScaventureItems").add_locations(get_location_names_with_ids([
            "Scaventure1","Scaventure2","Scaventure3"
        ]), SDLocation)
#
        world.get_region("OngardItems").add_locations(get_location_names_with_ids([
            "Ongard1","Ongard2","Ongard3",
        ]), SDLocation)
#
        world.get_region("DualistsItems").add_locations(get_location_names_with_ids([
            "Dualists1","Dualists2","Dualists3",
        ]), SDLocation)
#
        world.get_region("KisaijuItems").add_locations(get_location_names_with_ids([
            "Kisaiju1","Kisaiju2","Kisaiju3",
        ]), SDLocation)
#
        world.get_region("Griffin2Items").add_locations(get_location_names_with_ids([
            "GriffinBlack1","GriffinBlack2","GriffinBlack3"
        ]), SDLocation)
#
        world.get_region("EsquireItems").add_locations(get_location_names_with_ids([
            "Esquire1","Esquire2","Esquire3"
        ]), SDLocation)
#
        world.get_region("MothershipItems").add_locations(get_location_names_with_ids([
            "Mothership1","Mothership2","Mothership3"
        ]), SDLocation)

#Wardens
    if world.options.wardens:
#
        world.get_region("NyxItems").add_locations(get_location_names_with_ids([
            "Nyx1","Nyx1","Nyx1","Nyx"
        ]), SDLocation)
#
        world.get_region("ScatterItems").add_locations(get_location_names_with_ids([
            "Scatter1","Scatter2","Scatter3","Scatter"
        ]), SDLocation)
#
        world.get_region("CyphonItems").add_locations(get_location_names_with_ids([
            "Cyphon1","Cyphon2","Cyphon3","Cyphon"
        ]), SDLocation)
#
        world.get_region("EnriItems").add_locations(get_location_names_with_ids([
            "Enri1","Enri2","Enri3","Enri",
        ]), SDLocation)
#
        world.get_region("RudaItems").add_locations(get_location_names_with_ids([
            "Ruda1","Ruda2","Ruda3","Ruda"
        ]), SDLocation)
#
        world.get_region("RotItems").add_locations(get_location_names_with_ids([
            "Rot1","Rot2","Rot3","Rot"
        ]), SDLocation)
#
        world.get_region("WinkItems").add_locations(get_location_names_with_ids([
            "Wink1","Wink2","Wink3"
        ]), SDLocation)
#
        world.get_region("FinalGriffinItems").add_locations(get_location_names_with_ids([
            "GriffinFinal1","GriffinFinal2","GriffinFinal3","GriffinFinal4"
        ]), SDLocation)

#Chaos Wardens
    if world.options.chaoswardens:
#
        world.get_region("ChaosNyxItems").add_locations(get_location_names_with_ids([
            "ChaosNyx","ChaosNyx1","ChaosNyx2","ChaosNyx3"
        ]), SDLocation)
#
        world.get_region("ChaosScatterItems").add_locations(get_location_names_with_ids([
            "ChaosScatter","ChaosScatter1","ChaosScatter2","ChaosScatter3"
        ]), SDLocation)
#
        world.get_region("ChaosCyphonItems").add_locations(get_location_names_with_ids([
            "ChaosCyphon","ChaosCyphon1","ChaosCyphon2","ChaosCyphon3"
        ]), SDLocation)
#
        world.get_region("ChaosEnriItems").add_locations(get_location_names_with_ids([
            "ChaosEnri","ChaosEnri1","ChaosEnri2","ChaosEnri3"
        ]), SDLocation)
#
        world.get_region("ChaosRudaItems").add_locations(get_location_names_with_ids([
            "ChaosRuda","ChaosRuda1","ChaosRuda2","ChaosRuda3"
        ]), SDLocation)
#
        world.get_region("ChaosRotItems").add_locations(get_location_names_with_ids([
            "ChaosRot","ChaosRot1","ChaosRot2","ChaosRot3"
        ]), SDLocation)
#
        world.get_region("ChaosWinkItems").add_locations(get_location_names_with_ids([
            "ChaosWink","ChaosWink1","ChaosWink2","ChaosWink3"
        ]), SDLocation)
#
        world.get_region("PurpleHippoItems").add_locations(get_location_names_with_ids([
            "PurpleHippo1","PurpleHippo2","PurpleHippo3"
        ]), SDLocation)

    if world.options.omni:
        world.get_region("OmniItems").add_locations(get_location_names_with_ids([
            "Omni1","Omni2","Omni3",
        ]), SDLocation)

    if world.options.starstuds:
        world.get_region("Starstuds").add_locations(get_location_names_with_ids([
            "Starstud1","Starstud2","Starstud3","Starstud4","Starstud5","Starstud6","Starstud7","Starstud8","Starstud9",
            "Starstud10","Starstud11","Starstud12","Starstud13","Starstud14","Starstud15","Starstud16","Starstud17",
            "Starstud18","Starstud19",
            "Starstud20","Starstud21","Starstud22","Starstud23","Starstud24","Starstud25",
        ]), SDLocation)


    if world.options.shops:
# #
#         world.get_region("Shop").add_locations(get_location_names_with_ids([
# #No items here.
#
#         ]), SDLocation)
#
        world.get_region("Shop1").add_locations(get_location_names_with_ids([
            "Shop1", "Shop2","Shop3", "Shop4", "Shop5", "Shop6", "Shop7", "Shop8", "Shop9", "Shop10", "Shop11", "Shop12",
            "Shop13","Shop14", "Shop15", "Shop16", "Shop17",
        ]), SDLocation)
#
        world.get_region("Shop2").add_locations(get_location_names_with_ids([
            "Shop18","Shop19","Shop20","Shop21","Shop22",
        ]), SDLocation)
#
        world.get_region("Shop3").add_locations(get_location_names_with_ids([
            "Shop23","Shop24","Shop25","Shop26","Shop27","Shop28","Shop29",
        ]), SDLocation)
#
        world.get_region("Shop4").add_locations(get_location_names_with_ids([
            "Shop30","Shop31","Shop32","Shop33","Shop34",
        ]), SDLocation)
#
        world.get_region("Shop5").add_locations(get_location_names_with_ids([
            "Shop35","Shop36","Shop37","Shop38","Shop39","Shop40",
        ]), SDLocation)
#
        world.get_region("Shop6").add_locations(get_location_names_with_ids([
            "Shop41", "Shop42", "Shop43", "Shop44", "Shop45", "Shop46",
        ]), SDLocation)
#
        world.get_region("Shop7").add_locations(get_location_names_with_ids([
            "Shop47","Shop48","Shop49",
            "Shop50","Shop51","Shop52","Shop53","Shop54","Shop55","Shop56","Shop57","Shop58","Shop59",
        ]), SDLocation)

    if world.options.recollections:
#
        world.get_region("ReCollectionRed").add_locations(get_location_names_with_ids([
            "ReCollection2_1", "ReCollection2_2", "ReCollection2_3", "ReCollection2_4",
            "ReCollection2_5", "ReCollection2_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionBlue").add_locations(get_location_names_with_ids([
            "ReCollection5_1", "ReCollection5_2", "ReCollection5_3",
            "ReCollection5_4", "ReCollection5_5", "ReCollection5_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionGreen").add_locations(get_location_names_with_ids([
            "ReCollection3_1", "ReCollection3_2", "ReCollection3_3", "ReCollection3_4",
            "ReCollection3_5", "ReCollection3_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionPurple").add_locations(get_location_names_with_ids([
            "ReCollection4_1", "ReCollection4_2", "ReCollection4_3",
            "ReCollection4_4", "ReCollection4_5", "ReCollection4_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionOrange").add_locations(get_location_names_with_ids([
            "ReCollection7_1", "ReCollection7_2", "ReCollection7_3",
            "ReCollection7_4", "ReCollection7_5", "ReCollection7_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionBlack").add_locations(get_location_names_with_ids([
            "ReCollection1_1","ReCollection1_2","ReCollection1_3","ReCollection1_4",
            "ReCollection1_5","ReCollection1_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionYellow").add_locations(get_location_names_with_ids([
            "ReCollection6_1", "ReCollection6_2", "ReCollection6_3",
            "ReCollection6_4", "ReCollection6_5", "ReCollection6_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionGrey").add_locations(get_location_names_with_ids([
            "ReCollection8_1", "ReCollection8_2", "ReCollection8_3",
            "ReCollection8_4", "ReCollection8_5", "ReCollection8_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionExander").add_locations(get_location_names_with_ids([
            "ReCollection9_1", "ReCollection9_2", "ReCollection9_3",
            "ReCollection9_4", "ReCollection9_5", "ReCollection9_6",
        ]), SDLocation)
#
        world.get_region("ReCollectionWhite").add_locations(get_location_names_with_ids([
            "ReCollection10_1", "ReCollection10_2", "ReCollection10_3",
            "ReCollection10_4", "ReCollection10_5", "ReCollection10_6",
        ]), SDLocation)




def create_events(world: SDWorld) -> None:
    world.get_region("Hub1").locations.append(SDLocation(world.player, "Starstud1Empty", None, world.get_region("Hub1")))
    world.get_region("Hub2").locations.append(SDLocation(world.player, "Starstud2Empty", None, world.get_region("Hub2")))
    world.get_region("Red1").locations.append(SDLocation(world.player, "Starstud3Empty", None, world.get_region("Red1")))
    world.get_region("Red2").locations.append(SDLocation(world.player, "Starstud4Empty", None, world.get_region("Red2")))
    world.get_region("Red2").locations.append(SDLocation(world.player, "Starstud5Empty", None, world.get_region("Red2")))
    world.get_region("Orange1").locations.append(SDLocation(world.player, "Starstud6Empty", None, world.get_region("Orange1")))
    world.get_region("Orange1").locations.append(SDLocation(world.player, "Starstud24Empty", None, world.get_region("Orange1")))
    world.get_region("Orange2").locations.append(SDLocation(world.player, "Starstud7Empty", None, world.get_region("Orange2")))
    world.get_region("Hub3GreenSide").locations.append(SDLocation(world.player, "Starstud8Empty", None, world.get_region("Hub3GreenSide")))
    world.get_region("EsquireRoom").locations.append(SDLocation(world.player, "Starstud9Empty", None, world.get_region("EsquireRoom")))
    world.get_region("Yellow2").locations.append(SDLocation(world.player, "Starstud10Empty", None, world.get_region("Yellow2")))
    world.get_region("YellowLighthouse").locations.append(SDLocation(world.player, "Starstud11Empty", None, world.get_region("YellowLighthouse")))
    world.get_region("Green1").locations.append(SDLocation(world.player, "Starstud12Empty", None, world.get_region("Green1")))
    world.get_region("Green2").locations.append(SDLocation(world.player, "Starstud13Empty", None, world.get_region("Green2")))
    world.get_region("Green2").locations.append(SDLocation(world.player, "Starstud14Empty", None, world.get_region("Green2")))
    world.get_region("Blue1").locations.append(SDLocation(world.player, "Starstud15Empty", None, world.get_region("Blue1")))
    world.get_region("Blue4").locations.append(SDLocation(world.player, "Starstud16Empty", None, world.get_region("Blue4")))
    world.get_region("Blue5").locations.append(SDLocation(world.player, "Starstud17Empty", None, world.get_region("Blue5")))
    world.get_region("Purple1").locations.append(SDLocation(world.player, "Starstud18Empty", None, world.get_region("Purple1")))
    world.get_region("PurpleTower").locations.append(SDLocation(world.player, "Starstud19Empty", None, world.get_region("PurpleTower")))
    world.get_region("PurpleTower").locations.append(SDLocation(world.player, "Starstud20Empty", None, world.get_region("PurpleTower")))
    world.get_region("Black1").locations.append(SDLocation(world.player, "Starstud21Empty", None, world.get_region("Black1")))
    world.get_region("Black2").locations.append(SDLocation(world.player, "Starstud22Empty", None, world.get_region("Black2")))
    world.get_region("BlackDungeon").locations.append(SDLocation(world.player, "Starstud23Empty", None, world.get_region("BlackDungeon")))
    world.get_region("OmniZone1").locations.append(SDLocation(world.player, "Starstud25Empty", None, world.get_region("OmniZone1")))

    for i in range(25):
        location_name = f"Starstud{i + 1}Empty"
        location = world.get_location(location_name)
        starstud = Items.SDItem("Starstud", ItemClassification.progression, None, world.player)
        location.place_locked_item(starstud)





