-- HEALTH TRACKING APP

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(100) NOT NULL,
    email_id VARCHAR(100) NOT NULL UNIQUE,
    phone_no VARCHAR(20) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    reminder_time TIME NOT NULL,
    points INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE habit_template(
    template_id INT PRIMARY KEY AUTO_INCREMENT,
    template_name VARCHAR(100) NOT NULL
);

CREATE TABLE habit_category(
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE habit(
    habit_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    habit_name VARCHAR(200) NOT NULL,
    template_id INT,
    category_id INT NOT NULL,
    description TEXT,
    goal VARCHAR(100) NOT NULL,
    frequency ENUM('Daily','Weekly','Monthly'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (template_id) REFERENCES habit_template(template_id),
    FOREIGN KEY (category_id) REFERENCES habit_category(category_id)
);

CREATE TABLE rewards (
    reward_id INT PRIMARY KEY AUTO_INCREMENT,
    reward_title VARCHAR(100) NOT NULL,
    criteria_type ENUM('streak','points','level'),
    criteria_points INT NOT NULL,
    description TEXT NOT NULL,
    reward_type ENUM('badge','level','milestone')
);

CREATE TABLE user_rewards (
    user_reward_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    reward_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (reward_id) REFERENCES rewards(reward_id)
);

CREATE TABLE habit_log( 
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    habit_id INT NOT NULL UNIQUE,
    log_date DATE NOT NULL UNIQUE,
    status BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
);

CREATE TABLE reminder(
    reminder_id INT PRIMARY KEY AUTO_INCREMENT,
    habit_id INT NOT NULL,
    reminder_time TIME,
    frequency ENUM('Daily','Weekly','Monthly'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
);

CREATE TABLE notification (
    notification_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    type ENUM('reward','connection_request','connection_accept'),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE journal (
    journal_id INT PRIMARY KEY AUTO_INCREMENT,
    habit_id INT NOT NULL,
    content TEXT,
    mood ENUM('Active','Lazy','Motivated','Feeling Low','Dizzy'),
    challenges_faced TEXT,
    obstacles TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
);

CREATE TABLE connection(
    connection_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    friend_id INT NOT NULL,
    status ENUM('Pending','Accepted','Rejected','Blocked'),
    connected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (friend_id) REFERENCES users(user_id)
);

CREATE TABLE community(
    community_id INT PRIMARY KEY AUTO_INCREMENT,
    community_name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (created_by) REFERENCES users(user_id)
);

CREATE TABLE community_member(
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    community_id INT NOT NULL,
    user_id INT NOT NULL,
    status ENUM('Pending','Member','Rejected'),
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (community_id) REFERENCES community(community_id)
);

CREATE TABLE post (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    community_id INT,
    user_id INT NOT NULL,
    content TEXT,
    type ENUM('journal','badge','level_completion','milestone_achievement'),
    reward_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (community_id) REFERENCES community(community_id),
    FOREIGN KEY (reward_id) REFERENCES user_rewards(user_reward_id)
);

CREATE TABLE comment(
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);

CREATE TABLE IF NOT EXISTS user_bonus(
    bonus_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    habit_id INTEGER NOT NULL,
    bonus_type TEXT CHECK(bonus_type in ('streak','weekly'))
    bonus_date DATE NOT NULL,

    UNIQUE(user_id,habit_id,bonus_date,bonus_type)

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
);