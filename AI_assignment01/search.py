###### Write Your Library Here ###########
from collections import deque




#########################################


def search(maze, func):
    return {
        "bfs": bfs,
        "astar": astar,
        "astar_four_circles": astar_four_circles,
        "astar_many_circles": astar_many_circles
    }.get(func)(maze)


# -------------------- Stage 01: One circle - BFS Algorithm ------------------------ #

def bfs(maze):
    """
    [문제 01] 제시된 stage1의 맵 세가지를 BFS Algorithm을 통해 최단 경로를 return하시오.(20점)
    """
    start_point=maze.startPoint()

    path=[]

    ####################### Write Your Code Here ################################
    start_x, start_y = start_point
    queue = deque()
    queue.append(start_point)
    visited =[[0]*maze.cols for _ in range(maze.rows)]
    visited[start_x][start_y] = maze.getStatesSearch()+1
    while queue:
        x, y = queue.popleft()
        for new_x, new_y in maze.neighborPoints(x,y):
            if visited[new_x][new_y]==0:
                if maze.isObjective(new_x, new_y):
                    visited[new_x][new_y] = visited[x][y] + 1
                    length = visited[new_x][new_y]

                    cur_x= new_x
                    cur_y= new_y
                    path.append((cur_x, cur_y))
                    for j in range(1,length):
                        for temp_x, temp_y in maze.neighborPoints(cur_x,cur_y):
                            if(visited[temp_x][temp_y])==(length-j):
                                cur_x = temp_x
                                cur_y = temp_y
                                path.append((cur_x,cur_y))

                visited[new_x][new_y]= visited[x][y]+1
                queue.append((new_x,new_y))




    return path

    ############################################################################



class Node:
    def __init__(self,parent,location):
        self.parent=parent
        self.location=location #현재 노드

        self.obj=[]

        # F = G+H
        self.f=0
        self.g=0
        self.h=0

    def __eq__(self, other):
        return self.location==other.location and str(self.obj)==str(other.obj)

    def __le__(self, other):
        return self.g+self.h<=other.g+other.h

    def __lt__(self, other):
        return self.g+self.h<other.g+other.h

    def __gt__(self, other):
        return self.g+self.h>other.g+other.h

    def __ge__(self, other):
        return self.g+self.h>=other.g+other.h


# -------------------- Stage 01: One circle - A* Algorithm ------------------------ #

def manhatten_dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def astar(maze):

    """
    [문제 02] 제시된 stage1의 맵 세가지를 A* Algorithm을 통해 최단경로를 return하시오.(20점)
    (Heuristic Function은 위에서 정의한 manhatten_dist function을 사용할 것.)
    """

    start_point=maze.startPoint()

    end_point=maze.circlePoints()[0]

    path=[]

    ####################### Write Your Code Here ################################

    start_Node = Node(None, start_point)
    end_Node = Node(None, end_point)

    fringe_list = []
    closed_list = []

    fringe_list.append(start_Node)

    while fringe_list:
        cur_Node = fringe_list[0]
        cur_index= 0


        for index, node in enumerate(fringe_list):
            if node.__lt__(cur_Node):
                cur_Node = node
                cur_index = index
        fringe_list.pop(cur_index)
        closed_list.append(cur_Node)

        if cur_Node.__eq__(end_Node):
            cur = cur_Node
            while cur is not None:
                path.append(cur.location)
                cur = cur.parent
            return path[::-1]

        x, y =  cur_Node.location
        for child_x, child_y in maze.neighborPoints(x, y):
            new_Node = Node(cur_Node, (child_x,child_y))
            if new_Node in closed_list:
                continue

            new_Node.g = cur_Node.g+1
            new_Node.h = manhatten_dist(new_Node.location,end_Node.location)
            new_Node.f = new_Node.g+new_Node.h

            for check in fringe_list:
                if(new_Node.location == check.location and new_Node.g > check.g):
                    continue
            fringe_list.append(new_Node)


    return path

    ############################################################################


# -------------------- Stage 02: Four circles - A* Algorithm  ------------------------ #



def stage2_heuristic():
    pass


def astar_four_circles(maze):
    """
    [문제 03] 제시된 stage2의 맵 세가지를 A* Algorithm을 통해 최단 경로를 return하시오.(30점)
    (단 Heurstic Function은 위의 stage2_heuristic function을 직접 정의하여 사용해야 한다.)
    """

    end_points=maze.circlePoints()
    end_points.sort()

    path=[]

    ####################### Write Your Code Here ################################


















    return path

    ############################################################################



# -------------------- Stage 03: Many circles - A* Algorithm -------------------- #

def mst(objectives, edges):

    cost_sum=0
    ####################### Write Your Code Here ################################













    return cost_sum

    ############################################################################


def stage3_heuristic():
    pass


def astar_many_circles(maze):
    """
    [문제 04] 제시된 stage3의 맵 세가지를 A* Algorithm을 통해 최단 경로를 return하시오.(30점)
    (단 Heurstic Function은 위의 stage3_heuristic function을 직접 정의하여 사용해야 하고, minimum spanning tree
    알고리즘을 활용한 heuristic function이어야 한다.)
    """

    end_points= maze.circlePoints()
    end_points.sort()

    path=[]

    ####################### Write Your Code Here ################################





















    return path

    ############################################################################
