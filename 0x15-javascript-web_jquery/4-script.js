const $headerElem = $('header');
const $divRedHeader = $('DIV#toggle_header');

$divRedHeader.on('click', function () {
  const currentClass = $headerElem.attr('class');

  if (currentClass === 'red') {
    $headerElem.removeClass('red').addClass('green');
  } else if (currentClass === 'green') {
    $headerElem.removeClass('green').addClass('red');
  } else {
    $headerElem.addClass('red');
  }
});
