
class Audioplayer extends InterfaceStateUser {
    constructor() {
        super();
    }
    
    setState(state) {
        if(state > 0 && state < 8) {
            this.state = state;
            switch(state) {
                case State['DEVICE_STARTED']:
                    document.getElementById("audioItsMe").play();
                    setTimeout(function(){ document.getElementById("audioMain").play(); }, 1000);              
                    break;
                case State['OBSTACLE_PASSED']:
                    document.getElementById("audioMain").pause();
                    document.getElementById("audioHereWeGo").play();
                    setTimeout(function(){ document.getElementById("audioMain").play(); }, 1000);
                    break;
                case State['PACKAGE_PICKED_UP']:
                    document.getElementById("audioMain").pause();
                    document.getElementById("audioPowerUp").play();
                    setTimeout(function(){ document.getElementById("audioMain").play(); }, 1000);
                    break;
                case State['PACKAGE_DROPPED']:
                    document.getElementById("audioMain").pause();
                    document.getElementById("audioMamamia").play();
                    setTimeout(function(){ document.getElementById("audioMain").play(); }, 1000);
                    break;
                case State['DESTINATION_REACHED']:
                    document.getElementById("audioMain").pause();
                    document.getElementById("audioTheEnd").play();
                    break;
            }
        }
    }
}
