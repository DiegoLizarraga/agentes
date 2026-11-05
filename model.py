import mesa
import numpy as np

class SimpleAgent (mesa.Agent):
    def __init__(self, model):
        super().__init__(model)

        self.position = np.random.uniform(1,10,2)
        self.speed = np.random.uniform(-1, 1, 2)

    def step(self):
        self.position += self.position * self.speed


class SimpleModel (mesa. Model):
    def __init__(self, num_agents= 3, width=10, height=10):
        super().__init__()

        
        for i in range(num_agents):
            agent = SimpleAgent(self)
            self.agents.add(agent)
    def step(self):
        self.agents.shuffle_do("step")

    def show_stats(self):

        for a in self.agents:
            print(a.position, a.speed)

    def get_stats(self):
        return {
            "step": self.steps,
            "agents" : [
                {
                    "position": a.position.tolist(),
                    "speed": a.speed.tolist()
                }
                for a in self.agents
            ]

        }