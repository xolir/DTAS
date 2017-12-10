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
  axios
    .post(endpoints.getVotesEndpoint(), {
      "question_id": `${endpoints.getQuestionsEndpoint()}${questionId}/`,
      "user_id": `${endpoints.getUserEndpoint()}${user_id}/`,
    })
    .then(() => 'Vote has been added!')
    .catch(() => 'Vote has been rejected!')
);

export default {
  getVotes,
  getQuestions,
  sendLoginRequest,
  sendVote
}