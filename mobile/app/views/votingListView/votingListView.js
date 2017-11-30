import React from 'react';
import { Text, View } from 'react-native';
import Reactotron from 'reactotron-react-native'

import styles from '../../styles/stylesheet';

import api from '../../services/api/apiService';

import Question from '../../components/Question';

class votingListContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      questions: [],
    }
  }

  componentWillMount() {
    api.getQuestions().then(resp => {
      this.setState((prevState) => Object.assign({}, prevState, { questions: resp.data }));
    })
  }

  handleUserVote(question_id, user_id) {
    api.sendVote(question_id, user_id);
  }

  render() {
    Reactotron.log('statequestions');
    Reactotron.log(this.state.questions);
    return (
      <View style={styles.container}>
        <Text>Voting view</Text>
        {this.state.questions.map((question, index) => (
          <Question key={index} questionData={question} voteHandler={this.handleUserVote.bind(this)}/>
        ))}
      </View>
    )
  }
}

export default votingListContainer;