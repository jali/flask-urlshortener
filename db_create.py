from coreapp import db
from coreapp.models import Short

db.drop_all()
db.create_all()
db.session.add(Short("1", "http://google.co.uk"))
db.session.add(Short("2", "http://amazon.co.uk"))
db.session.commit()