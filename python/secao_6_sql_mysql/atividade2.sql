-- Insira 5 perfis para os usuários inseridos

INSERT INTO profiles (bio, description, user_id) VALUES
("Uma bio", "Uma description", (SELECT id FROM users WHERE email = "kriv@email.com")),
("Uma bio", "Uma description", (SELECT id FROM users WHERE email = "ruiz@email.com")),
("Uma bio", "Uma description", (SELECT id FROM users WHERE email = "thompson@email.com")),
("Uma bio", "Uma description", (SELECT id FROM users WHERE email = "luna@email.com")),
("Uma bio", "Uma description", (SELECT id FROM users WHERE email = "hudson@email.com"));