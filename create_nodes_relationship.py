#!/usr/bin/python
# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship

g = Graph(password="admin")

tx = g.begin()
joao = Node("User", name="João", gender="M", age="28")
tx.create(joao)

maria = Node("User", name="Maria", gender="F", age="26")
tx.create(maria)

jm = Relationship(joao, "FRIENDS_WITH", maria)
tx.create(jm)

tx.commit()

print g