from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter


# Make a world that is 50x50, on a 500x500 display.
from pd_ext.model import PdGrid
from pd_ext.portrayal import portrayPDAgent

canvas_element = CanvasGrid(portrayPDAgent, 50, 50, 500, 500)
chart = ChartModule([{"Label": "Cooperating_Agents", "Color": "Black"}], data_collector_name='datacollector')

model_params = {
    "schedule_type": UserSettableParameter(
        "choice",
        "Scheduler type",
        value="Random",
        choices=list(PdGrid.schedule_types.keys()),
    ),
    "height": 50,
    "width": 50,
    "initial_cooperation": UserSettableParameter("slider", "Initial Cooperation", 50, 0, 100, 0.1),
    "initial_manipulation": UserSettableParameter("slider", "Initial Manipulation", 50, 0, 100, 0.1),
    "defection_award": UserSettableParameter("slider", "Defection Award", 1.6, 0, 3, 0.1),
    "manipulation_capacity": UserSettableParameter("slider", "Manipulation Capacity", 50, 0, 100, 0.1),
}

server = ModularServer(PdGrid, [canvas_element, chart], "Prisoner's Dilemma", model_params)