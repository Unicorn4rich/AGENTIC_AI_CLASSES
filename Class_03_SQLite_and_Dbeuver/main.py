from sqlalchemy import create_engine, text


# Database file name
DB_FILE = "myTest.db"
# Create an SQLite engine connected to the real database
engine = create_engine(f"sqlite:///{DB_FILE}") # is naam ke database ko bnao


#1.Tables Create
# (with) ye database open or close karta hai or database ko open kar ke us se connection bnata hai.
with engine.connect() as conn: 
    conn.execute(text(           # ye sql query ko execute karta hai.
        """ 
        CREATE TABLE IF NOT EXISTS person_table( 
            id      INTEGER      PRIMARY KEY    AUTOINCREMENT,
            name   VARCHAR(25)    NOT NULL,
            age     INTEGER
        );
        """
    ))
    

#2. Insert Data    
# with engine.connect() as conn:
#     conn.execute(text(
#         """
#         INSERT INTO person_table
#         (name, age)
#         VALUES
#         ('Shoaib', 23),
#         ('Shahzaib', 21),
#         ('Awais', 13),
#         ('Ahmed', 20);
#         """
#     ))
#     conn.commit()
    
    
#3. Delete Data    
# with engine.connect() as conn:
#     conn.execute(text(
#         """
#         DELETE FROM person_table WHERE id = 2;
#         """
#     ))
#     conn.commit()    
    
 
#4. Update Data 
with engine.connect() as conn:
    conn.execute(text(
        """
        UPDATE person_table
        SET name = 'Alex'
        WHERE id = 3;
        """
    ))
    conn.commit()    