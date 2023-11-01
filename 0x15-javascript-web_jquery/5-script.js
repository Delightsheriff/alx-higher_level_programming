const $listElem = $('ul.my_list');
const $addListElem = $('div##add_item');

$addListElem.on('click', function () {
  const newListItem = $('<li>Item</li>');
  $listElem.append(newListItem);
});
