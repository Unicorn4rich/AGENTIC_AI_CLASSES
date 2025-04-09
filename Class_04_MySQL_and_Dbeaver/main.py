from sqlalchemy import create_engine, text


# MySQL Connection Details
USER = 'root'               # Username
PASSWORD = 'shoaibsql'       # Password
HOST = 'localhost'          # Local Server
DB_NAME = 'school'          # Target Database


# Establish SQLAlchemy Engine
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")


with engine.connect() as conn:
    conn.execute(text(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            age INT 
        );
        """
    ))
    
    
    
    
with engine.connect() as conn:
    conn.execute(text(
        """
        INSERT INTO students 
        (name, age) 
        VALUES
        ('azlaan', 1.1)
        """
    ))   
    conn.commit() 
    
    
    