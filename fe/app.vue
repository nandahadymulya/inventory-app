<script setup>
const { data } = await useFetch("http://127.0.0.1:8000/roles");
const roles = data.value.data;
</script>
<template>
  <div>
    <h1>Inventory App</h1>
    <div v-for="role in roles" :key="role.role_id">
      <p>{{ role.name }}</p>
    </div>
  </div>
</template>
