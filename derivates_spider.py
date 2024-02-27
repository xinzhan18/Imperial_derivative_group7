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
        ('game_id', game_id),
        ('limit', '1'))

    response = requests.get('https://pjonbpemisvmmpbaxefb.supabase.co/rest/v1/games', headers=headers, params=params)

    return response.json()


def get_user_info(headers, game_id):
    params = (
        ('select', '*'),
        ('game_id', game_id),
    )

    response = requests.get('https://pjonbpemisvmmpbaxefb.supabase.co/rest/v1/game-players', headers=headers,
                            params=params)
    return response.json()


def get_trade_history(headers, game_id):
    params = (
        ('select', '*'),
        ('game_id', game_id),
        ('order', 'created_at.desc'),
    )

    response = requests.get('https://pjonbpemisvmmpbaxefb.supabase.co/rest/v1/game-trades', headers=headers,
                            params=params)
    return response.json()

    # 累加过程中遇到NaN值则重新开始的函数
def cumsum_reset_at_nan(series):
    cumsum = []
    current_sum = 0
    for item in series:
        if np.isnan(item):
            current_sum = 0  # 遇到NaN，重置累加和
        else:
            current_sum += item
        cumsum.append(current_sum)
    return pd.Series(cumsum)

def get_user_pos(user1):
    user1['cumsum_pos'] = user1['pos'].cumsum()


    user1['open_prices'] = user1['price'] * user1['pos']
    user1['sum_open_prices'] = user1['open_prices'].cumsum()
    user1.loc[user1['cumsum_pos'] == 0, 'cumsum_pos'] = np.nan
    user1.loc[user1['cumsum_pos'] == 0, 'open_prices'] = np.nan
    user1 = user1.reset_index(drop=True)
    user1['sum_open_prices_open'] = cumsum_reset_at_nan(user1['open_prices'])
    user1['mean_prices'] = user1['sum_open_prices_open'] / user1['cumsum_pos'].abs()
    return user1


def get_mean_open_prices(user1):
    user1 = trade_his_df.loc[trade_his_df['actor'] == actor]
    user1.loc[user1['type'] == 'buy', 'pos'] = -1
    user1.loc[user1['type'] == 'sell', 'pos'] = 1
    mean_prices = user1.groupby(['market']).apply(get_user_pos)
    open_mean_prices = mean_prices['mean_prices'].groupby('market').last()
    sum_open_prices = mean_prices['sum_open_prices'].groupby('market').last()

    print(
        f'持仓收益{sum_open_prices.index[0]} 是 {sum_open_prices[0]}, 持仓收益{sum_open_prices.index[1]} 是 {sum_open_prices[1]},持仓收益{sum_open_prices.index[2]} 是 {sum_open_prices[2]}')

    print(
        f'开仓均价{open_mean_prices.index[0]} 是 {open_mean_prices[0]}, 开仓均价{open_mean_prices.index[1]} 是 {open_mean_prices[1]},开仓均价{open_mean_prices.index[2]} 是 {open_mean_prices[2]}')


general_info = get_general_info(headers, game_id)
user_info = get_user_info(headers, game_id)
last_date = ''
while True:
    time.sleep(1)
    trade_his = get_trade_history(headers, game_id)
    trade_his_df = pd.DataFrame(trade_his)
    trade_his_df = trade_his_df.sort_values('created_at')
    now_date = trade_his_df['created_at'].iloc[-1]
    if now_date != last_date:
        print(now_date)

        get_mean_open_prices(trade_his_df)
    last_date = now_date
    # print('*'*10)

# 将数据写入JSON文件
with open('data/general_info.json', 'w') as file:
    json.dump(general_info, file)

# 将数据写入JSON文件
with open('data/user_info.json', 'w') as file:
    json.dump(user_info, file)

# 将数据写入JSON文件
with open('data/trade_his.json', 'w') as file:
    json.dump(trade_his, file)
