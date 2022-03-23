from mesa import Agent
import random


class PDAgent(Agent):
    """Agent member of the iterated, spatial prisoner's dilemma model."""

    def __init__(self, pos, initial_cooperation, initial_manipulation, model, starting_move=None):
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
        self.manipulator = "False"
        if starting_move:
            self.move = starting_move
        else:
            ranNumber = random.randint(1, 100)
            if ranNumber <= initial_cooperation:
                self.move = "C"
            else:
                self.move = "D"
                ranNumber2 = random.randint(1, 100)
                if ranNumber2 <= initial_manipulation:
                    self.manipulator = "True"
        self.next_move = None

    @property
    def is_cooperating(self):
        return self.move == "C"

    @property
    def is_cooperating(self):
        if self.move == "C":
            return True

    @property
    def is_manipulating(self):
        return self.manipulator

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
        score = 0
        neighbors = self.model.grid.get_neighbors(self.pos, True)
        if self.model.schedule_type == "Simultaneous":
            moves = [neighbor.next_move for neighbor in neighbors]
        else:
            moves = [neighbor.move for neighbor in neighbors]
            # total number neighbors who cooperated
            # total_cooperators = [neighbor for neighbor in neighbors if neighbor.is_cooperating()]

            # if self.is_cooperating():
            # score = len(total_cooperators)
            # else:
            # score = self.model.defection_award * len(total_cooperators)
        return sum(self.model.update_payoff()[(self.move, move)] for move in moves)
