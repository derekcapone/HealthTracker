from datetime import datetime
import json


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_people(file_name):
    """
    Reads json file
    :return: dict of json file
    """
    f = open(file_name)
    file_text = f.read()
    f.close()
    return json.loads(file_text)


# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    people_dict = get_people("people.json")
    return people_dict


def add_person(fname, lname):
    # Get dict from file
    file_name = "people.json"
    people_dict = get_people(file_name)

    # Generate new dict and append to dict
    new_dict = {'fname': fname, 'lname': lname}
    people_dict["people"][lname] = new_dict
    new_dict_str = json.dumps(people_dict, indent=4, sort_keys=True)

    f = open(file_name, "w+")
    f.write(new_dict_str)
    f.close()

    return "{} {} added".format(fname, lname)


if __name__ == "__main__":
    new_str = add_person("Derek", "Capone")
    print(new_str)
