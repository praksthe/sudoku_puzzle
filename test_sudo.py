# project/test_basic.py
import os
import json
import unittest
from rest_api import app
from flask import jsonify
import requests
from sudoku import PuzzleSudoku

class BasicTests(unittest.TestCase, PuzzleSudoku):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        pass
        # app.config['TESTING'] = True
        # app.config['DEBUG'] = True
        # self.app = app.test_client()
        # self.assertEqual(app.debug, True)

    def test_sunny_day_scenario1(self):
        ###############
        #Positive scenario : input_json is taken and solved suduko puzzle.
        #Validation        : status code and response value is validated.
        #Final table       : Final resulatant table(2-D array) is also printe using class PuzzleSudoku method.
        ###############

        input_json = "78.4..12.6...75..9...6.1.78..7.4.26...1.5.93.9.4.6...5.7.3...1212...74...492.6..7"
        expected_result = [[7, 8, 5, 4, 3, 9, 1, 2, 6], [6, 1, 2, 8, 7, 5, 3, 4, 9], [4, 9, 3, 6, 2, 1, 5, 7, 8], [8, 5, 7, 9, 4, 3, 2, 6, 1], [2, 6, 1, 7, 5, 8, 9, 3, 4], [9, 3, 4, 1, 6, 2, 7, 8, 5], [5, 7, 8, 3, 9, 4, 6, 1, 2], [1, 2, 6, 5, 8, 7, 4, 9, 3], [3, 4, 9, 2, 1, 6, 8, 5, 7]]

        response = requests.post('http://localhost:5000/sudoku_puzzle', json=dict(data = input_json))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
        print "Final table scernario 1"
        self.pretty_print_in_2D(response.json())
        print "====end====="

    def test_sunny_day_scenario2(self):
        ###############
        #Positive scenario : input_json is taken and solved suduko puzzle.
        #Validation        : status code and response value is validated.
        #Final table       : Final resulatant table(2-D array) is also printe using class PuzzleSudoku method.
        ###############

        input_json = "...4..12.6...75..9...6.1.78..7.4......1.5....9.4.6...5.7.3...1..2....4....9......"
        expected_result = [[7, 3, 5, 4, 8, 9, 1, 2, 6], [6, 1, 8, 2, 7, 5, 3, 4, 9], [4, 9, 2, 6, 3, 1, 5, 7, 8], [2, 5, 7, 8, 4, 3, 9, 6, 1], [3, 6, 1, 9, 5, 2, 7, 8, 4], [9, 8, 4, 1, 6, 7, 2, 3, 5], [5, 7, 6, 3, 9, 4, 8, 1, 2], [8, 2, 3, 5, 1, 6, 4, 9, 7], [1, 4, 9, 7, 2, 8, 6, 5, 3]]

        response = requests.post('http://localhost:5000/sudoku_puzzle', json=dict(data = input_json))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
        print "\nFinal table sunny scernario 2"
        self.pretty_print_in_2D(response.json())
        print "====end====="

    def test_rainy_day_scenario1(self):
        ###############
        #Negative  scenario : input_json is string length is less than 81.
        #Validation        : status code and response value is validated.
        #Final table       : Final resulatant table is not created (400) invalid input from user
        ###############

        input_json = "4..12.6...75..9...6.1.78..7.4......1.5....9.4.6...5.7.3...1..2....4....9."

        response = requests.post('http://localhost:5000/sudoku_puzzle', json=dict(data = input_json))

        #import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        print("rainy-scenario1==> json is not of expected length of 81\n")

    def test_rainy_day_scenario2(self):
        ###############
        #Negative scenario : input_json is have invalid input for UI
        '''
        |7 8 0|7==========> should not have 7 again(this sample is taken from below input_json)
        |0 0 0|
        |1 2 0|
        '''
        #Validation        : status code and response value is validated.
        #Final table       : Final resulatant table is not created (400) invalid input from user
        ###############

        input_json = "78.7..12.6...75..9...6.1.78..7.4.26...1.5.93.9.4.6...5.7.3...1212...74...492.6..7"

        response = requests.post('http://localhost:5000/sudoku_puzzle', json=dict(data = input_json))

        self.assertEqual(response.status_code, 400)
        print("rainy-scenario2 ==> Invalid input val 7 in the Table[0][4] of the table from user\n")

    def test_rainy_day_scenario3(self):
        ###############
        #Negative scenario : input_json is have invalid input for UI
        '''
        |7 8 0|
        |6 8 0|==========> should not have 8 again(this sample is taken from below input_json)
        |1 2 0|
        '''
        #Validation        : status code and response value is validated.
        #Final table       : Final resulatant table is not created (400) invalid input from user
        ###############

        input_json = "78....12.68..75..9...6.1.78..7.4.26...1.5.93.9.4.6...5.7.3...1212...74...492.6..7"

        response = requests.post('http://localhost:5000/sudoku_puzzle', json=dict(data = input_json))

        self.assertEqual(response.status_code, 400)
        print("rainy-scenario3 ==> Invalid input val 8 in the Table[1][2] of the table from user\n")
     


if __name__ == "__main__":
    unittest.main()
