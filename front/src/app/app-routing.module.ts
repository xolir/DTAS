import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { UsersComponent } from './users/users.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UserDetailComponent } from './user-detail/user-detail.component';
import { PollsComponent } from './polls/polls.component';
import { PollDetailComponent } from './poll-detail/poll-detail.component';

const routes: Routes = [
  { path: 'users', component: UsersComponent},
  { path: 'dashboard', component: DashboardComponent},
  { path: 'detail/:id', component: UserDetailComponent },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'polls', component: PollsComponent},
  { path: 'question/:id', component: PollDetailComponent},
];

@NgModule({
  imports: [ RouterModule.forRoot(routes), HttpClientModule ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
