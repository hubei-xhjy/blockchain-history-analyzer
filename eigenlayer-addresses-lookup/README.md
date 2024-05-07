# Eigenlayer 交互地址查询

## 1. get_txn_by_etherscan.py

### 1. 获取 EigenLayer 合约地址

一般上，项目都会在他们的官网提供合约地址。通常在 Documentation 文档中。

1. 如 EigenLayer 的官网： https://www.eigenlayer.xyz/
2. 打开 Documentation 页面
3. 直接搜索 Contract，找到类似 `Contract Address`
   1. 会跳转到这里： https://docs.eigenlayer.xyz/eigenlayer/deployed-contracts/
4. 从文档中可以看到，这里提供了几个站外连接，我们点击 README.md 文档
5. 这时候会跳转到 GitHub（其他项目会有不同的方法，可能直接写在页面中）
   1. https://github.com/Layr-Labs/eigenlayer-contracts?tab=readme-ov-file#deployments

可以看到他们的表格如下：

| Name              | Proxy    | Implementation | Notes            |
| ----------------- | -------- | -------------- | ---------------- |
| DelegationManager | 0x012345 | 0xabcdef       | Proxy: TUP@4.7.1 |

我们只需要获取 Proxy 的合约就行，可以看到这里有一大串合约地址，都要留下来，以免有漏网之鱼

```
0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A
0x858646372CC42E1A627fcE94aa7A7033e7CF075A
0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338
0x135dda560e946695d6f155dacafc6f1f25c1f5af
0xD92145c07f8Ed1D392c1B88017934E301CC1c3Cd

0x54945180dB7943c0ed0FEE7EdaB2Bd24620256bc
0x93c4b944D05dfe6df7645A86cd2206016c51564D
0x1BeE69b7dFFfA4E2d53C2a2Df135C388AD25dCD2
0x9d7eD45EE2E8FC5482fa2428f15C971e6369011d
0x13760F50a9d7377e4F20CB8CF9e4c26586c658ff
0xa4C637e0F704745D182e4D38cAb7E7485321d059
0x57ba429517c3473B6d34CA9aCd56c0e735b94c02
0x0Fe4F44beE93503346A3Ac9EE5A26b130a5796d6
0x7CA911E83dabf90C90dD3De5411a10F1A6112184
0x8CA7A5d6f3acd3A7A8bC468a8CD0FB14B6BD28b6
0xAe60d8180437b5C34bB956822ac2710972584473
0x298aFB19A105D59E74658C4C334Ff360BadE6dd2
0xbeaC0eeEeeeeEEeEeEEEEeeEEeEeeeEeeEEBEaC0

0x5a2a4F2F3C18f09179B6703e63D9eDD165909073
0x7Fe7E9CC0F274d2435AD5d56D5fa73E47F6A23D8

0x5050389572f2d220ad927CcbeA0D406831012390
0xFEA47018D632A77bA579846c840d5706705Dc598
0x369e6F597e22EaB55fFb173C6d9cD234BD699111
0xBE1685C81aA44FF9FB319dD389addd9374383e90
```

### 2. 使用 Etherscan 搭配合约地址进行数据爬取

Etherscan 已经给我们提供了通过合约地址以及区块范围进行数据爬取的 API

> 注意：此 API 每次最大只返回 10000 条数据

```
https://api.etherscan.io/api
?module=account
&action=txlist
&address=合约地址
&startblock=起始区块
&endblock=结束区块
&page=1
&offset=10000
&sort=asc
&apikey={etherscan_api}
```

我们在这里做个示例，执行以下请求：

- 我们用 18905564 作为起始区块
- 这里我们用 19438188 作为结束区块
- 这里我们用 1 作为页数
- 这里我们用 1 作为偏移量（显示 1 条数据）
- 示例 API 

```
https://api.etherscan.io/api
?module=account
&action=txlist
&address=0x858646372CC42E1A627fcE94aa7A7033e7CF075A
&startblock=18905564
&endblock=19438188
&page=1
&offset=10000
&sort=asc
&apikey=你的 API Key
```

