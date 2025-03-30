<template>
  <div>
    <h1>Buscar Operadoras</h1>
    <input v-model="query" @input="searchOperadoras" placeholder="Digite o nome ou CNPJ" />
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.cnpj">
        {{ operadora.razao_social }} - {{ operadora.cnpj }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      operadoras: [],
    };
  },
  methods: {
    async searchOperadoras() {
      if (this.query.length >= 2) {
        const response = await axios.get(`http://localhost:8000/search/?q=${this.query}`);
        this.operadoras = response.data;
      }
    },
  },
};
</script>
