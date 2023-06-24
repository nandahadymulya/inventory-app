<script setup>
const { data } = await useFetch("http://127.0.0.1:8000/items");
const items = data.value;
console.log(items);
</script>

<template>
  <div class="dashboard">
    <div class="welcome">Dashboard</div>
    <div v-for="item in items" :key="item.item_id">
      <p>{{ item.name }}</p>
      <p>{{ item.description }}</p>
      <p>{{ item.quantity }}</p>
    </div>
    <div class="row"></div>
  </div>
</template>
