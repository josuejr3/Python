-- Remova um usuário qee tem permissão "PUT"

DELETE u from users u
INNER JOIN users_roles ur ON u.id = ur.user_id
INNER JOIN roles r on ur.role_id = r.id
WHERE r.name = "PUT" AND u.id = 110;
