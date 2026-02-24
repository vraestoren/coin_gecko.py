from requests import Session

class CoinGecko:
	def __init__(self) -> None:
		self.api = "https://api.coingecko.com"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}
	
	def ping(self) -> dict:
		return self.session.get(f"{self.api}/ping").json()
	
	def get_price(
			self,
			coins_ids: str,
			vs_currencies: str,
			include_market_cap: bool = False,
			include_24hr_vol: bool = False,
			include_last_updated_at: bool = False) -> dict:
		return self.session.get(
			f"{self.api}/simple/price?ids={coins_ids}&vs_currencies={vs_currencies}&include_market_cap={include_market_cap}&include_24hr_vol={include_24hr_vol}&include_last_updated_at={include_last_updated_at}").json()
	
	def get_token_price(
			self,
			platform_id: str,
			contact_addresses: str,
			vs_currencies: str,
			include_market_cap: bool = False,
			include_24hr_vol: bool = False,
			include_last_updated_at: bool = False) -> dict:
		return self.session.get(
			f"{self.api}/simple/token_price/{platform_id}?vs_currencies={vs_currencies}&include_market_cap={include_market_cap}&include_24hr_vol={include_24hr_vol}&include_last_updated_at={include_last_updated_at}").json()
	
	def get_supported_vs_currencies(self) -> dict:
		return self.session.get(
			f"{self.api}/simple/supported_vs_currencies").json()
	
	def get_coins_list(self, include_platform: bool = False) -> dict:
		return self.session.get(
			f"{self.api}/coins/list?include_platform={include_platform}").json()
	
	def get_markets(
			self,
			vs_currency: str,
			coin_ids: str = None,
			category: str = None,
			order: str = "market_cap_desc",
			per_page: int = 100,
			page: int = 1,
			sparkline: bool = False,
			price_change_percentage: str = None) -> dict:
		params = {
			"ids": coin_ids,
			"category": category,
			"price_change_percentage": price_change_percentage,

		}
		filtered_params = {
			key: value for key, value in params.items() if value is not None
		}
		return self.session.get(
			f"{self.api}/coins_markets?vs_currency={vs_currency}&order={order}&per_page={per_page}&page={page}&sparkline={sparkline}",
			params=filtered_params).json()
	
	def get_coin_current_data(
			self,
			coin_id: str,
			localization: bool = True,
			tickers: bool = True,
			market_data: bool = True,
			community_data: bool = True,
			developer_data: bool = True,
			sparkline: bool = False) -> dict:
		return self.session.get(
			f"{self.api}/coins/{coin_id}?localization={localization}&tickers={tickers}&market_data={market_data}&community_data={community_data}&developer_data={developer_data}&sparkline={sparkline}").json()
	
	def get_coin_tickers(
			self,
			coin_id: str,
			exchange_ids: str = None,
			include_exchange_logo: str = None,
			page: int = 1,
			order: str = None,
			depth: str = None) -> dict:
		params = {
			"exchange_ids": exchange_ids,
			"include_exchange_logo": include_exchange_logo,
			"order": order,
			"depth": depth
		}
		filtered_params = {
			key: value for key, value in params.items() if value is not None
		}
		return self.session.get(
			f"{self.api}/coins/{coin_id}/tickers?page={page}",
			params=filtered_params).json()
	
	def get_coin_historical_data(
			self,
			coin_id: str,
			date: str, 
			localization: bool = True) -> dict:
		return self.session.get(
			f"{self.api}/coins/{coin_id}/history?date={date}&localization={localization}").json()
	
	def get_coin_market_chart(
			self,
			coin_id: str,
			vs_currency: str,
			days: str,
			interval: str = "daily") -> dict:
		return self.session.get(
			f"{self.api}/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days={days}&interval={interval}").json()

	def get_coin_market_chart_range(
			self,
			coin_id: str,
			vs_currency: str,
			from_date: int,
			to_date: int) -> dict:
		return self.session.get(
			f"{self.api}/coins/{coin_id}/market_chart/range?vs_currency={vs_currency}&from={from_date}&to={to_date}").json()
	
	def get_coin_info_by_contract_address(
			self,
			platform_id: str,
			contract_address: str) -> dict:
		return self.session.get(
			f"{self.api}/coins/{platform_id}/contract/{contract_address}").json()
	
	def get_contract_address_market_chart(
			self,
			platform_id: str,
			contract_address: str,
			vs_currency: str,
			days: str) -> dict:
		return self.session.get(
			f"{self.api}/coins/{platform_id}/contract/{contract_address}/market_chart?vs_currency={vs_currency}&days={days}").json()
	
	def get_contract_address_market_chart_range(
			self,
			platform_id: str,
			contract_address: str,
			vs_currency: str,
			from_date: int,
			to_date: int) -> dict:
		return self.session.get(
			f"{self.api}/coins/{platform_id}/contract/{contract_address}/market_chart/range?vs_currency={vs_currency}&from={from_date}&to={to_date}").json()
	
	def get_coin_ohlc(
			self,
			coin_id: str,
			vs_currency: str,
			days: str) -> dict:
		return self.session.get(
			f"{self.api}/coins/{coin_id}/ohlc?vs_currency={vs_currency}&days={days}").json()
	
	def get_asset_platforms(self) -> dict:
		return self.session.get(f"{self.api}/asset_platforms").json()
	
	def get_all_categories(self) -> dict:
		return self.session.get(
			f"{self.api}/coins/categories/list").json()
	
	def get_all_categories_with_market_data(self, order: str = None) -> dict:
		params = {"order": order} if order else {}
		return self.session.get(
			f"{self.api}/coins/categories", params=params).json()
	
	def get_all_exchanges(
			self,
			per_page: int = 100,
			page: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/exchanges?per_page={per_page}&page={page}").json()
	
	def get_exchanges_with_market_data(self) -> dict:
		return self.session.get(f"{self.api}/exchanges/list").json()
	
	def get_exchange(self, exchange_id: str) -> dict:
		return self.session.get(
			f"{self.api}/exchanges/{exchange_id}").json()
	
	def get_exchange_tickers(
			self,
			exchange_id: str,
			coin_ids: str = None,
			include_exchange_logo: str = None,
			page: int = 1,
			order: str = None,
			depth: str = None) -> dict:
		params = {
			"coin_ids": coin_ids,
			"include_exchange_logo": include_exchange_logo,
			"order": order,
			"depth": depth
		}
		filtered_params = {
			key: value for key, value in params.items() if value is not None
		}
		return self.session.get(
			f"{self.api}/exchanges/{exchange_id}/tickers?page={page}",
			params=filtered_params).json()
	
	def get_all_market_indexes(
			self,
			per_page: int = 100,
			page: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/indexes?per_page={per_page}&page={page}").json()
	
	def get_market_index(
			self,
			market_id: str,
			index_id: str) -> dict:
		return self.session.get(
			f"{self.api}/indexes/{market_id}/{index_id}").json()
	
	def get_indexes_with_market_data(self) -> dict:
		return self.session.get(f"{self.api}/indexes/list").json()
	
	def get_all_derivative_tickers(
			self,
			include_tickers: str = "unexpired") -> dict:
		return self.session.get(
			f"{self.api}/derivatives?include_tickers={include_tickers}").json()
	
	def get_all_derivative_exchanges(
			self,
			order: str = None,
			per_page: int = 100,
			page: int = 1) -> dict:
		params = {"order": order} if order else {}
		return self.session.get(
			f"{self.api}/derivatives/exchanges?per_page={per_page}&page={page}",
			params=params).json()
	
	def get_derivative_exchange_data(
			self,
			exchange_id: str,
			include_tickers: str = "all") -> dict:
		return self.session.get(
			f"{self.api}/derivatives/exchanges/{exchange_id}?include_tickers={include_tickers}").json()
	
	def get_derivative_exchanges_list(self) -> dict:
		return self.session.get(
			f"{self.api}/derivative/exchanges/list").json()
	
	def get_volume_chart_data(self, exchange_id: str, days: int) -> dict:
		return self.session.get(
			f"{self.api}/exchanges/{exchange_id}/volume_chart?days={days}").json()
	
	def get_exchange_rates(self) -> dict:
		return self.session.get(
			f"{self.api}/exchange_rates").json()
	
	def search(self, query: str) -> dict:
		return self.session.get(
			f"{self.api}/search?query={query}").json()
	
	def get_trending_search(self) -> dict:
		return self.session.get(f"{self.api}/search/trending").json()
	
	def get_global_crypto_data(self) -> dict:
		return self.session.get(f"{self.api}/global").json()
	
	def get_global_crypto_defi_data(self) -> dict:
		return self.session.get(
			f"{self.api}/global/decentralized_finance_defi").json()
	
	def get_public_companies_data(self, coin_id: str) -> dict:
		return self.session.get(
			f"{self.api}/companies/public_treasury/{coin_id}").json()
