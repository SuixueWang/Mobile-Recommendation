#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'


import MySQLdb

def UnionFeature(id_ui,time_start,time_end):
    
    print '----- x_union -----'

    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()    

    
    # 构建mysql语句
    # 获取指定时间段内的联合特征,包括 浏览, 收藏, 加购物车, 购买. UF(Union Feature),B(Behavior)
    
    # ------------------------------- UF1 -------------------------------------------------
    sql_UF_B1 = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s' and\
                    behavior_type = '1'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF_B1)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF1_B1_dict = {}
    for key in results:
        UF1_B1_dict[(key[0],key[1])] = key[2]

    print '--- UF1 ---'

    # ------------------------------- UF2 -------------------------------------------------
    sql_UF_B2 = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s' and\
                    behavior_type = '2'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF_B2)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF2_B2_dict = {}
    for key in results:
        UF2_B2_dict[(key[0],key[1])] = key[2]
        
    print '--- UF2 ---'

    # ------------------------------- UF3 -------------------------------------------------
    sql_UF_B3 = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s' and\
                    behavior_type = '3'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF_B3)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF3_B3_dict = {}
    for key in results:
        UF3_B3_dict[(key[0],key[1])] = key[2]

    print '--- UF3 ---'

    # ------------------------------- UF4 -------------------------------------------------
    sql_UF_B4 = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s' and\
                    behavior_type = '4'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF_B4)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF4_B4_dict = {}
    for key in results:
        UF4_B4_dict[(key[0],key[1])] = key[2]
        
    print '--- UF4 ---'
    
    # ------------------------------- UF5 -------------------------------------------------
    # 用户对商品的所有行为次数
    sql_UF = "select user_id,item_id,count(*) from train_user\
              where buy_time between '%s' and '%s'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_UF)
    results = cur.fetchmany(execute)
    
    # 提取label那个时间段内购买记录的(U,I)
    UF5_dict = {}
    for key in results:
        UF5_dict[(key[0],key[1])] = key[2]    
    
    print '--- UF5 ---'
        
    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()
    
    
    # ------------------------------------------ 整理特征 ----------------------------------
    X_union = []
    for uid in id_ui:
        
        UF1 = UF1_B1_dict.get(uid,0)
        UF2 = UF2_B2_dict.get(uid,0)   
        UF3 = UF3_B3_dict.get(uid,0)   
        UF4 = UF4_B4_dict.get(uid,0)  
        UF5 = UF5_dict.get(uid,0)   
           
        X_union.append((UF1,UF2,UF3,UF4,UF5)) 

    return X_union



