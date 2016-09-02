MATCH (joao:User {name:"João"})-[l:LIKES]->(pages:Page)
RETURN joao, l, pages

