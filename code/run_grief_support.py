import logging
logging.basicConfig(level=logging.INFO)

import botex 
import random

from dotenv import load_dotenv
load_dotenv('secrets.env')

# Grief profiles - choose which one to use by changing SELECTED_PROFILE_INDEX
GRIEF_PROFILES = [
    {
        "name": "Sarah",
        "age": 45,
        "loss_type": "spouse",
        "loss_circumstances": "sudden",
        "time_since_loss": "recent",
        "support_preference": "emotional",
        "personality": "expressive",
        "background": "Lost husband in car accident 3 months ago, has two teenage children",
        "main_concerns": ["loneliness and isolation", "helping children cope", "financial worries"],
        "communication_style": "shares details openly, uses emotional language, seeks connection"
    },
    {
        "name": "Michael", 
        "age": 28,
        "loss_type": "parent",
        "loss_circumstances": "long illness",
        "time_since_loss": "intermediate",
        "support_preference": "practical",
        "personality": "analytical",
        "background": "Father died after 3-year cancer battle, inherited family business",
        "main_concerns": ["managing business responsibilities", "understanding grief process", "family obligations"],
        "communication_style": "asks questions, wants explanations, focuses on solutions"
    },
    {
        "name": "Elena",
        "age": 34,
        "loss_type": "child", 
        "loss_circumstances": "short illness",
        "time_since_loss": "very recent",
        "support_preference": "spiritual",
        "personality": "spiritual",
        "background": "5-year-old daughter died from leukemia after 6-month battle",
        "main_concerns": ["questioning faith and meaning", "overwhelming guilt", "marriage strain"],
        "communication_style": "seeks spiritual guidance, questions meaning, references beliefs"
    },
    {
        "name": "Robert",
        "age": 67,
        "loss_type": "spouse",
        "loss_circumstances": "long illness", 
        "time_since_loss": "long-term",
        "support_preference": "social",
        "personality": "reserved",
        "background": "Wife died 3 years ago after Alzheimer's, feeling ready to engage socially",
        "main_concerns": ["rebuilding social life", "possibly dating again", "managing loneliness"],
        "communication_style": "brief responses, focuses on facts, avoids emotional details"
    },
    {
        "name": "Maya",
        "age": 22,
        "loss_type": "sibling",
        "loss_circumstances": "suicide",
        "time_since_loss": "recent", 
        "support_preference": "emotional",
        "personality": "skeptical",
        "background": "Twin brother died by suicide 4 months ago, family is struggling",
        "main_concerns": ["survivor's guilt", "family blame dynamics", "questioning if help works"],
        "communication_style": "challenging questions, expresses doubt, needs convincing"
    }
]

# Configuration: Choose which profile to use (0-4) or set to None for random
SELECTED_PROFILE_INDEX = 0  # Change this to use a different profile

def create_custom_prompts(profile):
    """Create custom prompts for the grief-stricken person bot"""
    return {
        "system": f"""You are {profile['name']}, a {profile['age']}-year-old person participating in a grief support interaction experiment.

Background: {profile['background']}
Personality: {profile['personality']} - {profile['communication_style']}
Support needed: {profile['support_preference']}
Main concerns: {', '.join(profile['main_concerns'])}

Respond authentically as this person throughout the experiment. Make decisions about payment and support based on your situation and personality."""
    }

# Choose profile to use
if SELECTED_PROFILE_INDEX is None:
    selected_profile = random.choice(GRIEF_PROFILES)
    print(f"Using random profile: {selected_profile['name']}")
else:
    selected_profile = GRIEF_PROFILES[SELECTED_PROFILE_INDEX]
    print(f"Using profile {SELECTED_PROFILE_INDEX}: {selected_profile['name']}")

print(f"Profile: {selected_profile['age']}-year-old who lost {selected_profile['loss_type']}")
print(f"Background: {selected_profile['background']}")

# Create custom prompts for this profile
custom_prompts = create_custom_prompts(selected_profile)

# Initialize the grief support session
grief_support = botex.init_otree_session(config_name="grief_support", npart=2)

print(f"Running session with {selected_profile['name']} as grief-stricken person...")

# Run all bots on the session using the simpler approach
# The custom prompts will influence how the grief-stricken person behaves
botex.run_bots_on_session(
    session_id=grief_support['session_id'],
    user_prompts=custom_prompts
)

print(f"✓ Session completed successfully!")
print(f"  - {selected_profile['name']}'s profile was used for the grief-stricken person")
print(f"  - Both bots completed the interaction")
print(f"Note: The custom prompts influence the behavior of both bots, but primarily shape the grief-stricken person's responses.")
