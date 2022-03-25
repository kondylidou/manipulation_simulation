from mesa import Agent
import random


class PDAgent(Agent):
    """Agent member of the iterated, spatial prisoner's dilemma model."""

    def __init__(self, pos, initial_cooperation, manipulation, manipulators, defectors,
                 cooperators, manipulation_capacity, defection_award, model, starting_move=None):
        """
        Create a new Prisoner's Dilemma agent.

        Args:
            pos: (x, y) tuple of the agent's position.
            model: model instance
            starting_move: If provided, determines the agent's initial state:
                           C(ooperating) or D(efecting). Otherwise, random.
        """
        super().__init__(pos, model)
        self.manipulators = manipulators
        self.defectors = defectors
        self.cooperators = cooperators
        self.pos = pos
        self.score = 0
        self.manipulation = manipulation
        self.manipulation_capacity = manipulation_capacity
        self.defection_award = defection_award
        self.manipulator = "False"
        if starting_move:
            self.move = starting_move
        else:
            ranNumber = random.randint(1, 100)
            if ranNumber <= initial_cooperation:
                self.move = "C"
                self.cooperators.append(self)
            else:
                self.move = "D"
                self.defectors.append(self)
                ranNumber2 = random.randint(1, 100)
                if ranNumber2 <= manipulation:
                    self.manipulator = "True"
                    self.manipulators.append(self)
        self.next_move = None

    @property
    def is_cooperating(self):
        if self.move == "C":
            return True

    @property
    def is_defecting(self):
        if self.move == "D":
            return True

    @is_cooperating.setter  # is_cooperating or move
    def is_cooperating(self, value):  # value or move?
        self.move = value

    @property
    def is_manipulating(self):
        return self.manipulator

    @property
    def get_score(self):
        return self.score

    # checks his own score
    # compares his own score with the highest possible score after manipulation
    # decides for next move
    def manipulate(self, neighbors, best_neighbor):
        # check if all neighbors to manipulate can be manipulated
        # or the capacity is lower
        manipulate_all = False
        # next score reached without manipulation
        next_score = best_neighbor.get_score
        neighbors_to_manipulate = [neighbor for neighbor in neighbors
                                   if neighbor.is_defecting and neighbor.manipulator == "False"]

        if self.manipulation_capacity > len(neighbors_to_manipulate):
            # possible score reached after manipulation
            pos_score = self.defection_award * len(neighbors_to_manipulate)
            manipulate_all = True
        else:
            pos_score = self.defection_award * self.manipulation_capacity

        if pos_score > next_score:
            # possible score is greater so manipulate the neighbors
            # keep manipulating
            self.next_move = "D"
            if manipulate_all:
                for neighbor in neighbors_to_manipulate:
                    neighbor.move = "C"
            else:
                manipulated = random.choices(neighbors_to_manipulate, k=self.manipulation_capacity)
                for neighbor in manipulated:
                    neighbor.move = "C"
        else:
            self.next_move = best_neighbor.move

    def step(self):
        """Get the neighbors' moves, and change own move accordingly."""
        neighbors = self.model.grid.get_neighbors(self.pos, True, include_center=True)
        best_neighbor = max(neighbors, key=lambda a: a.score)
        if self.is_manipulating == "True":
            self.manipulate(neighbors, best_neighbor)
        else:
            self.next_move = best_neighbor.move
        if self.next_move == "C" and self.manipulator == "True":
            self.manipulator = "False"
            self.manipulators.remove(self)
            print("removed", len(self.manipulators))
            print("capacity", self.manipulation)
        if self.next_move == "D" and self.manipulator == "False" and best_neighbor.is_manipulating:
            print("here", len(self.manipulators))
            if len(self.manipulators) <= int((self.manipulation / 100) * len(self.defectors)):
                self.manipulator = "True"
                self.manipulators.append(self)
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
