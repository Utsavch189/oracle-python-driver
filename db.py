from dbsettings import CONN_STRING
import cx_Oracle

CONNECTION=cx_Oracle.connect(CONN_STRING)

cur=CONNECTION.cursor()

name='souravconn'

cur.execute(f"""
INSERT INTO STUDENT VALUES(
    '{name}'
)
""")
CONNECTION.commit()
cur.close()
CONNECTION.close()