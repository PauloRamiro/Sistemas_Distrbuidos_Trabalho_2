# Aplicação para Visualização de Ações

Aplicação desenvolvida para a disciplina de Sistemas Distribuídos.

## Descrição

Utilizando Streamlit, yfinance, pandas e plotly esta aplicação possui como objetivo permitir que usuários acessem informações do Yahoo Finance em forma de tabela e gráfico.
A aplicação está disponível de forma online pelo link: http://abre.ai/prsd2

## Iniciando

### Dependências

As depenências do programa estão listadas no arquivo `requirements.txt` para instalação utilizando o pip. Entre as dependências estão:
* streamlit;
* Cython;
* numpy;
* pandas;
* matplotlib;
* convertdate;
* pystan;
* yfinance;
* streamlit;
* plotly;
* ephem;
* sklearn.

### Instalação

A aplicação não precisa de instalação, somente suas dependências.

### Execução

A execução da aplicação varia de acordo com o método de instalação da biblioteca streamlit, consulte a documentação do seu ambiente virtual. Algumas opções de comandos são:
* pipenv e conda
```
streamlit run main.py
```

* Windows sem conda
```
python -m streamlit run main.py
```

Outra sequência de comandos pode ser necessária de acordo com sua instalação, em todos os casos caso a execução seja bem sucedida irá ser exibido um link local e na rede para a visualização da aplicação.
