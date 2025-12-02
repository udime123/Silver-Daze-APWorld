from __future__ import annotations

from typing import TYPE_CHECKING
import typing

from BaseClasses import Item, ItemClassification

from worlds.AutoWorld import World, WebWorld

if TYPE_CHECKING:
    from .World import SDWorld

#Sawyer: This time I said screwit and went with the old system we already had, hopefully it works.
#Sawyer: The APQuest version looked mean and scary but we can do it if we must.

class SDItem(Item):
    game = "Silver Daze"


class ItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.filler
    category: str = 'Card'
    max_quantity: int = 1
    weight: int = 1


# Item groups for easy management

party_members = {
    "Pinn": ItemData(3001, ItemClassification.progression, "Party"),
    "Geo": ItemData(3002, ItemClassification.progression, "Party"),
    "Kani": ItemData(3003, ItemClassification.progression, "Party"),
    "Shane": ItemData(3004, ItemClassification.progression, "Party"),
    "Jeff": ItemData(3005, ItemClassification.progression, "Party"),
    "Wink": ItemData(3006, ItemClassification.progression, "Party"),
    "Liza": ItemData(3007, ItemClassification.progression, "Party"),
}

mp3s = {
    "Freddie Freeloader": ItemData(1063, ItemClassification.useful, "MP3"),
    "Flossophy": ItemData(1044, ItemClassification.useful, "MP3"),
    "Big Shot": ItemData(1003, ItemClassification.useful, "MP3"),
    "Triage": ItemData(1065, ItemClassification.useful, "MP3"),
    "The Sign": ItemData(1045, ItemClassification.useful, "MP3"),
    "Wet Hands": ItemData(1010, ItemClassification.useful, "MP3"),
    "Move": ItemData(1001, ItemClassification.useful, "MP3"),
    "Low Ride": ItemData(1042, ItemClassification.useful, "MP3"),
    "Lost In Thought": ItemData(1062, ItemClassification.useful, "MP3"),
}

# In Visual Studio Code or another IDE you can collapse the dict to hide the cards
cards = {
    "Ultima": ItemData(352),
    "Finish Touch": ItemData(42),
    "Valor Drive": ItemData(25),
    "Sonic Boom": ItemData(29, ItemClassification.useful, "Card", 2),
    "Hopscotch": ItemData(154),
    "CoffeBrek": ItemData(155),
    "Fine Tune": ItemData(256),
    "SmokeBreak": ItemData(311),
    "PowerNap": ItemData(72),
    "Flatten": ItemData(18),
    "Dragon": ItemData(31, ItemClassification.progression, "Card"),
    "Kappa": ItemData(230, ItemClassification.progression, "Card"),
    "Unicorn": ItemData(187, ItemClassification.progression, "Card"),
    "Cyclops": ItemData(292, ItemClassification.progression, "Card"),
    "Phoenix": ItemData(86, ItemClassification.progression, "Card"),
    "Pulgasari": ItemData(345, ItemClassification.progression, "Card"),
    "Pixie": ItemData(137, ItemClassification.progression, "Card"),
    "Variacut": ItemData(30),
    "Morning Ray": ItemData(74, ItemClassification.useful, "Card", 2),
    "Zoner": ItemData(304),
    "Cold As Ice": ItemData(5),
    "Strife": ItemData(64, ItemClassification.useful, "Card", 2),
    "RATD": ItemData(4, ItemClassification.useful, "Card", 3),
    "WisdomDrive": ItemData(284),
    "LimitDrive": ItemData(225),
    "Storage": ItemData(180),
    "Shoot Star": ItemData(140),
    "MasterDrive": ItemData(76),
    "WeirdSig": ItemData(341),
    "BlitzDrive": ItemData(125),
    "Flexibility": ItemData(68),
    "AntiDrive": ItemData(329),
    "Thrashmetl": ItemData(317),
    "GuardiaDrive": ItemData(177),
    "FireSmash": ItemData(79),
    "ChronoShot": ItemData(268),
    "Lost Void": ItemData(90),
    "ChaaoticDance": ItemData(344),
    "All You Got (Foil)": ItemData(512),
    "Suprvulcan (Foil)": ItemData(772),
    "Wall (Foil)": ItemData(674),
    "Bubble (Foil)": ItemData(573),
    "Mesmer Eyes (Foil)": ItemData(837),
    "Overcharge (Foil)": ItemData(837),
    "Pushbie": ItemData(24),
    "Firstburst": ItemData(26),
    "Initiative": ItemData(28),
}

