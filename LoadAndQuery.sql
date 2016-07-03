
## ------------------------------------------- 创建表 --------------------------------------------------
create table train_item(
	item_id varchar(10),
	item_geohash varchar(10),
	item_category varchar(8)
);

create table train_user(
	user_id varchar(10),
	item_id varchar(10),
	behavior_type varchar(2),
	user_geohash varchar(10),
	item_category varchar(10),
	buy_time varchar(15)
);



## --------------------------------- 导入数据 -------------------------------------------

## 导入之前
mysql --local-infile=1 -u username -p `

# Then run the LOAD DATA LOCAL INFILE command again. 


LOAD DATA LOCAL INFILE '/tmp/train_item.csv'   
INTO TABLE train_item
CHARACTER SET utf8
FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'   
LINES TERMINATED BY '\r\n';


LOAD DATA LOCAL INFILE '/home/learning_resource/machine_learning/resource/MobileRecommendation/fresh_comp_offline/train_user.csv'   
INTO TABLE train_user
CHARACTER SET utf8
FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'   
LINES TERMINATED BY '\n';


## ------------------------------------ 创建索引 -------------------------------------------------

create index idx_u on train_user(user_id);
create index idx_i on train_user(item_id);
create index idx_t on train_user(buy_time);
create index idx_b on train_user(behavior_type);
create index idx_c on train_user(item_category);

create index idx_ui on train_user(user_id,item_id);

## -------------------------------------- 查询 --------------------------------------------------

select user_id,item_id,count(*) from train_user
where buy_time > '2014-12-17 02' and
      buy_time <  '2014-12-17 23' and
      behavior_type = '3' and behavior_type = '4'
group by user_id,item_id;

select user_id,item_id from train_user
where buy_time = '2014-12-17 03'
group by user_id,item_id;

select user_id,item_id,buy_time from train_user
where buy_time > '2014-12-16 23' and
      buy_time <  '2014-12-17 00'
group by user_id,item_id
order by buy_time
limit 0,100;

explain select user_id,item_id,buy_time from train_user
where buy_time between '2014-12-18 22' and '2014-12-19 00'
group by user_id,item_id
limit 0,100;


select count(*) from train_user
where buy_time between '2014-12-08 23' and '2014-12-09 23';





