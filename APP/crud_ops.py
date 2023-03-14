from .models import *
from .setups import db


def create_user(table, firstname, lastname, username, email, password):
    item = eval(f"{table}(firstname=firstname, lastname=lastname, username=username, email=email, password=password)")
    db.session.add(item)
    db.session.commit()


def get(table_name, id_):
    item = eval(f"{table_name}.query.get({id_})")
    return item


def read_by_order(table_name, col_name):
    item = eval(f'{table_name}.query.order_by({table_name}.{col_name}).all()')
    return item


def read(table_name, col_name, value, all_: bool = False):
    if all_:
        if '\'' in value:
            value = value.replace('\'', "\\'")
        item = eval(f"{table_name}.query.filter_by({col_name}='{value}').all()")
        return item
    else:
        if '\'' in value:
            value = value.replace('\'', "\\'")
        item = eval(f"{table_name}.query.filter_by({col_name}='{value}').first()")
        return item


def read_all(table_name):
    return eval(f'db.session.query({table_name}).all()')


def update(item, **attrs):
    """ attr: value """
    for (attr, value) in attrs.items():
        if '\'' in value:
            value = value.replace('\'', "\\'")

        exec(f"item.{attr} = value")
    db.session.commit()


def del_(item, commit: bool = True):
    db.session.delete(item)
    if commit:
        db.session.commit()


def make_list(table_name):
    data_list = read_all(table_name)
    item_info: dict
    n = 0
    for item in data_list:
        exec(f"item: {table_name}")
        data_list[n] = item.to_dict()
        n += 1
    return data_list
