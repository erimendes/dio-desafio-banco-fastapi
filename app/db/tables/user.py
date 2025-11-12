# app/db/tables/user.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    client = relationship("Client", back_populates="user", uselist=False)
    # full_name = Column(String, nullable=True)   
    # is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    # is_superuser = Column(Integer, default=0)  # 1 for superuser, 0 for regular user    
    # created_at = Column(String, nullable=False)
    # updated_at = Column(String, nullable=True)  
    # last_login = Column(String, nullable=True)
    # profile_picture = Column(String, nullable=True)
    # bio = Column(String, nullable=True)
    # location = Column(String, nullable=True)
    # website = Column(String, nullable=True)
    # phone_number = Column(String, nullable=True)
    # date_of_birth = Column(String, nullable=True)
    # gender = Column(String, nullable=True)
    # language = Column(String, nullable=True)
    # timezone = Column(String, nullable=True)
    # preferences = Column(String, nullable=True)
    # security_question = Column(String, nullable=True)
    # security_answer = Column(String, nullable=True)     
    # two_factor_enabled = Column(Integer, default=0)  # 1 for enabled, 0 for disabled
    # last_password_change = Column(String, nullable=True)
    # failed_login_attempts = Column(Integer, default=0)
    # account_locked_until = Column(String, nullable=True)
    # roles = Column(String, nullable=True)  # Comma-separated roles
    # permissions = Column(String, nullable=True)  # Comma-separated permissions
    # notes = Column(String, nullable=True)
    # tags = Column(String, nullable=True)  # Comma-separated tags
    # external_id = Column(String, nullable=True)  # For linking with external systems
    # metadata = Column(String, nullable=True)  # JSON string for additional metadata
    # last_modified_by = Column(String, nullable=True)
    # created_by = Column(String, nullable=True)
    # deleted_at = Column(String, nullable=True)
    # recovery_email = Column(String, nullable=True)
    # recovery_phone = Column(String, nullable=True)
    # marketing_opt_in = Column(Integer, default=0)  # 1 for opted-in, 0 for opted-out
    # terms_accepted = Column(Integer, default=0)  # 1 for accepted, 0 for not accepted   
    # privacy_accepted = Column(Integer, default=0)  # 1 for accepted, 0 for not accepted 
    # data_sharing_consent = Column(Integer, default=0)  # 1 for consented, 0 for not consented
    
    # def __repr__(self):
    #     return f"<User(username={self.username}, email={self.email})>"  
    