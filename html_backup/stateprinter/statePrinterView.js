
class StatePrinterView {
    constructor() {
        this.canvas = document.getElementById("stateviewCanvas");
        this.ctx = this.canvas.getContext("2d");
        this.ctx.strokeStyle="white";
        this.ctx.font = "20px Arial";
        this.ctx.textAlign = "center";
        this.ctx.fillText("Start", 60, 120);
        this.ctx.rect(50,65,20,20);
        this.ctx.moveTo(70,75);
        this.ctx.lineTo(200,75);
        this.ctx.fillText("Packet abgeholt", 210, 45);
        this.ctx.rect(200,65,20,20);
        this.ctx.moveTo(220,75);
        this.ctx.lineTo(350,75);
        this.ctx.fillText("Hindernisse überwindet", 360, 120);
        this.ctx.rect(350,65,20,20);
        this.ctx.moveTo(370,75);
        this.ctx.lineTo(500,75);
        this.ctx.fillText("Ziel erkannt", 510, 45);
        this.ctx.rect(500,65,20,20);
        this.ctx.moveTo(520,75);
        this.ctx.lineTo(650,75);
        this.ctx.fillText("Packet abgesetzt", 660, 120);
        this.ctx.rect(650,65,20,20);
        this.ctx.moveTo(670,75);
        this.ctx.lineTo(800,75);
        this.ctx.fillText("Ziel erreicht", 810, 45);
        this.ctx.rect(800,65,20,20);
        this.ctx.moveTo(820,75);
        this.ctx.lineTo(950,75);
        this.ctx.fillText("Stop", 960, 120);
        this.ctx.rect(950,65,20,20);
        this.ctx.stroke();
    }
    
    setStartState() {
        
    }
    
    setEndState() {
        
    }
    
    printDeviceStartet() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(50,65,20,20);
    }
    
    printPackagePickedUp() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(200,65,20,20);
    }
    
    printObstaclePassed() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(350,65,20,20);
    }
    
    printTargetDetected() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(500,65,20,20);
    }
    
    printTargetDropped() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(650,65,20,20);
    }
    
    printDestinationReached() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(800,65,20,20);
    }
    
    printDeviceStopped() {
        this.ctx.fillStyle = "rgb(245, 3, 24)";
        this.ctx.fillRect(950,65,20,20);
    }
}