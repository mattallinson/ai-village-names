function options() {
  var checkBox = document.getElementById("myCheck");
  var options = document.getElementById("options");
  if (checkBox.checked == true){
    options.style.display = "block";
  } else {
     options.style.display = "none";
  }
}

window.onload = options()