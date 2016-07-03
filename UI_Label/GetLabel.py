#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'

import MySQLdb

def GetLabel(id_ui,time_start, time_end):

    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()
    
    # 构建mysql语句
    # 获取指定时间段内的(U,I)
    sql_ui = "select user_id,item_id from train_user\
              where buy_time >= '%s' and\
                    buy_time <  '%s' and\
                    behavior_type = '4'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_ui)
    results_ui = cur.fetchmany(execute)
    
    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()
    
    # 提取label那个时间段内购买记录的(U,I)
    id_ui_dict = {}
    id_ui_buy = []
    for uid in results_ui:
        id_ui_dict[(uid[0],uid[1])] = 1
        id_ui_buy.append((uid[0],uid[1])) 


    # 如果训练(U,I)在后一天被购买,则标记为1,否则标记为0
    label_ui = []
    for uid in id_ui:
        if id_ui_dict.has_key(uid):
            label_ui.append(1)
        else:
            label_ui.append(0)
    
    # 返回
    return label_ui,id_ui_buy    





