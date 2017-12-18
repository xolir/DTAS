import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { PollService } from '../poll.service';
import { Poll } from '../poll';

@Component({
  selector: 'app-poll-detail',
  templateUrl: './poll-detail.component.html',
  styleUrls: ['./poll-detail.component.scss']
})

export class PollDetailComponent implements OnInit {
  @Input() poll: Poll;

  constructor(
    private route: ActivatedRoute,
    private pollService: PollService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getPoll();
  }

  getPoll(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.pollService.getPoll(id)
        .subscribe(poll => this.poll = poll);
    console.log(this.poll.user);
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    this.pollService.updatePoll(this.poll)
      .subscribe(() => this.goBack());
  }
}
