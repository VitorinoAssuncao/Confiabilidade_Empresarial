from enterprise_api.models.enterprise_models import Enterprise
from database.database import save
from database.database import commit

def create(data:dict) -> Enterprise:
    return save(
        Enterprise(
            name_enterprise = data['name_enterprise'],
            actual_confiability = 50
        )
    )