cards = {
    "RATD": ItemData(4),
    "Cold As Ice": ItemData(5),
    "Strife": ItemData(6),
    "Morning Ray": ItemData(7),
    "Spitfire": ItemData(10),
    "Seru": ItemData(11),
    "All You Got": ItemData(12),
    "All You Got (Foil)": ItemData(512),
    "Slug Shot": ItemData(13),
    "Drag It Out": ItemData(14),
    "InfernRay": ItemData(15),
    "BlazEdge": ItemData(16),
    "Seeing Red": ItemData(17),
    "Flatten": ItemData(18),
    "Projector": ItemData(19),
    "Off Wave": ItemData(23),
    "Pushbie": ItemData(24),
    "ValorDrive": ItemData(25),
    "FirstBurst": ItemData(26),
    "Initiative": ItemData(28),
    "Sonic Boom": ItemData(29),
    "VariaCut": ItemData(30),
    "Blaze": ItemData(34),
    "TobiasMoor": ItemData(35),
    "Bloody Heck": ItemData(38),
    "Parry": ItemData(39),
    "FRAGSLASH": ItemData(40),
    "FastestFist": ItemData(41),
    "Finish Touch": ItemData(42),
    "Re:Move": ItemData(43),
    "En Passant": ItemData(44),
    "Dragon+": ItemData(48),

    "Motivate": ItemData(52),
    "Gyro": ItemData(53),
    "Hear Me Out": ItemData(56),
    "Field Guard": ItemData(57),
    "Straight Shot": ItemData(58),
    "Softlock": ItemData(59),
    "NthngRhyms": ItemData(60),
    "The Right Time": ItemData(61),
    "Unleash (Foil)": ItemData(562),
    "Jewell": ItemData(64),
    "My Turn": ItemData(65),
    "Not Dead Yet": ItemData(66),
    "Flexibility": ItemData(68),
    "Warm Glow": ItemData(69),
    "ManaShield": ItemData(70),
    "ThiefBolt": ItemData(71),
    "PowerNap": ItemData(72),
    "Bubble": ItemData(73),
    "Bubble (Foil)": ItemData(573),
    "NovaBurst": ItemData(75),
    "MasterDrive": ItemData(76),
    "Pilfer": ItemData(77),
    "VariaJab": ItemData(78),
    "FireSmash": ItemData(79),
    "FRAGHEAL": ItemData(83),
    "Brightslice": ItemData(68),
    "OmniGuard": ItemData(68),
    "ScorchEarth": ItemData(87),
    "Dancer": ItemData(88),
    "SpecialWall": ItemData(89),
    "Lost Void": ItemData(90),
    "Phoenix Mira": ItemData(91),
    "Capitalism": ItemData(92),
    "Consume": ItemData(93),
    "Phoenix+": ItemData(98),

    "Flash": ItemData(102),
    "Soft Glow": ItemData(103),
    "Amp Up": ItemData(105),
    "Synchlite": ItemData(106),
    "Disarm": ItemData(108),
    "Quick Strike": ItemData(109),
    "Overwhelm": ItemData(112),
    "Execute": ItemData(114),
    "Streetlight": ItemData(115),
    "High Kick": ItemData(116),
    "Blacklight": ItemData(118),
    "Screen": ItemData(119),
    "Overcharge": ItemData(120),
    "You'll See": ItemData(121),
    "You'll See (Foil)": ItemData(621),
    "WhaleEarly": ItemData(122),
    "Hold It!": ItemData(123),
    "PainSplit": ItemData(124),
    "BlitzDrive": ItemData(125),
    "YellowJacket": ItemData(126),
    "VariaBolt": ItemData(127),
    "Chain Bolt": ItemData(128),
    "See The Light": ItemData(129),
    "Next Step": ItemData(130),
    "Beat Step": ItemData(133),
    "FRAGSTUN": ItemData(134),
    "Setback": ItemData(135),
    "Beatdown": ItemData(139),
    "Shoot Star": ItemData(140),
    "EggnogGuard": ItemData(141),
    "Glass Cannon": ItemData(142),

    "Somewhen": ItemData(156),
    "Somewhen (Foil)": ItemData(656),
    "TeaTime": ItemData(157),
    "3's A Crowd": ItemData(158),
    "Three's A Crowd": ItemData(159),
    "Dutch Angle": ItemData(160),
    "Mudsling": ItemData(161),
    "Phalanx": ItemData(162),
    "Look Alive": ItemData(163),
    "Helion": ItemData(164),
    "Drift": ItemData(166),
    "ItAin'tEasy": ItemData(167),
    "This Just In": ItemData(168),
    "Meat Shield": ItemData(169),
    "Once More": ItemData(170),
    "Why Lie?": ItemData(172),
    "GuardBreak": ItemData(173),
    "Wall": ItemData(174),
    "Wall (Foil)": ItemData(674),
    "UngaBunga": ItemData(175),
    "GuardiaDrive": ItemData(177),
    "Forcefield": ItemData(178),
    "VariaDrive": ItemData(179),
    "Storage": ItemData(180),
    "Deep Breath": ItemData(182),
    "Gamble Beam": ItemData(183),
    "BergainBin": ItemData(185),
    "Emerald": ItemData(188),
    "FRAGSHIELD": ItemData(189),
    "Robo Punch": ItemData(192),
    "Simple Playing": ItemData(193, ItemClassification.filler, "Card"),
    "GoMode": ItemData(194),
    "Unicorn+": ItemData(198),

    "Drive Bit": ItemData(206),
    "Schema": ItemData(209),
    "Rushdown": ItemData(210),
    "FeelingBlue": ItemData(211),
    "Be The One": ItemData(212),
    "Light Form": ItemData(213),
    "Microwave": ItemData(214),
    "Vizio": ItemData(215),
    "G.D.Break": ItemData(216),
    "Storm": ItemData(217),
    "D-Buster": ItemData(219),
    "Pullbie": ItemData(222),
    "JstDessrts": ItemData(223),
    "LimitDrive": ItemData(224),
    "VariaDive": ItemData(227),
    "Irritate": ItemData(228),
    "Progress": ItemData(229),
    "Grapevine": ItemData(231),
    "FRAGDRIVE": ItemData(234),
    "Wishful": ItemData(236),
    "Wishful (Foil)": ItemData(736),
    "Multiguard": ItemData(237),
    "Pointblank": ItemData(238),
    "Exploit": ItemData(239),
    "Defender": ItemData(241),
    "Vorpal": ItemData(242),
    "Save4thBase": ItemData(243),
    "Mono No Aware": ItemData(244),
    "Kappa+": ItemData(248),

    "Curiosity": ItemData(254),
    "Speed Mode": ItemData(255),
    "Fine Tune": ItemData(256),
    "Ampersand": ItemData(260),
    "Lydian Scale": ItemData(261),
    "Brainwave": ItemData(263),
    "Lavender": ItemData(266),
    "ChronoShot": ItemData(268),
    "ZettaBeam": ItemData(269),
    "ColorPoint": ItemData(271),
    "Suprvulcan": ItemData(272),
    "Suprvulcan (Foil)": ItemData(772),
    "Steamroll": ItemData(274),
    "ChargeBolt": ItemData(275),
    "CloudDitto": ItemData(278),
    "LSDJ": ItemData(279),
    "Contrarian": ItemData(281),
    "Improvise": ItemData(282),
    "WisdomDrive": ItemData(284),
    "Patience": ItemData(286),
    "Reflect": ItemData(287),
    "VariaBeam": ItemData(288),
    "Voidskipper": ItemData(290),
    "FRAGBOOST": ItemData(291),
    "Floodgate": ItemData(293),
    "Tranche-Voix": ItemData(295),
    "JumperJet": ItemData(296),
    "Cyclops+": ItemData(298),

    "CRT": ItemData(303),
    "Zoner": ItemData(304),
    "Play It Loud": ItemData(307),
    "Cellik": ItemData(308),
    "Switchblade": ItemData(310),
    "SmokeBreak": ItemData(311),
    "PaintItBlck": ItemData(312),
    "Wasting Time": ItemData(314),
    "PitchShift": ItemData(315),
    "Thrashmetl": ItemData(316),
    "Ace": ItemData(318),
    "Heavyweight": ItemData(319),
    "Disruption": ItemData(321),
    "SaltInWound": ItemData(322),
    "NoU": ItemData(323),
    "ShadowPulse": ItemData(324),
    "AntiDrive": ItemData(329),
    "Begrudge": ItemData(332),
    "Counter": ItemData(333),
    "VariaSlice": ItemData(334),
    "Mesmer Eyes": ItemData(337),
    "Mesmer Eyes (Foil)": ItemData(837),
    "CraftyCoyote": ItemData(339),
    "FRAGBLAST": ItemData(340),
    "WeirdSig": ItemData(341),
    "Backup": ItemData(342),
    "CursedSword": ItemData(343),
    "ChaoticDance": ItemData(344),
    "GeoRomancey": ItemData(347),
    "Pulgasari+": ItemData(348),
    "Ultima": ItemData(350),

    "Dragon": ItemData(31, ItemClassification.progression, "Card"),
    "Kappa": ItemData(230, ItemClassification.progression, "Card"),
    "Unicorn": ItemData(187, ItemClassification.progression, "Card"),
    "Cyclops": ItemData(292, ItemClassification.progression, "Card"),
    "Phoenix": ItemData(86, ItemClassification.progression, "Card"),
    "Pulgasari": ItemData(345, ItemClassification.progression, "Card"),
    "Pixie": ItemData(137, ItemClassification.progression, "Card"),
}

