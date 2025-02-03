
# SaneGenesis: AI-Powered Society Simulation

**SaneGenesis** is an ambitious simulation where independent AI entities interact, communicate, evolve, and make decisions in a dynamically generated world. Using reinforcement learning (RL), these agents have full freedom to cheat, lie, or act selfishly to maximize their personal gains. Over time, they develop their own languages, species, and civilizations, shaping a truly unique environment.

## Features

- **Fully Autonomous Agents:** Each entity operates independently, learning from its environment using RL.
- **Communication System:** Agents evolve their own languages and can communicate with one another for cooperation, deception, or manipulation.
- **Selfish Behavior:** Agents can act selfishly, form alliances, betray, and manipulate others for personal gain.
- **Dynamic World:** The world changes in real-time as agents interact, form societies, and evolve.
- **Species Evolution:** Entities can evolve, mutate, and create new species with unique abilities.
- **LLM Integration:** A local GPT model provides decision-making support and allows agents to reason and strategize.

## Installation

### Prerequisites

- Python 3.x
- Stable-Baselines3
- Pygame or Panda3D (for visualization)
- Local GPT model 

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Nikosane/sanegenesis.git
   cd sanegenesis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up the local GPT model:
   - Follow the official instructions for installing and setting up the model locally.
   
4. Run the simulation:
   ```bash
   python main.py
   ```

## Development Roadmap

### Phase 1: Core Mechanics (1-2 Weeks)
- Set up the RL environment
- Create basic agent behaviors (movement, simple actions)
- Implement reward system for decision-making

### Phase 2: Communication & Language (2-3 Weeks)
- Implement basic messaging system
- Train RL agents to develop their own language
- Integrate local GPT for decision-making

### Phase 3: Economy & Interaction (3-4 Weeks)
- Introduce trading, jobs, and economy simulation
- Develop trust, deception, and alliances among agents
- Expand species evolution mechanics

### Phase 4: Full-Scale Simulation (4+ Weeks)
- Enhance UI visualization for tracking entities
- Fine-tune rewards & behaviors for emergent complexity
- Optimize LLM integration for real-time communication

## Contributing

Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
