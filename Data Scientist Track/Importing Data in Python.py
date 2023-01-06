from sqlalchemy import create_engine
import pandas as pd

# Using sqlalchemy
engine = create_engine('sqlite:///_____')
con = engine.connect()
rs = con.execute("SELECT * FROM _____")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
con.close()


# Using the context manager
engine = create_engine('sqlite:///_____')

with engine.connect() as con:
    rs = con.execute('SELECT ____, ____, ____')
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()
