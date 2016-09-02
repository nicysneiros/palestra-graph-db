#!/usr/bin/python
# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship

g = Graph(password="admin")

tx = g.begin()

# USERS
joao = Node("User", name="João", gender="M", age="28")
tx.create(joao)

maria = Node("User", name="Maria", gender="F", age="26")
tx.create(maria)

francis = Node("User", name="Francis", gender="F", age="31")
tx.create(francis)

#FRIENDS WITH
joao_maria = Relationship(joao, "FRIENDS_WITH", maria)
tx.create(joao_maria)

maria_francis = Relationship(maria, "FRIENDS_WITH", francis)
tx.create(maria_francis)

#PAGES
coca = Node("Page", name="Coca-Cola", category="Comida/Bebida")
tx.create(coca)

beatles = Node("Page", name="The Beatles", category="Músico/Banda")
tx.create(beatles)

apple = Node("Page", name="Apple", category="Tecnologia")
tx.create(apple)

#LIKES
joao_coca = Relationship(joao, "LIKES", coca)
tx.create(joao_coca)

joao_beatles = Relationship(joao, "LIKES", beatles)
tx.create(joao_beatles)

maria_apple = Relationship(maria, "LIKES", apple)
tx.create(maria_apple)

francis_beatles = Relationship(francis, "LIKES", beatles)
tx.create(francis_beatles)

tx.commit()
