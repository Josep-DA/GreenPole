from .models import *
from .app_db import db


def create(table, return_: bool = False, **data):
    arguments = ""
    values = []
    n = 0
    for (name, value) in data.items():
        values.append(value)
        arguments += f"{name}=values[{n}], "
        n += 1
    item = eval(f"{table}({arguments[:-2]})")
    db.session.add(item)
    db.session.commit()
    if return_:
        return item


def get(table_name, id_):
    item = eval(f"{table_name}.query.get({id_})")
    return item


def read_by_order(table_name, col_name):
    item = eval(f'{table_name}.query.order_by({table_name}.{col_name}).all()')
    return item


def read(table_name, col_name, value):
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

