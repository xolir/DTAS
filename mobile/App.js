import React from 'react';
import { StyleSheet } from 'react-native';
import { Icon } from 'react-native-elements';
import { StackNavigator } from 'react-navigation';

import './app/config/reactotron';

import loginView from './app/views/loginView/loginView'
import votingListView from './app/views/votingListView/votingListView'

const Nav = StackNavigator({
  Login: {
    screen: loginView,
  },
  Questions: {
    path: 'questions',
    screen: votingListView,
  },
}, {
  initialRouteName: 'Login',
});

const styles = StyleSheet.create({
  container: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: '10%',
  },
});

const App = ( ) => (
  <Nav/>
);

export default () => <App/>;