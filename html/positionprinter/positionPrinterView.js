
class PositionPrinterView {
    constructor() {
        this.xMin = 50;
        this.xMax = 650;
        this.yMin = 60;
        this.yMax = 160;
        this.canvas = document.getElementById("positionviewCanvas");
        this.cube = new Cube(40, 40);
        this.ctx = this.canvas.getContext("2d");
    }
    
    drawBorders(){
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.strokeStyle="white";
        this.ctx.lineWidth="10";
        this.ctx.beginPath();
        this.ctx.moveTo(50,150);
        this.ctx.lineTo(50,400);
        this.ctx.stroke();
        this.ctx.closePath();
        this.ctx.beginPath();
        this.ctx.moveTo(650,50);
        this.ctx.lineTo(650,400);
        this.ctx.stroke();
        this.ctx.closePath();
        this.ctx.lineWidth="4";
        this.ctx.beginPath();
        this.ctx.moveTo(50,160);
        this.ctx.lineTo(650,60);
        this.ctx.stroke();
        this.ctx.closePath();
    }
    
    moveToStart() {
        this.drawBorders();
        this.cube.print(this.canvas, 150, 360);
    }
    
    moveToEnd() {
        this.drawBorders();
        this.cube.print(this.canvas, 550, 360);
    }
    
    moveTo(x, y) {
        this.drawBorders();
        let cubeWidthHalf = this.cube.width/2;
        let yLinePoint = this.yMax-(this.yMax-this.yMin)*(x+cubeWidthHalf-this.xMin)/(this.xMax-this.xMin);
        this.ctx.beginPath();
        this.ctx.moveTo(x+cubeWidthHalf,y);
        this.ctx.lineTo(x+cubeWidthHalf, yLinePoint);
        this.ctx.stroke();
        this.ctx.closePath();
        this.print(x,y);
        console.log("move to: "+x+", "+y);
    }
    
    print(x, y) {
        this.cube.print(this.canvas, x, y);
    }
}