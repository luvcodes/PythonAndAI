"""
数据定义的类
"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date            # 订单日期
        self.order_id = order_id    # 订单ID
        self.money = money          # 订单金额
        self.province = province    # 销售省份

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"

    def to_json(self):
        d = {"date": self.date, "order_id": self.order_id, "money": self.money, "province": self.province}
        import json
        return json.dumps(d)

# 测试to_json方法
if __name__ == '__main__':
    r = Record("2020-01-01", "10001", "100", "北京")
    # 使用了__str__方法来输出
    print(r)
    # 使用to_json方法来输出
    jsonRecord = r.to_json();
    print(jsonRecord)
    # 查看Record对象的类型
    print(type(r))
