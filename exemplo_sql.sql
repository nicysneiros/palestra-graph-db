SELECT u.nome, u.genero, u.idade 
   FROM Usuario u, Curte c, Pagina p 
   WHERE p.nome = "The Beatles"
      AND p.ID = c.ID_Pagina 
      AND c.ID_Usuario = u.ID