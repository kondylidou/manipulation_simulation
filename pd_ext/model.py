from mesa import Model
from mesa.time import BaseScheduler, RandomActivation, SimultaneousActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from pd_ext.agent import PDAgent


class PdGrid(Model):
    """Model class for iterated, spatial prisoner's dilemma model."""

    schedule_types = {
        "Sequential": BaseScheduler,
        "Random": RandomActivation,
        "Simultaneous": SimultaneousActivation,
    }

    defection_award = 1.6

    def __init__(
            self, width=50, height=50, initial_cooperation=50, initial_manipulation=50, defection_award=1.6,
            manipulation_capacity=50, schedule_type="Random", payoffs=None, seed=None
    ):
        """
        Create a new Spatial Prisoners' Dilemma Model.
        Args:
            width, height: Grid size. There will be one agent per grid cell.
            schedule_type: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        """
        self.initial_cooperation = initial_cooperation
        self.initial_manipulation = initial_manipulation
        self.defection_award = defection_award
        self.manipulation_capacity = manipulation_capacity
        self.grid = SingleGrid(width, height, torus=True)
        self.schedule_type = schedule_type
        self.schedule = self.schedule_types[self.schedule_type](self)

        # Create agents
        for x in range(width):
            for y in range(height):
                agent = PDAgent((x, y), initial_cooperation, initial_manipulation, self) 
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.datacollector = DataCollector(
            {
                "Cooperating_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "C"]
                )
            }
        )

        self.running = True
        self.datacollector.collect(self)

    def update_payoff(self):
        # This dictionary holds the payoff for this agent,
        # keyed on: (my_move, other_move)
        return {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): self.defection_award, ("D", "D"): 0}

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run(self, n):
        """Run the model for n steps."""
        for _ in range(n):
            self.step()
