from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    filtered_users = set()

    # Checks and add user by id immediately if provided
    if 'id' in args:
        for user in USERS:
            if user['id'] == args['id']:
                filtered_users.add(tuple(user.items()))
                break

    # Filters by name if provided
    if 'name' in args:
        name_query = args['name'].lower()
        for user in USERS:
            if name_query in user['name'].lower():
                filtered_users.add(tuple(user.items()))

    # Filters by age range if provided
    if 'age' in args:
        age_query = int(args['age'])
        for user in USERS:
            if age_query - 1 <= user['age'] <= age_query + 1:
                filtered_users.add(tuple(user.items()))

    # Filters by occupation if provided
    if 'occupation' in args:
        occupation_query = args['occupation'].lower()
        for user in USERS:
            if occupation_query in user['occupation'].lower():
                filtered_users.add(tuple(user.items()))

    # Converts the set of tuples back to list of dictionaries
    return [dict(user) for user in filtered_users]