### 代码解释

这段代码是为了从 Etherscan API 拉取特定以太坊智能合约地址的交易数据，并将其保存到本地文件中。以下是对代码各部分的详细解释：

1. **导入模块**:
   使用 `import requests` 导入 Python 的 `requests` 库，这是一个常用的库，用于发起 HTTP 请求。
2. **API 密钥和合约地址**:
   `etherscan_api_key` 存储了 Etherscan API 的密钥，这是进行 API 调用时验证用户的关键信息。
   `contract_addresses` 列表包含了需要查询交易信息的多个智能合约地址。
3. **区块范围**:
   `start_block` 和 `end_block` 定义了查询交易的起始和结束区块号。代码中将起始区块设定为 10000000，结束区块设定为 19438188。这样设定是为了确保涵盖了需要查询的所有交易数据。
4. **查询循环**:
   代码使用了一个外层的 `for` 循环遍历每一个合约地址，内层的 `while` 循环则用于持续查询直到没有更多数据。对于每个合约地址，代码构造一个 URL 来调用 Etherscan 的 API，获取该地址的交易列表。如果一页的结果满了（默认是 10000 条最大），就调整 `current_block` 来获取接下来的数据。
5. **构造 URL**:
   URL 包括合约地址、起始和结束区块号等参数。为了保证 URL 的正确，代码中有步骤替换 URL 中的空格和换行符。
6. **处理响应**:
   如果 HTTP 请求成功（状态码 200），则读取返回的数据并检查结果集的长度。如果结果集为 0，说明没有更多数据；否则，将数据写入本地文件。每次成功写入文件后，如果结果集达到 10000 条，就更新 `current_block` 并增加文件索引 `file_index`，准备写入新的文件。
7. **错误处理**:
   如果 HTTP 请求失败，会打印错误信息和状态码。

这段代码的主要功能是从 Etherscan API 拉取交易数据，并根据数据量可能将结果分成多个文件保存。这可以用于分析智能合约的交易历史或进行区块链数据的备份。

## 2. get_addresses_list.py

有了这些 tx 数据，接下来我们需要对这些数据进行分析。得出与这个智能合约交互的地址列表。

上面的 json 返回数据如下（节选）

```json
{
    "status": "1",
    "message": "OK",
    "result": [
        {
            "blockNumber": "18000269",
            "timeStamp": "1693070135",
            "hash": "0x853e2a2f40ccf327b850724e538846a5268ead8e7fb3f359abbb678a469b9759",
            "nonce": "214",
            "blockHash": "0x89d54f887e7f948d9f9c0c7d6144c90f31cd81618c1d7c1772d9b2ac23c50691",
            "transactionIndex": "154",
            "from": "0xd06210462fa34227ecfff888c143fccd32b89157",
            "to": "0x858646372cc42e1a627fce94aa7a7033e7cf075a",
            "value": "0",
            "gas": "285000",
            "gasPrice": "12600604735",
            "isError": "1",
            "txreceipt_status": "0",
            "input": "0xe7a050aa0000000000000000000000001bee69b7dfffa4e2d53c2a2df135c388ad25dcd2000000000000000000000000ae78736cd615f374d3085123a210448e74fc63930000000000000000000000000000000000000000000000000166d2f688429c50",
            "contractAddress": "",
            "cumulativeGasUsed": "16328658",
            "gasUsed": "32119",
            "confirmations": "1815150",
            "methodId": "0xe7a050aa",
            "functionName": "depositIntoStrategy(address strategy,address token,uint256 amount)"
        }
    ]
}
```

可以得到以下信息：

1. 我们所需的数据都在 result 数组里
2. 重要的几个字段有：
   1. from
   2. to
   3. isError

其中，isError 是用来检查这个 tx 是否成功的，0 表示成功，1 表示失败。

