CREATE TABLE user (
  user_id bigint NOT NULL PRIMARY KEY,
  user_xp bigint,
  user_balance bigint,
  total_activity_complete int
);

CREATE TABLE ranking_levels (
  role_id bigint NOT NULL PRIMARY KEY,
  xp_requirement bigint NOT NULL
);

CREATE TABLE infraction_type (
  inf_type_id int NOT NULL PRIMARY KEY,
  inf_type_name varchar(32) NOT NULL,
  inf_type_worth int NOT NULL
);

CREATE TABLE infractions (
  inf_id bigint NOT NULL PRIMARY KEY,
  user_id bigint NOT NULL,
  inf_type_id int NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id),
  FOREIGN KEY (inf_type_id) REFERENCES infraction_type(inf_type_id)
);

CREATE TABLE reputation (
  rep_id bigint NOT NULL PRIMARY KEY,
  rep_date date NOT NULL,
  rep_reason tinytext NOT NULL,
  user_id bigint NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE boost_type (
  boost_type_id int NOT NULL PRIMARY KEY,
  boost_type_name varchar(32) NOT NULL,
  boost_type_multi_allowed BOOL NOT NULL
);

CREATE TABLE boost_affect (
  boost_affect_id int NOT NULL PRIMARY KEY,
  boost_affect_type varchar(32) NOT NULL
);

CREATE TABLE boost (
  boost_id int NOT NULL PRIMARY KEY,
  boost_amount float NOT NULL,
  boost_expire dateTIME,
  boost_type_id int NOT NULL,
  boost_affect_id int NOT NULL,
  user_id bigint NOT NULL,
  FOREIGN KEY (boost_type_id) REFERENCES boost_type(boost_type_id),
  FOREIGN KEY (boost_affect_id) REFERENCES boost_affect(boost_affect_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE user_boost (
  user_boost_id bigint NOT NULL PRIMARY KEY,
  boost_id int NOT NULL,
  user_id bigint NOT NULL,
  FOREIGN KEY (boost_id) REFERENCES boost(boost_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE item_category (
  item_category_id int NOT NULL PRIMARY KEY,
  item_category_name varchar(32) NOT NULL
);

CREATE TABLE item (
  item_id int NOT NULL PRIMARY KEY,
  item_name varchar(32) NOT NULL,
  item_category_id int NOT NULL
  sell_worth int,
  FOREIGN KEY (item_category_id) REFERENCES item_category(item_category_id)
);

CREATE TABLE inventory (
  inv_id bigint NOT NULL PRIMARY KEY,
  user_id bigint NOT NULL,
  item_id int NOT NULL,
  item_count int NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id),
  FOREIGN KEY (item_id) REFERENCES item(item_id)
);

CREATE TABLE achievement (
  achievement_id int NOT NULL PRIMARY KEY,
  achievement_name varchar(32) NOT NULL
);

CREATE TABLE user_achievement (
  user_achieve_id bigint NOT NULL PRIMARY KEY,
  user_id bigint NOT NULL,
  achievement_id int NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id),
  FOREIGN KEY (achievement_id) REFERENCES achievement(achievement_id)
);

CREATE TABLE activity (
  activity_id int NOT NULL PRIMARY KEY,
  activity_name varchar(32) NOT NULL,
);

CREATE TABLE active_activity (
  active_activity bigint NOT NULL PRIMARY KEY,
  activity_id int NOT NULL,
  user_id bigint NOT NULL,
  complete bool NOT NULL,
  FOREIGN KEY (activity_id) REFERENCES activity(activity_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE fish (
  fish_id int NOT NULL PRIMARY KEY,
  item_id int NOT NULL,
  FOREIGN KEY (item_id) REFERENCES item(item_id)
);
