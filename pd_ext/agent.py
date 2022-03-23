from mesa import Agent
import random

class PDAgent(Agent):
    """Agent member of the iterated, spatial prisoner's dilemma model."""


    def __init__(self, pos, initial_cooperation, model, starting_move=None): #def __init__(self, pos, model, starting_move="C"):
        """
        Create a new Prisoner's Dilemma agent.

        Args:
            pos: (x, y) tuple of the agent's position.
            model: model instance
            starting_move: If provided, determines the agent's initial state:
                           C(ooperating) or D(efecting). Otherwise, random.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.score = 0
        if starting_move:
            self.move = starting_move
        else:
            ranNumber = random.randint(0, 100) 
            if ranNumber < initial_cooperation:
                self.move = "C"
            else:
                self.move = "D"
        self.next_move = None

    @property
    def isCooroperating(self):
        return self.move == "C"

    def step(self):
        """Get the neighbors' moves, and change own move accordingly."""
        neighbors = self.model.grid.get_neighbors(self.pos, True, include_center=True)
        best_neighbor = max(neighbors, key=lambda a: a.score)
        self.next_move = best_neighbor.move

        if self.model.schedule_type != "Simultaneous":
            self.advance()

    def advance(self):
        self.move = self.next_move
        self.score += self.increment_score()

    def increment_score(self):
        neighbors = self.model.grid.get_neighbors(self.pos, True)
        if self.model.schedule_type == "Simultaneous":
            moves = [neighbor.next_move for neighbor in neighbors]
        else:
            moves = [neighbor.move for neighbor in neighbors]
        return sum(self.model.update_payoff()[(self.move, move)] for move in moves)
