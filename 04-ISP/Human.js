import {Workable} from "./Workable.js"

export class Human extends Workable {
  work() {
    console.log("Humano trabajando...");
  }

  eat() {
    console.log("Humano comiendo...");
  }
}