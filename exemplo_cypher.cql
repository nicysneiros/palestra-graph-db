MATCH (User {name: "João") -[:LIKES]-> (pages)
RETURN pages