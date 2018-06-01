
class Cube extends InterfacePrintable {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
        this.x = 0;
        this.y = 0;
    }
    
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