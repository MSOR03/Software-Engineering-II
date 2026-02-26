// LSP - Liskov Substitution Principle
// Las subclases no deben romper el comportamiento esperado.
import {FlyingBird} from "./Bird.js";
import {Penguin} from "./Penguin.js"

const sparrow = new FlyingBird();
const penguin = new Penguin();

sparrow.fly();
penguin.swim();
