SAFETY_KEYWORDS = [
    "burning",
    "fire",
    "smoke",
    "explosion",
    "electrical shock"
]


def should_escalate(query):

    query = query.lower()

    for keyword in SAFETY_KEYWORDS:

        if keyword in query:

            return True

    return False