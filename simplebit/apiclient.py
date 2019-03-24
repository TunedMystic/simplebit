import requests

from simplebit import settings


class CoinMarketCapError(Exception):
    pass


class CoinMarketCapClient:
    def __init__(self):
        self.root_url = 'https://pro-api.coinmarketcap.com/v1'

    def _get(self, path, **kwargs):
        params = kwargs.pop('params', {})
        params['CMC_PRO_API_KEY'] = settings.CMC_API_KEY
        return requests.get(f'{self.root_url}/{path}', params=params)

    def _clean_symbols(self, symbols):
        if not symbols:
            raise CoinMarketCapError('No symbols provided')

        if isinstance(symbols, str):
            return symbols.upper()

        if isinstance(symbols, list):
            return ','.join(str(x).upper() for x in symbols if x)

        raise CoinMarketCapError('symbols must be a string or list')

    def get_info(self, symbols):
        cleaned_symbols = self._clean_symbols(symbols)
        url_params = {'symbol': cleaned_symbols}
        response = self._get('cryptocurrency/info', params=url_params)

        if not response.ok:
            print(f'[CoinMarketCapClient] Failed to fetch data, [symbols] {cleaned_symbols}, [status] {response.status_code}, [reason] {response.reason}')
            return

        return response.json()
