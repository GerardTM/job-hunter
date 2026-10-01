from app.database import Base, engine


def test_database_connection():
    Base.metadata.create_all(bind=engine)

    with engine.connect() as connection:
        assert connection is not None