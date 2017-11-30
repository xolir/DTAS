import React from 'react';
import { Text, View, StyleSheet, Button } from 'react-native';

const styles = StyleSheet.create({
});

const Question = ({ questionData, voteHandler }) => (
  <View style={styles}>
    <Text>Question text: { questionData.question_text }</Text>
    <Text>End date: { questionData.end_date }</Text>
    <Text>Publication Date: { questionData.pub_date } </Text>
    { questionData.user.map(user => (
      <View>
        <Text>{ user.name }</Text>
        <Text>{ user.surname }</Text>
        <Text>{ user.birthday }</Text>
        <Button title="Vote" onPress={() => voteHandler(questionData.id, user.id)}>Vote</Button>
      </View>
    ))}
  </View>
);

export default Question;
