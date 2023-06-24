<script setup>
const { data } = await useFetch("http://127.0.0.1:8000/roles");
const roles = data.value;
</script>

<template>
  <div class="w-full">
    <div class="welcome">Dashboard</div>
    <div v-for="role in roles" :key="role.role_id">
      <p>{{ role.name }}</p>
    </div>
    <div class="row"></div>
  </div>
</template>
