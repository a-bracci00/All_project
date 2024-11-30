 function sayhello() {
    console.log("website published!");
}

function sayhello1() {
    document.getElementById("prompt").innerHTML="website published!";
}
function deleteAccount(params) {
    document.getElementById("prompt2").innerHTML="account deleted";
}

function orderlist(params) {
    document.getElementById("prompt1").innerHTML="item ordered";
}

function deleteAccount(params) {
    document.getElementById("prompt2").innerHTML="account deleted";
}

function save(params) {
    document.getElementById('prompt3').innerHTML="progress saved";
}

var username=document.getElementById("usernameinput").value;

function register() {
    var username=document.getElementById("usernameinput").value;
    console.log(userame);
}

function register(params) {
    var username=document.getElementById("usernameinput").value;
    document.getElementById("message").innerHTML=username+",you're signed up!"
}

function addreview(params) {
    var review= document.getElementById("reviewtext").value;
    var addedreview=document.getElementById("addedreview");
    addedreview.innerHTML=review;
}

function register1(params) {
    document.getElementById("usernameinput1").value="";
}

function share(params) {
    var post= document.getElementById("posttext").value;
    console.log(post);
}

function search(params) {
    var searchword= document.getElementById("searchinput").value;
    document.getElementById("message").innerHTML=searchword;
}

function signup(params) {
    var email= document.getElementById("email");
    console.log(email);
}

function addreview(params) {
    var review= document.getElementById("reviewtext").value;
    var addedreview= document.getElementById("addedreview");
    addedreview.innerHTML=review;
}

function publish(params) {
    var el=document.querySelector("p");
}

function publish(params) {
    var el=document.querySelector("p");
    el.innerHTML="website published!";
}

function publish(params) {
    var el= document.querySelector("#prompt4");
    el.innerHTML="website published";
}

function publish(params) {
    var el= document.querySelector(".prompt6");
    el.innerHTML="website published!";
}

function publish(params) {
    var el=document.querySelector("h3");
    el.innerHTML="website published";
}

function publish(params) {
    var el= document.querySelector("p.prompt5");
    el.innerHTML="website published";
}

function publish(params) {
    var el=document.querySelector("p.pront7");
    el.innerHTML="website published!";
}

function publish(params) {
    var el= document.querySelector("prompt9 update");
    el.innerHTML="web site published";
}

function showattribute(params) {
    var el= document.querySelector("img");
    console.log(el.src);
}

function showattribute1(params) {
    var el= document.querySelector("a");
    console.log(el.href);
}

function changeattribute(params) {
    var el= document.querySelector("img");
    el.src="https://m.media-amazon.com/images/I/61gPBk-11hL._AC_SX522_.jpg";
}

function changequestiontype(params) {
    var el= document.querySelector("input");
    el.type="checkbox";
}

function addstylesheet(params) {
    var el=document.querySelector("link");
    el.href="style.css";
}

function showattribute(params) {
    var el= document.querySelector("img");
    console.log(el.src);
}

var el=document.querySelector("input");
el.type="password";

var el= document.querySelector("input");
el.type="password";
el.placeholder="1234";

function showcolor(params) {
    var el=document.querySelector("p");
    console.log(el.style.color);
}

function changecolor(params) {
    var el= document.querySelector("p");
    el.style.color="#d7465f";
}

function changecolor1(params) {
    var el= document.querySelector("p");
    el.style.backgroundColor="#d7465f";
}

function changestyle(params) {
    var el= document.querySelector("img");
    el.style.borderRadius="45px";
}

function changelayout(params) {
    var el= document.querySelector("a");
    el.styledisplay="block";
};

function changestyle1(params) {
    var el= document.querySelector("p");
    el.style.backgroundColor="aliceblue";
    el.style.borderRadius="45px";
}

function displayattribute(params) {
    var el=document.querySelector("img");
    var imagelink=el.getAttribute("src");
    console.log(imagelink);
}

function displayattribute1(params) {
    var el=document.querySelector("a");
    var link= el.getAttribute("href");
    console.log(link);
}

function displayattribute2(params) {
    var el=document.querySelector("a");
    var imagestyle=el.getAttribute("href");
    console.log(imagestyle);
}

function showattribute3(params) {
    var el=document.querySelector("a");
    var imagestyle=el.getAttribute("style");
    var imagelink=el.getAttribute("href");
    console.log(imagestyle+""+imagelink);
}

function showattribute4(params) {
    var el=document.querySelector("a");
    var link=el.getAttribute("style");
    console.log(link);
}

function changeprofile(params) {
    var el=document.querySelector("img");
    el.setAttribute("src","https://quifinanza.it/wp-content/uploads/sites/5/2020/10/Nutella-fondente.jpg");
}

