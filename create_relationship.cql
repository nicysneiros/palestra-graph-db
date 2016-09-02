
MATCH (joao:User), (maria:User)
WHERE joao.name='João' AND maria.name='Maria'
CREATE (joao)-[f:FRIENDS_WITH]->(maria)
RETURN joao, f, maria

