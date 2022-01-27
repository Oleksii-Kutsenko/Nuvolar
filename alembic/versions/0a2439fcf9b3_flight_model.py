"""Flight model

Revision ID: 0a2439fcf9b3
Revises: f1513f9d6737
Create Date: 2022-01-26 23:03:38.802951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0a2439fcf9b3'
down_revision = 'f1513f9d6737'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('aircraft_serial_number', sa.String(), nullable=True),
    sa.Column('arrival', sa.DateTime(timezone=True), nullable=True),
    sa.Column('arrival_airport', sa.String(length=4), nullable=True),
    sa.Column('departure', sa.DateTime(timezone=True), nullable=True),
    sa.Column('departure_airport', sa.String(length=4), nullable=True),
    sa.CheckConstraint('departure < arrival'),
    sa.CheckConstraint('departure > CURRENT_TIMESTAMP'),
    sa.ForeignKeyConstraint(['aircraft_serial_number'], ['aircrafts.serial_number'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flights')
    # ### end Alembic commands ###
