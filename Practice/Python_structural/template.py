######## BEFORE ########
# https://youtu.be/t0mCrXHsLbI
# https://tinyurl.com/yj4s9wuc

from typing import List

class Application:
    def __init__(self, trading_strategy = "average"):
        self.trading_strategy = trading_strategy

    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")

application = Application("average")
application.check_prices("BTC/USD")


######## AFTER ########
from typing import List
from abc import abstractmethod, ABC

class ExchangeMethod(ABC):

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass

class Binance(ExchangeMethod):
    def connect(self):
        print(f"Connecting to Binance exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 20, 30, 40, 50]

class Coinbase(ExchangeMethod):
    def connect(self):
        print(f"Connecting to Coinbase exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [15, 15, 35, 45, 65]
    
class TradingBot(ABC):

    def __init__(self, exchange: ExchangeMethod) -> None:
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, prices:List[float]) -> bool:
        pass
    
    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass
    
    def check_price(self, coin:str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should by {coin}")
        elif should_sell:
            print(f"You should sell {coin}")
        else:
            print(f"No action needed fo {coin}")

class AverageTrading(TradingBot):

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)
    
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)
    
    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)

class MinMaxTrading(TradingBot):
    
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)
        
    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)
        
app = AverageTrading(Coinbase())
app.check_price("BTC/USD")
