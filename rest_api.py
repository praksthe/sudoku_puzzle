from flask import Flask, render_template, jsonify, request
from sudoku import PuzzleSudoku

MAX_NO_INPUT_VAL_FOR_CELLS_IN_TABLE = 81

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/sudoku_puzzle', methods=['POST'])
def add_star():
    sudo_2d_array = [([0] * 9) for i in range(9)]
    sudo_input_str = request.json['data'].replace('.','0') #request.get_json()
    if len(sudo_input_str) != MAX_NO_INPUT_VAL_FOR_CELLS_IN_TABLE:
        return jsonify({'error_msg': 'invalid input data'}), 400
    k = 0
    for i in range(9):
        for j in range(9):
       	    sudo_2d_array[i][j] = int(sudo_input_str[k])
            k += 1
    sudoku_puzz = PuzzleSudoku()
    result = sudoku_puzz.get_working_table(sudo_2d_array)
    if not result:
        return jsonify({'error_msg': 'invalid input data'}), 400
        
    print sudo_2d_array 
    return jsonify(sudo_2d_array)

@app.route('/', methods= ['GET', 'POST'])
def index():
    return render_template('./sudoku.html')

if __name__ == '__main__':
    app.run(debug=True)
