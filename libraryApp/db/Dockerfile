FROM mysql/mysql-server
ADD ./book.sql  /docker-entrypoint-initdb.d

EXPOSE 3306

CMD ["mysqld"]
