import utility
import constants

class Transaction:
    def __init__(self, data, list: bool = False) -> None:
        if list:
            self.sender, self.receiver, self.date, self.amount, self.remark = data
        else:
            self.sender = data.get('sender')
            self.receiver = data.get('receiver')
            self.date = utility.get_date_from_str(data.get('date'))
            self.amount = data.get('amount')
            self.remark = data.get('remark', None)

    def __str__(self) -> str:
        str_obj = f"""
            'sender': {self.sender},
            'receiver': {self.receiver},
            'date': {self.date.strftime('%x')},
            'amount': {self.amount},
            'remark': {self.remark},
        """
        return str_obj

    def to_dict(self):
        return dict({
            'sender': self.sender,
            'receiver': self.receiver,
            'date': self.date.strftime('%x'),
            'amount': self.amount,
            'remark': self.remark,
        })

def fetch_stored_transactions(raw: bool = False):
    trans_data = utility.read_json_file(constants.TRANSACTION_FILE_PATH)
    if raw:
        return trans_data
    trans_objs = [Transaction(raw_trans) for raw_trans in trans_data]
    return trans_objs

def filter_trans(entity_name: str):
    all_transactions = fetch_stored_transactions()
    trans_to_ent = [x for x in all_transactions if x.name == entity_name]
    return trans_to_ent

def filter_trans(st: str, end: str):
    st_dt = utility.get_date_from_str(st)
    en_dt = utility.get_date_from_str(end)
    all_transactions = fetch_stored_transactions()
    trans_in_period = [x for x in all_transactions if x.date >= st_dt and x.date <= en_dt]
    return trans_in_period

def show_available_transaction(args) -> None:
    valid_trans = filter_trans(args)
    if len(valid_trans) == 0:
        print('No transactions present')
    else:
        valid_trans.sort(key=lambda r: r.trans.date)
        for trans in valid_trans:
            print(trans)

def add_new_trans(tr: Transaction):
    raw_tr = tr.to_dict()
    old_tr_rec = fetch_stored_transactions(raw=True)
    if old_tr_rec is None:
        old_tr_rec = list({})
    old_tr_rec.append(raw_tr)
    utility.update_json_file(old_tr_rec, constants.TRANSACTION_FILE_PATH)


raw_transactions_list = {}
for x in range(1, 10):
    raw_trans = {
        "sender": f"send{x}",
        "receiver": f"resc{x}",
        "date": f"12/01/22",
        "amount": null,
        "remark": null
    }

    month, date, year