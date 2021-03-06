"""empty message

Revision ID: 12552e0f37fd
Revises: 
Create Date: 2022-04-06 18:23:57.726440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12552e0f37fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('director',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('film',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('date', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('film_categories',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], )
    )
    op.create_table('film_countries',
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], )
    )
    op.create_table('film_directors',
    sa.Column('directors_id', sa.Integer(), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['directors_id'], ['director.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('film_directors')
    op.drop_table('film_countries')
    op.drop_table('film_categories')
    op.drop_table('film')
    op.drop_table('director')
    op.drop_table('country')
    op.drop_table('category')
    # ### end Alembic commands ###
