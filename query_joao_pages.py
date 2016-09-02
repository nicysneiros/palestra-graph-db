#!/usr/bin/python
# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeSelector

g = Graph(password="admin")
selector = NodeSelector(g)
joao = selector.select("User", name="João").first()

joao_likes = g.match(start_node=joao, rel_type="LIKES")


for like in joao_likes:
	page = like.end_node()
	print(page)

