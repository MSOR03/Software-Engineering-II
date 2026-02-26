// DIP - Dependency Inversion Principle
// Depender de abstracciones y no de implementaciones concretas.
import { UserService } from "./UserService.js";
import { MySQLDatabase } from "./MySQLDatabase.js";
import { MongoDatabase } from "./MongoDatabase.js";

const mysql = new MySQLDatabase();
const mongo = new MongoDatabase();

const userServiceWithMySQL = new UserService(mysql);
const userServiceWithMongo = new UserService(mongo);

userServiceWithMySQL.saveUser({ name: "Maicol" });
userServiceWithMongo.saveUser({ name: "Ana" });
