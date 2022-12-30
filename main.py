import entity
import utility
import constants
import sys
import uuid

def fetch_transactions():
    pass

def add_new_transaction():
    pass

def add_new_entity(args):
    print(f'Adding New Entity')
    ent_obj = entity.Entity(args, list=True)
    entity.add_new_entity(ent_obj)


def show_available_entities(args):
    '''
    Fetch data of entities from storage and display them
    '''
    print('Available Entities Are As Follows:')
    entity.show_available_entities()

def help(args):
    help_message = f'''
    This is a help message,
    It is meant to make you understand how to run this project
    This might later be replaced with an interactive cli script
    For Viewing Stored Entities run with -> show_entities
    For adding a new Entity run with -> add_entity name remark
    '''
    print(help_message)
    print(args)

if __name__ == '__main__':
    print('running main function')
    func, args = sys.argv[1], sys.argv[2:]
    constants.FUNCTION_NAME_DICT[func](args)

