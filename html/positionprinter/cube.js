/**
 * This class is used to represent a cube.
 * @type Cube
 */
class Cube extends InterfacePrintable {
    /**
     * This method creates a new instance of Cube
     * @param {int} width
     * @param {int} height
     * @returns {Cube}
     */
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
        this.x = 0;
        this.y = 0;
    }
    
    /**
     * This method prints the cube inside a given area.
     * @param {Object} area : a canvas in which the cube can be printed
     * @param {int} newX
     * @param {int} newY
     */
    print(area, newX, newY) {
        let ctx = area.getContext("2d");
        this.x = newX;
        this.y = newY;
        ctx.beginPath();
        ctx.rect(newX, newY, this.width, this.height);
        ctx.stroke();
        ctx.closePath();
    }
}