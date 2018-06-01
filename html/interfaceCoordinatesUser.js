
class InterfaceCoordinatesUser {
    constructor() {
        if(this.setCoordinates === undefined) {
            throw new TypeError("Must override method");
        }
    }
}