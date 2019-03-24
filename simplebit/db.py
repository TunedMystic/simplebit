from pathlib import Path

from simplebit import constants, settings


def create_tables(conn):
    sql = Path(f'{settings.SQL_DIR}/create_tables.sql').read_text()
    with conn:
        cursor = conn.cursor()
        cursor.executescript(sql)
        cursor.close()


def create_asset(conn, data, batch=False):
    sql = """
        INSERT INTO crypto (name, symbol, asset_hash, category, logo, description, website, platform, platform_token_address)
        VALUES (:name, :symbol, :asset_hash, :category, :logo, :description, :website, :platform, :platform_token_address);
    """
    with conn:
        cursor = conn.cursor()
        cursor_exec = getattr(cursor, 'executemany' if batch else 'execute')
        cursor_exec(sql, data)
        cursor.close()


def search_assets(conn, search_text):
    sql = """
        SELECT c.name, c.symbol, c.asset_hash
        FROM crypto c
        WHERE c.name LIKE :search_text
        ORDER BY c.id ASC
        LIMIT 40;
    """
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, {'search_text': f'%{search_text}%'})
        r = cursor.fetchall()
        cursor.close()
    return r


def get_asset_detail(conn, asset_hash):
    sql = """
        SELECT c.name, c.symbol, c.asset_hash, c.category, c.logo, c.description, c.website, c.platform, c.platform_token_address
        FROM crypto c
        WHERE c.asset_hash LIKE :asset_hash;
    """
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, {'asset_hash': f'{asset_hash}%'})
        r = cursor.fetchone()
        cursor.close()
    return r


def get_related_crypto(conn, asset_hash, category, platform):
    sql = """
    SELECT c.symbol, c.asset_hash
    FROM crypto c
    WHERE (
        c.category = :category AND
        (c.platform = :platform OR c.platform IS NULL) AND
        c.asset_hash NOT LIKE :asset_hash
    )
    ORDER BY random()
    LIMIT 5;
    """
    data = {
        'category': category,
        'platform': platform,
        'asset_hash': f'{asset_hash}%',
    }
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, data)
        r = cursor.fetchall()
        cursor.close()
    return r


def get_asset_dynamic_field(conn, asset_hash, field_name):
    sql = """
        SELECT :field_name
        FROM crypto
        WHERE asset_hash LIKE :asset_hash;
    """
    data = {
        'asset_hash': f'{asset_hash}%',
        'field_name': field_name
    }
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, data)
        r = cursor.fetchone()
        cursor.close()
    return dict(r)
