import { Component, OnInit } from '@angular/core';

import { Poll } from '../poll';
import { PollService } from '../poll.service';

@Component({
  selector: 'app-polls',
  templateUrl: './polls.component.html',
  styleUrls: ['./polls.component.scss', '../app.component.scss']
})
export class PollsComponent implements OnInit {
  polls: Poll[];

  constructor(private pollService: PollService) { }

  ngOnInit() {
    this.getPolls();
  }

  getPolls(): void {
    this.pollService.getPolls()
      .subscribe(polls => this.polls = polls);
  }

}
