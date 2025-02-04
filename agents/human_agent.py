from agents.base_agent import BaseAgent
import random

class HumanAgent(BaseAgent):
    def __init__(self, agent_id, intelligence=1.5, morality=0.8):
        super().__init__(agent_id, species="human", intelligence=intelligence, morality=morality)

    def make_decision(self):
        """Humans are more strategic and social."""
        actions = ["negotiate", "trade", "cooperate", "lie", "plan"]
        if self.morality < 0.5:
            actions.append("deceive")
        return random.choice(actions)
