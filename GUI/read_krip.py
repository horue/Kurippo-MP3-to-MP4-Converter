import configparser

config = configparser.ConfigParser()
config.read(r'GUI\user.krip')


def get_path():
    path = config['Settings'].get('favorite_path')
    return path

def get_theme():
    theme = config['Settings'].get('theme')
    return theme


if __name__ == '__main__':
    print(get_path())
    print(get_theme())