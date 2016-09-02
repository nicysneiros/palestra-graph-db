from py2neo import Graph
from igraph import Graph as IGraph
graph = Graph()

query = '''
MATCH (c1:Character)-[r:INTERACTS]->(c2:Character)
RETURN c1.name, c2.name, r.weight AS weight
'''

ig = IGraph.TupleList(graph.run(query), weights=True)
clusters = IGraph.community_walktrap(ig, weights="weight").as_clustering()