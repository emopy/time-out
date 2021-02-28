import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint

import inquirer

questions = [
    inquirer.List('lang',
                  message="What type of alarm do you want?",
                  choices=['normal', 'angry', 'owo', 'pirate'],
              ),
]

answers = inquirer.prompt(questions)

pprint(answers)
