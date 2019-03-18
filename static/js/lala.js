$(function () {
    $('img').each(function () {
        var img_path = String($(this).attr('src'))
        img_path = "{% static '"+ img_path + "'%}"
        $(this).attr('src',img_path)

    })
    console.log($('body').html())
})
// $(function () {
//     $('img').each(function () {
//         var imgPath = $(this).attr('src')
//
//         imgPath = "{% static '" + imgPath + "'%}"
//
//         $(this).attr('src',imgPath)
//     })
//
//     console.log($('body').html())
// })