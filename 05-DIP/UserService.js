export class UserService {
  constructor(database) {
    this.database = database;
  }

  saveUser(user) {
    this.database.save(user);
  }
}