from database.database import db

class Enterprise(db.Model):
    __tablename__ = 'enterprises'
    id_enterprise = db.Column(db.Integer,primary_key=True)
    name_enterprise = db.Column(db.String,nullable=False)
    actual_confiability = db.Column(db.Integer,nullable=True)

    def __init__(self,**args):
        super(Enterprise,self).__init__(**args)

    def serialize(self) -> dict:
        return{
            'id_enterprise' : self.id_enterprise,
            'name_enterprise' : self.name_enterprise,
            'actual_confiability' : self.actual_confiability
        }
