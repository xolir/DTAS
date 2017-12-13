import React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import { Button } from 'react-native-elements';

const styles = StyleSheet.create({
});

const Question = ({ questionData, voteHandler, isDisabled }) => (
  <View style={styles}>
    <Text>Question text: { questionData.question_text }</Text>
    <Text>End date: { new Date(questionData.end_date).toDateString() }</Text>
    <Text>Publication Date: { new Date(questionData.pub_date).toDateString() } </Text>
    { questionData.user.map((user, index) => (
      <View key={index}>
        <Text>{ user.name }</Text>
        <Text>{ user.surname }</Text>
        <Text>{ user.birthday }</Text>
        <Button
          disabled={isDisabled}
          title="Vote"
          onPress={() => voteHandler(questionData.id, user.id)}
        >Vote {isDisabled}</Button>
      </View>
    ))}
  </View>
);

export default Question;
