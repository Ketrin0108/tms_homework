CREATE DATABASE chat;
use chat;

create table users (
    id int not null AUTO_INCREMENT,
    username varchar(18) NOT NULL UNIQUE,
    password varchar(16) NOT NULL,
    PRIMARY KEY (id)
);

create table messages (
    id int not null AUTO_INCREMENT,
    text TEXT,
    created_at DATETIME,
    PRIMARY KEY (id)
);

create table user_messages (
    id int not null AUTO_INCREMENT,
    from_user INT NOT NULL,
    to_user INT NOT NULL,
    message_id INT NOT NULL,
    is_read bool,
	FOREIGN KEY (from_user) REFERENCES users(id),
    FOREIGN KEY (to_user) REFERENCES users(id),
    FOREIGN KEY (message_id) REFERENCES messages(id),
	PRIMARY KEY (id)
);


create table followers (
    id int not null AUTO_INCREMENT,
    user_id INT NOT NULL,
    follower_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (follower_id) REFERENCES users(id),
    PRIMARY KEY (id)
);

insert into users (username, password) values ('Sergey', '12345');
insert into users (username, password) values ('Alesya', '12345');
insert into users (username, password) values ('Katya', '12345');

insert into messages (text, created_at) values ('Привет, как дела?', NOW());

insert into user_messages (from_user, to_user, message_id) values (1, 2, 1);
insert into user_messages (from_user, to_user, message_id) values (1, 3, 1);

SELECT *
FROM users u
JOIN user_messages um ON u.id = um.from_user
JOIN messages m ON um.message_id = m.id;

SELECT count(user_id)
FROM followers
GROUP BY user_id;

insert into users (username, password) values ('Kira', '23456');
insert into users (username, password) values ('Lena', '12345');
insert into users (username, password) values ('Roma', '12345');
insert into users (username, password) values ('Artsiom', '12345');

insert into followers (user_id, follower_id) values (1, 2);
insert into followers (user_id, follower_id) values (1, 3);
insert into followers (user_id, follower_id) values (1, 4);
insert into followers (user_id, follower_id) values (1, 5);
insert into followers (user_id, follower_id) values (3, 5);
insert into followers (user_id, follower_id) values (3, 6);
insert into followers (user_id, follower_id) values (7, 1);

SELECT count(user_id)
FROM followers
GROUP BY user_id;

SELECT u.username,
count(f.follower_id) AS num_followers
FROM users u
LEFT JOIN followers f ON u.id=f.follower_id
GROUP BY u.id
ORDER BY num_followers DESC LIMIT 1;

SELECT u.username,
count(f.follower_id) AS num_followers
FROM users u
LEFT JOIN followers f ON u.id=f.follower_id
GROUP BY u.id
having count(f.follower_id)<1;

SELECT * FROM users WHERE id=1;

insert into messages (text, created_at) values ('Привет, что ты делаешь?', NOW());

insert into user_messages (from_user, to_user, message_id) values (3, 4, 2);
insert into user_messages (from_user, to_user, message_id) values (3, 5, 2);

SELECT m.id, m.text, um.to_user, um.is_read
FROM messages m
JOIN user_messages um  ON m.id= um.id
WHERE um.to_user= 2 and is_read=1;

UPDATE user_messages
SET is_read = 1
WHERE id = 1;


UPDATE user_messages
SET is_read = 0
WHERE id = 3;

UPDATE user_messages
SET is_read = 0
WHERE id = 2;

UPDATE user_messages
SET is_read = 0
WHERE id = 4;

SELECT u.username, um.message_id, um.is_read
FROM users u
JOIN user_messages um  ON u.id= um.to_user
WHERE is_read=0;

insert into user_messages (from_user, to_user, message_id) values (1, 2, 2);

UPDATE user_messages
SET is_read = 1
WHERE id = 5;


SELECT um.from_user,um.to_user,um.is_read,m.text,m.created_at
FROM user_messages um
LEFT JOIN messages m  ON um.message_id= m.id
WHERE um.from_user=1 and um.to_user=2
ORDER BY m.created_at ASC;

SELECT u.username,
count(um.to_user) AS num_of_messages
FROM users u
JOIN user_messages um  ON u.id=um.to_user
GROUP BY u.id
ORDER BY num_of_messages DESC LIMIT 1;

SELECT AVG(message_id) AS average_messages
FROM user_messages;