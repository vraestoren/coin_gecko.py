from requests import Session

class CoinGecko:
	def __init__(self) -> None:
		self.api = "https://api.coingecko.com/api/v3"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params or {}).json()

	def _build_params(self, **kwargs) -> dict:
		return {key: value for key, value in kwargs.items() if value is not None}

	def get_price(
			self,
			coin_ids: str,
			vs_currencies: str,
			include_market_cap: bool = False,
			include_24hr_vol: bool = False,
			include_24hr_change: bool = False,
			include_last_updated_at: bool = False,
			precision: str = None) -> dict:
		params = self._build_params(
			ids=coin_ids,
			vs_currencies=vs_currencies,
			include_market_cap=include_market_cap,
			include_24hr_vol=include_24hr_vol,
			include_24hr_change=include_24hr_change,
			include_last_updated_at=include_last_updated_at,
			precision=precision)
		return self._get("/simple/price", params)

	def get_token_price(
			self,
			platform_id: str,
			contract_addresses: str,
			vs_currencies: str,
			include_market_cap: bool = False,
			include_24hr_vol: bool = False,
			include_24hr_change: bool = False,
			include_last_updated_at: bool = False,
			precision: str = None) -> dict:
		params = self._build_params(
			contract_addresses=contract_addresses,
			vs_currencies=vs_currencies,
			include_market_cap=include_market_cap,
			include_24hr_vol=include_24hr_vol,
			include_24hr_change=include_24hr_change,
			include_last_updated_at=include_last_updated_at,
			precision=precision)
		return self._get(f"/simple/token_price/{platform_id}", params)

	def get_supported_vs_currencies(self) -> dict:
		return self._get("/simple/supported_vs_currencies")

	def get_coins_list(
			self, include_platform: bool = False) -> dict:
		params = self._build_params(include_platform=include_platform)
		return self._get("/coins/list", params)

	def get_markets(
			self,
			vs_currency: str,
			coin_ids: str = None,
			category: str = None,
			order: str = "market_cap_desc",
			per_page: int = 100,
			page: int = 1,
			sparkline: bool = False,
			price_change_percentage: str = None,
			locale: str = None,
			precision: str = None) -> dict:
		params = self._build_params(
			vs_currency=vs_currency,
			ids=coin_ids,
			category=category,
			order=order,
			per_page=per_page,
			page=page,
			sparkline=sparkline,
			price_change_percentage=price_change_percentage,
			locale=locale,
			precision=precision)
		return self._get("/coins/markets", params)

	def get_coin_current_data(
			self,
			coin_id: str,
			localization: bool = True,
			tickers: bool = True,
			market_data: bool = True,
			community_data: bool = True,
			developer_data: bool = True,
			sparkline: bool = False) -> dict:
		params = self._build_params(
			localization=localization,
			tickers=tickers,
			market_data=market_data,
			community_data=community_data,
			developer_data=developer_data,
			sparkline=sparkline)
		return self._get(f"/coins/{coin_id}", params)

	def get_coin_tickers(
			self,
			coin_id: str,
			exchange_ids: str = None,
			include_exchange_logo: bool = None,
			page: int = 1,
			order: str = None,
			depth: bool = None) -> dict:
		params = self._build_params(
			exchange_ids=exchange_ids,
			include_exchange_logo=include_exchange_logo,
			page=page,
			order=order,
			depth=depth)
		return self._get(f"/coins/{coin_id}/tickers", params)

	def get_coin_historical_data(
			self,
			coin_id: str,
			date: str,
			localization: bool = True) -> dict:
		params = self._build_params(
			date=date, localization=localization)
		return self._get(f"/coins/{coin_id}/history", params)

	def get_coin_market_chart(
			self,
			coin_id: str,
			vs_currency: str,
			days: str,
			interval: str = None,
			precision: str = None) -> dict:
		params = self._build_params(
			vs_currency=vs_currency,
			days=days,
			interval=interval,
			precision=precision)
		return self._get(f"/coins/{coin_id}/market_chart", params)

	def get_coin_market_chart_range(
			self,
			coin_id: str,
			vs_currency: str,
			from_date: int,
			to_date: int,
			precision: str = None) -> dict:
		params = self._build_params(
			vs_currency=vs_currency,
			**{"from": from_date},
			to=to_date,
			precision=precision)
		return self._get(f"/coins/{coin_id}/market_chart/range", params)

	def get_coin_ohlc(
			self,
			coin_id: str,
			vs_currency: str,
			days: str,
			precision: str = None) -> dict:
		params = self._build_params(
			vs_currency=vs_currency,
			days=days,
			precision=precision)
		return self._get(f"/coins/{coin_id}/ohlc", params)

	def get_coin_info_by_contract_address(
			self,
			platform_id: str,
			contract_address: str) -> dict:
		return self._get(f"/coins/{platform_id}/contract/{contract_address}")

	def get_contract_address_market_chart(
			self,
			platform_id: str,
			contract_address: str,
			vs_currency: str,
			days: str,
			precision: str = None) -> dict:
		params = self._build_params(
			vs_currency=vs_currency,
			days=days,
			precision=precision)
		return self._get(
			f"/coins/{platform_id}/contract/{contract_address}/market_chart",
			params)

	def get_contract_address_market_chart_range(
			self,
			platform_id: str,
			contract_address: str,
			vs_currency: str,
			from_date: int,
			to_date: int,
			precision: str = None) -> dict:
		params = self._build_params(
			vs_currency=vs_currency,
			**{"from": from_date},
			to=to_date,
			precision=precision)
		return self._get(
			f"/coins/{platform_id}/contract/{contract_address}/market_chart/range",
			params)

	def get_asset_platforms(
			self,
			filter: str = None) -> dict:
		params = self._build_params(filter=filter)
		return self._get("/asset_platforms", params)

	def get_all_categories(self) -> dict:
		return self._get("/coins/categories/list")

	def get_all_categories_with_market_data(
			self,
			order: str = None) -> dict:
		params = self._build_params(order=order)
		return self._get("/coins/categories", params)

	def get_all_exchanges(
			self,
			per_page: int = 100,
			page: int = 1) -> dict:
		params = self._build_params(per_page=per_page, page=page)
		return self._get("/exchanges", params)

	def get_exchanges_list(self) -> dict:
		return self._get("/exchanges/list")

	def get_exchange(
			self,
			exchange_id: str) -> dict:
		return self._get(f"/exchanges/{exchange_id}")

	def get_exchange_tickers(
			self,
			exchange_id: str,
			coin_ids: str = None,
			include_exchange_logo: bool = None,
			page: int = 1,
			order: str = None,
			depth: bool = None) -> dict:
		params = self._build_params(
			coin_ids=coin_ids,
			include_exchange_logo=include_exchange_logo,
			page=page,
			order=order,
			depth=depth)
		return self._get(f"/exchanges/{exchange_id}/tickers", params)

	def get_volume_chart_data(
			self,
			exchange_id: str,
			days: int) -> dict:
		params = self._build_params(days=days)
		return self._get(f"/exchanges/{exchange_id}/volume_chart", params)

	def get_all_market_indexes(
			self,
			per_page: int = 100,
			page: int = 1) -> dict:
		params = self._build_params(per_page=per_page, page=page)
		return self._get("/indexes", params)

	def get_market_index(
			self,
			market_id: str,
			index_id: str) -> dict:
		return self._get(f"/indexes/{market_id}/{index_id}")

	def get_indexes_list(self) -> dict:
		return self._get("/indexes/list")

	def get_all_derivative_tickers(
			self,
			include_tickers: str = "unexpired") -> dict:
		params = self._build_params(include_tickers=include_tickers)
		return self._get("/derivatives", params)

	def get_all_derivative_exchanges(
			self,
			order: str = None,
			per_page: int = 100,
			page: int = 1) -> dict:
		params = self._build_params(
			order=order, per_page=per_page, page=page)
		return self._get("/derivatives/exchanges", params)

	def get_derivative_exchange_data(
			self,
			exchange_id: str,
			include_tickers: str = "all") -> dict:
		params = self._build_params(include_tickers=include_tickers)
		return self._get(f"/derivatives/exchanges/{exchange_id}", params)

	def get_derivative_exchanges_list(self) -> dict:
		return self._get("/derivatives/exchanges/list")

	def get_exchange_rates(self) -> dict:
		return self._get("/exchange_rates")

	def search(
			self,
			query: str) -> dict:
		params = self._build_params(query=query)
		return self._get("/search", params)

	def get_trending_search(self) -> dict:
		return self._get("/search/trending")

	def get_global_crypto_data(self) -> dict:
		return self._get("/global")

	def get_global_crypto_defi_data(self) -> dict:
		return self._get("/global/decentralized_finance_defi")

	def get_public_companies_data(
			self,
			coin_id: str) -> dict:
		return self._get(f"/companies/public_treasury/{coin_id}")
