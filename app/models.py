from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, Text
from sqlalchemy.orm import relationship 
from datetime import datetime
from .database import Base 

class Interview(Base):
    __tablename__ = "interviews"
        
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), unique=True, index=True, nullable=False) 
    role = Column(String(50), nullable=False) 
    difficulty = Column(String(20), nullable=False)
    started_at = Column(DateTime, default=datetime.timezone.utc) 
    completed_at = Column(DateTime, nullable=True) 
    questions = Column(JSON) 
    current_index = Column(Integer, default=0)
    
    answers = relationship("Answer", back_populates="interview")
    
class Answer(Base):
    __table__="answers"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), ForeignKey("interviews.session_id"), nullable=False)
    question_id = Column(Integer, nullable=False)
    question_text = Column(Text) 
    answer_text = Column(Text) 
    time_taken = Column(Integer)
    submitted_at = Column(DateTime, default=datetime.timezone.utc) 
    ai_score = Column(Integer, nullable=True) #(we'll add this later)
    ai_feedback = Column(Text, nullable=True)
    
    interview = relationship("Interview", back_populates="answers")
    
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50), index=True, nullable=False)
    difficulty = Column(String(20), index=True, nullable=False)
    question_type = Column(String(50))
    question_text = Column(Text, nullable=False)
    category = Column(String(100)) 