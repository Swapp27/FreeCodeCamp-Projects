import numpy as np

def cal(list):
    if len(list)<9 :
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        b = a.reshape(3,3)
        mean = [np.mean(b, axis = 0).tolist(), np.mean(b,axis = 1).tolist(), np.mean(a).tolist()]
        variance = [np.var(b,axis = 0).tolist(),np.var(b,axis=1).tolist(),np.var(a).tolist()]
        stdev = [np.std(b,axis=0).tolist(),np.std(b,axis=1).tolist(),np.std(a).tolist()]
        m1 = [np.max(b,axis=0).tolist(),np.max(b,axis=1).tolist(),np.max(a).tolist()]
        m2 = [np.min(b,axis=0).tolist(),np.min(b,axis=1).tolist(),np.min(a).tolist()]
        s = [np.sum(b,axis=0).tolist(),np.sum(b,axis=1).tolist(),np.sum(a).tolist()]

        result = {"mean" : mean, "variance":variance,"standard deviation":stdev,"max":m1,"min":m2,"sum":s}
    return result