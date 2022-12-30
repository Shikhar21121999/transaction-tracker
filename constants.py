import main
import utility

ENTITIES_FILE_PATH = r'entities.json'
TRANSACTION_FILE_PATH = r'transactions.json'

FUNCTION_NAME_DICT = {
    'help': main.help,
    'read_json_file': utility.read_json_file,
    'show_entities': main.show_available_entities,
    'add_entity': main.add_new_entity
}