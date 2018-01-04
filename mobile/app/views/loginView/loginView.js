import React from "react";
import { View } from "react-native";
import { withState, compose } from "recompose";
import { Button, FormInput, FormLabel } from "react-native-elements";

import api from "../../services/api/apiService";

import styles from "../../styles/stylesheet";

const loginUser = (login, password, navigation) => {
  navigation.navigate("Questions");
};

const votingContainer = ({
  navigation,
  login,
  password,
  setLogin,
  setPassword
}) => (
  <View style={styles.container}>
    <FormLabel>Login Sample</FormLabel>
    <FormInput
      onChangeText={e => {
        setLogin(() => e);
      }}
    />
    <FormLabel>Password</FormLabel>
    <FormInput
      onChangeText={e => {
        setPassword(() => e);
      }}
    />
    <Button
      title="login"
      onPress={() => loginUser(login, password, navigation)}
    />
  </View>
);

export default compose(
  withState("login", "setLogin", ""),
  withState("password", "setPassword", "")
)(votingContainer);
