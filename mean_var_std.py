import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(list).reshape(3,3)
        mean_axis_0 = np.mean(arr,axis=0).tolist()
        mean_axis_1 = np.mean(arr,axis=1).tolist()
        mean = np.mean(arr)
        variance_axis_0 = np.var(arr,axis=0).tolist()
        variance_axis_1 = np.var(arr,axis=1).tolist()
        variance = np.var(arr).tolist()
        std_axis_0 = np.std(arr,axis=0).tolist()
        std_axis_1 = np.std(arr,axis=1).tolist()
        std = np.std(arr).tolist()
        max_axis_0 = np.max(arr,axis=0).tolist()
        max_axis_1 = np.max(arr,axis=1).tolist()
        max = np.max(arr).tolist()
        min_axis_0 = np.min(arr,axis=0).tolist()
        min_axis_1 = np.min(arr,axis=1).tolist()
        min = np.min(arr).tolist()
        sum_axis_0 = np.sum(arr,axis=0).tolist()
        sum_axis_1 = np.sum(arr,axis=1).tolist()
        sum = np.sum(arr).tolist()
        results = {
        'mean': [mean_axis_0,mean_axis_1,mean],
        'variance': [variance_axis_0,variance_axis_1,variance],
        'standard deviation': [std_axis_0,std_axis_1,std],
        'max': [max_axis_0,max_axis_1,max],
        'min': [min_axis_0,min_axis_1,min],
        'sum': [sum_axis_0,sum_axis_1,sum]
        }
        return results
    
        