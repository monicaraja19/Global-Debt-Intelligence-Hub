from sqlalchemy import create_engine

def getDBConnection():
    db_engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/global_debt_intelligence_hub")
    return db_engine

    
    
    