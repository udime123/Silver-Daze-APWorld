from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class minibosses(Toggle):
    """
    This toggles whether minibosses drop important items.
    NOTE: You may still need to defeat minibosses if they are blocking your path to progression
    """
    display_name = "Enable Miniboss Drops"
    default = 1

class wardens(Toggle):
    """
    This toggles whether Wardens drop important items.
    NOTE: This only includes normal Wardens, Chaos Wardens are a different option
    """
    display_name = "Enable Warden Drops"
    default = 1

class chaoswardens(Toggle):
    """
    This toggles whether Chaos Wardens drop important items.
    NOTE: This only includes Chaos Wardens, normal Wardens are a different option
    """
    display_name = "Chaos Warden Drops"
    default = 1

class omni(Toggle):
    """
    This toggles whether Omni drops important items.
    """
    display_name = "Omni Drops"
    default = 0


class shops(Toggle):
    """
    This toggles whether shops contain important items.
    """
    display_name = "Enable Shops"
    default = 1

class recollections(Toggle):
    """
    This toggles whether ReCollections contain important items.
    """
    display_name = "Enable ReCollections"
    default = 1

class starstuds(Toggle):
    """
    This toggles whether Starstuds contain important items.
    """
    display_name = "Enable Starstuds"
    default = 1

@dataclass
class SilverDazeOptions(PerGameCommonOptions):
         #starting_party_member: starting_party_member
         minibosses: minibosses
         wardens: wardens
         chaoswardens: chaoswardens
         shops: shops
         recollections: recollections
         starstuds: starstuds
         omni: omni