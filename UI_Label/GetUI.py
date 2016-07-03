#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wsx'

# 导包
import MySQLdb
import time

'''
import MySQLdb
提取(U,I)
'''
def GetUI_offline(time_start, time_end, time_end_lable):
    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()
    
    # 先从下一天获取有那些用户有购买记录
    sql_i = "select item_id from train_user\
              where buy_time between '%s' and '%s'\
              group by item_id; "%(time_end,time_end_lable)
              
    # 执行数据库操作
    execute = cur.execute(sql_i)
    results_i = cur.fetchmany(execute)
    
    i_dict = {}
    for i in results_i:
        i_dict[i[0]] = 0
    print 'Len(i_dict) is',len(i_dict)
    # ---------------------------------------------------------------------
    # 构建mysql语句
    # 获取指定时间段内的(U,I)
    sql_ui = "select user_id,item_id from train_user\
              where buy_time between '%s' and '%s'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_ui)
    results_ui = cur.fetchmany(execute)
    
    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()
    
    id_ui = []
    for uid in results_ui:
        i = uid[1]
        if i_dict.has_key(i):
            id_ui.append((uid[0],uid[1]))

    return id_ui

'''

'''
def GetUI_online(time_start, time_end):
    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db='MobileRec')
    cur = conn.cursor()
    
    # 先从下一天获取有那些用户有购买记录
    sql_i = "select item_id from train_item\
              group by item_id; "
              
    # 执行数据库操作
    execute = cur.execute(sql_i)
    results_i = cur.fetchmany(execute)
    
    i_dict = {}
    for i in results_i:
        i_dict[i[0]] = 0
    print 'Len(i_dict) is',len(i_dict)
    # ---------------------------------------------------------------------
    # 构建mysql语句
    # 获取指定时间段内的(U,I)
    sql_ui = "select user_id,item_id from train_user\
              where buy_time between '%s' and '%s'\
              group by user_id,item_id; "%(time_start,time_end)
              
    # 执行数据库操作
    execute = cur.execute(sql_ui)
    results_ui = cur.fetchmany(execute)
    
    # 关闭数据库
    conn.commit()
    cur.close()
    conn.close()
    
    id_ui = []
    for uid in results_ui:
        i = uid[1]
        if i_dict.has_key(i):
            id_ui.append((uid[0],uid[1]))

    return id_ui


'''
主函数
'''
if __name__ == '__main__':
    print 'start'
    time1 = time.time()
    
    time_start = '2014-12-16 01'
    time_end   = '2014-12-16 23'
    

    
    print 'Total time is ',time.time() - time1
    print 'over'

