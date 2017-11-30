import axios from 'axios';

import endpoints from './urlService';

const getVotes = () => (
  axios.get(endpoints.getVotesEndpoint())
);

const getQuestions = () => (
  axios.get(endpoints.getQuestionsEndpoint())
);

const sendLoginRequest = (login, password) => (
  axios.post(endpoints.getLoginEndpoint(), {
    login,
    password
  })
);

const sendVote = (questionId, user_id) => (
  axios.post(endpoints.getVotesEndpoint(), {
    "question_id": `http://localhost:8000/api/questions/${questionId}`,
    "user_id": `http://localhost:8000/api/users/${user_id}/`,
  })
);

export default {
  getVotes,
  getQuestions,
  sendLoginRequest,
  sendVote
}