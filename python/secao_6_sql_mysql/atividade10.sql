-- Selecione usuários com perfis e permissões ordenando por salário por ordem decrescente

SELECT u.id as uid, u.first_name, r.name, p.bio, u.salary FROM users u
INNER JOIN users_roles ur ON u.id = ur.user_id
INNER JOIN roles r ON ur.role_id = r.id
INNER JOIN profiles p ON p.user_id = u.id
ORDER BY u.salary DESC;