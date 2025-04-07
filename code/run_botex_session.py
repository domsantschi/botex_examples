import logging
logging.basicConfig(level=logging.INFO)

import botex 

from dotenv import load_dotenv
load_dotenv('secrets.env')

stakeholder = botex.init_otree_session(config_name = "stakeholder", npart = 1)

botex.run_bots_on_session(
  session_id = stakeholder['session_id']
)