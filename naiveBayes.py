# dataset link : http://archive.ics.uci.edu/ml/datasets/Balloons

def processAssignedClasses (assignedClasses) :
    processedAssignedClasses = []
    for i in range(0, len(assignedClasses)) :
        assignedClass = assignedClasses[i]
        if (assignedClass[len(assignedClass) - 1] == '\n') :
            processedAssignedClasses.append(assignedClass[:len(assignedClass) - 1])
        else :
            processedAssignedClasses.append(assignedClass)
    return processedAssignedClasses

def loadDataset (filePath) :
    dataFile = open(filePath, 'r')
    tuples = []
    assignedClasses = []
    for line in dataFile :
        values = line.split(',')
        attributeValues = []
        for i in range(0, len(values)) :
            if (i == len(values) - 1) :
                assignedClasses.append(values[i])
            else :
                attributeValues.append(values[i])
        tuples.append(attributeValues)
    yield tuples
    assignedClasses = processAssignedClasses(assignedClasses)
    yield assignedClasses

def naiveBayesClassifier(tuples, assignedClasses, testTuple) :
    distinctClassesWithFrequencies = {}
    for i in range(0, len(assignedClasses)) :
        if (assignedClasses[i] not in distinctClassesWithFrequencies) :
            distinctClassesWithFrequencies[assignedClasses[i]] = 1
        else :
            distinctClassesWithFrequencies[assignedClasses[i]] += 1
    totalNumOfTuples = len(assignedClasses)
    classProbabilities = {}
    for classType in distinctClassesWithFrequencies :
        classProbabilities[classType] = float(distinctClassesWithFrequencies[classType]) / totalNumOfTuples
    classAssignmentScore = {}
    for classType in classProbabilities :
        classAssignmentScore[classType] = classProbabilities[classType]
    for i in range(0, len(testTuple)) :
        attributeValue = testTuple[i]
        classFrequenciesWithSameAttributeValue = {}
        for classType in classProbabilities :
            classFrequenciesWithSameAttributeValue[classType] = 1
        for j in range(0, len(tuples)) :
            if (tuples[j][i] == attributeValue) :
                classFrequenciesWithSameAttributeValue[assignedClasses[j]] += 1
        for classType in classProbabilities :
            classAssignmentScore[classType] *= (float(classFrequenciesWithSameAttributeValue[classType]) / (distinctClassesWithFrequencies[classType] + 1))
    yield classAssignmentScore
    assignedClass = None
    maxClassAssignmentScore = 0
    for classType in classAssignmentScore :
        if (classAssignmentScore[classType] > maxClassAssignmentScore) :
            maxClassAssignmentScore = classAssignmentScore[classType]
            assignedClass = classType
    yield assignedClass

def main () :
    filePath = 'adult-stretch.data'
    processedData = []
    for result in loadDataset(filePath) :
        processedData.append(result)
    tuples = processedData[0]
    assignedClasses = processedData[1]
    testTuple =  ['YELLOW', 'SMALL', 'STRETCH', 'ADULT']
    classificationResult = []
    for result in naiveBayesClassifier(tuples, assignedClasses, testTuple) :
        classificationResult.append(result)
    classAssignmentScore = classificationResult[0]
    assignedClass = classificationResult[1]
    print('Scores for being assigned to the different classes are : ')
    print(classAssignmentScore)
    print('Assigned class is : ', end = '')
    print(assignedClass)

main ()
