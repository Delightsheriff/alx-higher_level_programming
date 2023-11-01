const $headerElem = $('header');
const $divRed_Header = $('div#red_header');

$divRed_Header.on('click', function() {
    $headerElem.css("color", "#FF0000");
});
