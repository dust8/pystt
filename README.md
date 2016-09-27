# pystt
[![PyPI version](https://badge.fury.io/py/pystt.svg)](https://badge.fury.io/py/pystt)

## 介绍

**pystt** 是 **STT** 的序列化和反序列化库. **STT** 是斗鱼自创的序列化和反序列化算法.
支持 **python3**.

### STT 规定

1. 键 key 和值 value 直接采用‘@=’分割
2. 数组采用‘/’分割
3. 如果 key 或者 value 中含有字符‘/’，则使用‘@S’转义
4. 如果 key 或者 value 中含有字符‘@’，使用‘@A’转义

## 安装

从 PyPi 安装:

```
$ pip install pystt
```

## 使用

``` python
>>> import pystt  

>>> pystt.dumps(['value1', 'value2', 'value3'])    
'value1/value2/value3/'

>>> pystt.loads('key1@=value1/key2@=value2/key3@=value3/')
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
