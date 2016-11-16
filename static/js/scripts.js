/**
 * Created by jparayilkumarji on 11/16/16.
 */

$('.btn').click(function () {
    processUrl($("#urlInput").val())
})

function processUrl(url){
    $.ajax({
        url: 'http://127.0.0.1:5000/submit',
        data: {'urlName':url},
        method: "POST",
        type: "POST",
        success: function (result) {
            if (result.isOk == false) alert(result.message);
        },
        async: true
    });
}
