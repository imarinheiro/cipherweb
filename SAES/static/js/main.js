$(document).ready(function () {

    $('#js-blocos .menu .item').tab();

    $('#js-round-1 .menu .item').tab({
        context: "#js-round-1"
    });

    $('#js-round-2 .menu .item').tab({
        context: "#js-round-2"
    });

    $('#js-round-3 .menu .item').tab({
        context: "#js-round-3"
    });

    $('.ui.accordion').accordion();

    $('.ui.negative.message .close').on('click', function () {
        $(this)
            .closest('.ui.negative.message')
            .transition('fade')
        ;
    });
});