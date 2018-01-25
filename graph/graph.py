# If key not in d,  d[key] is created to avoid KeyError
from collections import defaultdict

class Graph():
    def __init__(self, directed=True):
        self.graph = defaultdict(set)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].add(v)
        if not self.directed:
            self.graph[v].add(u)

    def getEdges(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges

    def findPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        for node in self.graph[start]:
            if node not in path:
                newPath = self.findPath(node, end, path)
                if newPath:
                    return newPath
                return None

    def findAllPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        paths = []
        for node in self.graph[start]:
            if node not in path:
                newPaths = self.findAllPaths(node, end, path)
                for newPath in newPaths:
                    paths.append(newPath)
        return paths

    def findShortestPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newPaths = self.findAllPaths(node, end, path)
                for newPath in newPaths:
                    if not shortest or len(newPath) < len(shortest):
                        shortest = newPath
        return shortest


if __name__ == "__main__":
    myGraph = Graph()
    myGraph.addEdge('a', 'c')
    myGraph.addEdge('b', 'c')
    myGraph.addEdge('b', 'e')
    myGraph.addEdge('c', 'd')
    myGraph.addEdge('c', 'e')
    myGraph.addEdge('e', 'b')
    myGraph.addEdge('e', 'c')

    print(myGraph.getEdges())
    print(myGraph.graph)

    print(myGraph.findPath('a', 'e'))
    print(myGraph.findAllPaths('a', 'e'))
    print(myGraph.findShortestPath('a', 'e'))
