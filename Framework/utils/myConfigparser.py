import configparser
from pathlib import Path

cfgFile = 'conf.ini'
cfgFileDit = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDit).joinpath(cfgFile)

config.read(CONFIG_FILE)

def getconfig():

    return config['prod']['url']

print(getconfig())
