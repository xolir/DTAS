import React from "react";
import { Text, View, StyleSheet } from "react-native";
import Reactotron from "reactotron-react-native";

import styles from "../../styles/stylesheet";

import api from "../../services/api/apiService";

import Question from "../../components/Question";

const popUpstyles = StyleSheet.create({
  activePopup: {
    display: "flex",
    borderWidth: 1,
    borderRadius: 2,
    borderColor: "#ddd",
    borderBottomWidth: 0,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    elevation: 1,
    marginLeft: 5,
    marginRight: 5,
    marginTop: 10,
    padding: 15,
    backgroundColor: "#00ff1f"
  },
  hiddenPopup: {
    display: "none"
  }
});

class votingListContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      questions: [],
      apiResponse: "empty",
      showApiResponse: false,
      disabledVoteButton: []
    };
  }

  componentWillMount() {
    api.getQuestions().then(resp => {
      this.setState(prevState => ({
        ...prevState,
        questions: resp.data
      }));
    });
  }

  handleUserVote(question_id, user_id) {
    this.setState(state => ({
      ...state,
      disabledVoteButton: state.disabledVoteButton.concat(question_id)
    }));

    api.sendVote(question_id, user_id).then(resp => {
      this.setState(state => ({
        ...state,
        apiResponse: resp,
        showApiResponse: true
      }));
      setTimeout(
        () =>
          this.setState(state => ({
            ...state,
            showApiResponse: false
          })),
        2500
      );
    });
  }

  render() {
    Reactotron.log("state", this.state);
    return (
      <View style={styles.container}>
        <Text
          style={
            this.state.showApiResponse
              ? popUpstyles.activePopup
              : popUpstyles.hiddenPopup
          }
        >
          {this.state.apiResponse}
        </Text>
        {this.state.questions.map((question, index) => (
          <Question
            key={index}
            questionData={question}
            voteHandler={this.handleUserVote.bind(this)}
            isDisabled={this.state.disabledVoteButton.includes(question.id)}
          />
        ))}
      </View>
    );
  }
}

export default votingListContainer;
