import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { catchError, map, tap } from 'rxjs/operators';

import { Poll } from './poll';
import { MessageService } from './message.service';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class PollService {
  private pollsUrl = 'http://localhost:8000/api/questions/';
  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  private log(message: String) {
    this.messageService.add('PollsService' + message);
  }

  getPolls (): Observable<Poll[]> {
    return this.http.get<Poll[]>(this.pollsUrl)
      .pipe(
        tap(polls => this.log(`fetched polls`)),
        catchError(this.handleError('getPolls', []))
      );
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      console.error(error);

      this.log(`${operation} failed: ${error.message}`);

      return of(result as T);
    };
  }

  getPoll(id: number): Observable<Poll> {
    const url = `${this.pollsUrl}${id}`;
    return this.http.get<Poll>(url).pipe(
      tap(_ => this.log(`fetched poll id=${id}`)),
      catchError(this.handleError<Poll>(`getPoll id=${id}`))
    );
  }

  updatePoll (poll: Poll): Observable<any> {
    return this.http.put(this.pollsUrl, poll, httpOptions).pipe(
      tap(_ => this.log(`updated poll id=${poll.id}`)),
      catchError(this.handleError<any>('updatedPoll'))
    );
  }

}