function changeimage(params) {
    var el= document.querySelector("img");
    el.setAttribute("src","https://i.imgur.com/fOMTegD.jpeg");
    console.log(el.getAttribute("src"));
}

function changetype(params) {
    var el=document.querySelector("input");
    el.setAttribute("type","range");
}

function updateelement(params) {
    var el=document.querySelector("input");
    el.setAttribute("placeholder","1234");
}

function displayitem(params) {
    var el=document.querySelector("li");
    console.log(el.innerHTML);
}

function displayitem(params) {
    var el=document.getElementsByTagName("li");
    console.log(el);
}

function displayitem(params) {
    var el=document.getElementsByTagName("li");
    console.log(el[0].innerHTML);
}

function displayitem(params) {
    var el=document.getElementsByTagName("li");
    console.log(el.length);
}

function displayitem1(params) {
    var el=document.getElementsByClassName("urgent");
    console.log("you have"+el.length+"urgent tasks");
}

function displayitem1(params) {
    var el=document.getElementsByClassName("urgent");
    console.log(el[0].innerHTML);
}

function displayitem1(params) {
    var el=document.getElementsByClassName("adventure");
    el[0].innerHTML="dawn of justice";
}

function displayitem2(params) {
    var el=document.getElementsByTagName("h3");
    console.log(el[0].innerHTML);
}

function displayitem2(params) {
    var el=document.getElementsByTagName("h3");
    console.log(el[2].innerHTML);
}

function displayitem(params) {
    var el= document.querySelectorAll("urgent");
    console.log(el.length);
}

function displayitem3(params) {
    var el= document.querySelectorAll("h3.news");
    console.log(el.length);
}

function displayitem3(params) {
    var el= document.querySelectorAll(".movie,.tech");
    console.log(el.length);
}

function displayitem3(params) {
    var el= document.querySelectorAll(".movie,.tech,button");
    console.log(el[2].innerHTML);
}

function turnbold(params) {
    var el= document.querySelector("p");
    el.setAttribute("class","bold");
}

function turnitalic(params) {
    var el= document.querySelector("p");
    el.setAttribute("class","italic");
}

function addbold(params) {
    var el= document.querySelector("p");
   el.classList.add("bold");
}

function removebold(params) {
    var el=document.querySelector("p");
    el.classList.remove("bold");
}

function togglebold(params) {
    var el=document.querySelector("p");
    el.classList.toggle("bold");
}

function addclasses(params) {
    var el= document.querySelector("p");
    el.classList.add("highlight","underline");
}

function removeclasses(params) {
    var el=document.querySelector("p");
    el.classList.remove("highlight","underline");
}

function publish(params) {
    prompt10.innertext="website published";
}
var prompt=document.querySelector("#prompt10");
var el=document.querySelector("button");
el.onclick=publish;

function changecolor(params) {
    el.style.fontWeight="bold";
}
var el=document.querySelector("button");
el.onclick=changecolor;

function changecolor1(params) {
    item.classList.toggle("pink");
}
var item=document.querySelector("div");
item.onclick=changecolor1;

function changecolor1(params) {
    item.classList.toggle("pink");
}
var item=document.querySelector("div");
item.ondblclick=changecolor1;

function changeonscroll(params) {
    textarea.style.backgroundColor="alice blue";
}
var textarea= document.querySelector("textarea");
textarea.onscroll=changeonscroll;

function updatevalue(params) {
    log.innertext=input.value;
}
var input= document.querySelector("input");
var log=document.getElementsById("log");
input.onchange=updatevalue;

function updatevalue(params) {
    log1.innertext=input.value.length;
}
var input=document.querySelector("input");
var log1= document.getElementsById("log1");
input.oninput=updatevalue;

function updatevalue(params) {
    log.innertext=input.value;
}
var input=document.querySelector("input");
var log= document.getElementById("log2");
input.onchange=updatevalue;

function changecolor(params) {
    item.classList.toggle("pink1");
}
var item= document.querySelector("div");
item.addEventListener("click",changecolor);

function changecolor(params) {
    item.classList.toggle("pink2");
    item.removeEventListener("click",changecolor);
}
var item= document.querySelector("div");
item.addEventListener("click",changecolor);

function changewidth(params) {
    item.classList.toggle("width");
}
function changeheight(params) {
    item.classList.toggle("height");
}
var item=document.querySelector("div");
var el=document.querySelector("button");
el[0].addEventListener("click",changeheight);
el[0].addEventListener("click",changewidth);
el[1].addEventListener("click",changeheight);
el[2].addEventListener("click",changewidth);

function removeitem(params) {
 Itemone.innertext="";
}
var clearbutton=document.querySelector("button");
var Itemone=document.querySelector("#item-1");
clearbutton.addEventListener("click",removeitem);

