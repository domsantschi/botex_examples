import logging
logging.basicConfig(level=logging.INFO)

import botex 

from dotenv import load_dotenv
load_dotenv('secrets.env')

# Choose which game to run by changing the config_name:
# "mftrust" for the original trust game
# "grief_support" for the new grief support interaction game

# Run the grief_support game (new)
grief_support = botex.init_otree_session(config_name = "grief_support", npart = 2)
botex.run_bots_on_session(session_id = grief_support['session_id'])

# Uncomment the lines below to run the mftrust game instead:
# mftrust = botex.init_otree_session(config_name = "mftrust", npart = 2)
# botex.run_bots_on_session(session_id = mftrust['session_id'])