import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';

const HomeScreen = () => {
  const [pesquisas, setPesquisas] = useState([]);

  useEffect(() => {
    // NOTA: Substitua pelo endereço IP da sua máquina.
    fetch('http://192.168.1.100:5000/pesquisas')
      .then((response) => response.json())
      .then((data) => setPesquisas(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Pesquisas Atribuídas</Text>
      <FlatList
        data={pesquisas}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.pesquisaItem}>
            <Text style={styles.pesquisaTitle}>{item.titulo}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  pesquisaItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  pesquisaTitle: {
    fontSize: 18,
  },
});

export default HomeScreen;
