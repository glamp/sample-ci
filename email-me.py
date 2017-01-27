import time
import random
from bandit import Bandit
import json

email = {
    'recipients': ['greg@yhathq.com', 'colin@yhathq.com'],
    'subject': 'This is a test email',
    'body': 'Hi Colin'
}

with open('/job/metadata/email.json', 'wb') as f:
    f.write(json.dumps(email))

