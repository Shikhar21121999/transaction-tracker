import utility
import constants

class Entity:
    def __init__(self, data, list: bool = False) -> None:
        if list:
            self.name, self.remark = data[0], data[1]
        else:
            self.name = data.get('name')
            self.remark = data.get('remark')

    def __str__(self) -> str:
        str_obj = f"""
        Name: {self.name},
        Remark: {self.remark}
        """
        return str_obj

    def to_dict(self):
        return dict({
            'name': self.name,
            'remark': self.remark
        })

def fetch_stored_entities(raw: bool = False):
    entity_data = utility.read_json_file(constants.ENTITIES_FILE_PATH)
    if raw:
        return entity_data
    entity_objs = [Entity(raw_entity) for raw_entity in entity_data]
    return entity_objs

def show_available_entities() -> None:
    stored_entities = fetch_stored_entities()
    if len(stored_entities) == 0:
        print('No Entities present yet')
    else:
        for entity in stored_entities:
            print(entity)

def add_new_entity(ent: Entity):
    raw_entity = ent.to_dict()
    old_entities = fetch_stored_entities(raw=True)
    if old_entities is None:
        old_entities = list({})
    old_entities.append(raw_entity)
    utility.update_json_file(old_entities, constants.ENTITIES_FILE_PATH)