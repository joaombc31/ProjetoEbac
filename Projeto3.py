import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# === Carregar o dataset ===
df = pd.read_csv('ecommerce_estatistica.csv')

# === Gráfico 1: Mapa de Calor de Correlação ===
colunas_corr = ['Nota', 'N_Avaliações', 'Desconto', 'Preço']
df_corr = df[colunas_corr].corr()

fig_corr = px.imshow(df_corr,
                     text_auto=True,
                     color_continuous_scale='viridis',
                     title="Correlação entre Nota, Avaliações, Desconto e Preço")

# === Gráfico 2: Área - Preço vs. N_Avaliações por Temporada ===
df_sorted = df.sort_values("N_Avaliações")
fig_area = px.area(df_sorted,
                   x="N_Avaliações",
                   y="Preço",
                   color="Temporada",
                   title="Preço vs Número de Avaliações por Temporada")

# === Gráfico 3: Histograma da Temporada ===
fig_hist = px.histogram(df,
                        x='Temporada',
                        color_discrete_sequence=['green'],
                        title='Frequência de Vendas por Temporada')

# === Gráfico 4: Dispersão - Desconto vs Qtd_Vendidos_Cod ===
fig_disp = px.scatter(df,
                      x='Desconto',
                      y='Qtd_Vendidos_Cod',
                      title='Dispersão: Desconto x Quantidade Vendida')

# === Criar App Dash ===
app = Dash(__name__)
app.title = "Dashboard Ecommerce"

app.layout = html.Div([
    html.H1("📊 Dashboard - Ecommerce Estatística", style={'textAlign': 'center'}),

    html.H2("Mapa de Calor de Correlação"),
    dcc.Graph(figure=fig_corr),

    html.H2("Preço vs Avaliações por Temporada"),
    dcc.Graph(figure=fig_area),

    html.H2("Frequência de Vendas por Temporada"),
    dcc.Graph(figure=fig_hist),

    html.H2("Dispersão: Desconto x Quantidade Vendida"),
    dcc.Graph(figure=fig_disp),
])

# === Rodar servidor ===
if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=True)