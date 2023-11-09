def minimumSpanningTreeTotalWeight(adjM):
    numVertices = len(adjM)
    selected = [0] * numVertices
    no_edge = 0
    selected[0] = True
    
    total_weight = 0
    
    while no_edge < numVertices - 1:
        minimum = float("Inf")
        x = 0
        y = 0
        for i in range(numVertices):
            if selected[i]:
                for j in range(numVertices):
                    if ((not selected[j]) and adjM[i][j]):
                        if minimum > adjM[i][j]:
                            minimum = adjM[i][j]
                            x = i
                            y = j
        total_weight += adjM[x][y]
        selected[y] = True
        no_edge += 1
    
    return total_weight

def test_minimumSpanningTreeTotalWeight():
    # Example adjacency matrix
    adjM = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    
    # Expected MST weight might be 16 (for the above example)
    expected_weight = 16
    
    # Check if the function returns the expected weight
    print( minimumSpanningTreeTotalWeight(adjM) == expected_weight)

# Run the test
test_minimumSpanningTreeTotalWeight()