keys = {
    "Yellow Key": ItemData(2010, ItemClassification.progression, "Key"),
    "Green Key": ItemData(2011, ItemClassification.progression, "Key"),
    "Blue Key": ItemData(2012, ItemClassification.progression, "Key"),
    "Purple Key": ItemData(2013, ItemClassification.progression, "Key"),
    "Red Key": ItemData(2014, ItemClassification.progression, "Key"),
    "Orange Key": ItemData(2015, ItemClassification.progression, "Key"),
    "Black Key": ItemData(2016, ItemClassification.progression, "Key"),

    "Blue_Zone()": ItemData(2018, ItemClassification.progression, "Glitch"),
    "._locale": ItemData(2019, ItemClassification.progression, "Glitch"),

    "Memfinder": ItemData(2009, ItemClassification.progression, "Memfinder"),

    "Red Fragment": ItemData(2022, ItemClassification.progression, "Fragment"),
    "Orange Fragment": ItemData(2023, ItemClassification.progression, "Fragment"),
    "Yellow Fragment": ItemData(2024, ItemClassification.progression, "Fragment"),
    "Green Fragment": ItemData(2025, ItemClassification.progression, "Fragment"),
    "Blue Fragment": ItemData(2026, ItemClassification.progression, "Fragment"),
    "Purple Fragment": ItemData(2027, ItemClassification.progression, "Fragment"),
    "Black Fragment": ItemData(2028, ItemClassification.progression, "Fragment"),
}

