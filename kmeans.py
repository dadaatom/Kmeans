import math

def kmeans(items, k, seed = 0, maxIterations = 100):
    allKeys = items.keys()

    random.seed(seed)
    centroidKeys = random.sample(allKeys, k)

    centroids = []

    for key in centroidKeys:
        centroids.append(list(items[key].values()))

    iteration = 0

    while iteration < maxIterations:
        iteration += 1

        #Clear state groupings
        groupings = {}

        for x in range(0, k):
            groupings[x] = []

        #Fill state groupings based off centroids
        for key in allKeys:
            vector = list(mapped[key].values())

            bestIndex = -1
            bestDistance = math.inf  # init big num

            for index in range(0, k):
                centroid = centroids[index]
                if vector == centroid:
                    bestIndex = index
                    #bestDistance = distance
                    break

                distance = 0
                for i in range(0, len(centroid)):
                    difference = (vector[i] - centroid[i])
                    distance = distance + difference*difference

                if distance < bestDistance:
                    bestIndex = index
                    bestDistance = distance

            groupings[bestIndex].append(key)

        #Sort labels in groupings
        for x in groupings.keys():
            groupings[x] = sorted(groupings[x])

        previousCentroids = centroids.copy()

        centroids = {}

        #Find new centroids as an average of all centroids in that state grouping
        for index in range(0, k):
            count = len(groupings[index])

            mean = []

            if count > 0:
                for key in groupings[index]:
                    vector = list(mapped[key].values())

                    if len(mean) == 0:
                        mean = vector
                    else:
                        for i in range(0, len(vector)):
                            mean[i] = mean[i] + vector[i]

                for i in range(0, len(mean)):
                    mean[i] = mean[i] / count
            else:
                mean = previousCentroids[index]

            centroids[index] = mean

        #If new centroids are the same than exit
        if centroids == previousCentroids:
            return list(groupings.values())

    return []
