$(document).ready(function () {
    $('.search_select select').selectpicker();
})

$(document).ready(function(){
    var timesSelectClicked = 0;
    $('.select_substation').click(function(e) {
           if (timesSelectClicked == 0)
        {
            timesSelectClicked += 1;
        }
        else if (timesSelectClicked == 1)
        {
            // alert($('.select_podstation option:selected').val());
            timesSelectClicked = 1;
            window.location.href = 'http://127.0.0.1:8000/res/addTcp/showSubstation/' + $('.select_substation option:selected').val() + '/';
        }
  });
});
