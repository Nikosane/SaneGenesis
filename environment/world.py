class World:
    def __init__(self):
        self.agents = []  # List of all agents in the world
        self.resources = {"food": 1000, "money": 5000}  # Initial resource pool
        self.time_step = 0  # Simulation time tracker

    def add_agent(self, agent):
        """Adds an agent to the world."""
        self.agents.append(agent)

    def update_world_state(self):
        """Updates the world state each time step."""
        self.time_step += 1
        print(f"Time Step: {self.time_step}")
        
        for agent in self.agents:
            agent.perceive_environment(self)
            action = agent.make_decision()
            print(f"{agent} decided to {action}")

    def distribute_resources(self):
        """Handles global resource distribution."""
        for agent in self.agents:
            if self.resources["food"] > 0:
                agent.update_resources("food", 1)
                self.resources["food"] -= 1

    def enforce_rules(self):
        """Applies world rules (e.g., punishments, rewards)."""
        pass  # To be implemented later

    def __str__(self):
        return f"World State - Time Step: {self.time_step}, Agents: {len(self.agents)}, Resources: {self.resources}"
