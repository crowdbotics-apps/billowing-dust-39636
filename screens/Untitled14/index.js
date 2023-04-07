import { useNavigation } from "@react-navigation/native";
import { Pressable } from "react-native";
import { Text } from "react-native";
import React from "react";
import { StyleSheet, ScrollView, SafeAreaView } from "react-native";

const Untitled14 = () => {
  const navigation = useNavigation();
  return <SafeAreaView style={styles.safeArea}>
        <ScrollView contentContainerStyle={{
      backgroundColor: '#f0f0f1',
      padding: 10,
      position: 'relative',
      flex: 1
    }}><Pressable onPress={() => {
        navigation.navigate("eventHome");
      }}><Text style={styles.PafGMwaP}>Events</Text></Pressable><Pressable onPress={() => {
        navigation.navigate("Untitled20");
      }}><Text style={styles.OCIABZhS}>create event</Text></Pressable><Pressable onPress={() => {
        navigation.navigate("Untitled24");
      }}><Text style={styles.GxGjMvzE}>Tickets</Text></Pressable><Pressable onPress={() => {
        navigation.navigate("notifications");
      }}><Text style={styles.NcWkesUO}>Notification icon</Text></Pressable></ScrollView>
    </SafeAreaView>;
};

const styles = StyleSheet.create({
  safeArea: {
    height: '100%'
  },
  PafGMwaP: {
    width: 100,
    height: 50,
    lineHeight: 14,
    fontSize: 14,
    borderRadius: 0
  },
  OCIABZhS: {
    width: 100,
    height: 50,
    lineHeight: 14,
    fontSize: 14,
    borderRadius: 0
  },
  GxGjMvzE: {
    width: 100,
    height: 50,
    lineHeight: 14,
    fontSize: 14,
    borderRadius: 0
  },
  NcWkesUO: {
    width: 100,
    height: 50,
    lineHeight: 14,
    fontSize: 14,
    borderRadius: 0
  }
});
export default Untitled14;