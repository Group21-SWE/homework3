'''Module fills in a given array with random integers'''
import subprocess

def random_array(arr):
    ''' Fills in an array with random integers. '''
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
