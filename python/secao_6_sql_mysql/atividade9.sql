-- Selecione usuários com perfis e permissões (opcional)

SELECT u.id as uid, u.first_name, r.name, p.bio FROM users u
LEFT JOIN users_roles ur ON u.id = ur.user_id
LEFT JOIN roles r ON ur.role_id = r.id
LEFT JOIN profiles p ON p.user_id = u.id;