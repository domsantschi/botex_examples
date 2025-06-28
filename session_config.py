# Grief Support Session Configuration
# 
# This file allows you to easily configure which grief profile to use
# for your botex sessions. Simply change the settings below and run
# the session script.

# Profile Selection
# -----------------
# Set to "predefined" to use a predefined profile by index
# Set to "random" to generate a completely random profile
# Set to "custom" to create a custom profile with specific characteristics
PROFILE_TYPE = "predefined"

# If using predefined profile, specify the index (0-4):
# 0: Sarah - 45, sudden spousal loss, expressive, emotional support
# 1: Michael - 28, long parental illness, analytical, practical support  
# 2: Elena - 34, child illness, spiritual, meaning-making support
# 3: Robert - 67, long spousal illness, reserved, social support
# 4: Maya - 22, sibling suicide, skeptical, emotional support
PREDEFINED_PROFILE_INDEX = 0

# Session Configuration
# --------------------
# Number of sessions to run
NUM_SESSIONS = 1

# Whether to show detailed profile information before running
SHOW_PROFILE_DETAILS = True

# Whether to demonstrate the custom prompts (without running sessions)
DEMONSTRATE_PROMPTS_ONLY = False

# Custom Profile Settings (only used if PROFILE_TYPE = "custom")
# -------------------------------------------------------------
CUSTOM_PROFILE = {
    "name": "Chris",
    "age": 35,
    "loss_type": "pet",  # Options: spouse, parent, child, sibling, friend, pet
    "loss_circumstances": "sudden",  # Options: sudden, illness_short, illness_long, suicide, accident
    "time_since_loss": "recent",  # Options: very_recent, recent, intermediate, long_term
    "support_preference": "emotional",  # Options: practical, emotional, spiritual, social
    "personality_trait": "expressive",  # Options: expressive, reserved, analytical, spiritual, skeptical
    "custom_details": {
        "specific_situation": "Lost beloved dog in unexpected accident",
        "main_challenge": "Others don't understand the depth of the bond"
    }
}

# Advanced Settings
# ----------------
# Whether to run comparative sessions with multiple profiles
RUN_COMPARATIVE_SESSIONS = False

# Whether to run all predefined profiles in sequence
RUN_ALL_PROFILES = False

# LLM Configuration (optional - will use defaults from secrets.env if not specified)
# --------------------------------------------------------------------------------
# MODEL = "gpt-4o-2024-08-06"  # Uncomment to override default model
# THROTTLE = False  # Uncomment to override default throttling

# Export Settings
# ---------------
# Whether to export session data after completion
EXPORT_DATA = True
EXPORT_PREFIX = "grief_support_session"
