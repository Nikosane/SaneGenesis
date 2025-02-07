import random
import json

class ReinforcementLearning:
    def __init__(self, learning_rate=0.1, discount_factor=0.9):
        self.q_table = {}  # State-action value table
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def get_q_value(self, state, action):
        """Retrieves the Q-value for a given state-action pair."""
        return self.q_table.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        """Updates the Q-value based on agent experience."""
        max_future_q = max([self.get_q_value(next_state, a) for a in ["trade", "steal", "cooperate", "lie", "explore"]], default=0.0)
        current_q = self.get_q_value(state, action)
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_future_q)
        self.q_table[(state, action)] = new_q

    def choose_action(self, state):
        """Chooses an action based on Q-values (with some randomness)."""
        if random.random() < 0.1:  # Exploration rate
            return random.choice(["trade", "steal", "cooperate", "lie", "explore"])
        return max(["trade", "steal", "cooperate", "lie", "explore"], key=lambda action: self.get_q_value(state, action))

# language_model.py - GPT-based decision-making
class LanguageModel:
    def __init__(self, model):
        self.model = model

    def generate_response(self, prompt):
        """Generates a decision or response using the language model."""
        return self.model.generate(prompt)  # Placeholder for actual GPT API call

# Data storage - agents_data.json and world_data.json
class DataStorage:
    def __init__(self, agents_file="data/agents_data.json", world_file="data/world_data.json"):
        self.agents_file = agents_file
        self.world_file = world_file

    def save_agents(self, agents):
        """Saves agent data to JSON."""
        with open(self.agents_file, "w") as f:
            json.dump([agent.__dict__ for agent in agents], f, indent=4)

    def save_world(self, world_state):
        """Saves world data to JSON."""
        with open(self.world_file, "w") as f:
            json.dump(world_state, f, indent=4)

    def load_agents(self):
        """Loads agent data from JSON."""
        try:
            with open(self.agents_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def load_world(self):
        """Loads world data from JSON."""
        try:
            with open(self.world_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
