-- Removendo a permissão de algum usuário

DELETE FROM users_roles WHERE user_id = (SELECT id FROM users WHERE email = "hudson@email.com") AND
role_id = (SELECT id FROM roles WHERE name = "PUT");