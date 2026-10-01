from app.database import Base, engine
from app.models.job_offer import JobOffer


def init_database():
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized")


if __name__ == "__main__":
    init_database()