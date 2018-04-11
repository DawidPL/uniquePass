function userPassword(){
  var data = document.getElementById("user_value");
  document.getElementById("user_value_button").disabled = false;
  while (data == null){
  document.getElementById("user_value_button").disabled = true;
  }
  return data;
}
