with open('template.txt', 'r') as file:
    template_content = file.read()



# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

x = 1
def generate_invitations(template, attendees):
    if isinstance(template_content, str) and isinstance(attendees, list):
        for i in attendees:
            data = {
                'name': i.get('name', 'N/A') or 'N/A',
                'event_title': i.get('event_title', 'N/A') or 'N/A',
                'event_date': i.get('event_date', 'N/A') or 'N/A',
                'event_location': i.get('event_location', 'N/A') or 'N/A'
                
            }
            
            with open(f"output_{X}.txt", 'w') as file:
                file.write(template_content.format(**data))
            print(template_content.format(**data))
            X = X + 1
    else:
        return "Function failed"

generate_invitations(template_content, attendees)