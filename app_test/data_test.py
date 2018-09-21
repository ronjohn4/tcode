from app import tcode_data
import os
import unittest
import datetime


class TestStringMethods(unittest.TestCase):
    database = 'tcode_db_test.db'

    def setUp(self):
        # Delete previous instances of the DB that weren't cleaned up
        try:
            os.remove(self.database)
            print('Previous database file deleted: {0}'.format(self.database))
        except Exception as e:
            print(e)

        self.db = tcode_data.DB(self.database)

    def tearDown(self):
        del self.db

        # Only clean up db file if not needed for offline manual checking
        # try:
        #     os.remove(self.database)
        # except Exception as e:
        #     print(e)


    def test_conn(self):
        self.assertIsNotNone(self.db.conn)

    def test_shirt_object_id(self):
        shirt = self.db.shirt(42, 'code snippet goes here', datetime.datetime.now(), datetime.datetime.now())
        self.assertEqual(shirt.id, 42)

    def test_shirt_object_snippet(self):
        shirt = self.db.shirt(42, 'code snippet goes here', datetime.datetime.now(), datetime.datetime.now())
        self.assertEqual(shirt.snippet, 'code snippet goes here')

    def test_shirt_object_last_updated(self):
        n = datetime.datetime.now()
        shirt = self.db.shirt(42, 'code snippet goes here', n, n)
        self.assertEqual(shirt.last_updated, n)

    def test_shirt_object_added(self):
        n = datetime.datetime.now()
        shirt = self.db.shirt(42, 'code snippet goes here', n, n)
        self.assertEqual(shirt.added, n)

    def test_shirt_object_addlist(self):
        n = datetime.datetime.now()
        shirt = self.db.shirt(42, 'code snippet goes here', n, n)
        self.assertEqual(shirt.addlist(), (shirt.snippet, shirt.last_updated, shirt.added))

    def test_shirt_insert(self):
        snippet = self.db.shirt(42, 'code snippet goes here', datetime.datetime.now(), datetime.datetime.now())
        row_id = self.db.insert_snippet(snippet)
        self.assertIsNotNone(row_id)
