class Config:
    """Configuration settings for the simulation."""
    LOG_FILE = "simulation.log"
    AGENT_START_RESOURCES = {
        "food": 10,
        "money": 5,
        "influence": 1
    }
    SIMULATION_TICKS = 100  # Number of steps in the simulation
    EXPLORATION_RATE = 0.1  # Probability of taking a random action
