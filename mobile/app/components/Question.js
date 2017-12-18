import React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import { Button } from 'react-native-elements';
import { withState, compose } from 'recompose';

const styles = StyleSheet.create({
  containerStyle: {
    borderWidth: 1,
    borderRadius: 2,
    borderColor: '#ddd',
    borderBottomWidth: 0,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    elevation: 1,
    marginLeft: 5,
    marginRight: 5,
    marginTop: 10,
    padding: 15
  },
  header: {
    fontSize: 20,
    paddingBottom: 5,
  },
  accordionButton: {
    borderTopWidth: 1,
    borderColor: '#ddd'
  }
});

const Question = ({ questionData, voteHandler, isDisabled, isAccordionActive, toggleAccordion }) => (
  <View>
    <View style={styles.containerStyle}>
      <Text style={styles.header}>{ questionData.question_text }</Text>
      <Text>End date: { new Date(questionData.end_date).toDateString() }</Text>
      <Text>Publication Date: { new Date(questionData.pub_date).toDateString() } </Text>
      <Text
        style={styles.accordionButton}
        onPress={() => toggleAccordion(() => !isAccordionActive)}>{ isAccordionActive ? 'Hide' : 'Show more'}</Text>
    </View>
    <View display={isAccordionActive ? 'flex': 'none'} style={questionData.user.length ? styles.containerStyle : null}>
    { questionData.user.map((user, index) => (
      <View key={index}>
        <Text>{ user.name }</Text>
        <Text>{ user.surname }</Text>
        <Text>Born { user.birthday }</Text>
        <Button
          disabled={isDisabled}
          title="Vote"
          onPress={() => voteHandler(questionData.id, user.id)}
        >Vote</Button>
      </View>
    ))}
    </View>
    <View display={isAccordionActive && !questionData.user.length ? 'flex': 'none'} style={ styles.containerStyle}>
      <Text>This voting has currently no options</Text>
      <Text>please try again later</Text>
    </View>
  </View>
);

export default compose(
  withState('isAccordionActive', 'toggleAccordion', false)
)(Question)