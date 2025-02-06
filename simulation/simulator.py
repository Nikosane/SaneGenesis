from environment.world import World
from environment.resources import Resources
from environment.rules import Rules

class Simulator:
    def __init__(self):
        self.world = World()
        self.resources = Resources()
        self.rules = Rules()
        self.running = True

    def run(self, steps=10):
        """Runs the simulation for a given number of steps."""
        for _ in range(steps):
            if not self.running:
                break
            
            print("\n--- Simulation Step ---")
            self.world.update_world_state()
            self.world.distribute_resources()
            
            for agent in self.world.agents:
                action = agent.make_decision()
                self.rules.enforce(agent, action)

            print(self.world)

    def stop(self):
        """Stops the simulation."""
        self.running = False
