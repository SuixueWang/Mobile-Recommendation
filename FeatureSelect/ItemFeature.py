#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'

import MySQLdb
import numpy as np

def ItemFeature(id_ui,time_start_ui,time_start,time_end):
    
    print '----- x_item -----'

    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()  

    id_i = set(list(np.array(id_ui)[:,1]))
    
    # 用逗号分隔开
    item_list = ",".join(map(str, list(id_i)))
    
    # ------------------------------- 商品特征 I1 -----------------------------------
    # 商品被多少人浏览
    sql_i1 = "select item_id,count(distinct(user_id)) from train_user\
              where item_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '1'\
              group by item_id; "%(item_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i1)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I1_B1_dict = {}
    for key in results:
        I1_B1_dict[key[0]] = key[1]

    print '--- I1 ---'
    
    # ------------------------------- 商品特征 I2 -----------------------------------
    # 商品被多少人收藏
    sql_i2 = "select item_id,count(distinct(user_id)) from train_user\
              where item_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '2'\
              group by item_id; "%(item_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i2)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I2_B2_dict = {}
    for key in results:
        I2_B2_dict[key[0]] = key[1]

    print '--- I2 ---'

    # ------------------------------- 商品特征 I3 -----------------------------------
    # 商品被多少人加入购物车
    sql_i3 = "select item_id,count(distinct(user_id)) from train_user\
              where item_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '3'\
              group by item_id; "%(item_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i3)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I3_B3_dict = {}
    for key in results:
        I3_B3_dict[key[0]] = key[1]

    print '--- I3 ---'

    # ------------------------------- 商品特征 I4 -----------------------------------
    # 商品被多少人购买
    sql_i4 = "select item_id,count(distinct(user_id)) from train_user\
              where item_id in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '4'\
              group by item_id; "%(item_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i4)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I4_B4_dict = {}
    for key in results:
        I4_B4_dict[key[0]] = key[1]

    print '--- I4 ---'

    # ------------------------------ 下面计算商品行为次数/商品所属品牌行为次数 ------------------------------
    
    # 先提取商品所属品牌
    sql_i_c = "select item_id,item_category from train_user\
               where item_id in (%s) and\
                     buy_time between '%s' and '%s'\
                     group by item_id,item_category;"%(item_list,time_start_ui,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i_c)
    results = cur.fetchmany(execute)
    
    # 映射关系: 商品 -> 品牌
    I_C_dict = {}
    cat = []
    for key in results:
        I_C_dict[key[0]] = key[1]
        cat.append(key[1])
    
    # 用逗号分隔开
    cat_list = ",".join(map(str, list(set(cat))))
    
    
    # ------------------------------- 商品特征 I5 -----------------------------------
    # 商品被浏览人次/商品所属品牌被浏览人次
    sql_i5 = "select item_category,count(distinct(user_id)) from train_user\
              where item_category in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '1'\
              group by item_category; "%(cat_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i5)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I5_B1_dict = {}
    for key in results:
        I5_B1_dict[key[0]] = key[1]

    print '--- I5 ---'

    # ------------------------------- 商品特征 I6 -----------------------------------
    # 商品被浏览人次/商品所属品牌被浏览人次
    sql_i6 = "select item_category,count(distinct(user_id)) from train_user\
              where item_category in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '2'\
              group by item_category; "%(cat_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i6)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I6_B2_dict = {}
    for key in results:
        I6_B2_dict[key[0]] = key[1]

    print '--- I6 ---'

    # ------------------------------- 商品特征 I7 -----------------------------------
    # 商品被浏览人次/商品所属品牌被浏览人次
    sql_i7 = "select item_category,count(distinct(user_id)) from train_user\
              where item_category in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '3'\
              group by item_category; "%(cat_list,time_start,time_end)
    
    # 执行数据库操作
    execute = cur.execute(sql_i7)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I7_B3_dict = {}
    for key in results:
        I7_B3_dict[key[0]] = key[1]

    print '--- I7 ---'

    # ------------------------------- 商品特征 I8 -----------------------------------
    # 商品被浏览人次/商品所属品牌被浏览人次
    sql_i8 = "select item_category,count(distinct(user_id)) from train_user\
              where item_category in (%s) and\
                    buy_time between '%s' and '%s' and\
                    behavior_type = '4'\
              group by item_category; "%(cat_list,time_start,time_end)   
    
    # 执行数据库操作
    execute = cur.execute(sql_i8)
    results = cur.fetchmany(execute)
    
    # 用字典保存
    I8_B4_dict = {}
    for key in results:
        I8_B4_dict[key[0]] = key[1]

    print '--- I8 ---'

    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()

# ------------------------------------------ 整理特征 ----------------------------------
    X_item = []
    for uid in id_ui:
        
        id_i = uid[1]
        
        I1 = I1_B1_dict.get(id_i,0)
        I2 = I2_B2_dict.get(id_i,0)   
        I3 = I3_B3_dict.get(id_i,0)   
        I4 = I4_B4_dict.get(id_i,0)
        
        I5 =  (1.0 + I1)/(2.0 + I5_B1_dict.get(I_C_dict[id_i],0)) 
        I6 =  (1.0 + I2)/(2.0 + I6_B2_dict.get(I_C_dict[id_i],0)) 
        I7 =  (1.0 + I3)/(2.0 + I7_B3_dict.get(I_C_dict[id_i],0)) 
        I8 =  (1.0 + I4)/(2.0 + I8_B4_dict.get(I_C_dict[id_i],0))  
           
        X_item.append((I1,I2,I3,I4,I5,I6,I7,I8)) 
    
    return X_item

