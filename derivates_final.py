import json
import time
import numpy as np
import requests
import pandas as pd

import warnings

# 忽略所有警告
warnings.filterwarnings("ignore")

api_key = ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTY0MTQ2MzU4MSwiZXhwIjoxOTU3MDM5NTgxfQ'
           '.cabJNPlvva_BDUWIgOSRlqnFS2HzrA8I5Aw6sY_1O2E'),
game_id = 'eq.op-PyjkPu7rO'

headers = {'apikey': api_key[0]}
actor = 'dc16afcd-8787-45fd-8921-a531ec0cefa1'


def get_general_info(headers, game_id):
    params = (
        ('select', '*'),
        ('participants', 'fts.dc16afcd-8787-45fd-8921-a531ec0cefa1'),
    )

    response = requests.get('https://pjonbpemisvmmpbaxefb.supabase.co/rest/v1/archives', headers=headers, params=params)

    return response.json()




general_info = get_general_info(headers, game_id)



# 将数据写入JSON文件
with open('data/final_info.json', 'w') as file:
    json.dump(general_info, file)

