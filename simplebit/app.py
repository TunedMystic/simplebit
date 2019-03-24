import falcon

from simplebit import constants, cx, db, settings


class RootResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.media = {'app': 'simplebit'}


class AssetListResource:
    def on_get(self, request, response):
        search_text = request.params.get('q', '')
        rows = db.search_assets(cx.get(), search_text)
        response_data = []
        response_data = [
            {
                'id': row['asset_hash'][:15],
                'symbol': row['symbol'],
                'name': row['name'],
                '_detail': f'{settings.ROOT_URL}/assets/{row["asset_hash"][:15]}'
            }
            for row in rows
        ]
        response.status = falcon.HTTP_200
        response.media = response_data


class AssetDetailResource:
    def on_get(self, request, response, asset_hash):
        row = db.get_asset_detail(cx.get(), asset_hash)
        if not row:
            raise falcon.HTTPNotFound()

        # Build response for crypto detail.
        response_data = {
            'name': row['name'],
            'symbol': row['symbol'],
            'asset_hash': row['asset_hash'][:15],
            'category': constants.CATEGORIES_BY_CODE[row['category']],
            'logo': row['logo'],
            'website': row['website'],
            'description': row['description']
        }

        # Include platform info if the crypto is a token.
        if row['category'] == constants.CRYPTO_CATEGORY_TOKEN:
            response_data['platform'] = {
                'name': row['platform'],
                'token_address': row['platform_token_address'],
            }

        # Get related cryptos.
        related_crypto_rows = db.get_related_crypto(cx.get(),
                                                    row['asset_hash'][:15],
                                                    row['category'],
                                                    row['platform'])
        related_crypto = [
            {
                'symbol': row['symbol'],
                '_detail': f'{settings.ROOT_URL}/assets/{row["asset_hash"][:15]}'
            }
            for row in related_crypto_rows
        ]
        response_data['related_crypto'] = related_crypto

        response.status = falcon.HTTP_200
        response.media = response_data


class AssetDetailFieldResource:
    def on_get(self, request, response, asset_hash, field_name):
        if field_name not in constants.VALID_ASSET_FIELD_NAMES:
            raise falcon.HTTPBadRequest()

        # value = db.get_asset_dynamic_field(cx.get(), asset_hash, field_name)
        row = db.get_asset_detail(cx.get(), asset_hash)
        if not row:
            raise falcon.HTTPNotFound()

        response.status = falcon.HTTP_200
        response.body = row[field_name]


def get_api():
    print('[get_api]')
    app = falcon.API()
    app.add_route('/', RootResource())
    app.add_route('/assets', AssetListResource())
    app.add_route('/assets/{asset_hash}', AssetDetailResource())
    app.add_route('/assets/{asset_hash}/{field_name}', AssetDetailFieldResource())
    return app


def get_app():
    print('[get_app]')
    cx.init()
    return get_api()
