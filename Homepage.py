import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import json
import requests
from streamlit_lottie import st_lottie

### Title and Subheader
st.set_page_config( 
    page_title="Internacionalidad",
    page_icon="👨‍✈️",
)


st.title("Internacionalidad Tec de Monterrey🌎✈")
#st.subheader("Jose Luis Quevedo-A01251583 👽")


#st.markdown('### Key Netrics')

kp1, kp2, kp3 = st.columns(3)
kp1.metric(label = "Cantidad de Estudiantes",
           value= 8031,
        )
kp2.metric(label = "Estudiantes en su Primera Opción",
           value= '99.66%',
           delta = 8004
)
kp3.metric(label = "Intercambio",
           value= '1.74%',
           delta = -140
)

### Data to work with

dv = pd.read_excel('DataCharts.xlsx')


fig1 = px.parallel_categories(dv, dimensions=['Escuela', 'Nivel','Prim','Intercambio'],
                color='Promedio', color_continuous_scale=px.colors.diverging.Tropic,
                labels={'Escuela':'Programa de Estudio','Nivel':'Nivel de Estudio','Prim': 'Primera Opción','Intercambio': 'Intercambio' })



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_5i5tlydx.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high 
    height=None,
    width=None,
    key=None,
)



st.header("Estado Actual ⬇")
chart1 = st.plotly_chart(fig1, use_container_width=True)


