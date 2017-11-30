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
    "question_id": `${endpoints.getVotesEndpoint()}${questionId}/`,
    "user_id": `${endpoints.getUserEndpoint()}${user_id}/`,
  })
);

export default {
  getVotes,
  getQuestions,
  sendLoginRequest,
  sendVote
}