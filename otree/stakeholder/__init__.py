import string
import random
from otree.api import *

doc = """
Single player variant of the investment game. The player acts as an investor
who can invest money, which gets multiplied. The return is automatically calculated.
"""

class C(BaseConstants):
    NAME_IN_URL = 'stakeholder'
    PLAYERS_PER_GROUP = None  # Single-player game
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 1
    RETURN_RATE = 0.5  # 50% of the multiplied amount is returned

def create_id():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    id_public = ''.join(random.choices(chars, k=4))
    id_private = ''.join(random.choices(chars, k=4))
    return "{} {}".format(id_public, id_private)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=cu(0),
        max=C.ENDOWMENT,
        doc="""Amount to invest:""",
        label="Please enter an amount from 0 to 100:",
    )
    returned_amount = models.CurrencyField()  # Automatically calculated

class Player(BasePlayer):
    # Add the missing 'stakeholder_consensus' field
    stakeholder_consensus = models.StringField(
        label="Stakeholder Consensus",
        choices=["Negative Stakeholder Consensus", "Positive Stakeholder Consensus"],
    )

    # Existing fields
    condition = models.StringField(
        label="Condition assigned to the player",
        choices=["Low Stakeholder Relevance", "High Stakeholder Relevance"],
    )
    # Fields to store user inputs
    ebit = models.FloatField(label="EBIT")
    net_sales = models.FloatField(label="Net Sales")
    market_cap = models.FloatField(label="Market Capitalization")
    altman_z = models.FloatField(label="Altman Z-Score", initial=0)  # Calculated Z-Score
    justifications = models.LongStringField(
        label="Please provide your written justifications for your assessment."
    )

    # # Fields to store second assessment inputs
    # ebit_assessment2 = models.FloatField(label="EBIT (Assessment 2)", initial=0)
    # net_sales_assessment2 = models.FloatField(label="Net Sales (Assessment 2)", initial=0)
    # market_cap_assessment2 = models.FloatField(label="Market Capitalization (Assessment 2)", initial=0)
    # altman_z_assessment2 = models.FloatField(label="Altman Z-Score (Assessment 2)", initial=0)
    # justifications_assessment2 = models.LongStringField(
    #     label="Justifications for Assessment 2"
    # )

    # Fields for Controls
    risk_attitudes = models.IntegerField(
        label="Are you generally a person who is willing to take risks or do you try to avoid taking risks?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal,
    )
    disclosure_transparency = models.IntegerField(
        label="Do you believe that Acme LLC should provide additional information about its ESG impacts and stakeholder engagement process?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal,
    )
    esg_relevance = models.IntegerField(
        label="How strongly do you personally agree that companies should sacrifice profitability to promote ESG themes?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal,
    )

    # Single-choice questions
    stakeholder_attributes = models.StringField(
        label="Which of the following describes the relevance of the stakeholders consulted for the ESG prioritization initiative?",
        choices=[
            "Low power, legitimacy, and urgency",
            "High power, legitimacy, and urgency",
        ],
        widget=widgets.RadioSelect,
    )
    trendline = models.StringField(
        label="Which of the following describes the trendline of the stakeholder consensus depicted in Acme's ESG theme prioritization chart?",
        choices=[
            "Negative correlation",
            "Positive correlation",
        ],
        widget=widgets.RadioSelect,
    )

    # Multiple-choice questions
    internal_stakeholders = models.LongStringField(
        label="When considering internal stakeholders, who did you think about?",
        blank=True,  # Allow blank if no options are selected
    )
    internal_stakeholders_other = models.StringField(
        label="If other, please explain:",
        blank=True,
    )
    external_stakeholders = models.LongStringField(
        label="When considering external stakeholders, who did you think about?",
        blank=True,  # Allow blank if no options are selected
    )
    external_stakeholders_other = models.StringField(
        label="If other, please explain:",
        blank=True,
    )

    # Add these fields to track individual selections
    internal_investors = models.BooleanField(initial=False)
    internal_suppliers = models.BooleanField(initial=False)
    internal_customers = models.BooleanField(initial=False)
    internal_regulators = models.BooleanField(initial=False)
    internal_ngos = models.BooleanField(initial=False)
    internal_community = models.BooleanField(initial=False)
    internal_media = models.BooleanField(initial=False)
    
    # Add these fields to track individual selections
    external_employees = models.BooleanField(initial=False)
    external_executive = models.BooleanField(initial=False)
    external_board = models.BooleanField(initial=False)
    external_chairman = models.BooleanField(initial=False)
    external_ceo = models.BooleanField(initial=False)
    
    age = models.StringField(
        label="What is your age?",
        choices=[
            "Less than 25 years old",
            "25-34 years old",
            "35-44 years old",
            "45-54 years old",
            "55-64 years old",
            "65-74 years old",
            "Above 74 years old",
        ],
        widget=widgets.RadioSelect,
    )
    gender = models.StringField(
        label="What is your gender?",
        choices=["Male", "Female", "Other"],
        widget=widgets.RadioSelect,
    )
    qualification = models.StringField(
        label="Please select the highest academic qualification that you have.",
        choices=[
            "Diploma",
            "Bachelor Degree",
            "Masters Degree",
            "Doctoral Degree",
            "None of the above",
        ],
        widget=widgets.RadioSelect,
    )
    finance_experience = models.IntegerField(
        label="How many years of full-time working experience in a finance role do you have?",
        min=0,
    )
    investment_research = models.IntegerField(
        label="How involved are you with investment research?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal,
    )
    risk_assessments = models.IntegerField(
        label="How involved are you with risk assessments?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal,
    )

    # New field to store feedback
    feedback = models.LongStringField(
        label="Participant feedback",
        blank=True,  # Optional field
    )

