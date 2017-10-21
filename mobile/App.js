import React from 'react';
import { StyleSheet } from 'react-native';
import { Icon } from 'react-native-elements';
import { TabNavigator } from 'react-navigation';

import loginView from './app/views/loginView/loginView'
import votingView from './app/views/votingView/votingView'

const Nav = TabNavigator(
  {
    Login: {
      screen: loginView,
      navigationOptions: {
        tabBarLabel: 'Dashboard',
        tabBarIcon: () => <Icon name="browser" size={35} color={'blue'} />
      },
    },
    Voting: {
      screen: votingView,
      navigationOptions: {
        tabBarLabel: 'Voting',
        tabBarIcon: () => <Icon name="box" size={35} color={'blue'} />
      },
    },
  },
  {
    mode: 'modal',
    headerMode: 'none',
  }
);

const styles = StyleSheet.create({
  container: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: '10%',
  },
  navigation: {
    backgroundColor: 'red',
  }
});

const App = ( ) => (
  <Nav style={styles.container}/>
);

export default () => <App/>;