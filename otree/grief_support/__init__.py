import string
import random

from otree.api import *

doc = """
This is a game where two individuals interact:
a) a person who recently lost a beloved one (grief-stricken person)
b) a person who provides services for people who lost a beloved one (service provider)

The two participants can chat with each other and the grief-stricken person
can decide how much to pay for the services, while the service provider
can decide how much effort to put into helping.
"""

class C(BaseConstants):
    NAME_IN_URL = 'grief_support'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    INITIAL_BUDGET = cu(100)  # Budget for the grief-stricken person
    EFFORT_MULTIPLIER = 2  # How much more effective professional help is

# This is running the N*(1/62^4) risk that two public IDs are identical.
# I am willing to take that risk ;-)
 
def create_id():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    id_public = ''.join(random.choices(chars, k = 4))
    id_private = ''.join(random.choices(chars, k = 4))
    return("{} {}".format(id_public, id_private))

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    # Messages exchanged between participants
    initial_message = models.LongStringField(
        label="Please enter your initial message to the grief-stricken person:",
        blank=True
    )
    
    response_message = models.LongStringField(
        label="Please enter your response to the service provider:",
        blank=True
    )
    
    final_message = models.LongStringField(
        label="Please enter your final message:",
        blank=True
    )
    
    # Payment from grief-stricken person to service provider
    payment_amount = models.CurrencyField(
        min=cu(0),
        max=C.INITIAL_BUDGET,
        doc="""Amount willing to pay for support services:""",
        label="How much are you willing to pay for support services (0 to 100):",
    )
    
    # Effort level provided by service provider
    effort_level = models.IntegerField(
        min=0,
        max=10,
        doc="""Effort level to provide support (0-10):""",
        label="How much effort will you put into providing support (0 = minimal, 10 = maximum):",
    )
    
    # Service provider's response to payment
    service_quality = models.IntegerField(
        min=0,
        max=10,
        doc="""Quality of service provided (0-10):""",
        label="What quality of service will you provide (0 = minimal, 10 = exceptional):",
    )

class Player(BasePlayer):
    well_being = models.CurrencyField(initial = cu(0))  # Accumulated well-being/satisfaction
    
    comprehension_check = models.IntegerField(
        label="What is the role of payment in this interaction?",
        blank=False,
        choices=[
            [1, 'It only benefits the service provider'],
            [2, 'It only benefits the grief-stricken person'],
            [3, 'It enables better support services, potentially benefiting both parties'],
        ],
    )
    
    manipulation_check = models.IntegerField(
        label="What was your role in the experiment?",
        blank=False,
        choices=[
            [1, 'Grief-stricken person'],
            [2, 'Service provider'],
        ]
    )

    empathy = models.IntegerField(
        label="I can easily understand how others are feeling.",
        blank=False,
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neutral'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
        ]
    )
    
    support_seeking = models.IntegerField(
        label="I am comfortable seeking help from others when I need it.",
        blank=False,
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neutral'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
        ]
    )
    
    helping_motivation = models.IntegerField(
        label="I am motivated to help others who are going through difficult times.",
        blank=False,
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neutral'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
        ]
    )
    
    professional_trust = models.IntegerField(
        label="I believe professional service providers genuinely care about helping people.",
        blank=False,
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neutral'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
        ]
    )

    feedback = models.LongStringField(
        label="Do you have any feedback about this interaction that you want to share?",
        blank=True
    )


# --- Functions ----------------------------------------------------------------

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.well_being = cu(0)
            p.participant.part_id = create_id()
    
def effort_level_max(group: Group):
    return 10

def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)  # Grief-stricken person
    p2 = group.get_player_by_id(2)  # Service provider
    
    # Calculate well-being for grief-stricken person
    # Higher service quality and effort improve well-being, payment reduces budget
    support_received = (group.service_quality + group.effort_level) * C.EFFORT_MULTIPLIER
    p1.payoff = C.INITIAL_BUDGET - group.payment_amount + support_received
    
    # Calculate payoff for service provider
    # Payment received minus cost of effort
    effort_cost = group.effort_level * 5  # Each effort point costs 5 points
    p2.payoff = group.payment_amount - effort_cost
    
    p1.participant.well_being += p1.payoff
    p2.participant.well_being += p2.payoff


# --- Pages --------------------------------------------------------------------
    
class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class InitialMessage(Page):
    """This page is only for P2 (service provider) and only in the first round
    P2 has the option to send an initial message to P1 (grief-stricken person)"""

    form_model = 'group'
    form_fields = ['initial_message']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.round_number == 1

class MessageWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    pass

class Response(Page):
    """This page is for P1 (grief-stricken person) to respond and decide on payment"""

    form_model = 'group'
    form_fields = ['response_message', 'payment_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        initial_message = group.in_round(1).initial_message
        message_exists = initial_message != ""
        return dict(message_exists=message_exists, initial_message=initial_message)

class ServiceWaitPage(WaitPage):
    pass

class ServiceProvision(Page):
    """This page is for P2 (service provider) to decide on effort and service quality"""

    form_model = 'group'
    form_fields = ['effort_level', 'service_quality', 'final_message']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(
            payment_amount=group.payment_amount,
            response_message=group.response_message
        )

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    """This page displays the outcomes of the interaction"""

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        
        support_received = (group.service_quality + group.effort_level) * C.EFFORT_MULTIPLIER
        effort_cost = group.effort_level * 5

        return dict(
            support_received=support_received,
            effort_cost=effort_cost,
            p1_well_being=group.get_player_by_id(1).participant.well_being,
            p2_well_being=group.get_player_by_id(2).participant.well_being,
            final_message=group.final_message
        )

class Checks(Page):
    """This page is displayed after the experimental run is complete."""
    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS
    
    form_model = 'player'
    form_fields = [
        'comprehension_check', 'manipulation_check', 
        'empathy', 'support_seeking', 'helping_motivation', 'professional_trust',
        'feedback'
    ]

class Thanks(Page):
    """This page is displayed after the experimental run is complete."""
    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            participant_id=player.participant.part_id
        )

page_sequence = [
    Introduction,
    InitialMessage,
    MessageWaitPage,
    Response,
    ServiceWaitPage,
    ServiceProvision,
    ResultsWaitPage,
    Results,
    Checks,
    Thanks
]
