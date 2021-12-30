import numpy as np

def pareto_frontier_multi(myArray):
    # Sort on first dimension
    myArray = myArray[myArray[:,0].argsort()]
    # Add first row to pareto_frontier
    pareto_frontier = myArray[0:1,:]
    # Test next row against the last row in pareto_frontier
    for row in myArray[1:,:]:
        if sum([row[x] >= pareto_frontier[-1][x]
                for x in range(len(row))]) == len(row):
            # If it is better on all features add the row to pareto_frontier
            pareto_frontier = np.concatenate((pareto_frontier, [row]))
    return pareto_frontier
"""
    myArray = np.array([[0.28,0.36,0.3],
                        [0.04,0.07,0.65],
                        [0.73,0.8,0.59],
                        [0.32,0.81,0.6],
                        [0.63,0.71,0.34],
                        [0.07,0.1,0.31],
                        [0.41,0.49,0.57],
                        [0.17,0.27,0.59]])
"""
def test():
    myArray = np.array([[0.28,0.36,0.3],
                        [0.73,0.8,0.59],
                        [0.63,0.71,0.34],
                        [0.41,0.49,0.57]])
    print(pareto_frontier_multi(myArray))

test()