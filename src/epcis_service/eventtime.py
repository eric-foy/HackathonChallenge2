import time
from datetime import datetime, timezone

def now():
    return datetime.utcnow().isoformat(timespec='seconds')

#2005-04-03T20:33:31.116-06:00
