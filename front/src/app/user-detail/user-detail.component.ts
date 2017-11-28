import { Component, OnInit, Input } from '@angular/core';
import { User } from '../user';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { UserService } from '../user.service';

@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.css']
})
export class UserDetailComponent implements OnInit {
  @Input() user: User;

  constructor(
    private route: ActivatedRoute,
    private userService: UserService,
    private location: Location
  ) { }

  ngOnInit() {
    const name = +this.route.snapshot.paramMap.get('name');
    this.userService.getUsers()
        .subscribe(user => this.user = user);
  }
  }

}
