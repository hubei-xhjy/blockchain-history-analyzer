# 一些网站

## 查询空投情况

https://firestore.googleapis.com/v1/projects/mode-claim/databases/wallet-stats/documents/wallets/0xb4fb31e7b1471a8e52dd1e962a281a732ead59c1

> [!important] 这里走的是 Google 的 Firestore 服务，可能会检测到爬虫行为，导致返回 403 错误。所以 需要使用代理进行查询。

### 无效账户返回值

```json
{
    "error": {
        "code": 404,
        "message": "Document \"projects/mode-claim/databases/wallet-stats/documents/wallets/0x369c54759cb1ae18a897ed2c6230cf2043b92ef9\" not found.",
        "status": "NOT_FOUND"
    }
}
```

### 有效账户返回值

```json
{
    "name": "projects/mode-claim/databases/wallet-stats/documents/wallets/0xb4fb31e7b1471a8e52dd1e962a281a732ead59c1",
    "fields": {
        "mode_tokens": {
            "doubleValue": 9785760.0908318423
        },
        "total_points": {
            "doubleValue": 70372666.9790003
        }
    },
    "createTime": "2024-05-07T05:28:49.176094Z",
    "updateTime": "2024-05-07T05:28:49.176094Z"
}
```

```json
{
    "name": "projects/mode-claim/databases/wallet-stats/documents/wallets/0xd35f7f2acd4df8d1221d6dfb334810eba9f728b1",
    "fields": {
        "total_points": {
            "doubleValue": 269896.0224684081
        },
        "mode_tokens": {
            "doubleValue": 37530.732296016809
        }
    },
    "createTime": "2024-05-07T05:34:53.803300Z",
    "updateTime": "2024-05-07T05:34:53.803300Z"
}
```

## 查询账户情况

https://ref.mode.network/users/get-user-by-wallet-address?wallet=0xb4fb31e7b1471a8e52dd1e962a281a732ead59c1

### 无效账户返回值

```json
{
    "data": {
        "User": {
            "Wallet": {
                "String": "0x369c54759cb1ae18a897ed2c6230cf2043b92ef9",
                "Valid": true
            },
            "BridgeTx": {
                "String": "0x78936e1e1a9bad2f2bea06810987e086656293a5de69c0890e9a86f53eefe170",
                "Valid": true
            },
            "ModeDomainNftID": {
                "String": "",
                "Valid": false
            },
            "HasTwitterLogin": true
        },
        "Rank": {
            "Total": "0.002616000000000000",
            "UserRank": 191698
        },
        "Epochs": [
            {
                "epoch": 0,
                "points": 0.002616
            }
        ],
        "UserConversion": {
            "InvitedBy": {
                "String": "0xfd282d9f4d06c4bdc6a41af1ae920a0ad70d18a3",
                "Valid": true
            },
            "RedirectID": {
                "String": "bHpLJocX51U8eF8WUBAzGnWoHIwJRV",
                "Valid": true
            }
        }
    }
}
```

**如果这个账户完全没有交互过**

```json
{
    "error": "code=400, message=unknown user",
    "message": "unknown user"
}
```

### 有效账户返回值

```json
{
    "data": {
        "User": {
            "Wallet": {
                "String": "0xb4fb31e7b1471a8e52dd1e962a281a732ead59c1",
                "Valid": true
            },
            "BridgeTx": {
                "String": "0x86b2647a99ba2f6e768d015bdb1c7e4f224e23fbaa8f8ebbab21c4aa14ecefa8",
                "Valid": true
            },
            "ModeDomainNftID": {
                "String": "",
                "Valid": false
            },
            "HasTwitterLogin": true
        },
        "Rank": {
            "Total": "2344367.496464078188509223",
            "UserRank": 8
        },
        "Epochs": [
            {
                "epoch": 0,
                "points": 1239.657174
            }
        ],
        "UserConversion": {
            "InvitedBy": {
                "String": "0xb851220202c019d1645cb9f75dcc5ef7a66aaca9",
                "Valid": true
            },
            "RedirectID": {
                "String": "zwWs5JezYHD62S3QzBJ8V6qPmMZrGq",
                "Valid": true
            }
        }
    }
}
```

另一钱包：排名 1183

```json
{
    "data": {
        "User": {
            "Wallet": {
                "String": "0xd35f7f2acd4df8d1221d6dfb334810eba9f728b1",
                "Valid": true
            },
            "BridgeTx": {
                "String": "0xa0f26c6b90f5efa8e8a009145cc383563a952b37866bbf66301d6cfe229da386",
                "Valid": true
            },
            "ModeDomainNftID": {
                "String": "",
                "Valid": false
            },
            "HasTwitterLogin": true
        },
        "Rank": {
            "Total": "11156.695640533510157774",
            "UserRank": 1183
        },
        "Epochs": [
            {
                "epoch": 0,
                "points": 165.176333
            }
        ],
        "UserConversion": {
            "InvitedBy": {
                "String": "",
                "Valid": false
            },
            "RedirectID": {
                "String": "",
                "Valid": false
            }
        }
    }
}
```