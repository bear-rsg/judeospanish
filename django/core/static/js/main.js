$(document).ready(function() {

    // Language / Translation / i18n
    var languageVisible = false;
    $('#language-show').on('click', function() {
        // Hide language popup
        if (languageVisible) {
            $('#language-popup').animate({left: '-15em'});
            $(this).animate({left: '0em'});
            languageVisible = false;
        }
        // Show language popup
        else {
            $('#language-popup').animate({left: '0'});
            $(this).animate({left: '6em'});
            languageVisible = true;
        }
    });

    // Accordian
    $('.accordian-item-header').on('click', function() {
        // Toggle visibility of the body, which comes next after the header
        $(this).next().slideToggle();
        // Toggle icon
        var headerSymbol = $(this).find('.accordian-item-header-symbol').first();
        if (headerSymbol.text() == '+') headerSymbol.text('-');
        else headerSymbol.text('+');
    });

});