from selene.support.jquery_style_selectors import s


class UserTable(object):
    def __init__(self):
        self.table = s("#users_table")

    def user_names(self):
        return self.table.ss("tbody > tr > td:nth-child(2)")
