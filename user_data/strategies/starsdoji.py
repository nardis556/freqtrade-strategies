# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

# --------------------------------

class starsdoji(IStrategy):
    """
    #ported by nardis556

    """

    # Minimal ROI designed for the strategy.
    # adjust based on market conditions. We would recommend to keep it low for quick turn arounds
    # This attribute will be overridden if the config file contains "minimal_roi"
    minimal_roi = {
        "0": 0.1
    }

    # Optimal stoploss designed for the strategy
    stoploss = -0.2

    # Optimal timeframe for the strategy
    timeframe = '15m'

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['morningStar'] = ta.CDLMORNINGSTAR(dataframe['open'], dataframe['high'], dataframe['low'], dataframe['close'])
        dataframe['eveningStar'] = ta.CDLEVENINGSTAR(dataframe['open'], dataframe['high'], dataframe['low'], dataframe['close'])
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['morningStar'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['eveningStar'] < 0)
            ),
            'sell'] = 1
        return dataframe
