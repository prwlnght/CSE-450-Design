
import time

def DFS(m_map, start, goal, heuristic, diagnoal_allowed=False, peanlize_diagonals=False):
    start_time = time.time()
    # set this to the coordinates of the neighbors you want to check eg. (0, 1) to go one right, (0, -1) to go one right etc.
    # put code to handle checking only non-diagonal neighbors according to diagonal_allowed? parameter
    neighbors = []
    all_checked = [] #this is a list of coordinates to plot the entire search path.
    path = [] #this is the shortest path

    '''
    Enter your code here 




    '''

    end_time = time.time()
    return False, all_checked, path, end_time-start_time