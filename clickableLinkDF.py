import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "Site": "DuckDuckGo Google Bing".split(),
        "URL": ["https://duckduckgo.com/","https://www.google.com/", "https://www.bing.com/"],
        "Traffic" : [np.random.rand(5) for _ in range(3)],
        "Random" : np.random.randint(0, 10, size=3)
    }
)

func = lambda s: f">> {s}"

stly = df.style.format({'URL': func, 'Site': func}).highlight_max(subset='Random')

# st.dataframe(stly)

# st.dataframe(df, column_config=
#              {"URL": st.column_config.LinkColumn("URL"),
#               "Traffic": st.column_config.LineChartColumn(width='small')})

st.dataframe(stly, column_config=
             {"URL": st.column_config.LinkColumn("URL"),
              "Traffic": st.column_config.LineChartColumn(width='small')})

# st.table(stly)

# if st.button("Run"):
#     with open("idthings.js") as f:
#         js = f'''
#         <script>
#         {f.read()} 
#         </script>
#         '''
#     st.components.v1.html(js)