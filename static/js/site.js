// JavaScript Document
var source = new EventSource('/page/temp');
source.addEventListener('message', function(e) {
// Пришли какие-то данные
$('#temp').text(e.data);
var i = document.getElementById('format')
if (e.data<27) { i.href="/static/css/2.css";}
	else {i.href="/static/css/1.css";}
            },false);
            
var source2 = new EventSource('/page/hum');
source2.addEventListener('message', function(e) {
$('#hum').text(e.data);}, false);
 