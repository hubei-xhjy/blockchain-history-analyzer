# blockchain-history-analyzer

区块链链上数据抓取与分析，几个不同的案例作为演示

## 要求

通过 EtherScan 进行数据爬取，需要一个 API Key, 需要注册一个账号，才能获取到 API Key
免费的 API Key 只能每秒进行 5 次请求

## 运行方法

克隆本仓库，然后创建虚拟环境，再安装 python 依赖即可

```bash
git clone https://github.com/hubei-xhjy/blockchain-history-analyzer.git
cd blockchain-history-analyzer
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python eigenlayer-addresses-lookup/1. get_txn_by_etherscan.py # 以此类推
```

## EigenLayer 交互用户的地址查询

> EigenLayer 已在 2024 年 3 月 15 日进行快照，现在我们需要根据和他交互过的地址进行数据分析。我们可以通过 EigenLayer 相关合约来获取想要的数据

