/*document.getElementById("daily_pass").innerHTML = generatePass();
function generatePass(){
  var y = 0;
  var x = Math.random()*10;
  while (y.length != a.lenght()){
    z = Math.floor(Math.random()*10);
    x += z;
    y++;
  }
  return window.alert(x);

}
*/
document.getElementById("auto_pass_generate_button").innerHTML = autoGeneratePass();
function autoGeneratePass(){
  var x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var y = Math.random()*10 + 1;
  var res = 0;
  var i = 0;
  for (i <10 ; i++)
    res += x.charAt(Math.floor(Math.random()*x.lenght));
  document.getElementById("auto_pass_generate").value = res;
  return res;
}
function mOver(obj){
  obj.innerHTML = autoGeneratePass()
}
function mOut(obj){
  obj.innerHTML = " "
}
