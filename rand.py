'''
Method for creating a random array
'''

import subprocess

def random_array(arr):
    '''
    This take an array and randomizes it with integers
    
    Parameters
    -----
    arr - array to be randomizzed
    
    Returns
    -----
    randomized array
    '''
    shuffled_num = None
    i = 0
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
