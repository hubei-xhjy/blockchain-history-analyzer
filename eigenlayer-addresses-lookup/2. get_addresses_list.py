import os
import json

# 这个合约地址和 get_txn_from_etherscan.py 相对应，用来获取 output 文件夹中的文件。
contract_addresses = [
    "0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A",
    "0x858646372CC42E1A627fcE94aa7A7033e7CF075A",
    "0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338",
    "0x135dda560e946695d6f155dacafc6f1f25c1f5af",
    "0xD92145c07f8Ed1D392c1B88017934E301CC1c3Cd",
    "0x54945180dB7943c0ed0FEE7EdaB2Bd24620256bc",
    "0x93c4b944D05dfe6df7645A86cd2206016c51564D",
    "0x1BeE69b7dFFfA4E2d53C2a2Df135C388AD25dCD2",
    "0x9d7eD45EE2E8FC5482fa2428f15C971e6369011d",
    "0x13760F50a9d7377e4F20CB8CF9e4c26586c658ff",
    "0xa4C637e0F704745D182e4D38cAb7E7485321d059",
    "0x57ba429517c3473B6d34CA9aCd56c0e735b94c02",
    "0x0Fe4F44beE93503346A3Ac9EE5A26b130a5796d6",
    "0x7CA911E83dabf90C90dD3De5411a10F1A6112184",
    "0x8CA7A5d6f3acd3A7A8bC468a8CD0FB14B6BD28b6",
    "0xAe60d8180437b5C34bB956822ac2710972584473",
    "0x298aFB19A105D59E74658C4C334Ff360BadE6dd2",
    "0xbeaC0eeEeeeeEEeEeEEEEeeEEeEeeeEeeEEBEaC0",
    "0x5a2a4F2F3C18f09179B6703e63D9eDD165909073",
    "0x7Fe7E9CC0F274d2435AD5d56D5fa73E47F6A23D8",
    "0x5050389572f2d220ad927CcbeA0D406831012390",
    "0xFEA47018D632A77bA579846c840d5706705Dc598",
    "0x369e6F597e22EaB55fFb173C6d9cD234BD699111",
    "0xBE1685C81aA44FF9FB319dD389addd9374383e90"
]

wallet_addresses = set() # 用于存储钱包地址的集合

counter = 0

for contract_address in contract_addresses:
    print(f"Processing contract address: {contract_address}")
    # 获取 output 文件夹中，所有以 contract_address 开头的 json 文件，如果没有则跳过
    files = [f for f in os.listdir('output') if f.startswith(contract_address) and f.endswith('.json')]

    for file in files:
        # 读取 json 文件
        with open(f'output/{file}', 'r') as f:
            data = json.load(f)

            # 获取交易信息，判断是否 isError 如果 isError 为 1 则跳过，
            # 否则获取 from 和 to 字段并加到钱包集合中
            for txn in data['result']:
                if txn['isError'] == "1":
                    continue
                from_address = txn['from']
                to_address = txn['to']
                wallet_addresses.add(from_address)
                wallet_addresses.add(to_address)

# 输出钱包地址集合
with open('output/wallet_addresses.csv', 'w') as f:
    for address in wallet_addresses:
        f.write(address + "\n")

print(f"Total wallet addresses: {len(wallet_addresses)}")