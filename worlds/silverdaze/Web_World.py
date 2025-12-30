from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .Options import option_groups, option_presets



class APQuestWebWorld(WebWorld):
    game = "Silver Daze"

    theme = "ice"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up APQuest for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Sawyer Friend"],
    )


    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
