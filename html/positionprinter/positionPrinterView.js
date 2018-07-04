/**
 * This class is a view class. It provides methods for printing elements like
 * the cube in a canvas.
 * @type PositionPrinterView
 */
class PositionPrinterView {
    /**
     * Creates a new instance of PositionPrinterView.
     * This method instantiates a cube and sets the context.
     */
    constructor() {
        this.xMin = 50;
        this.xMax = 650;
        this.yMin = 60;
        this.yMax = 160;
        this.initialX = 165;
        this.initialY = 360;
        this.finalX = 165;
        this.finalY = 360;
        this.cubePickedUp = false;
        this.cubeDropped = false;
        this.canvas = document.getElementById("positionviewCanvas");
        this.cube = new Cube(40, 40);
        this.ctx = this.canvas.getContext("2d");
    }
    
    /**
     * This method draws the initial setup including masts and the rope
     * between them.
     */
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
    
    /**
     * This method moves the cube to its starting position
     */
    moveToStart() {
        //ToDo: Depend on cubepickup
        this.drawBorders();
        this.cube.print(this.canvas, this.initialX, this.initialY);
    }
    
    /**
     * This method moves the cube to its final position
     */
    moveToEnd() {
        //ToDo: Depend on cubepickup
        this.drawBorders();
        this.cube.print(this.canvas, this.finalX, this.finalY);
    }
    
    /**
     * This method prints the cube and the graber depending on if the
     * cube is picked up or dropped down.
     * @param {int} x
     * @param {int} y
     */
    moveTo(x, y) {
        this.drawBorders();
        let cubeWidthHalf = this.cube.width/2;
        let yLinePoint = this.yMax-(this.yMax-this.yMin)*(x+cubeWidthHalf-this.xMin)/(this.xMax-this.xMin);
        this.ctx.beginPath();
        this.ctx.moveTo(x+cubeWidthHalf, y);
        this.ctx.lineTo(x+cubeWidthHalf, yLinePoint);
        this.ctx.stroke();
        this.ctx.closePath();
        this.ctx.beginPath();
        this.ctx.moveTo(x-1, y);
        this.ctx.lineTo(1+x+cubeWidthHalf*2, y);
        this.ctx.stroke();
        this.ctx.closePath();
        this.ctx.beginPath();
        this.ctx.moveTo(x-1, y+20);
        this.ctx.lineTo(x-1, y);
        this.ctx.stroke();
        this.ctx.closePath();
        this.ctx.beginPath();
        this.ctx.moveTo(1+x+cubeWidthHalf*2, y+20);
        this.ctx.lineTo(1+x+cubeWidthHalf*2, y);
        this.ctx.stroke();
        this.ctx.closePath();
        if(this.cubePicketUp){
            this.print(x,y);
        } else if(this.cubeDropped) {
            this.print(this.finalX, this.finalY);
        } else {
            this.print(this.initialX, this.initialY);
        }
    }
    
    /**
     * This method should be called, when the cube becomes removed from
     * its initial position.
     * @param {boolean} bool
     */
    setCubePicketUp(bool) {
        this.cubePicketUp = bool;
    }
    
    /**
     * This method should be called, when the cube reached its final position
     * @param {boolean} bool
     */
    setCubeDropped(bool) {
        this.cubeDropped = bool;
    }
    
    /**
     * This method sets the coordinates, where the cube should finally be printed.
     * @param {int} x
     * @param {int} y
     */
    setFinalCoordinates(x, y) {
        this.finalX = x;
        this.finalY = y;
    }
    
    /**
     * This method calls the printmethod of elements that
     * can be printed in the canvas.
     * @param {int} x
     * @param {int} y
     */
    print(x, y) {
        this.cube.print(this.canvas, x, y);
    }
}