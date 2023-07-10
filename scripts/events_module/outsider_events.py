import random

from scripts.cat.cats import Cat
from scripts.events_module.generate_events import GenerateEvents
from scripts.game_structure.game_essentials import game
from scripts.event_class import Single_Event
from scripts.screens.catlist_screens import otherClanNames, otherClansList


# ---------------------------------------------------------------------------- #
#                               New Cat Event Class                              #
# ---------------------------------------------------------------------------- #

class OutsiderEvents:
    """All events with a connection to outsiders."""

    def __init__(self) -> None:
        self.event_sums = 0
        self.had_one_event = False
        self.generate_events = GenerateEvents()
        pass

    def killing_outsiders(self, cat: Cat):
        # killing outside cats
        if cat.outside:
            if random.getrandbits(6) == 1 and not cat.dead:
                cat.die()
                if cat.exiled:
                    text = f'Rumors reach your Clan that the exiled {cat.name} has died recently.'
                elif cat.status in ['kittypet', 'loner', 'rogue', 'former Clancat']:
                    text = f'Rumors reach your Clan that the {cat.status} ' \
                           f'{cat.name} has died recently.'
                elif cat.otherclan1 and cat.status == "leader" and cat.dead is True:
                    text= f"When {game.clan.name} arrives at the Gathering, they are shocked to find out that {otherClansList[0]}Clan's leader {cat.name} has died."
                elif cat.otherclan1 and cat.status == "leader" and (cat.dead is False or cat.dead is None):
                    text= None  # Leaders are secretive about lives, and this information wouldn't be public knowledge, so no event
                elif cat.otherclan1 and cat.status != "leader":
                    text = f'A patrol informs you that the {cat.status} {cat.name} from {otherClansList[0]}Clan died this past moon.'
                else:
                    cat.outside = False
                    text = f"Will they reach StarClan, even so far away? {cat.name} isn't sure, " \
                           f"but as they drift away, they hope to see " \
                           f"familiar starry fur on the other side."
                game.cur_events_list.append(
                    Single_Event(text, "birth_death", cat.ID))
                
    def lost_cat_become_outsider(self, cat: Cat):
        """ 
        this will be for lost cats becoming kittypets/loners/etc
        TODO: need to make a unique backstory for these cats so they still have thoughts related to their clan
        """
        if random.getrandbits(7) == 1 and not cat.dead:
            self.become_kittypet(cat)

    def become_kittypet(self, cat: Cat):
        # TODO: Make backstory for all of these + for exiled cats
        cat.status = 'kittypet'

    def become_loner(self, cat: Cat):
        cat.status = 'loner'

    def become_rogue(self, cat: Cat):
        """Cats will probably only become rogues if they were exiled formerly"""
        cat.status = 'rogue'
