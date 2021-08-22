import configparser


def config(file='config.ini'):
    config = configparser.ConfigParser()
    config.read(file)
    return config


def db_connection():
    # "postgres://pajak:omemji@localhost:5432/dbsiella"
    cfg = config()
    conn = ["postgresql://", cfg['DATABASE']['USER'], ':',
            cfg['DATABASE']['PASSWORD'], "@", cfg['DATABASE']['HOSTNAME'],
            ":", cfg['DATABASE']['PORT'] ,"/",cfg['DATABASE']['DB']]
    return ''.join(conn)


def msg_connection():
    cfg = config()
    return cfg['MESSAGING']
