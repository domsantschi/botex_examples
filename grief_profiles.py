"""
Grief Support Participant Profiles Configuration

This file contains different profiles of people seeking grief support to create
more diverse and realistic conversations in the grief_support oTree experiment.
"""

import random
from typing import Dict, List, Any

# Define different types of losses
LOSS_TYPES = {
    "spouse": {
        "relationship": "spouse/partner",
        "typical_age_range": (40, 80),
        "common_concerns": [
            "loneliness and isolation",
            "financial worries about single income",
            "learning to do tasks my partner used to handle",
            "deciding what to do with shared belongings",
            "social situations as a single person"
        ]
    },
    "parent": {
        "relationship": "parent",
        "typical_age_range": (25, 70),
        "common_concerns": [
            "feeling orphaned regardless of age",
            "regrets about things left unsaid",
            "managing inherited responsibilities",
            "family dynamics and inheritance conflicts",
            "preserving their memory and legacy"
        ]
    },
    "child": {
        "relationship": "child",
        "typical_age_range": (20, 60),
        "common_concerns": [
            "overwhelming guilt and questioning 'what if'",
            "marriage and family strain",
            "questioning faith and meaning in life",
            "inability to focus at work",
            "fear of having more children"
        ]
    },
    "sibling": {
        "relationship": "sibling",
        "typical_age_range": (15, 80),
        "common_concerns": [
            "complicated family dynamics",
            "survivor's guilt",
            "changing role within the family",
            "childhood memories and shared experiences",
            "supporting aging parents through their grief"
        ]
    },
    "friend": {
        "relationship": "close friend",
        "typical_age_range": (16, 80),
        "common_concerns": [
            "feeling excluded from 'official' mourning",
            "not being recognized as a legitimate griever",
            "navigating relationships with the family",
            "preserving the friendship's memory",
            "finding support when others don't understand the depth of the friendship"
        ]
    },
    "pet": {
        "relationship": "beloved pet",
        "typical_age_range": (8, 80),
        "common_concerns": [
            "others not taking the loss seriously",
            "decision-making about euthanasia",
            "emptiness in daily routines",
            "whether to get another pet",
            "feeling judged for the depth of grief"
        ]
    }
}

# Different circumstances of loss
LOSS_CIRCUMSTANCES = {
    "sudden": {
        "description": "unexpected and sudden (accident, heart attack, etc.)",
        "typical_emotions": ["shock", "disbelief", "anger", "regret"],
        "common_phrases": [
            "I can't believe they're gone",
            "It happened so fast",
            "I never got to say goodbye",
            "I keep expecting them to walk through the door"
        ]
    },
    "illness_short": {
        "description": "after a brief illness (few weeks/months)",
        "typical_emotions": ["exhaustion", "relief mixed with guilt", "regret"],
        "common_phrases": [
            "It all happened so quickly",
            "I feel guilty for feeling relieved",
            "I wasn't prepared for how fast it went",
            "I'm exhausted from caregiving"
        ]
    },
    "illness_long": {
        "description": "after a long illness (years of caregiving)",
        "typical_emotions": ["relief", "guilt about relief", "caregiver fatigue", "identity loss"],
        "common_phrases": [
            "I don't know who I am without being their caregiver",
            "Part of me is relieved the suffering is over",
            "I feel guilty for having a life now",
            "I watched them disappear long before they died"
        ]
    },
    "suicide": {
        "description": "by suicide",
        "typical_emotions": ["guilt", "anger", "shame", "confusion", "stigma"],
        "common_phrases": [
            "I keep wondering what I could have done differently",
            "I'm angry at them but also miss them desperately",
            "People don't know what to say to me",
            "I feel like I failed them"
        ]
    },
    "accident": {
        "description": "in an accident",
        "typical_emotions": ["trauma", "anger at circumstances", "what-if thinking"],
        "common_phrases": [
            "If only they had left five minutes later",
            "I keep replaying that day",
            "I'm angry at the other driver/situation",
            "It feels so senseless"
        ]
    }
}

# Time since loss
TIME_SINCE_LOSS = {
    "very_recent": {
        "timeframe": "1-4 weeks ago",
        "typical_state": "acute grief, shock, numbness",
        "common_needs": ["immediate practical support", "validation of feelings", "help with arrangements"]
    },
    "recent": {
        "timeframe": "1-6 months ago",
        "typical_state": "raw grief, emotional volatility",
        "common_needs": ["coping strategies", "understanding grief process", "social support"]
    },
    "intermediate": {
        "timeframe": "6 months - 2 years ago",
        "typical_state": "waves of grief, trying to rebuild",
        "common_needs": ["meaning-making", "identity reconstruction", "managing anniversary reactions"]
    },
    "long_term": {
        "timeframe": "2+ years ago",
        "typical_state": "integrated grief, occasional difficult moments",
        "common_needs": ["continued growth", "helping others", "managing unexpected grief surges"]
    }
}

