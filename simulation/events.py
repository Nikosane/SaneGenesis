import random

class Events:
    def __init__(self):
        self.event_list = [
            {"name": "Earthquake", "impact": {"food": -50, "money": -100}},
            {"name": "Economic Boom", "impact": {"money": 200}},
            {"name": "Drought", "impact": {"water": -100}},
            {"name": "Scientific Discovery", "impact": {"influence": 10}}
        ]

    def trigger_event(self, world):
        """Randomly triggers an event that affects world resources."""
        event = random.choice(self.event_list)
        print(f"Event Triggered: {event['name']}")
        
        for resource, change in event["impact"].items():
            if resource in world.resources:
                world.resources[resource] += change
                print(f"{resource} changed by {change}")

    def __str__(self):
        return f"Possible Events: {[event['name'] for event in self.event_list]}"
