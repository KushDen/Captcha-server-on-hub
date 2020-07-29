function loading() {
    import json
    while (true) {
        dynamic_data = 'not_done'
        var your_generated_table = $('table'),
        dynamic_data = JSON.parse(your_generated_table.attr('data-dynamic'));
        while (dynamic_data != 'done') {
            console.log("loading");
            $("#loading").show();
            $("#content").hide();
        }
        while (dynamic_data === 'done') {
            $("#content").show();
            $("#show").hide();
        }
    }
}
