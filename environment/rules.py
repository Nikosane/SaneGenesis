class Rules:
    def __init__(self):
        self.laws = [
            "No stealing allowed (Penalty: -5 money)",
            "Honest trade is rewarded (+2 money)",
            "Lying has a chance of backfiring (Lose 3 influence)"
        ]

    def enforce(self, agent, action):
        """Enforces rules based on agent actions."""
        if action == "steal":
            agent.update_resources("money", -5)
        elif action == "trade":
            agent.update_resources("money", 2)
        elif action == "lie":
            if agent.intelligence < 1.0:  # Less intelligent agents are worse at lying
                agent.update_resources("influence", -3)

    def get_rules(self):
        """Returns the list of world rules."""
        return self.laws

    def __str__(self):
        return f"World Rules: {self.laws}"
