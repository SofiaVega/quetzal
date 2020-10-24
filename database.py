from pony import orm

db = orm.Database()
class User(db.Entity):
   username = orm.Required(str)
   password = orm.Required(str)

orm.set_sql_debug(True)
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

with orm.db_session:
    p1 = User(username='Sofia_Soto', password='hola')
    p2 = User(username='Eduardo_Larios', password='1234')




