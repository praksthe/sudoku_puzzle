
//main
$(function () {

    $('#sudoku_get_solution').on('click', function () {

        var puzzle = ""
        for (i = 0; i < 81; i++) {
            if ($('#cell-' + i).val() == "") {
                puzzle += '.'
            } else {
                puzzle += $('#cell-' + i).val()
            }
        }
        // $.post('http://127.0.0.1:5000/', {data: JSON.stringify(global_data)}).done(function(data){
        //     game.drawBoard(JSON.parse(data));
        // });
        var json_data = JSON.stringify({ data: puzzle });
        console.log(json_data);
        $.ajax({
            contentType: 'application/json',
            data: json_data,
            dataType: 'json',
            success: function (data) {
                console.log(data);
                var counter = 0;
                for (i = 0; i < 9; i++) {
                    for (j = 0; j < 9; j++) {
                        console.log('#solution-cell-' + counter);
                        $('#solution-cell-' + counter).val(data[i][j]);
                        counter++;
                    }
                    // counter++;
                }
            },
            error: function (e) {
                if(e.status == 400) {
                    alert('The sudoku puzzle inputs are invalid. \n Please try again');
                } else {
                    console.log(e);
                    alert('There was an error in puzzle problem. \n'+ e.statusText);
                }
                
            },
            processData: false,
            type: 'POST',
            url: 'http://localhost:5000/sudoku_puzzle'
        });
    });
});