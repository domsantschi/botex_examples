# Grief Profile System Documentation

## Overview

The grief profile system allows you to create diverse, realistic participants for the grief support interaction game. Instead of having generic LLM bots, you can now have participants with specific backgrounds, personalities, and grief experiences that lead to more varied and meaningful conversations.

## Quick Start

The easiest way to run sessions with profiles is:

```bash
python run_configured_grief_sessions.py
```

This uses the settings in `session_config.py`. By default, it runs one session with Sarah's profile (recent spousal loss).

## Available Profile Types

### 1. Predefined Profiles

Five carefully crafted profiles representing different grief situations:

| Index | Name | Age | Loss Type | Circumstances | Time Since | Support Type | Personality |
|-------|------|-----|-----------|---------------|------------|--------------|-------------|
| 0 | Sarah | 45 | Spouse | Sudden | Recent | Emotional | Expressive |
| 1 | Michael | 28 | Parent | Long illness | Intermediate | Practical | Analytical |
| 2 | Elena | 34 | Child | Short illness | Very recent | Spiritual | Spiritual |
| 3 | Robert | 67 | Spouse | Long illness | Long-term | Social | Reserved |
| 4 | Maya | 22 | Sibling | Suicide | Recent | Emotional | Skeptical |

### 2. Random Profiles

Automatically generated profiles with random combinations of:
- Loss types: spouse, parent, child, sibling, friend, pet
- Circumstances: sudden, illness_short, illness_long, suicide, accident
- Time since loss: very_recent, recent, intermediate, long_term
- Support preferences: practical, emotional, spiritual, social
- Personality traits: expressive, reserved, analytical, spiritual, skeptical

### 3. Custom Profiles

Create your own profiles with specific characteristics.

## Usage Examples

### Basic Usage (Default)

```python
# Uses session_config.py settings
python run_configured_grief_sessions.py
```

### Quick Profile Testing

```python
from grief_profiles import get_predefined_profile

# Test a specific profile
profile = get_predefined_profile(0)  # Sarah
print(profile.get_background_prompt())
```

### Advanced Scripting

```python
import botex
from grief_profiles import get_random_profile, create_custom_profile

# Run with random profile
profile = get_random_profile()
grief_support = botex.init_otree_session(config_name="grief_support", npart=2)

# Create custom prompts
custom_prompts = create_grief_persona_prompts(profile)

# Run with profile-specific behavior
botex.run_single_bot(
    url=grief_support['bot_urls'][0],
    user_prompts=custom_prompts
)
```

## Configuration Options

Edit `session_config.py` to customize:

### Profile Selection
```python
PROFILE_TYPE = "predefined"  # or "random" or "custom"
PREDEFINED_PROFILE_INDEX = 0  # 0-4 for predefined profiles
```

### Session Settings
```python
NUM_SESSIONS = 1  # Number of sessions to run
SHOW_PROFILE_DETAILS = True  # Show profile info before running
```

### Custom Profile Creation
```python
CUSTOM_PROFILE = {
    "name": "Alex",
    "age": 30,
    "loss_type": "friend",
    "loss_circumstances": "accident", 
    "time_since_loss": "recent",
    "support_preference": "emotional",
    "personality_trait": "expressive"
}
```

## How Profiles Affect Conversations

### System Prompts
Each profile generates a custom system prompt that tells the LLM:
- Who they are (name, age, background)
- What they lost and how
- Their current emotional state
- Their personality and communication style
- What kind of support they're seeking

### Example System Prompt
```
You are Sarah, a 45-year-old person who lost your spouse/partner 
unexpected and sudden (accident, heart attack, etc.) 1-6 months ago.

Your loss circumstances: The death was unexpected and sudden. 
You are currently experiencing raw grief, emotional volatility.

Your personality: You are open about emotions, talks freely about feelings. 
Your communication style: shares details, uses emotional language, seeks connection.

Your primary concerns include: loneliness and isolation, financial worries 
about single income, learning to do tasks my partner used to handle.

You are seeking emotional processing and validation...
```

### Behavioral Impact
Profiles influence:
- **Payment decisions**: Based on financial situation and trust level
- **Message content**: Reflects personality and communication style  
- **Response to service provider**: Based on current needs and skepticism level
- **Emotional expression**: Matches personality trait (expressive vs. reserved)

## Available Scripts

### 1. `run_configured_grief_sessions.py` (Recommended)
- Main runner using configuration file
- Easiest to use and customize
- Saves session logs automatically

### 2. `code/run_grief_support_advanced.py`
- Direct scripting with profiles
- More programming control
- Good for testing specific combinations

### 3. `code/run_grief_support_with_profiles.py`
- Basic profile demonstration
- Shows how profiles work without full botex integration

### 4. `grief_profiles.py`
- Profile definitions and creation functions
- Can be imported and used in other scripts

## Benefits of the Profile System

### Research Benefits
- **Realistic diversity**: Represents actual grief experiences
- **Controlled variation**: Systematic testing of different circumstances
- **Reproducible results**: Predefined profiles ensure consistency
- **Rich interactions**: More meaningful conversations than generic bots

### Conversation Quality
- **Authentic responses**: Based on real grief experiences
- **Varied communication styles**: Different personality expressions
- **Contextual decision-making**: Payment and trust decisions reflect circumstances
- **Emotional authenticity**: Responses match grief stage and type

### Testing Capabilities
- **Service provider training**: Test responses to different client types
- **System validation**: Ensure game works across grief situations  
- **Comparative analysis**: Study how different profiles interact with services
- **Edge case testing**: Include difficult situations like suicide or child loss

## Data Export

Session logs are automatically saved when `EXPORT_DATA = True` in configuration:

```json
{
  "timestamp": "20240628_143022",
  "session_id": "abc123",
  "profile": {
    "name": "Sarah",
    "age": 45,
    "loss_type": "spouse",
    "loss_circumstances": "sudden",
    "time_since_loss": "recent",
    "support_preference": "emotional", 
    "personality_trait": "expressive"
  },
  "session_info": { ... }
}
```

## Best Practices

### For Research
1. **Use predefined profiles** for consistent, comparable results
2. **Document which profiles** you use in each experiment
3. **Run multiple sessions** per profile to see variation
4. **Compare across profiles** to understand how circumstances affect behavior

### For Development
1. **Start with one profile** to test basic functionality
2. **Use random profiles** to test edge cases
3. **Create custom profiles** for specific testing scenarios
4. **Monitor conversation quality** and adjust prompts if needed

### For Production
1. **Balance profile types** across sessions
2. **Consider ethical implications** of simulated grief
3. **Validate that profiles** represent real populations appropriately
4. **Document methodology** for transparency

## Extending the System

### Adding New Loss Types
```python
LOSS_TYPES["grandparent"] = {
    "relationship": "grandparent",
    "typical_age_range": (15, 50),
    "common_concerns": ["family tradition loss", "generational wisdom gap"]
}
```

### Adding New Personality Traits
```python
PERSONALITY_TRAITS["pragmatic"] = {
    "description": "focuses on practical solutions and moving forward",
    "communication_style": "goal-oriented, solution-focused, brief"
}
```

### Custom Prompt Templates
You can modify the prompt generation in `create_grief_persona_prompts()` to:
- Add more specific guidance for certain loss types
- Include cultural or demographic considerations
- Adjust communication style instructions
- Add experimental condition instructions

This system provides a robust foundation for studying grief support interactions while maintaining experimental rigor and ethical sensitivity.