# Support preferences
SUPPORT_PREFERENCES = {
    "practical": {
        "focus": "practical help and concrete strategies",
        "typical_requests": [
            "help organizing their belongings",
            "guidance on legal/financial matters",
            "strategies for daily life management",
            "help with memorial planning"
        ]
    },
    "emotional": {
        "focus": "emotional processing and validation",
        "typical_requests": [
            "someone to listen without judging",
            "validation that what I'm feeling is normal",
            "help processing difficult emotions",
            "safe space to share memories"
        ]
    },
    "spiritual": {
        "focus": "meaning-making and spiritual concerns",
        "typical_requests": [
            "help finding meaning in the loss",
            "exploring questions about afterlife",
            "connecting with spiritual practices",
            "understanding why this happened"
        ]
    },
    "social": {
        "focus": "rebuilding social connections",
        "typical_requests": [
            "help navigating social situations",
            "connecting with others who understand",
            "rebuilding social identity",
            "managing others' reactions to my grief"
        ]
    }
}

# Personality traits that affect grief expression
PERSONALITY_TRAITS = {
    "expressive": {
        "description": "open about emotions, talks freely about feelings",
        "communication_style": "shares details, uses emotional language, seeks connection"
    },
    "reserved": {
        "description": "private about emotions, prefers practical approach",
        "communication_style": "brief responses, focuses on facts, avoids emotional details"
    },
    "analytical": {
        "description": "tries to understand and analyze the grief process",
        "communication_style": "asks questions, wants explanations, seeks frameworks"
    },
    "spiritual": {
        "description": "finds meaning through faith or spirituality",
        "communication_style": "references beliefs, seeks spiritual guidance, questions meaning"
    },
    "skeptical": {
        "description": "doubtful about help, may be resistant to suggestions",
        "communication_style": "challenging questions, expresses doubt, needs convincing"
    }
}

class GriefProfile:
    """Represents a specific grief profile for a participant"""
    
    def __init__(self, profile_data: Dict[str, Any]):
        self.loss_type = profile_data['loss_type']
        self.loss_circumstances = profile_data['loss_circumstances']
        self.time_since_loss = profile_data['time_since_loss']
        self.support_preference = profile_data['support_preference']
        self.personality_trait = profile_data['personality_trait']
        self.age = profile_data.get('age', self._generate_age())
        self.name = profile_data.get('name', self._generate_name())
        self.custom_details = profile_data.get('custom_details', {})
    
    def _generate_age(self) -> int:
        """Generate appropriate age based on loss type"""
        age_range = LOSS_TYPES[self.loss_type]['typical_age_range']
        return random.randint(age_range[0], age_range[1])
    
    def _generate_name(self) -> str:
        """Generate a name for the profile"""
        names = ["Alex", "Sam", "Jordan", "Casey", "Riley", "Morgan", "Taylor", "Avery"]
        return random.choice(names)
    
    def get_background_prompt(self) -> str:
        """Generate a background prompt for the LLM to adopt this persona"""
        loss_info = LOSS_TYPES[self.loss_type]
        circumstances_info = LOSS_CIRCUMSTANCES[self.loss_circumstances]
        time_info = TIME_SINCE_LOSS[self.time_since_loss]
        support_info = SUPPORT_PREFERENCES[self.support_preference]
        personality_info = PERSONALITY_TRAITS[self.personality_trait]
        
        background = f"""You are {self.name}, a {self.age}-year-old person who lost your {loss_info['relationship']} {circumstances_info['description']} {time_info['timeframe']}. 

Your loss circumstances: The death was {circumstances_info['description']}. You are currently experiencing {time_info['typical_state']}.

Your personality: You are {personality_info['description']}. Your communication style: {personality_info['communication_style']}.

Your primary concerns include: {', '.join(random.sample(loss_info['common_concerns'], min(3, len(loss_info['common_concerns']))))}

You are seeking {support_info['focus']}. You typically need: {', '.join(support_info['typical_requests'][:2])}.

Your emotional state often includes: {', '.join(circumstances_info['typical_emotions'][:2])}.

When interacting with the service provider, respond authentically as this person would, drawing on these experiences and needs. Be genuine about your grief while staying true to your personality style."""

        return background
    
    def get_initial_response_guidance(self) -> str:
        """Get guidance for crafting the initial response to service provider"""
        circumstances_info = LOSS_CIRCUMSTANCES[self.loss_circumstances]
        support_info = SUPPORT_PREFERENCES[self.support_preference]
        
        guidance = f"""When responding to the service provider's introduction, consider:
- You are looking for {support_info['focus']}
- You might use phrases like: {random.choice(circumstances_info['common_phrases'])}
- Your main concerns right now are: {', '.join(TIME_SINCE_LOSS[self.time_since_loss]['common_needs'])}
- Communicate in a way that reflects your {PERSONALITY_TRAITS[self.personality_trait]['description']} personality"""
        
        return guidance