接下来要做的事情就是对所有交互过的地址进行收集并去重。

### 代码解释

这段代码用于从之前通过 Etherscan API 获取的交易数据中提取出所有唯一的钱包地址，并将它们保存到一个文本文件中。以下是对代码各部分的详细解释：

1. **导入模块**:
   使用 `import os` 和 `import json` 导入 Python 的 `os` 库和 `json` 库。`os` 库用于操作文件和目录，`json` 库用于解析 JSON 文件。
2. **初始化数据**:
   `contract_addresses` 列表包含了所有需要处理的智能合约地址。这些地址之前已通过其他脚本用来获取交易数据。
   `wallet_addresses` 是一个集合（set），用于存储不重复的钱包地址。
3. **处理文件**:
   代码遍历 `contract_addresses` 中的每个地址。对于每个地址，它查找 `output` 目录下以该地址开头且以 `.json` 结尾的所有文件。
4. **读取和解析数据**:
   对于找到的每个文件，代码打开文件并加载 JSON 数据。它遍历每个交易数据的 'result' 部分，对每个交易项进行处理。
5. **筛选交易数据**:
   代码检查每个交易是否有错误（通过 'isError' 字段）。如果 `isError` 为 `1`，则忽略该交易；否则，将交易的发送方（'from'）和接收方（'to'）地址添加到 `wallet_addresses` 集合中。
6. **保存结果**:
   将 `wallet_addresses` 集合中的地址写入到 `output/wallet_addresses.txt` 文件中，每个地址占一行。
7. **输出统计信息**:
   最后，打印出存储的钱包地址总数，以帮助了解处理的结果规模。

## 3. track_eigenlayer_airdrop_by_address.py

现在有了所有的地址列表，接下来就是向空投项目方发送请求，查询空投额度：

通过一次前端请求过程中，我们使用开发者工具获取到了官方的空投 API 地址：

```python
url = "https://claims.eigenfoundation.org/clique-eigenlayer-api/campaign/eigenlayer/credentials?walletAddress={}"
```

我们发现官方并没有对 IP 进行禁止（流量限制），所以我们可以只挂一个 VPN 就开始暴力请求

因为这是一个很漫长的请求，所以我加入了 tqdm 来追踪进度

### 代码解释

这段代码旨在从一个 CSV 文件中读取钱包地址，通过并发请求一个 API 来获取关于每个钱包地址的额外数据（例如资格令牌信息），并将结果写入到一个新的 CSV 文件中。下面是对代码的详细解释：

1. **导入必要的模块**:
   - `requests` 用于发起网络请求。
   - `csv` 用于处理 CSV 文件读写。
   - `tqdm` 提供进度条功能，让用户可视化处理进度。
   - `ThreadPoolExecutor` 用于实现多线程并发，提高请求处理的效率。
2. **定义 API URL**:
   `url` 定义了用来获取数据的 API 地址，该地址需要填入一个钱包地址。
3. **读取钱包地址**:
   使用 `csv.reader` 从 "output/wallet_addresses.csv" 文件中读取钱包地址。首先读取标题行，并检查是否已经包含 'Tokens' 列。如果没有，将 'Tokens' 添加到标题行中。
4. **定义辅助函数 `fetch_token_data`**:
   这个函数接收一行数据（即一个钱包地址），向 API 发送请求，并处理响应。成功获取数据后，将其添加到该行；如果请求失败或发生异常，则记录相应的错误信息。
5. **多线程处理**:
   使用 `ThreadPoolExecutor` 创建一个线程池，最多允许 10 个并发线程。这些线程将并行地为每个钱包地址调用 `fetch_token_data` 函数。
6. **写入新的 CSV 文件**:
   结果被写入到 "output/wallet_addresses_updated.csv" 文件中。首先写入更新后的标题行，然后写入每行的处理结果。
7. **进度条显示**:
   使用 `tqdm` 包装 `executor.map` 的调用，显示处理进度条，提供用户友好的进度显示。
