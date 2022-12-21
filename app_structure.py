from plotly import graph_objs as go
import streamlit as st
import webbrowser
import data_pre_processing

sidebar_data_list = []


class Header:
    @staticmethod
    def print_it():
        st.title("Análise das ações")


class Sidebar:
    @staticmethod
    def print_it():
        global sidebar_data_list
        ticker_name_select = Sidebar.select_ticker()
        selected_period = Sidebar.select_period()
        #selected_real_comp = Sidebar.prediction_x_reality()

        sidebar_data_list = [ticker_name_select, selected_period]#, selected_real_comp]

    @staticmethod
    def select_ticker():
        df_tickers = (data_pre_processing.DataTicker.collecting_data_name_in_csv())["ticker_company"]

        st.sidebar.header("Área de Ações")
        st.sidebar.write("Nessa seção você irá selecionar a ação a ser analisada,"
                         + " veja/digite a ação, logo abaixo:")
        ticker_name_select = st.sidebar.selectbox("Escolha uma ação:", df_tickers)
        ticker_name_select = (ticker_name_select.split('-')[0] + ".SA")  # select ticker code
        return ticker_name_select

    @staticmethod
    def select_period():
        periods = ["1 minuto", "2 minutos", "5 minutos", "15 minutos", "30 minutos"]
        periods += ["1 hora", "1 dia", "5 dias", "1 semana"]

        st.sidebar.header("Área de Intervalos")
        st.sidebar.write("Nessa seção você irá selecionar o intervalo a ser analisado,"
                         + " veja os intervalos abaixo:")
        selected_period = st.sidebar.selectbox("Escolha um intervalo:", periods)
        return selected_period


class Body:

    @staticmethod
    def print_it():
        ticker_name_select = sidebar_data_list[0]  # Collected global variable data, extracted from the Sidebar class
        selected_period = sidebar_data_list[1]  # Collected global variable data, extracted from the Sidebar class
        #selected_real_comp = sidebar_data_list[2]  # Collected global variable data, extracted from the Sidebar class

        df_ticker = data_pre_processing.DataTicker.collecting_data_in_yfinance(ticker_name_select, selected_period)

        Body.show_data_graph(selected_period, ticker_name_select, df_ticker)
        #Body.show_data_prediction(selected_real_comp, df_ticker)

    @staticmethod
    def show_data_graph(selected_period, ticker_name_select, df_ticker):
        st.subheader("Tabelas de valores  -  " + ticker_name_select[:-3])
        st.write(df_ticker)
        st.download_button(
            "Baixar tabela como CSV",
            df_ticker.to_csv(index=False).encode('utf-8'),
            f"{ticker_name_select[:-3]} - {selected_period}.csv",
            "text/csv",
            key='download-csv'
            )

        st.subheader("Gráfico CandleStick sem ajuste de valores:")
        st.write("Ao analisar os dados das ações sem nenhum ajuste nos dados é feita apenas uma análise histórica dos dados, \
            logo, vai ser possível observar quedas/aumentos bruscas nos valores das ações, nos gráficos, de um dia para o outro. \
            Porém, essas quedas ou aumentos não, necessáriamente, indicam que houveram de fato uma valorização/desvalorização no \
            valor do papel e sim que o papel sofreu algum tipo de evento finaceiro.")
        if st.button('Click aqui para saber mais...'):
            webbrowser.open_new_tab("https://dvinvest.com.br/aprenda/blog/introducao-aos-eventos-corporativos")

        fig = go.Figure(data=[go.Candlestick(x=df_ticker['Datetime'],
                open=df_ticker['Open'],
                high=df_ticker['High'],
                low=df_ticker['Low'],
                close=df_ticker['Close'])])

        st.plotly_chart(fig)

        st.subheader("Gráfico de preços de fechamentos ajustados")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_ticker["Datetime"],
                                 y=df_ticker["Adj Close"],
                                 name="Fechamento ajustado",
                                 line_color="blue"))
        st.plotly_chart(fig2)