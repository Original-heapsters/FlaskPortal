drop table if exists apps;
create table apps (
  id integer primary key autoincrement,
  title text not null,
  link text not null
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username text not null,
  password text not null,
  subscriptions text,
  rejections text
);

insert into users VALUES (0,'user','pass','0','0')