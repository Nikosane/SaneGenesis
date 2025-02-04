from agents.base_agent import BaseAgent
import random

class AnimalAgent(BaseAgent):
    def __init__(self, agent_id, intelligence=0.5, morality=1.0):
        super().__init__(agent_id, species="animal", intelligence=intelligence, morality=morality)

    def make_decision(self):
        """Animals act on instincts rather than complex strategies."""
        actions = ["hunt", "flee", "graze", "defend"]
        return random.choice(actions)
