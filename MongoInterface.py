import pymongo
import json


def get_private_value(val_name):
    """
    Gets a value from the private
    :param val_name: name of private value to retrieve
    :return: string containing private value
    """
    f = open("private_values.json")
    priv_str = f.read()
    f.close()
    ret_dict = json.loads(priv_str)
    return ret_dict[val_name]


def get_mongo_pw():
    """
    Gets MongoDB password from private values
    :return: password string for MongoDB
    """
    return get_private_value("mongo_pw")


def connect_to_database():
    """
    Connects to database
    :return: Database object
    """
    pw = get_private_value("mongo_pw")
    db_name = get_private_value("db_name")
    conn_str = "mongodb+srv://derekcapone7:{}@restful-db-fugmi.mongodb.net/{}?retryWrites=true&w=majority".format(pw, db_name)
    client = pymongo.MongoClient(conn_str)
    return client[db_name]


def connect_to_collection(col_name):
    """
    Connect to desired collection within database
    :param col_name: name of the collection
    :return: collection object
    """
    db = connect_to_database()

    col_name = get_private_value("collection")
    return db[col_name]


def find_top_layer_obj(collection, obj_name):
    """
    Takes collection and searches it for the top layer object named "obj_name"
    :param collection: MongoDB Collection object to search
    :param obj_name: String containing the top layer object name
    :return: Dict containing the entire top layer object of name "obj_name"
    """
    search_dic = {obj_name: {"$exists": True}}
    return list(collection.find(search_dic))


def insert_document(collection, new_dict):
    """
    Inserts a single document into the collection provided
    :param collection: MongoDB Collection object
    :param new_dict: dict to be inserted into collection
    :return: Resulting InsertOneResult object
    """
    return collection.insert_one(new_dict)


if __name__ == "__main__":
    col = connect_to_collection("PeopleData")

    dicti = find_top_layer_obj(col, "name")

    print(dicti)