import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read(r'GUI\user.krip')
    return config

def save_path(p):
    config = load_config() 
    if 'Settings' not in config:
        config['Settings'] = {}
    config['Settings']['favorite_path'] = p
    with open(r'GUI\user.krip', 'w') as configfile:
        config.write(configfile)


def save_theme(t):
    config = load_config()  
    if 'Settings' not in config:
        config['Settings'] = {}
    config['Settings']['theme'] = t
    with open(r'GUI\user.krip', 'w') as configfile:
        config.write(configfile)
