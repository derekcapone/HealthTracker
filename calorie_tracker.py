from datetime import datetime
import mongo_interface as mng

def get_current_datestamp():
    """
    Get current datestamp
    :return: String  of current date in YYYY-MM-DD format
    """
    return datetime.now().strftime("%Y-%m-%d")


def get_person_calories(name):
    """
    Gets calorie data for the given person
    :param name: Name of person to get calorie data for
    :return: Object containing all info in calorie data query
    """
    # connect to collection
    col = mng.connect_to_collection("PeopleData")

    dict_query = {"name": name}
    cal_data = mng.find_populated_field(col, dict_query)

    if len(cal_data) == 0:
        print("Cannot find entry in database")

    return cal_data


def update_person_calories(name, calories, datestamp=None):
    """
    Updates the calories for a person on a given day
    :param name: Name of person in database to update
    :param calories: Number of calories to log for given date
    :param datestamp: datestamp of date to add calories (format: YYYY-MM-DD)
    """
    # if date isn't specified, log for today
    if datestamp is None:
        datestamp = get_current_datestamp()

    # connect to collection
    col = mng.connect_to_collection("PeopleData")

    # set up queries
    name_query = {"name": name}
    calstring = "Calories.{}".format(datestamp)
    newvalues = {"$set": {calstring: calories}}

    # update document in collection
    col.update_one(name_query, newvalues)


if __name__ == "__main__":
    update_person_calories("Peter", 542156)

