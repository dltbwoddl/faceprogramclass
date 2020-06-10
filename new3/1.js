let faceclasses = ['#Bronze', '#Silver', '#Gold', '#Platinum', '#Diamond', '#Master', '#Challenger'];
let  buttoncolorback = ["brown",'silver','gold','rgb(127, 187, 255)','Aqua','antiquewhite','AliceBlue'];
function classcolor(facecnumber=6,colors="AliceBlue",classtext= '<div style="color:black">' + 'Challenger,' + '<br>' + '천상계 얼굴의 소유자' + '</div>')
{
document.getElementById("wait").style.backgroundColor = buttoncolorback[facecnumber];
document.getElementById("wait").innerHTML =classtext;
document.querySelector(faceclasses[facecnumber]).style.backgroundColor =buttoncolorback[facecnumber] ;
}

