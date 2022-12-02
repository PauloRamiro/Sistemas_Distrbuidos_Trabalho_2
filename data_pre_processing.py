import pandas as pd
import yfinance as yf


class DataTicker:
    @staticmethod
    def collecting_data_name_in_csv():
        path = "tickers.csv"
        return pd.read_csv(path, delimiter=";")

    @staticmethod
    def collecting_data_in_yfinance(ticker_cd, period):
        if period == "1 minuto":
            df = yf.download(ticker_cd, period=Prediction_Date_MAX.for_1_min(), interval="1m")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d %H:%M:%S")
            return df

        elif period == "2 minutos":
            df = yf.download(ticker_cd, period=Prediction_Date_MAX.for_2_min(), interval="2m")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d %H:%M:%S")
            return df

        elif period == "5 minutos":
            df = yf.download(ticker_cd, period=Prediction_Date_MAX.for_5_min(), interval="5m")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d %H:%M:%S")
            return df

        elif period == "15 minutos":
            df = yf.download(ticker_cd, period=Prediction_Date_MAX.for_15_min(), interval="15m")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d %H:%M:%S")
            return df

        elif period == "30 minutos":
            df = yf.download(ticker_cd, period=Prediction_Date_MAX.for_30_min(), interval="30m")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d %H:%M:%S")
            return df

        elif period == "1 hora":
            df = yf.download(ticker_cd, period=Prediction_Date_MAX.for_1_hour(), interval="1h")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d %H:%M:%S")
            return df

        elif period == "1 dia":
            df = yf.download(ticker_cd, interval="1d")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d")
            return df

        elif period == "5 dias":
            df = yf.download(ticker_cd, interval="5d")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d")
            return df

        elif period == "1 semana":
            df = yf.download(ticker_cd, interval="1wk")
            df.reset_index(inplace=True)
            column_list = list(df.columns)
            column_list[0] = "Datetime"
            df.columns = column_list
            df["Datetime"] = df["Datetime"].dt.strftime("%Y/%m/%d")
            return df


class Prediction_Date_MAX:
    """
        This class defines the dates that will be used to obtain the
        exchange data through the yfinance library, in order to
        obtain as much data as possible.
    """
    @staticmethod
    def for_1_min():
        period_max = "7d"
        return period_max

    @staticmethod
    def for_2_min():
        period_max = "60d"
        return period_max

    @staticmethod
    def for_5_min():
        period_max = "60d"
        return period_max

    @staticmethod
    def for_15_min():
        period_max = "60d"
        return period_max

    @staticmethod
    def for_30_min():
        period_max = "60d"
        return period_max

    @staticmethod
    def for_1_hour():
        period_max = "730d"
        return period_max