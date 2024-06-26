"""
演示字典的课后练习：升职加薪，对所有级别为1级的员工，级别上升1级，薪水增加1000元
"""

info_dict = {
    "王力鸿": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰轮": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊节": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学油": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德滑": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"员工在升值加薪之前的结果：{info_dict}")

# for循环遍历字典
for name in info_dict:
    # if条件判断符合条件员工
    if info_dict[name]["级别"] == 1:
        # 升职加薪操作
        employee_info_dict = info_dict[name]
        employee_info_dict["级别"] = 2    # 级别+1
        employee_info_dict["工资"] += 1000    # 工资+1000
        info_dict[name] = employee_info_dict

print(f"对员工进行升级加薪后的结果是：{info_dict}")
