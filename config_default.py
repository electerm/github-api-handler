"""default config"""
import pydash as _
import imp
import logging

__all__ = ['conf']

hasLocalConfig = False

try:
  imp.load_source('config', './config.py')
  from config import conf as localConfig
  hasLocalConfig = True
except FileNotFoundError:
  logging.debug('no config')

conf = {
  'port': 5060,
  'host': 'localhost',
  'apiName': 'api',
  'githubReleaseJsonPath': 'electerm-github-release.json'
}

if hasLocalConfig:
  _.objects.assign(conf, localConfig)