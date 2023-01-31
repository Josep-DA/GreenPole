function current_li_change(element) {
  let current_li = document.getElementById("current");

  current_li.id = "not-current";
  element.parentElement.id = "current";
};

function clear_search_input() {
  let search_input = document.getElementById("search-input");
  
  search_input.value = "";
};

function rotate(element) {
  let third_div = document.getElementById("third-div")

  if (element.id == 'flipped') {
    element.style.transform = "rotate(0deg)";
    element.id = "not_flipped";
    element.parentElement.style.borderRadius = "0"
    third_div.style.display = "block";
  } else {
    element.style.transform = "rotate(180deg)";
    element.id = "flipped"
    element.parentElement.style.borderRadius = "5em"
    third_div.style.display = "none";
  };
};