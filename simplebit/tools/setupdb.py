from simplebit import cx, db


def setup():
    print('[setup]')
    cx.init()
    conn = cx.get()

    print('[create tables]')
    db.create_tables(conn)

    print('[setup] done')


setup()
