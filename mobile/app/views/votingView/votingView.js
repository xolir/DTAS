import React from 'react';
import { Text, View } from 'react-native';

import styles from '../../styles/stylesheet';

import Question from '../../components/Question';

class votingContainer extends React.Component {
  constructor() {
    super();
  }

  render() {
    return (
      <View style={styles.container}>
        <Text>Voting view</Text>
        {this.state.questions.map((question, index) => (
          <Question key={index} questionData={question}/>
        ))}
      </View>
    )
  }
}

export default votingContainer;