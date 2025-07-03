-- Inserir 5 usuários novos

INSERT INTO users (first_name, last_name, email, password_hash) VALUES
("Kristoff", "Kriv", "kriv@email.com", round(rand() * 10000)),
("Stefan", "Ruiz", "ruiz@email.com", round(rand() * 10000)),
("Willey", "Thompson", "thompson@email.com", round(rand() * 10000)),
("Anne", "Luna", "luna@email.com", round(rand() * 10000)),
("Hurley", "Hudson", "hudson@email.com", round(rand() * 10000));


UPDATE users SET salary = ROUND(RAND() * 10000, 2) WHERE id IN (111, 110, 109, 108, 107);
