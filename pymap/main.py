import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

#naver api

client_id = "qpbql4sseo"
client_pw = "QjzP0jp9LS5sq8NOaxqErzz9aoGPNUQzjP8yW9fL"

api_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"