# --- Functions ----------------------------------------------------------------

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.wealth = cu(0)
            p.participant.part_id = create_id()
            # Randomly assign a condition
            p.condition = random.choice(['Low Stakeholder Relevance', 'High Stakeholder Relevance'])
            # Randomly assign Stakeholder Consensus (Condition 3 or 4)
            p.stakeholder_consensus = random.choice(['Negative Stakeholder Consensus', 'Positive Stakeholder Consensus'])

# def set_payoffs(group: Group):
#     player = group.get_player_by_id(1)
#     multiplied_amount = group.sent_amount * C.MULTIPLIER
#     group.returned_amount = multiplied_amount * C.RETURN_RATE
#     player.payoff = C.ENDOWMENT - group.sent_amount + group.returned_amount
#     player.participant.wealth += player.payoff

# --- Pages --------------------------------------------------------------------

class Introduction(Page):
    pass

class Background(Page):
    pass

class Strategy(Page):
    pass

class Condition1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            condition=player.condition
        )

class Assessment(Page):
    form_model = 'player'
    form_fields = [
        'ebit',
        'net_sales',
        'market_cap',
        'justifications',
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Calculate the Z-Score and store it in the player model
        total_assets = 90000
        total_liabilities = 65000
        current_assets = 50000
        current_liabilities = 40000
        retained_earnings = 5000

        # Financial ratios
        x1 = (current_assets - current_liabilities) / total_assets
        x2 = retained_earnings / total_assets
        x3 = player.ebit / total_assets
        x4 = player.market_cap / total_liabilities
        x5 = player.net_sales / total_assets

        # Calculate Z-Score
        player.altman_z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1 * x5

class Condition2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            condition=player.condition,
            stakeholder_consensus=player.stakeholder_consensus,  # Pass stakeholder_consensus to the template
        )

class Controls(Page):
    form_model = 'player'
    form_fields = [
        'risk_attitudes',
        'disclosure_transparency',
        'esg_relevance',
    ]

class Checks(Page):
    form_model = 'player'
    form_fields = [
        'stakeholder_attributes',
        'trendline',
        'internal_stakeholders_other',
        'external_stakeholders_other',
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Combine selected checkboxes into a single string for internal stakeholders
        internal_selected = player.participant.vars.get('internal_stakeholders', [])
        player.internal_stakeholders = ', '.join(internal_selected)

        # Combine selected checkboxes into a single string for external stakeholders
        external_selected = player.participant.vars.get('external_stakeholders', [])
        player.external_stakeholders = ', '.join(external_selected)

class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'qualification',
        'finance_experience',
        'investment_research',
        'risk_assessments',
    ]

class Thanks(Page):
    form_model = 'player'
    form_fields = ['feedback']  # Capture feedback in the database

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            participant_id=player.participant.part_id
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Save feedback to the database
        feedback = player.feedback
        if feedback:
            print(f"Feedback received: {feedback}")

# Update the page sequence
page_sequence = [
    Introduction,
    Background,
    Strategy,
    Condition1,
    Condition2,
    Assessment,
    Checks,
    Controls,
    Demographics,
    Thanks,
]