/**
 * This class is a view class. It provides methods for printing coordinates, states
 * and messages
 * @type LogPrinterView
 */
class LogPrinterView {
    /**
     * Creates a new instance of LogPrinterView.
     * This method instantiates the output area.
     */
    constructor() {
        this.output = document.getElementById("logEntries");
    }
    
    /**
     * This method is used to print a change in the x-coordinate
     * @param {int} x
     */
    printX(x) {
        let pTag = document.createElement('p');
        let content = "Die x-Koordinate hat sich verändert und ist neu: "+x;
        pTag.textContent = content;
        this.output.appendChild(pTag);
        this.output.scrollTop = this.output.scrollHeight;
    }
    
    /**
     * This method is used to print a change in the y-coordinate
     * @param {int} y
     */
    printY(y) {
        let pTag = document.createElement('p');
        let content = "Die y-Koordinate hat sich verändert und ist neu: "+y;
        pTag.textContent = content;
        this.output.appendChild(pTag);
        this.output.scrollTop = this.output.scrollHeight;
    }
    
    /**
     * This method is used to print a change in the x- and y-coordinate
     * @param {int} x
     * @param {int} y
     */
    print(x, y) {
        let pTag = document.createElement('p');
        let content = "Die Koordinaten haben sich verändert und sind neu: "+x+", "+y;
        pTag.textContent = content;
        this.output.appendChild(pTag);
        this.output.scrollTop = this.output.scrollHeight;
    }
    
    /**
     * This method is used to print a change of State
     * @param {State} state
     */
    printState(state) {
        let pTag = document.createElement('p');
        let content = "Der Status hat sich verändert und ist neu: "+state;
        pTag.textContent = content;
        this.output.appendChild(pTag);
        this.output.scrollTop = this.output.scrollHeight;
    }
    
    /**
     * This method is used to print a change of message
     * @param {String} message
     */
    printMessage(message) {
        let pTag = document.createElement('p');
        let content = "Die Nachricht hat sich verändert und ist neu: "+message;
        pTag.textContent = content;
        this.output.appendChild(pTag);
        this.output.scrollTop = this.output.scrollHeight;
    }
}