@echo off
cd /d "%~dp0"

echo Verificando dependências do projeto...

REM Verifica se pip está disponível
python -m pip --version >nul 2>&1 || (
    echo Python ou pip não estão instalados corretamente.
    pause
    exit /b
)

REM Instala bibliotecas se necessário
python -c "import dash" 2>nul || (
    echo Instalando Dash...
    pip install dash
)

python -c "import plotly" 2>nul || (
    echo Instalando Plotly...
    pip install plotly
)

python -c "import pandas" 2>nul || (
    echo Instalando Pandas...
    pip install pandas
)

echo.
echo Iniciando o aplicativo Dash...

REM Abrir o navegador automaticamente no link do Dash
start http://127.0.0.1:8050

REM Rodar o app em segundo plano e esperar finalização
python Projeto3.py

echo.
echo Pressione qualquer tecla para encerrar o terminal...
pause >nul