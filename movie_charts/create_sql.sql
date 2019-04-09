-- 标题 图片 主演 上映时间 评分

create table movie_charts(
    id int not null auto_increment,
    title varchar(64) not null,
    picture varchar(256),
    actors varchar(256),
    release_date varchar(128),
    score decimal,
    primary key(id)
)default charset=utf8;
