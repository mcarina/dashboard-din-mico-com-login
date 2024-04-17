import plotly.express as px
import plotly.io as pio

def dashboard_plot(user_coordenadoria):
    # Dados de exemplo
    dados = {
        "Categorias": ["A", "B", "C"],
        "Valores": [10, 15, 7]
    }
    # Criar um gráfico de barras com Plotly
    fig = px.bar(dados, x='Categorias', y='Valores', title=f"Gráfico de Barras, {user_coordenadoria}")
    # Converter o gráfico para HTML
    graph_html = pio.to_html(fig, full_html=False)
    return graph_html