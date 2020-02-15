// Javascript script that adds, removes and clears LI elements from a list when the user clicks

$(document).ready(() => {

  const list = $('UL.my_list')

  $('DIV#add_item').click(() => { list.append('<li>Item</li>') });

  $('DIV#remove_item').click(() => { list.children().last().remove() });

  $('DIV#clear_list').click(() => { list.empty('<li>Item</li>') });
})
