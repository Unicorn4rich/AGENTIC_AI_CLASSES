# Import kar rahe hain zaroori libraries
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv



# .env file load kar rahe hain
load_dotenv()

# DATABASE_URL ko environment se read kar rahe hain
DATABASE_URL = os.getenv("DATABASE_URL_UNPOOLED")

# SQLAlchemy engine create kar rahe hain
engine = create_engine(DATABASE_URL)

user_list = []

def main():
    with engine.connect() as conn:
        conn.execute(text(
            """ 
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
            """
        ))
        conn.commit()
        
        
        # # Optional: Sample data insert karne ke liye (commented by default)
        # conn.execute(text(
        #     """
        #     INSERT INTO users 
        #     (name, email)
        #     VALUES 
        #     ('Shoaib', 'shobi@example.com'),
        #     ('Ahmed', 'ahmed@example.com');
        #     """
        # ))
        # conn.commit()
        
        # Data fetch kar rahe hain Database se.
        result = conn.execute(text("SELECT * FROM users;")).mappings()
        
        for row in result: # loop laga kar aik aik kar ke data get kar rhy hain.
            user_list.append(dict(row)) # Row ko dictionary mein convert karke print kar rahe hain.
            
        print("🤑", user_list) # Final list ko print kar rahe hain.
        
        
        
        
if __name__ == "__main__":
    main()        