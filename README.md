# K-Means Algorithm

K-Means algorithm implemented from scratch using Python.

Expected parameters:

- items: A dictionary where each key is the item label and the value is another dictionary where each axis is contained in a label/value pair.
    (i.e. We want to cluster hats so item 'Baseball_Cap' has a dictionary where the attributes being evaluated are ('Color': 2, 'Size': 10, 'Style': 1))
- k: Number of centroids to be initialised.
- seed: Seed used to randomly pick the initial centroids. Default 0.
- maxIterations: Maximum iterations before forced exit of the algorithm, if this limit is reach it will return an empty array. Default 100.
  
Expected output

  - Returns a list where each sublist is the item labels clustered around the same centroid.
  - If the function doesn't converge within a set number of iteration (100 by default) the output will be an empty list.
