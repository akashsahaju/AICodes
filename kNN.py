def processAssignedClassValues(assignedClassValues) :
    processedAssignedClassValues = []
    for i in range(0, len(assignedClassValues)) :
        if (assignedClassValues[i][len(assignedClassValues[i]) - 1] == '\n') :
            processedAssignedClassValues.append(assignedClassValues[i][:len(assignedClassValues[i]) - 1])
        else :
            processedAssignedClassValues.append(assignedClassValues[i])
    return processedAssignedClassValues

def loadDataset (filePath) :
    dataset = open(filePath, 'r')
    tupleValues = []
    assignedClassValues = []
    for line in dataset :
        values = line.split(',')
        numOfAttributes = len(values) - 1
        attributeValues = []
        for j in range(0, len(values)) :
            if (j == numOfAttributes) :
                assignedClassValues.append(values[j])
            else :
                attributeValues.append(float(values[j]))
        tupleValues.append(attributeValues)
    yield tupleValues
    assignedClassValues =  processAssignedClassValues(assignedClassValues)
    yield assignedClassValues

def getEuclideanDistance (vector1, vector2) :
    distance = 0
    for i in range(0, len(vector1)) :
        distance += (vector1[i] -  vector2[i]) ** 2
    return distance ** 0.5

def kNN (testTuple, tupleValues, assignedClassValues, numOfNeighbours) :
    try :
        import Queue as Q
    except ImportError :
        import queue as Q
    q = Q.PriorityQueue()
    for i in range(0, len(tupleValues)) :
        q.put((getEuclideanDistance(testTuple, tupleValues[i]), i))
    classFrequencies = {}
    count = 0
    while count != numOfNeighbours and not q.empty() :
        count += 1
        classValue = assignedClassValues[(q.get())[1]]
        if classValue not in classFrequencies :
            classFrequencies[classValue] = 1
        else :
            classFrequencies[classValue] += 1
    assignedClass = None
    highestClassFrequency = 0
    for classValue in classFrequencies :
        if classFrequencies[classValue] > highestClassFrequency :
            highestClassFrequency = classFrequencies[classValue]
            assignedClass = classValue
    return assignedClass

def main () :
    filePath = 'iris.data'
    parsedDataset = []
    for result in loadDataset(filePath) :
        parsedDataset.append(result)
    tupleValues = parsedDataset[0]
    assignedClassValues = parsedDataset[1]
    numOfNeighbours = 5
    testTuple = [5.0, 3.0, 1.0, 1.0]
    assignedClass = kNN(testTuple, tupleValues, assignedClassValues, numOfNeighbours)
    print('The assigned class is : ', end = '')
    print(assignedClass)

main()
