-- Create Database and User

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT TO 'user_0d_2'@'localhost' ON hbtn_0d_2.*;
