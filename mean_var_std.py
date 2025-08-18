import numpy as np

def calculate(list):
    if len(list) !=9 :
        raise ValueError("List must contain nine numbers.")

    array = np.array(list).reshape(3, 3)

    calculations = {}

    meanAxis1 = np.mean(array, axis=0).tolist()
    meanAxis2 = np.mean(array, axis=1).tolist()
    meanFlattened = np.mean(array).tolist()
    calculations['mean'] = [meanAxis1, meanAxis2, meanFlattened]

    varianceAxis1 = np.var(array, axis=0).tolist()
    varianceAxis2 = np.var(array, axis=1).tolist()
    varianceFlattened = np.var(array).tolist()
    calculations['variance'] = [varianceAxis1, varianceAxis2, varianceFlattened]

    stdAxis1 = np.std(array, axis=0).tolist()
    stdAxis2 = np.std(array, axis=1).tolist()
    stdFlattened = np.std(array).tolist()   
    calculations['standard deviation'] = [stdAxis1, stdAxis2, stdFlattened]

    maxAxis1 = np.max(array, axis=0).tolist()
    maxAxis2 = np.max(array, axis=1).tolist()
    maxFlattened = np.max(array).tolist()
    calculations['max'] = [maxAxis1, maxAxis2, maxFlattened]
    
    minAxis1 = np.min(array, axis=0).tolist()
    minAxis2 = np.min(array, axis=1).tolist()
    minFlattened = np.min(array).tolist()
    calculations['min'] = [minAxis1, minAxis2, minFlattened]

    sumAxis1 = np.sum(array, axis=0).tolist()
    sumAxis2 = np.sum(array, axis=1).tolist()
    sumFlattened = np.sum(array).tolist()
    calculations['sum'] = [sumAxis1, sumAxis2, sumFlattened]

    return calculations