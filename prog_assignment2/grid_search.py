import numpy
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import os
import platform
import sys
import pickle

sys.path.append('../')
sys.path.append('./')
sys.path.append('./impl/')

import time


working_directory = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from dfs import DFS
from bfs import BFS
from astar import ASTAR

if platform.system() == 'Windows':
    import resources_windows as resources
else:
    import resources_unix as resources

workspace_dir = resources.workspace_dir
test_files_dir = os.path.join(workspace_dir, 'prog_assignment2', 'test_files')

delay = 0.0000001  # for visualization purposes,for the final plotting.
algos = [DFS, BFS, ASTAR]  # the algorithms to run
m_test_filename = 'no-obstacles.pkl'


# booleans
to_create_plots = True  # set to false to disable plotting
to_test_from_pickles = True  # Please find a way to visualize and inspect some saved runs to get an idea of what is needed
to_save_results = False  # Set this to true if you want to save all data to a pickle at the end of execution. Optional
to_plot_all_paths_taken = True  # Set this to false, if you want to plot only the shortest path takenn
to_time_delay = False  # set this to true to visualize the path taken


# A Heuristic for Astar
def euclidean(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


# A Heuristic for Astar
def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


# set the heuristic to use for Astar
heuristic = euclidean
# try different seeds to get a different map
np.random.seed(30)


# initialize the graphing elements
def init_graph(m_array, start, end, fig):
    x_axis = (-1, m_array.shape[0])
    y_axis = (-1, m_array.shape[1])
    ax = fig.gca()
    plt.grid()
    plt.scatter(start[0], start[1], c='b', s=200)
    plt.scatter(end[0], end[1], c='g', s=200)

    ax.set_xticks(numpy.arange(0, x_axis[1], 1))
    ax.set_yticks(numpy.arange(0, y_axis[1], 1))

    # plot road blocks
    for x in range(m_array.shape[0]):
        for y in range(m_array.shape[1]):
            if m_array[x, y] == 1:
                plt.scatter(x, y, c='r')
    return ax


def plot_search_paths(m_array, m_path, all_checked, start, end, ax, path_found, tried_color, found_color):
    # plt.clf()

    if to_plot_all_paths_taken:
        m_all_paths_x = [i[0] for i in all_checked]
        m_all_paths_y = [i[1] for i in all_checked]

        plt.plot([start[0], m_all_paths_x[1]], [start[1], m_all_paths_y[1]], color=tried_color)
        for i in range(0, len(m_all_paths_x) - 1, 1):
            # the if condition below is to avoid plotting 'jumps' in the all search paths list.
            # Ideally your list should have handled retracing
            if abs(m_all_paths_x[i] - m_all_paths_x[i + 1]) + abs(m_all_paths_y[i] - m_all_paths_y[i + 1]) <= 2:
                plt.plot(m_all_paths_x[i:i + 2], m_all_paths_y[i:i + 2], color=tried_color)
                if to_time_delay:
                    plt.pause(delay)
                plt.draw()

    # plot the final segment returned in a different color
    if path_found:
        m_path_x = [i[0] for i in reversed(m_path)]
        m_path_y = [i[1] for i in reversed(m_path)]
        plt.plot([start[0], m_path_x[0]], [start[1], m_path_y[0]], color=found_color)
        for i in range(0, len(m_path_x), 1):
            plt.plot(m_path_x[i:i + 2], m_path_y[i:i + 2], color=found_color)
            if to_time_delay:
                plt.pause(delay)


'''
Saves the results to a new .pkl file 
'''


def save_results(nmap, all_checked_s, this_paths, start, end, successes, algos, times):
    now = int(round(time.time() * 1000))
    filename = str(len(algos)) + '_' + str(now) + '.pkl'
    filepath = os.path.join(test_files_dir, filename)
    with open(filepath, 'wb') as f2:
        pickle.dump([nmap, all_checked_s, this_paths, start, end, successes, algos, times], f2)


def test_from_pickles(filename=m_test_filename):
    if filename is None:
        filepaths = os.listdir(test_files_dir)
        for file in filepaths:
            filepath = os.path.join(test_files_dir, file)
            if filepath.endswith('.pkl'):
                with open(filepath, 'rb') as f:
                    return (pickle.load(f))
    elif filename.endswith('.pkl'):
        filepath = os.path.join(test_files_dir, filename)
        with open(filepath, 'rb') as f:
            return (pickle.load(f))
    else:
        print('File path is invalid!')


def grid_search_test():
    # set algos to include or exclude searches
    global algos

    # set this boolean to true if you want to visualize or inspect how the code should run
    if to_test_from_pickles:

        nmap, all_checked_s, this_paths, start, end, successes, algos, times = test_from_pickles()
        m_rows = nmap.shape[0]
        m_cols = nmap.shape[1]

    else:
        # creating a random map
        m_rows = 25
        m_cols = 25
        p_obstacles = 0  # 0-1 float, the probablity of obstacles in the grid. Set this to lower to get 'easier' grids
        nmap = np.random.choice(2, p=(1.0 - p_obstacles, p_obstacles), size=(m_rows, m_cols))
        start = (np.random.randint(m_rows), np.random.randint(m_cols))
        end = (np.random.randint(m_rows), np.random.randint(m_cols))

        all_checked_s = [0] * len(algos)
        this_paths = [0] * len(algos)
        successes = [0] * len(algos)
        times = [0] * len(algos)
        # make sure that start and end points aren't blocked
        nmap[start[0], start[1]] = 0
        nmap[end[0], end[1]] = 0

        for i in range(len(algos)):
            successes[i], all_checked_s[i], this_paths[i], times[i] = algos[i](nmap, start, end, heuristic,
                                                                               diagnoal_allowed=True, peanlize_diagonals=False)

    # plotting
    if to_create_plots:
        fig = plt.figure()
        ax = init_graph(nmap, start, end, fig)
    light_color = [(0, .2, .6), (0, .6, 0), (.6, .3, .2)]
    main_color = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]

    for i in range(len(algos)):
        if successes[i] is True:
            if to_create_plots:
                plot_search_paths(nmap, this_paths[i], all_checked_s[i], start, end, ax, successes[i], light_color[i],
                                  main_color[i])
        else:
            print('No Path Exists!')
            if to_create_plots:
                plot_search_paths(nmap, [(0, 0)], all_checked_s[i], start, end, ax, successes[i], light_color[i],
                                  main_color[i])
        #print(this_paths[i])
        #print(all_checked_s[i])
        print(algos[i].__name__, times[i])

    if to_save_results:
        save_results(nmap, all_checked_s, this_paths, start, end, successes, algos, times)

    if to_create_plots:
        plt.show()


if __name__ == '__main__':
    grid_search_test()
