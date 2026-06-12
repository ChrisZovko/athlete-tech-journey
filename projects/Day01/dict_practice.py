sessions = [
    {"type": "bjj", "minutes": 60},
    {"type": "muay thai", "minutes": 90},
    {"type": "bjj", "minutes": 45},
]

def minutes_per_type(sessions):
    totals = {}
    for session in sessions: 
        if session["type"] in totals:
            totals[session["type"]] += session["minutes"]
        else:
            totals[session["type"]] = session["minutes"]
    return totals   

def count_per_type(sessions):
    counts = {}
    for session in sessions: 
        if session["type"] in counts:
            counts[session["type"]] += 1
        else:
            counts[session["type"]] = 1
    return counts

def longest_per_type(sessions):
    longest = {}
    for session in sessions: 
        if session["type"] in longest:
            longest[session["type"]] = max(longest[session["type"]], session["minutes"])
        else:
            longest[session["type"]] = session["minutes"]
    return longest


print(minutes_per_type(sessions))
print(count_per_type(sessions)) 
print(longest_per_type(sessions))