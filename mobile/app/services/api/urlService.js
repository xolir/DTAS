import apiConfig from '../../config/config.json';

const getVotesEndpoint = () => (
  `${apiConfig.apiEndpoint}/votes/`
);

const getQuestionsEndpoint = () => (
  `${apiConfig.apiEndpoint}/questions/`
);

const getLoginEndpoint = () => (
  `${apiConfig.apiEndpoint}/???`
)

export default {
  getVotesEndpoint,
  getQuestionsEndpoint,
  getLoginEndpoint
}