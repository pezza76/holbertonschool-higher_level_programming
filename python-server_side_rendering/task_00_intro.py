with open('template.txt', 'r') as file:
    template_content = file.read()



# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

def generate_invitations(template, attendees):
    if isinstance(template_content, str) and isinstance(attendees, list):
        for i in attendees:
            print(template_content.format(**i))
    else:
        return "Function failed"

generate_invitations(template_content, attendees)