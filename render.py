import pandas as pd
from graphviz import Graph

df = pd.read_csv("network.csv")

LINE_COLOURS = {
    "VIC": "red",
    "CIN": "blue",
    "CNW": "orange",
    "NUR": "green",
    "RIV": "purple"
}

g = Graph("ComblexNetwork", format="svg")

g.attr(
    bgcolor="white",
    overlap="false",
    splines="true",
    fontname="Arial"
)

nodes = set()

for _, row in df.iterrows():
    a = row["From"]
    b = row["To"]
    line = row["Line"]

    colour = LINE_COLOURS.get(line, "black")

    if a not in nodes:
        g.node(a, shape="circle", style="filled", fillcolor="lightgrey")
        nodes.add(a)

    if b not in nodes:
        g.node(b, shape="circle", style="filled", fillcolor="lightgrey")
        nodes.add(b)

    g.edge(a, b, color=colour, penwidth="3")

g.render("output/comblex_network", cleanup=True)
print("SVG generated")
