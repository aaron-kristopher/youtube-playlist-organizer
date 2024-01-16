import re

regex = r"(?i)(?:episode|ep)\s*(?P<episode_number>\d{1,4})(?:\s+of\s+\d+\s*)?.*"

def get_episode_number(title):
    match = re.search(regex, title)
    if match:
        return int(match.group("episode_number"))
    else:
        return None  # Or handle cases where no episode number is found

