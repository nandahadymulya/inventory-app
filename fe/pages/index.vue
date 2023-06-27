<script setup>
import { useAuthStore } from "@/stores/auth.js";
definePageMeta({
  middleware: "auth",
});

const authStore = useAuthStore();

const authMe = async () => {
  await authStore.fetchUser();
};

const getAuthUser = computed(() => authStore.getUser);
console.log(getAuthUser);

const items = ref([]);
const fetchItems = async () => {
  const res = await fetch("http://localhost:8000/items");
  console.log(res.status);
  items.value = await res.json();
};

const updateItem = (id) => {
  console.log(id);
};

const deleteItem = (id) => {
  confirm("Are you sure you want to delete this item?");
  console.log(id);
};

onMounted(() => {
  fetchItems();
  authMe();
});
</script>

<template>
  <div class="w-full">
    <div class="text-center text-3xl pb-5">
      Welcome, {{ getAuthUser.username }}! <br />
      <span class="text-2xl text-zinc-400">
        You are logged in as {{ getAuthUser.role }}.
      </span>
    </div>

    <div class="text-2xl text-center font-bold p-2 w-fit mx-auto rounded">
      Your Items :
    </div>
    <div class="flex flex-wrap gap-10 justify-center items-center py-5">
      <div v-for="item in items" :key="item.name">
        <div class="max-w-sm rounded overflow-hidden shadow-lg">
          <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">{{ item.name }}</div>
            <p class="text-gray-700 text-base">
              {{ item.description }}
            </p>
          </div>
          <div class="px-6 pt-4 pb-2">
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-xl font-semibold text-gray-700 mr-2 mb-2"
            >
              {{ item.quantity }}
            </span>
          </div>
          <div class="px-6 pt-4 pb-2">
            <span
              @click="updateItem(item.item_id)"
              class="inline-block bg-amber-600 rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2 cursor-pointer"
            >
              Update
            </span>
            <span
              @click="deleteItem(item.item_id)"
              class="inline-block bg-red-600 rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2 cursor-pointer"
            >
              Delete
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
