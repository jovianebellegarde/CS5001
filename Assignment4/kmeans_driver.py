'''
CS5001 Fall 2019
HW 3 Prog 3, K means
Joviane Bellegarde
10/14/19
Consulted with my HW 2 distance.py file for the euclidean function
Consulted https://pynative.com/python-random-sample/ for random.sample()
'''

from kmeans_viz import *
import random
import math

DATA = [[-32.97, -21.06], [9.01, -31.63], [-20.35, 28.73], [-0.18, 26.73],
        [-25.05, -9.56], [-0.13, 23.83], [19.88, -18.32], [17.49, -14.09],
        [17.85, 27.17], [-30.94, -8.85], [4.81, 42.22], [-4.59, 11.18],
        [9.96, -35.64], [24.72, -11.39], [14.44, -43.31], [-10.49, 33.55],
        [4.24, 31.54], [-27.12, -17.34], [25.24, -12.61], [20.26, -4.7],
        [-16.4, -19.22], [-15.31, -7.65], [-26.61, -20.31], [15.22, -30.33],
        [-29.3, -12.42], [-50.24, -21.18], [-32.67, -13.11], [-30.47, -17.6],
        [-23.25, -6.72], [23.08, -9.34], [-25.44, -6.09], [-37.91, -4.55],
        [0.14, 34.76], [7.93, 49.21], [-6.76, 12.14], [-19.13, -2.24],
        [12.65, -7.23], [11.25, 25.98], [-9.03, 22.77], [9.29, -26.2],
        [15.83, -1.45], [-22.98, -27.37], [-25.12, -23.35], [21.12, -26.68],
        [20.39, -24.66], [26.69, -28.45], [-45.42, -25.22], [-8.37, -21.09],
        [11.52, -16.15], [7.43, -32.89], [-31.94, -11.86], [14.48, -10.08],
        [0.63, -20.52], [9.86, 13.79], [-28.87, -17.15], [-29.67, -22.44],
        [-20.94, -22.59], [11.85, -9.23], [30.86, -21.06], [-3.8, 22.54],
        [-5.84, 21.71], [-7.01, 23.65], [22.5, -11.17], [-25.71, -14.13],
        [-32.62, -15.93], [-7.27, 12.77], [26.57, -13.77], [9.94, 26.95],
        [-22.45, -23.18], [-34.7, -5.62], [29.53, -22.88], [0.7, 31.02],
        [-22.52, -10.02], [-23.36, -14.54], [-19.44, -12.94], [-0.5, 23.36],
        [-45.27, -19.8], [8.95, 13.63], [47.16, -14.46], [5.57, 4.85],
        [-19.03, -25.41], [28.16, -13.86], [-15.42, -14.68], [10.19, -25.08],
        [0.44, 23.65], [-20.71, -20.94], [35.91, -20.07], [42.81, -21.88],
        [5.1, 9.33], [-15.8, -18.47], [5.39, -26.82], [-40.53, -17.16],
        [-29.54, 23.72], [7.8, 23.4], [-22.19, -27.76], [-23.48, -25.01],
        [-21.2, -21.74], [23.14, -24.14], [-28.13, -13.04], [-24.38, -6.79]]


def euclidean(x1, y1, x2, y2):
    '''
    function: euclidean(x1, y1, x2, y2) takes in 4 numbers to calculate distance
    parameters: 4 numbers, floats, 2 sets of coordinates
    returns: a float of the euclidean distance between 2 coordinates
    '''
    coordinate_1 = abs(x2 - x1)
    coordinate_2 = abs(y2 - y1)
    distance = math.sqrt(coordinate_1 ** 2 + coordinate_2 ** 2)
    return distance


def assignment(centroids_list):
    '''
    function: assignment(centroids_list)
    parameters: a list of lists, the DATA set
    returns: a list of lists, with the DATA set and the closest data point
    '''
    # Initializing an empty list, to put my list of lists for the centroids
    # and their closest data points
    data_centroid_list = []
    for i in range(len(DATA)):

        # This code is to find the pass the centroid, and the DATA point
        # through the euclidean equation and find smallest distance
        distances = []
        for j in range(len(centroids_list)):
            minimum = euclidean(DATA[i][0], DATA[i][1], centroids_list[j][0],
                                centroids_list[j][1])
            
            # This adds all of the distances to the distances list
            distances.append(minimum)

        # This code is using the min function to find the shortest distance
        # amongst the 4 centroids and the assigned DATA point
        smallest_distance = min(distances)
        min_index = distances.index(smallest_distance)

        # The index of the DATA point and its corresponding centroid is added
        # to the data centroid list
        data_centroid_list.append([i, min_index])

    return data_centroid_list



def main():

    # Assigning the 4 centroids from the DATA list
    centroids = random.sample(DATA, 4)

    # This passes the centroids through the data assignment function to be able
    # to draw the data assignments in turtle
    data_assignment = assignment(centroids)

    # Turn the centroids into a list to pass through the draw_centroids function
    centroid_list = list(centroids)
    
    # Assigning the 4 colors I want to use into a list fo colors
    # Calling the draw_centroids and draw_assignment functions here
    colors = ['green', 'red', 'purple', 'blue']
    draw_centroids(centroid_list, colors)
    draw_assignment(centroid_list, DATA, data_assignment, colors)

main()
