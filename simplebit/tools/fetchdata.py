import time

from simplebit import constants, cx, db
from simplebit.apiclient import CoinMarketCapClient
from simplebit.utils import batch, make_asset_hash
from simplebit.constants import CRYPTO_SYMBOLS


CATEGORIES = {
    'coin': constants.CRYPTO_CATEGORY_COIN,
    'token': constants.CRYPTO_CATEGORY_TOKEN
}


class CmcPipeline:
    def __init__(self):
        self.client = CoinMarketCapClient()
        self.conn = cx.get()
        self.wait_time = 3

    def _normalize_asset_data(self, response_data):
        normalized_data = []

        for asset_item in response_data['data'].values():
            try:
                website = asset_item.get('urls', {}).get('website', [])[0]
            except IndexError:
                website = None

            normalized_item = {
                'name': asset_item['name'],
                'symbol': asset_item['symbol'],
                'asset_hash': make_asset_hash(asset_item['name'], asset_item['symbol']),
                # 'category': CATEGORIES.get(asset_item['category'], constants.CRYPTO_CATEGORY_NONE),
                'category': constants.CATEGORIES_BY_NAME[asset_item['category']],
                'logo': asset_item['logo'],
                'description': asset_item['description'],
                'website': website,
                'platform': (asset_item.get('platform') or {}).get('name'),
                'platform_token_address': (asset_item.get('platform') or {}).get('token_address'),
            }

            normalized_data.append(normalized_item)
        return normalized_data

    def run(self):
        for i, symbol_batch in enumerate(batch(CRYPTO_SYMBOLS, 15)):
            print(f'[fetchdata] {i}')
            response_data = self.client.get_info(symbol_batch)

            if not response_data:
                print('   - nothing found. skipping...')
                continue

            normalized_asset_data = self._normalize_asset_data(response_data)
            db.create_asset(self.conn, normalized_asset_data, batch=True)
            print(f'   - created {len(normalized_asset_data)} assets')
            print('   - sleeping')

            time.sleep(self.wait_time)
            # if i == 3:
            #     break
        print('done...')


if __name__ == '__main__':
    cx.init()
    CmcPipeline().run()
