# Grief Support Interaction Game

## Overview

The grief_support game is a two-player interaction experiment where participants take on the roles of:

1. **Grief-stricken person**: Someone who recently lost a beloved one and is seeking support services
2. **Service provider**: A professional who provides support services for people in grief

## Game Mechanics

### Structure
- **Players per group**: 2
- **Number of rounds**: 3
- **Initial budget**: 100 points for the grief-stricken person

### Flow of Interaction

1. **Introduction** (Round 1 only)
   - Both players see the game instructions
   - Roles are randomly assigned

2. **Initial Message** (Round 1 only, Service Provider)
   - Service provider can send an introduction message
   - Optional: Can describe their services, approach, experience
   - This helps build trust and set expectations

3. **Response** (Grief-stricken Person)
   - Reads the service provider's introduction (if any)
   - Decides how much to pay for services (0-100 points)
   - Can send a response message describing their needs

4. **Service Provision** (Service Provider)
   - Sees the payment amount and response message
   - Decides on effort level (0-10) - costs 5 points per level
   - Decides on service quality (0-10) - represents actual value delivered
   - Can send a final message to the client

5. **Results**
   - Both players see the outcomes of their interaction
   - Payoffs are calculated and displayed

### Payoff Calculations

**Grief-stricken person:**
- Payoff = Initial Budget - Payment + Support Received
- Support Received = (Effort Level + Service Quality) × Effort Multiplier (2)

**Service provider:**
- Payoff = Payment Received - Effort Cost
- Effort Cost = Effort Level × 5

### Example
If the grief-stricken person pays 60 points and the service provider chooses effort level 5 and service quality 7:

- Support received = (5 + 7) × 2 = 24 points
- Grief-stricken person's payoff = 100 - 60 + 24 = 64 points
- Service provider's payoff = 60 - (5 × 5) = 35 points

## Key Features

### Communication
- **Initial message**: Service provider introduces their services
- **Response message**: Grief-stricken person shares their needs
- **Final message**: Service provider can provide additional support or explanations

### Strategic Elements
- **For grief-stricken person**: Balance between getting help and conserving budget
- **For service provider**: Balance between earning payment and providing quality service
- **Trust building**: Messages help establish rapport and set expectations

### Measurements
The game includes post-experiment questionnaires measuring:
- Empathy
- Support-seeking behavior
- Helping motivation
- Professional trust
- Feedback on the interaction

## Running the Game

### With botex
```python
import botex
from dotenv import load_dotenv
load_dotenv('secrets.env')

# Initialize and run the game
grief_support = botex.init_otree_session(config_name="grief_support", npart=2)
botex.run_bots_on_session(session_id=grief_support['session_id'])
```

### Manual testing
The game can also be run manually through the oTree interface at the `/grief_support` URL when the oTree server is running.

## Files Structure

```
otree/grief_support/
├── __init__.py              # Main game logic
├── Introduction.html        # Game instructions
├── InitialMessage.html      # Service provider introduction
├── Response.html           # Grief-stricken person response
├── ServiceProvision.html   # Service provider's service decisions
├── Results.html            # Round results display
├── Checks.html             # Post-game questionnaire
└── Thanks.html             # Final thank you page
```

## Comparison with mftrust

| Aspect | mftrust | grief_support |
|--------|---------|---------------|
| **Context** | Business/Investment | Personal Support Services |
| **Roles** | Investor & Manager | Grief-stricken Person & Service Provider |
| **Key Decision** | Investment amount | Payment for services |
| **Provider Decision** | Dividend return | Effort & service quality |
| **Communication** | Single message option | Multiple message exchanges |
| **Rounds** | 3 | 3 |
| **Focus** | Trust and reciprocity | Empathy and professional care |

The grief_support game maintains the same technical structure as mftrust while introducing a more emotionally meaningful context that allows for studying different aspects of human behavior and trust in professional care relationships.
