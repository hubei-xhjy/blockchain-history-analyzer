import requests

etherscan_api_key = ""
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
# 要查询的起始区块（尽可能的早，这样确保不会漏掉）
start_block = 10000000
current_block = start_block
# 要查询的结束区块（直到快照那天就行）
# TODO: 后面写个查询工具，实现根据快照日获取当日高度
end_block = 19438188
file_index = 1

for contract_address in contract_addresses:
    while True:
        url = f"""https://api.etherscan.io/api
        ?module=account
        &action=txlist
        &address={contract_address}
        &startblock={current_block}
        &endblock={end_block}
        &page=1
        &offset=10000
        &sort=asc
        &apikey={etherscan_api_key}"""

        url = url.replace(" ", "").replace("\n", "")

        print(f"URL: {url}")
        response = requests.get(url)

        if response.status_code == 200:
            # 进行数据处理
            data = response.json()
            result = data["result"]
            result_len = len(result)

            if result_len == 0:
                print("No more data.")
                break

            with open(f"output/{contract_address}-transactions-{file_index}.json", "w") as file:
                file.write(response.text)

            if result_len == 10000:
                # 表示可能还有数据没爬完
                # 获取最后一个 tx 的 blockNumber
                last_tx_block_number = int(result[-1]["blockNumber"])
                current_block = last_tx_block_number # 就选当前的区块，免得查询结果之间有漏网之鱼
                file_index += 1
                continue
            else:
                break
        else:
            print("Error:", response.status_code)