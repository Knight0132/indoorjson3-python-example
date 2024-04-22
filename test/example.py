"""
File Name: test.py

Copyright (c) 2023 - 2024 IndoorJson

Author: Ziwei Xiang <knightzz1016@gmail.com>
Create Date: 2024/4/19
"""

from indoorjson3 import deserialization, graph_visualize, hypergraph_visualize
import os

if __name__ == "__main__":

    filename = "test/example.json"
    indoor_space = deserialization(filename)
    graph_visualize(indoor_space, "result/graph.html")
    hypergraph_visualize(indoor_space, "result/hypergraph.html")
