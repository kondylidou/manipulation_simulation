# Manipulation Simulation

This project is a computer simulation of a multi-agent extended prisoner’s dilemma using manipulation. The aim is to investigate if the outcome for all agents is better with or without the possibility of manipulation. 

## Classic Prisoner’s dilemma

One of the most prominently studied phenomena in Game Theory is the "Prisoner's Dilemma." The Prisoner's Dilemma, which was formulated by Melvin Drescher and Merrill Flood and named by Albert W. Tucker, is an example of a class of games called non-zero-sum games.

In zero-sum games, total benefit to all players add up to zero, or in other words, each player can only benefit at the expense of other players (e.g. chess, football, poker --- one person can only win when the opponent loses). On the other hand, in non-zero-games, each person's benefit does not necessarily come at the expense of someone else. In many non-zero-sum situations, a person can benefit only when others benefit as well. Non-zero-sum situations exist where the supply of a resource is not fixed or limited in any way (e.g. knowledge, artwork, and trade). Prisoner's Dilemma, as a non-zero-sum game, demonstrates a conflict between rational individual behavior and the benefits of cooperation in certain situations. The classical prisoner's dilemma is as follows:

Two suspects are apprehended by the police. The police do have enough evidence to convict these two suspects. As a result, they separate the two, visit each of them, and offer both the same deal: "If you confess, and your accomplice remains silent, he goes to jail for 10 years and you can go free. If you both remain silent, only minor charges can be brought upon both of you and you guys get 6 months each. If you both confess, then each of you two gets 5 years."

Each suspect may reason as follows: "Either my partner confesses or not. If he does confess and I remain silent, I get 10 years while if I confess, I get 5 years. So, if my partner confesses, it is best that I confess and get only 5 years than 10 years in prison. If he didn't, then by confessing, I go free, whereby remaining silent, I get 6 months. Thus, if he didn't confess, it is best to confess, so that I can go free. Whether or not my partner confesses or not, it is best that I confess."

In a non-iterated prisoner's dilemma, the two partners will never have to work together again. Both partners are thinking in the above manner and decide to confess. Consequently, they both receive 5 years in prison. If neither would have confessed, they would have only gotten 6 months each. The rational behavior paradoxically leads to a socially unbeneficial outcome.

Payoff Matrix

|                  | **Cooperate**  | **Defect**    |
| :---             |     :---:      |          ---: |
| **Cooperate**    | (0.5, 0.5)     | (10, 0)       |
| **Defect**       | (0, 10)        |  (5, 5)       |

## Classic Prisoner’s dilemma

