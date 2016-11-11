drop table if exists apps;
create table apps (
  id integer primary key autoincrement,
  title text not null,
  link text not null
);