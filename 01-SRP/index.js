import {UserService} from "./UserService.js"
import {EmailService} from "./EmailService.js"
import {DatabaseService} from "./DatabaseService.js"

const userService = new UserService();
const dbService = new DatabaseService();
const emailService = new EmailService();

const user = { name: "Maicol", email: "maicol@email.com" };

userService.addUser(user);
emailService.sendWelcomeEmail(user);
dbService.save(userService.getUsers());
