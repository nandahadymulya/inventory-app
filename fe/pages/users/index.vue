<script setup>
const { data } = await useFetch("http://127.0.0.1:8000/users");
const users = data.value;
console.log(users);
</script>

<template>
  <div class="dashboard">
    <div class="welcome">Dashboard</div>
    <div v-for="user in users" :key="user.user_id">
      <p>{{ user.user_id }}</p>
      <p>{{ user.fullname }}</p>
      <p>{{ user.username }}</p>
    </div>
    <div class="row"></div>
  </div>
</template>
