const $headerElem = $('header');
const $updateHeader = $('div#update_header');

$updateHeader.on('click', function () {
  $headerElem.text('New Header!!!');
});
