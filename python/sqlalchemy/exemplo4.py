# Criação de metadados

import sqlalchemy as sa

# Construtor dos metadados da tabela
metadata = sa.MetaData()

# Construindo a tabela e passando os metadados dela
t = sa.Table(
    "comments", metadata,
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("name", sa.String(), nullable=False),
    sa.Column("comment", sa.String(), nullable=False),
    sa.Column("live", sa.String(), nullable=False),
    sa.Column("created_at", sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint("id")
)