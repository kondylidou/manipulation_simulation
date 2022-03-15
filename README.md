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
| **Cooperate**    | (0.5, 0.5)     | (0, 10)       |
| **Defect**       | (10, 0)        |  (5, 5)       |

## Iterated Prisoner's Dilemma

In an Iterated Prisoner's Dilemma where you have more than two players and multiple rounds, such as this one, the scoring is different. In this model, it is assumed that an increase in the number of people who cooperate will increase proportionately the benefit for each cooperating player (which would be a fine assumption, for example, in the sharing of knowledge). For those who do not cooperate, assume that their benefit is some factor (alpha) multiplied by the number of people who cooperate (that is, to continue the previous example, the non-cooperating players take knowledge from others but do not share any knowledge themselves). How much cooperation is incited is dependent on the factor multiple for not cooperating. Consequently, in an iterated prisoner's dilemma with multiple players, the dynamics of the evolution in cooperation may be observed.

Payoff Matrix

|                  | **Cooperate**  | **Defect**    |
| :---             |     :---:      |          ---: |
| **Cooperate**    | (1, 1)         | (0, alpha)    |
| **Defect**       | (alpha, 0)     |  (0, 0)       |

## Iterated Prisoner's Dilemma with Manipulation (Extended prisoner’s Dilemma)

In the iterated prisoner’s dilemma we will add one more factor, manipulation. As in Machiavelli's game theory the world is separated in manipulators and manipulated players. Some criminals are now able to manipulate the rest to cooperate or defect. So two more parameters will be added, the initial percentage of manipulators and the manipulative capacity of each individual.

## How it works

Decide what percentage of patches should cooperate at the initial stage of the simulation and change the INITIAL-COOPERATION and the INITIAL-MANIPULATION sliders to match what you would like. Next, determine the DEFECTION-AWARD multiple (mentioned as alpha in the payoff matrix above) for defecting or not cooperating. The Defection-Award multiple varies from range of 0 to 3. Furthermore, determine the MANIPULATION-CAPACITY multiple for manipulation other individuals. The Manipulation-Capacity multiple varies from range of 0 to 3.  Note that red patches will defect and blue patches will cooperate. Press START to make the patches interact with their eight neighboring patches. First, they count the number of neighboring patches that are cooperating. If a patch is cooperating, then its score is number of neighboring patches that also cooperated. If a patch is defecting, then its score is the product of the number of neighboring patches who are cooperating and the Defection-Award multiple. 

what happens if a patch is manipulating ?

HOW IT WORKS

Each patch will either cooperate (blue) or defect (red) in the initial start of the model. At each cycle, each patch will interact with all of its 8 neighbors to determine the score for the interaction. Should a patch have cooperated, its score will be the number of neighbors that also cooperated. Should a patch defect, then the score for this patch will be the product of the Defection-Award multiple and the number of neighbors that cooperated (i.e. the patch has taken advantage of the patches that cooperated).

what happens if a patch is manipulating ?

