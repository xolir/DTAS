import { User } from './user';

export const USERS: User[] = [
    {
        url: 'http://localhost:4100/api/users/6/',
        email: 'gabi179@gmail.com',
        name: 'Gabriela',
        surname: 'Pałka',
        role: 'Voter',
        birthday: '1995-10-28'
    },
    {
        url: 'http://localhost:4100/api/users/1/',
        email: 'axeris123@gmail.com',
        name: 'Artur',
        surname: 'Nowakowski',
        role: 'Admin',
        birthday: '1996-05-20'
    },
    {
        url: 'http://localhost:4100/api/users/5/',
        email: 'artur.nowakowski1@gmail.com',
        name: 'Artur',
        surname: 'Nowakowski',
        role: 'Candidate',
        birthday: '1996-05-20'
    },
    {
        url: 'http://localhost:4100/api/users/8/',
        email: 'admin@admin.com',
        name: 'Admin',
        surname: 'Admin',
        role: 'Admin',
        birthday: '2017-11-17'
    }
];
