import { Component, OnInit } from '@angular/core';

import { User } from '../user';
import { UserService } from '../user.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {

  // selectedUser: User;

  users: User[];

  constructor(private userService: UserService) { }

  ngOnInit() {
    this.getUsers();
  }

  /*onSelect(user: User): void {
    this.selectedUser = user;
  }*/

  getUsers(): void {
    // this.users = this.userService.getUsers();
    const name = +this.route.snapshot.paramMap.get('name');
    this.userService.getUsers()
        .subscribe(users => this.users = users);
  }

}
