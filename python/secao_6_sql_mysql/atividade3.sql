-- Inserir permissões (roles) para os usuários inseridos

INSERT INTO users_roles (user_id, role_id) VALUES
(
    (SELECT id FROM users WHERE email = "kriv@email.com"),
    (SELECT id FROM roles WHERE name = 'PUT')
),
(
    (SELECT id FROM users WHERE email = "ruiz@email.com"),
    (SELECT id FROM roles WHERE name = 'POST')
),
(
    (SELECT id FROM users WHERE email = "thompson@email.com"),
    (SELECT id FROM roles WHERE name = 'GET')
),
(
    (SELECT id FROM users WHERE email = "luna@email.com"),
    (SELECT id FROM roles WHERE name = 'PUT')
),
(
    (SELECT id FROM users WHERE email = "hudson@email.com"),
    (SELECT id FROM roles WHERE name = 'PUT')
),
(
    (SELECT id FROM users WHERE email = "hudson@email.com"),
    (SELECT id FROM roles WHERE name = 'GET')
);
