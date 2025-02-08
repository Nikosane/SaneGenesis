from simulation.simulator import Simulator
from utils.logger import Logger
from utils.config import Config

if __name__ == "__main__":
    logger = Logger(Config.LOG_FILE)
    logger.log("Starting SaneGenesis simulation...")
    
    simulator = Simulator()
    simulator.run()
    
    logger.log("Simulation finished.")
