#%%
import plotly.graph_objects as go

fig = go.Figure(
    data = [go.Sankey(node = dict(pad = 15,
                                  thickness = 20,
                                  line = dict(color = "black",width = 0.5),
                                  label = [" A1 ","A2"," B1","B2","C1","C2" ],
                                  color = "blue"),
                      link = dict(source = [0,1,0,2,3,3 ], # os índices correspondem aos rótulos, por exemplo, A1, A2, A1, B1, ...
                                  target = [2,3,3,4,4,5 ],
                                  value = [8,4,2,8,4,2 ]
                                  )
                      )
            ]
)
# %%
