<template>
  <div id="app">
    <h1>Code Comment-to-API-Documentation Generator</h1>
    <form @submit.prevent="handleUpload" class="upload-form">
      <input type="file" @change="handleFileChange" accept=".zip" />
      <button type="submit">Generate Docs</button>
    </form>

    <div v-if="loading" class="status-message">Generating documentation...</div>
    <div v-if="error" class="error-message">{{ error }}</div>

    <div v-if="documentationData" class="docs-container">
      <div v-for="(docs, fileName) in documentationData" :key="fileName" class="file-docs">
        <h2>{{ fileName }}</h2>
        <div v-for="(item, index) in docs" :key="index" class="doc-item">
          <h3>{{ item.name }}</h3>
          <p><strong>Type:</strong> {{ item.type }}</p>
          <p v-if="item.parameters.length"><strong>Parameters:</strong> {{ item.parameters.join(', ') }}</p>
          <p class="docstring"><strong>Docstring:</strong> <br>{{ item.docstring }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const file = ref(null);
const documentationData = ref(null);
const loading = ref(false);
const error = ref(null);

const handleFileChange = (event) => {
  file.value = event.target.files[0];
};

const handleUpload = async () => {
  if (!file.value) {
    error.value = "Please select a file first.";
    return;
  }
  
  error.value = null;
  loading.value = true;
  documentationData.value = null;

  const formData = new FormData();
  formData.append('file', file.value);

  try {
    const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    documentationData.value = response.data;
  } catch (err) {
    console.error("Error uploading file:", err);
    error.value = "An error occurred while generating documentation. Please try again.";
  } finally {
    loading.value = false;
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.upload-form {
  margin-bottom: 20px;
}

.docs-container {
  text-align: left;
  margin: 0 auto;
  max-width: 800px;
}

.file-docs {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
}

.doc-item {
  border-bottom: 1px solid #eee;
  padding-bottom: 15px;
  margin-bottom: 15px;
}

.doc-item:last-child {
  border-bottom: none;
}

.docstring {
  white-space: pre-wrap;
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 4px;
}

.status-message {
  color: #007bff;
  font-weight: bold;
}

.error-message {
  color: #dc3545;
  font-weight: bold;
}
</style>