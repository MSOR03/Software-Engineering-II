// ISP - Interface Segregation Principle
// No obligar a una clase a implementar cosas que no necesita.

import {Human} from "./Human.js" 
import {Robot} from "./Robot.js"

const human = new Human();
const robot = new Robot();

human.work();
human.eat();
robot.work();
