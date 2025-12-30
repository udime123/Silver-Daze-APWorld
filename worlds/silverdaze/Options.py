from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


#Win Condition (Entropy, Omni, Bounty Hunt, Memo Hunt, ChaoticDance)

#Number of Memos (1-14)

#Number of Bounties (1-9)
#Bounties could be any Chaos Warden, Omni, or Purple Hippo

class goal(Choice):
    """
    This selects the victory condition from the following:
    Entropy - Collect seven party members and beat Entropy.
    Omni - Reach Omni and defeat them using any strategy.
    """
    display_name = "Victory Condition"
    option_entropy = 0
    option_omni = 1

    default = option_entropy

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
    Note! Disabling this could prevent Omni from being beatable.
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

class easylogic(Toggle):
    """
    This creates an easier path for the player which prevents logic requiring the use of the multicolored doors found
    in other zones.
    """
    display_name = "Easy Logic"
    default = 0

class omniscaling(Toggle):
    """
    This toggles whether Omni scales the party's level down to 50 when fought.
    """
    display_name = "Omni Level Scaling"
    default = 1


@dataclass
class SilverDazeOptions(PerGameCommonOptions):
         #starting_party_member: starting_party_member
         goal: goal
         easylogic: easylogic
         omniscaling: omniscaling

         minibosses: minibosses
         wardens: wardens
         chaoswardens: chaoswardens
         shops: shops
         recollections: recollections
         starstuds: starstuds
         omni: omni


options_groups = [
    OptionGroup(
        "Gameplay",
        [goal,omniscaling,easylogic]
    ),
    OptionGroup(
        "Excluded Locations",
        [starstuds,omni,minibosses,wardens,chaoswardens,shops,recollections]
    ),

]