consumables = {
    "Heal Token": ItemData(2002, ItemClassification.filler, "Filler", 0),
    "Evade Token": ItemData(2003, ItemClassification.filler, "Filler", 0),
    "Hi-Heal Token": ItemData(2004, ItemClassification.filler, "Filler", 0),
    # Tent Token Here
    "Sneak Token": ItemData(2006, ItemClassification.filler, "Filler", 0),
}

starstuds = {
    "Starstud": ItemData(None, ItemClassification.progression, "Event", 25)
}

#Sawyer: This should give us some random fillers. Let's look into adding traps later.
def get_random_filler_item_name(world: SDWorld) -> str:
    fillers = [
        "Evade Token", "Sneak Token",
        "ChaoticDance",
    ]
    randomResult = world.random.randint(0, len(fillers) - 1)
    return fillers[randomResult]

item_table = {
    # This includes all entries in those other dicts in this one
    **party_members,
    **cards,
    **mp3s,
    **keys,
    **consumables,

    # Events - Note that these are items!

    # Other Items
    #  "Sneak Token":          ItemData(2006,       ItemClassification.filler, "Filler",   1),
}

#Sawyer: Make a random starting member.
def get_random_member(world: SDWorld) -> SDItem:
    #Sawyer: First we get the keys (names of the values) from the party member list.
    members = [key for key, val in party_members.items()]
    #Sawyer: Then we get a random number from the length of that list.
    randomResult = world.random.randint(0, len(members) - 1)
    #Sawyer: Then we get the member belonging to that random number we picked.
    member_name = members[randomResult]
    starty_member = world.create_item(member_name)
    #Next we grab the PinnJoin location which is where the first party member is always given.
    location = world.multiworld.get_location("PinnJoin", world.player)
    #Finally, add it to the location.
    location.place_locked_item(starty_member)
    return starty_member
    #members.remove(starty_member)

def create_all_items(world: SDWorld):
    itempool = []

    for name in item_table:
        itempool.append(world.create_item(name))

    # Starting Party Member given at game start
    #if world.options.starting_party_member:
    itempool.remove(get_random_member(world))

    # other steps here maybe

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


def create_item(self, name: str) -> SDItem:
    item_data = item_table[name]
    item = SDItem(name, item_data.classification, item_data.code, self.player)
    return item