
# 📊 Projeto Dash - Visualização de Dados com E-commerce

Este projeto é uma aplicação interativa criada com a biblioteca **Dash**, que visualiza informações do arquivo `ecommerce_estatistica.csv`.

A aplicação permite que o usuário explore:
- Mapa de calor de correlações entre variáveis numéricas
- Gráfico de área mostrando preço ao longo das avaliações
- Frequência de vendas por temporada
- Relação entre desconto e quantidade vendida

---

## 🚀 Como executar

### 1. Pré-requisitos
- Python 3 instalado no sistema
- Acesso à internet para instalar as bibliotecas (caso não estejam presentes)

### 2. Estrutura da pasta
```
📁 Projeto_Dash/
├── Projeto3.py
├── ecommerce_estatistica.csv
└── iniciar_dash.bat
```

### 3. Rodar o projeto

#### ✔️ Opção recomendada: Usar o arquivo `.bat`

Dê **duplo clique** em `iniciar_dash.bat`  
✅ Ele vai:
- Verificar/instalar automaticamente as bibliotecas (`dash`, `plotly`, `pandas`)
- Abrir o navegador com o Dash
- Executar o app no terminal
- Encerrar apenas quando você apertar uma tecla

#### ✔️ Opção manual (via terminal)

Caso prefira usar o terminal:

```bash
pip install dash pandas plotly
python Projeto3.py
```

Depois, abra o navegador em:  
👉 http://127.0.0.1:8050

---

## 📝 Tecnologias usadas

- Python 3
- Dash
- Plotly Express
- Pandas

---

## 📂 Autor

Desenvolvido por **João**  
Aluno do curso de Análise de Dados – EBAC
