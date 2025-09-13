import plotly.express as px
import pandas as pd
import numpy as np

def generar_grafico():
    # Datos aleatorios
    n = 150
    num_grupos = 3
    np.random.seed(42)
    x = np.random.randn(n)
    y = np.random.randn(n)
    grupos = np.random.choice([f"Grupo {i+1}" for i in range(num_grupos)], size=n)

    df = pd.DataFrame({
        "x": x,
        "y": y,
        "Grupo": grupos
    })

    fig = px.scatter(
        df,
        x="x",
        y="y",
        color="Grupo",
        symbol="Grupo",
        title="Scatterplot Interactivo con Plotly",
        labels={"x": "Eje X", "y": "Eje Y"}
    )

    return fig.to_html(full_html=False)
