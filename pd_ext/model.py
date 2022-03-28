from mesa import Model
from mesa.time import BaseScheduler, RandomActivation, SimultaneousActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from pd_ext.agent import PDAgent
import time


class PdGrid(Model):
    """Model class for iterated, spatial prisoner's dilemma model."""

    schedule_types = {
        "Sequential": BaseScheduler,
        "Random": RandomActivation,
        "Simultaneous": SimultaneousActivation,
    }

    defection_award = 1.5

    def __init__(
            self, width=50, height=50, initial_cooperation=50, manipulation=50, manipulators=None,
            defection_award=1.5, manipulation_capacity=50, schedule_type="Random", payoffs=None, seed=None
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
        self.manipulation = manipulation
        self.manipulators = []
        self.defectors = []
        self.cooperators = []
        self.defection_award = defection_award
        self.manipulation_capacity = manipulation_capacity
        self.grid = SingleGrid(width, height, torus=True)
        self.schedule_type = schedule_type
        self.schedule = self.schedule_types[self.schedule_type](self)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.file_link = 'CSV/' + timestr + '.csv'
        print(self.file_link)

        # Create agents
        for x in range(width):
            for y in range(height):
                agent = PDAgent((x, y), initial_cooperation, manipulation, self.manipulators,
                                self.defectors, self.cooperators, manipulation_capacity, defection_award, self)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.datacollector = DataCollector(
            {
                "Cooperating_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "C"]
                ),
                "Defecting_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "D"]
                ),
                "Manipulating_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.is_manipulating == "True"]
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
        export_array = self.datacollector.get_model_vars_dataframe()
        export_array.to_csv(self.file_link)

    def run(self, n):
        """Run the model for n steps."""
        for _ in range(n):
            self.step()
