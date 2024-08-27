Theoritically Time complexity for prediction in decision tree is O(log2(n)). Because based on input features, tree is traversed from root to leaf node during making prediction. The height of balanced binary tree is O(log2(n)).

The time taken in training the decision tree is O(nlog2(n)) + O(n) for one dimension. For m dimensional data, the time complexity of tree is [O(nlog2(n)) + O(n)]*m

O(nlog2(n)) is the time taken in sorting O(n) is the time taken in finding the best split