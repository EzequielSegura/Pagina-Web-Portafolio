const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const w = canvas.width = document.body.offsetWidth;
const h = canvas.height = document.body.offsetHeight;

ctx.fillStyle = '#000';
ctx.fillRect(0, 0, w, h);

if (ctx) {
    var X = w / 2;
    var Y = 125;
    var r = 100;
    ctx.strokeStyle = "#fff";
    ctx.fillStyle = "#000";
    ctx.lineWidth = 5;
    ctx.arc(X,Y,r,0,2*Math.PI);
    ctx.fill();
    ctx.stroke();
}