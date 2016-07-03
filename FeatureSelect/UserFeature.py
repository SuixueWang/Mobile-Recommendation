#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'

import MySQLdb
import numpy as np

def UserFeature(id_ui,time_start,time_end):
    
    print '----- x_user -----'

    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()  

    id_u = set(list(np.array(id_ui)[:,0]))
    
    # 用逗号分隔开
    user_list = ",".join(map(str, list(id_u)))
    
    # ------------------------------- 用户特征 U1 -----------------------------------
    # 用户浏览商品量
    sql_u1 = "select user_id,count(distinct(item_id)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '1'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u1)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U1_B1_dict = {}
    for key in results:
        U1_B1_dict[key[0]] = key[1]

    print '--- U1 ---'
    
    # ------------------------------- 用户特征 U2 -----------------------------------
    # 用户收藏商品量
    sql_u2 = "select user_id,count(distinct(item_id)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '2'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u2)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U2_B2_dict = {}
    for key in results:
        U2_B2_dict[key[0]] = key[1]

    print '--- U2 ---'

    # ------------------------------- 用户特征 U3 -----------------------------------
    # 用户加入购物车商品量
    sql_u3 = "select user_id,count(distinct(item_id)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '3'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u3)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U3_B3_dict = {}
    for key in results:
        U3_B3_dict[key[0]] = key[1]
    
    print '--- U3 ---'
        
    # ------------------------------- 用户特征 U4 -----------------------------------
    # 用户购买商品量
    sql_u4 = "select user_id,count(distinct(item_id)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '4'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u4)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U4_B4_dict = {}
    for key in results:
        U4_B4_dict[key[0]] = key[1]

    print '--- U4 ---'

    # ------------------------------- 用户特征 U5 -----------------------------------
    # 用户浏览品牌量
    sql_u5 = "select user_id,count(distinct(item_category)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '1'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u5)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U5_B1_dict = {}
    for key in results:
        U5_B1_dict[key[0]] = key[1]

    print '--- U5 ---'

    # ------------------------------- 用户特征 U6 -----------------------------------
    # 用户收藏品牌量
    sql_u6 = "select user_id,count(distinct(item_category)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '2'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u6)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U6_B2_dict = {}
    for key in results:
        U6_B2_dict[key[0]] = key[1]
    
    print '--- U6 ---'

    # ------------------------------- 用户特征 U7 -----------------------------------
    # 用户加入购物车品牌量
    sql_u7 = "select user_id,count(distinct(item_category)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '3'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u7)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U7_B3_dict = {}
    for key in results:
        U7_B3_dict[key[0]] = key[1]
        
    print '--- U7 ---'
        
    # ------------------------------- 用户特征 U8 -----------------------------------
    # 用户购买品牌量
    sql_u8 = "select user_id,count(distinct(item_category)) from train_user\
              where user_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '4'\
              group by user_id; "%(user_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_u8)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    U8_B4_dict = {}
    for key in results:
        U8_B4_dict[key[0]] = key[1]

    print '--- U8 ---'

    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()
    
    # ------------------------------------------ 整理特征 ----------------------------------
    X_user = []
    for uid in id_ui:
        
        id_u = uid[0]
        
        U1 = U1_B1_dict.get(id_u,0)
        U2 = U2_B2_dict.get(id_u,0)   
        U3 = U3_B3_dict.get(id_u,0)   
        U4 = U4_B4_dict.get(id_u,0) 
        U5 = U5_B1_dict.get(id_u,0)
        U6 = U6_B2_dict.get(id_u,0)   
        U7 = U7_B3_dict.get(id_u,0)   
        U8 = U8_B4_dict.get(id_u,0)   
        
        U9 = (1.0+U4)/(2.0+U1)
        U10 = (1.0+U4)/(2.0+U2)
        U11 = (1.0+U4)/(2.0+U3)
        
        U12 = (1.0+U8)/(2.0+U5)
        U13 = (1.0+U8)/(2.0+U6)
        U14 = (1.0+U8)/(2.0+U7)
           
        X_user.append((U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14)) 
    
    return X_user
    









