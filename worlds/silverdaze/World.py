

from collections.abc import Mapping
from typing import Any, Callable

# Imports base Archipelago autoworld.
from worlds.AutoWorld import World

from BaseClasses import Entrance, Region, CollectionState

# Imports our files. We use capitals for the paths.
from . import Items, Locations, Options, Regions, Rules, Web_World
import logging
logger = logging.getLogger("Silver Daze")
logger.setLevel(logging.WARNING)






class SDWorld(World):
    """
    Silver Daze is a 2025 Coming-of-Age RPG where you collect cards and battle monsters to save a fractured world.
    The game includes a comprehensive randomizer mode in which the player collects keys and party members to access
    new locations.
    """
    game = "Silver Daze"

    #Sawyer: Webworld will be important eventually so we might as well add that now.
    web = Web_World.SilverDazeWebWorld()

    options_dataclass = Options.SilverDazeOptions
    options: Options.SilverDazeOptions

    #Sawyer: We used to define these here but we'll do it in Regions and Items instead.
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = {key: item.code for (key, item) in Items.item_table.items()}

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

    def generate_early(self) -> None:
        if (self.options.emblempool < self.options.emblemcount and self.options.goal == 2):
            logger.warning(
                f"Silver Daze ({self.player_name}): "
                f"There are fewer emblems in the pool than required to beat the game. "
                f"The difference will be added to the pool.")

    # #Sawyer: Slotdata currently contains Goal.
    def fill_slot_data(self) -> Mapping[str, Any]:


        # This is just options.
        return self.options.as_dict(
            "minibosses","wardens","chaoswardens","omni","shops","recollections","starstuds","goal",
            "omniscaling","emblemcount"
        )
