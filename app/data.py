import sqlite3
# import os


class DB():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self._create_connection(self.db_file)
        self._create_shirts_table()


    def commit(self):
        self.conn.commit()


    def _create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file.  The database will be created if it doesn't exist.
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

        return None


    def commit(self):
        self.conn.commit()


    def _create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)


    def _create_shirts_table(self):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :return:
        """
        create_table_sql = """ CREATE TABLE IF NOT EXISTS shirts (
                                                id integer PRIMARY KEY,
                                                snippet text,
                                                last_updated text,
                                                added text
                                            ); """

        self._create_table(create_table_sql)


    def insert_snippet(self, snippet):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO shirts(snippet,last_updated,added) VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, snippet.addlist())
        return cur.lastrowid


    class shirt():
        def __init__(self):
            self.id = None
            self.snippet = None
            self.last_updated = None
            self.added = None

        def __init__(self, id, snippet, last_updated, added):
            self.id = id
            self.snippet = snippet
            self.last_updated = last_updated
            self.added = added

        def addlist(self):
            return (self.snippet, self.last_updated, self.added)

        def __str__(self):
            return 'snippet: ' + str(self.id) + '|' + self.snippet + '|' + str(self.last_updated) + '|' + str(self.added)




def _create_tasks_table(self):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :return:
    """
    create_table_sql = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""
    self._create_table(create_table_sql)


def _insert_task(self, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?) '''
    cur = self.conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def _select_all_tasks(self):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = self.conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    return rows

def _select_project_by_id(self, project_id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = self.conn.cursor()
    cur.execute("SELECT * FROM projects WHERE id=?", (project_id,))

    rows = cur.fetchall()
    return rows

def _update_task(self, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = self.conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def _delete_task(self, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = self.conn.cursor()
    cur.execute(sql, (id,))


