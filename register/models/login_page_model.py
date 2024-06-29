""" """

def user_sign_in(model, username, password)-> list:
    # select user_info from the database in talbe employee where username and password are equal to the given username and password
    sql_cmd = model.sql_cmd["user_sign_in"]
    data = (username, password)
    login_info = model.select_login_data(sql_cmd, data)
    return login_info