import leafmap


m = leafmap.Map(center=(22.439, 120.538), zoom=14, height="600px") 
m.split_map(
    left_layer="HYBRID", right_layer="ESA WorldCover 2020"
)
m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
