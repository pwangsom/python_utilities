import numpy as np

class A3Normalizer:

    def __init__(self):
        self.workflow_lines = []
        return

    def normalize(self):

        objective_list = [[cols[6], cols[7], cols[8]] for cols in self.workflow_lines]
        objective_array = np.asarray(objective_list)

        _max = np.max(objective_array, axis=0)
        _min = np.min(objective_array, axis=0)

        for _solution in self.workflow_lines:
            _solution[9] = (_solution[6]-_min[0])/(_max[0]-_min[0])
            _solution[10] = (_solution[7]-_min[1])/(_max[1]-_min[1])
            _solution[11] = (_solution[8]-_min[2])/(_max[2]-_min[2])

        return self.workflow_lines