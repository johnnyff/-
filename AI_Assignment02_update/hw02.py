from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


## Example Agent
class ReflexAgent(Agent):

    def Action(self, gameState):
        move_candidate = gameState.getLegalActions()

        scores = [self.reflex_agent_evaluationFunc(gameState, action) for action in move_candidate]
        bestScore = max(scores)
        Index = [index for index in range(len(scores)) if scores[index] == bestScore]
        get_index = random.choice(Index)

        return move_candidate[get_index]

    def reflex_agent_evaluationFunc(self, currentGameState, action):
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        oldFood = currentGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        return successorGameState.getScore()


def scoreEvalFunc(currentGameState):
    return currentGameState.getScore()


class AdversialSearchAgent(Agent):

    def __init__(self, getFunc='scoreEvalFunc', depth='2'):
        self.index = 0
        self.evaluationFunction = util.lookup(getFunc, globals())

        self.depth = int(depth)


class MinimaxAgent(AdversialSearchAgent):

    """
    [문제 01] MiniMax의 Action을 구현하시오. (20점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """

    def Action(self, gameState):
        ####################### Write Your Code Here ################################
        move_candidate = gameState.getLegalActions()
        final_value = float('-inf')
        move = Directions.STOP

        for action in move_candidate:

            value = self.Min_value(gameState.generateSuccessor(0, action), 1, 0)
            if value > final_value:
                final_value = value
                move = action

        return move

    def Min_value(self, gameState, agent_index, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = float("inf")
        move_candidate = gameState.getLegalActions(agent_index)

        if agent_index == gameState.getNumAgents()-1:
            for action in move_candidate:
                successor = gameState.generateSuccessor(agent_index, action)
                value = min(value, self.Max_value(successor, depth + 1))
        else:
            for action in move_candidate:
                successor = gameState.generateSuccessor(agent_index, action)
                value = min(value, self.Min_value(successor, agent_index + 1, depth))

        return value

    def Max_value(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = float("-inf")
        move_candidate = gameState.getLegalActions()
        for action in move_candidate:
            successor = gameState.generateSuccessor(0, action)
            value = max(value, self.Min_value(successor, 1, depth))

        return value

        ############################################################################


class AlphaBetaAgent(AdversialSearchAgent):
    """
    [문제 02] AlphaBeta의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """

    def Action(self, gameState):
        ####################### Write Your Code Here ################################
        alpha = float("-inf")
        beta = float("inf")
        final_value = float("-inf")
        move = Directions.STOP
        for action in gameState.getLegalActions(0):
            value = self.alpha_beta_min_value(gameState.generateSuccessor(0,action), 0,1, alpha, beta)
            if value > final_value:
                final_value = value
                move = action
        return move

    def alpha_beta_max_value(self, gameState, depth, alpha, beta):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = float("-inf")
        move = Directions.STOP
        move_candidate = gameState.getLegalActions(0)
        for action in move_candidate:
            value2 = self.alpha_beta_min_value(gameState.generateSuccessor(0, action), depth, 1, alpha, beta)
            if value2 > value:
                value = value2
            if value > beta:
                return value
            alpha = max(alpha, value)
        return value

    def alpha_beta_min_value(self, gameState, depth, agent_index, alpha, beta):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = float("inf")
        move_candidate = gameState.getLegalActions(agent_index)

        if agent_index == gameState.getNumAgents() - 1:
            for action in move_candidate:
                value2 = self.alpha_beta_max_value(gameState.generateSuccessor(agent_index, action), depth+1, alpha, beta)
                if value2 < value:
                    value = value2

                if value < alpha:
                    return value
                beta = min(beta, value)
        else:
            for action in move_candidate:
                value2= self.alpha_beta_min_value(gameState.generateSuccessor(agent_index, action), depth,
                                                            agent_index+1, alpha, beta)
                if value2 < value:
                    value= value2
                if value < alpha:
                    return value

                beta = min(beta, value)
        return value
        ############################################################################


class ExpectimaxAgent(AdversialSearchAgent):
    """
    [문제 03] Expectimax의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """

    def Action(self, gameState):
        ####################### Write Your Code Here ################################
        move_candidate = gameState.getLegalActions()
        final_value = float('-inf')
        move = Directions.STOP

        for action in move_candidate:

            value = self.Exp_value(gameState.generateSuccessor(0, action), 1, 0)
            if value > final_value:
                final_value = value
                move = action

        return move

    def Exp_value(self, gameState, agent_index, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = 0
        move_candidate = gameState.getLegalActions(agent_index)

        if agent_index == gameState.getNumAgents() - 1:
            for action in move_candidate:
                successor = gameState.generateSuccessor(agent_index, action)
                suc_value = self.Max_value(successor, depth + 1)
                value += (suc_value/len(move_candidate))
        else:
            for action in move_candidate:
                successor = gameState.generateSuccessor(agent_index, action)
                suc_value = self.Exp_value(successor, agent_index + 1, depth)
                value += (suc_value / len(move_candidate))
        return value

    def Max_value(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = float("-inf")
        move_candidate = gameState.getLegalActions()
        for action in move_candidate:
            successor = gameState.generateSuccessor(0, action)
            value = max(value, self.Exp_value(successor, 1, depth))

        return value