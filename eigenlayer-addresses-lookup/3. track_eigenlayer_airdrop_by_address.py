import requests
import csv
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# API 地址
url = "https://claims.eigenfoundation.org/clique-eigenlayer-api/campaign/eigenlayer/credentials?walletAddress={}"

# 读取数据
with open("output/wallet_addresses.csv") as address_file:
    reader = csv.reader(address_file)
    headers = next(reader)  # 读取标题行
    
    # 检查是否已经有 'Tokens' 列，如果没有则添加
    if 'Tokens' not in headers:
        headers.append('Tokens')
    
    # 读取所有行数据，准备多线程处理
    rows = list(reader)

def fetch_token_data(row):
    """辅助函数，用于发送 API 请求并处理响应。"""
    try:
        response = requests.get(url.format(row[0]), timeout=10)
        if response.status_code == 200:
            tokens = response.json()["data"]["pipelines"]["tokenQualified"]
            row.append(tokens)
        else:
            row.append('Failed to retrieve')
    except Exception as e:
        print(f"Error processing {row[0]}: {str(e)}")
        row.append('Error')
    return row

# 使用线程池处理请求
with ThreadPoolExecutor(max_workers=10) as executor, \
     open("output/wallet_addresses_updated.csv", mode="w", newline='') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(headers)  # 写入标题行
    
    # 包装 tqdm 来显示进度条
    results = list(tqdm(executor.map(fetch_token_data, rows), total=len(rows), desc="Processing addresses"))
    
    # 写入处理结果
    for result in results:
        writer.writerow(result)