# Predefined profiles for consistent testing
PREDEFINED_PROFILES = [
    {
        "name": "Sarah",
        "age": 45,
        "loss_type": "spouse",
        "loss_circumstances": "sudden",
        "time_since_loss": "recent",
        "support_preference": "emotional",
        "personality_trait": "expressive",
        "custom_details": {
            "specific_situation": "Lost husband in car accident, has two teenage children",
            "main_challenge": "How to help children cope while dealing with own grief"
        }
    },
    {
        "name": "Michael",
        "age": 28,
        "loss_type": "parent",
        "loss_circumstances": "illness_long",
        "time_since_loss": "intermediate",
        "support_preference": "practical",
        "personality_trait": "analytical",
        "custom_details": {
            "specific_situation": "Father died after 3-year cancer battle, inherited family business",
            "main_challenge": "Managing business responsibilities while grieving"
        }
    },
    {
        "name": "Elena",
        "age": 34,
        "loss_type": "child",
        "loss_circumstances": "illness_short",
        "time_since_loss": "very_recent",
        "support_preference": "spiritual",
        "personality_trait": "spiritual",
        "custom_details": {
            "specific_situation": "5-year-old daughter died from leukemia after 6-month battle",
            "main_challenge": "Questioning faith and finding meaning"
        }
    },
    {
        "name": "Robert",
        "age": 67,
        "loss_type": "spouse",
        "loss_circumstances": "illness_long",
        "time_since_loss": "long_term",
        "support_preference": "social",
        "personality_trait": "reserved",
        "custom_details": {
            "specific_situation": "Wife died 3 years ago after Alzheimer's, feeling ready to engage socially again",
            "main_challenge": "Rebuilding social life and possibly dating again"
        }
    },
    {
        "name": "Maya",
        "age": 22,
        "loss_type": "sibling",
        "loss_circumstances": "suicide",
        "time_since_loss": "recent",
        "support_preference": "emotional",
        "personality_trait": "skeptical",
        "custom_details": {
            "specific_situation": "Twin brother died by suicide, family is struggling",
            "main_challenge": "Survivor's guilt and family blame dynamics"
        }
    }
]

def get_random_profile() -> GriefProfile:
    """Generate a random grief profile"""
    profile_data = {
        'loss_type': random.choice(list(LOSS_TYPES.keys())),
        'loss_circumstances': random.choice(list(LOSS_CIRCUMSTANCES.keys())),
        'time_since_loss': random.choice(list(TIME_SINCE_LOSS.keys())),
        'support_preference': random.choice(list(SUPPORT_PREFERENCES.keys())),
        'personality_trait': random.choice(list(PERSONALITY_TRAITS.keys()))
    }
    return GriefProfile(profile_data)

def get_predefined_profile(index: int = None) -> GriefProfile:
    """Get a predefined profile by index, or random if index not specified"""
    if index is None:
        index = random.randint(0, len(PREDEFINED_PROFILES) - 1)
    
    if index >= len(PREDEFINED_PROFILES):
        raise ValueError(f"Profile index {index} not available. Max index: {len(PREDEFINED_PROFILES) - 1}")
    
    return GriefProfile(PREDEFINED_PROFILES[index])

def get_all_predefined_profiles() -> List[GriefProfile]:
    """Get all predefined profiles"""
    return [GriefProfile(profile) for profile in PREDEFINED_PROFILES]

def create_custom_profile(**kwargs) -> GriefProfile:
    """Create a custom profile with specified parameters"""
    profile_data = {
        'loss_type': kwargs.get('loss_type', random.choice(list(LOSS_TYPES.keys()))),
        'loss_circumstances': kwargs.get('loss_circumstances', random.choice(list(LOSS_CIRCUMSTANCES.keys()))),
        'time_since_loss': kwargs.get('time_since_loss', random.choice(list(TIME_SINCE_LOSS.keys()))),
        'support_preference': kwargs.get('support_preference', random.choice(list(SUPPORT_PREFERENCES.keys()))),
        'personality_trait': kwargs.get('personality_trait', random.choice(list(PERSONALITY_TRAITS.keys()))),
        'age': kwargs.get('age'),
        'name': kwargs.get('name'),
        'custom_details': kwargs.get('custom_details', {})
    }
    return GriefProfile(profile_data)

if __name__ == "__main__":
    # Example usage
    print("=== Random Profile ===")
    random_profile = get_random_profile()
    print(random_profile.get_background_prompt())
    print()
    
    print("=== Predefined Profile ===")
    predefined_profile = get_predefined_profile(0)
    print(predefined_profile.get_background_prompt())
    print()
    
    print("=== Custom Profile ===")
    custom_profile = create_custom_profile(
        loss_type="pet",
        personality_trait="expressive",
        name="Chris"
    )
    print(custom_profile.get_background_prompt())
