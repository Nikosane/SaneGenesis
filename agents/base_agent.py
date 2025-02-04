import random

class BaseAgent:
    def __init__(self, agent_id, species="generic", intelligence=1.0, morality=1.0):
        self.agent_id = agent_id  # Unique agent identifier
        self.species = species  # Agent type (e.g., human, animal)
        self.intelligence = intelligence  # Affects decision-making
        self.morality = morality  # Lower values mean higher tendency to cheat/deceive
        self.memory = []  # Stores past interactions
        self.resources = {"food": 10, "money": 5, "influence": 1}  # Starting resources

    def perceive_environment(self, world_state):
        """Processes world data and updates internal state."""
        pass  # To be implemented based on environment structure

    def make_decision(self):
        """Chooses an action based on state and goals."""
        actions = ["trade", "steal", "cooperate", "lie", "explore"]
        if self.morality < 0.5:  # Less moral agents tend to cheat
            actions.append("deceive")
        return random.choice(actions)  # Placeholder for RL-based decision

    def interact(self, other_agent):
        """Interacts with another agent."""
        action = self.make_decision()
        print(f"Agent {self.agent_id} ({self.species}) chooses to {action} with Agent {other_agent.agent_id}")
        
        # Log the interaction
        self.memory.append({"target": other_agent.agent_id, "action": action})
        other_agent.memory.append({"source": self.agent_id, "action": action})

    def update_resources(self, resource, amount):
        """Updates agent's resources based on outcomes."""
        if resource in self.resources:
            self.resources[resource] += amount

    def __str__(self):
        return f"Agent {self.agent_id} | Species: {self.species} | Intelligence: {self.intelligence} | Morality: {self.morality}"
