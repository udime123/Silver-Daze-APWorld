

from collections.abc import Mapping
from typing import Any, Callable

# Imports base Archipelago autoworld.
from worlds.AutoWorld import World

from BaseClasses import Entrance, Region, CollectionState

# Imports our files. We use capitals for the paths.
from . import Items, Locations, Options, Regions, Rules





class SDWorld(World):
    """
    This will describe Silver Daze eventually
    """
    game = "Silver Daze"

    #Webworld will be important eventually so we might as well add that now.
    #web = WebWorld.SilverDazeWebWorld()

    options_dataclass = Options.SilverDazeOptions
    options: Options.SilverDazeOptions

    #Sawyer: We used to define these here but we'll do it in Regions and Items instead.
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    #item_name_to_id = Items.ITEM_NAME_TO_ID
    item_name_to_id = {key: item.code for (key, item) in Items.item_table.items()}
    #item_name_to_id = Items.item_table

    @staticmethod
    def connect_2way(r1: Region, r2: Region, rule: Callable[[CollectionState], bool]):
        #Credit Emily, thank you!
        r1.connect(connecting_region=r2, rule=rule)
        r2.connect(connecting_region=r1, rule=rule)

    #Sawyer: You start in Geo's Room, after all.
    origin_region_name = "GeoRoom"

    #Sawyer: These are important rules, check APQuest for an explanation.
    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    def set_rules(self) -> None:
        Rules.set_all_rules(self)

    def create_items(self) -> None:
        Items.create_all_items(self)

    #Sawyer: Time to make items, of course!
    def create_item(self, name: str) -> Items.SDItem:
        return Items.create_item(self, name)

    #Sawyer: We should make sure we have filler items too.
    #Sawyer: ATM these will just be Heal Tokens but honestly most Tokens work, maybe even some weak cards.
    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)



    # #Sawyer: Slotdata currently contains Goal.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # This is just options.
        return self.options.as_dict(
            "minibosses","wardens","chaoswardens","omni","shops","recollections","starstuds","goal"
        )
