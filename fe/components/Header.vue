<script setup>
const isMenuOpen = ref(false);
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const menus = ref([
  { name: "Home", to: "/" },
  { name: "Items", to: "/items" },
  { name: "Users", to: "/users" },
]);
</script>

<template>
  <header class="bg-gray-900 text-white">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <h1 class="text-2xl">Inventory App</h1>

      <!-- Mobile Menu Button -->
      <button
        @click="toggleMenu"
        class="block md:hidden text-white focus:outline-none"
      >
        <svg
          class="w-6 h-6"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          ></path>
        </svg>
      </button>

      <nav class="hidden md:block">
        <ul class="flex space-x-4">
          <div v-for="menu in menus" :key="menu.name">
            <NuxtLink :to="menu.to" class="text-white hover:text-gray-300">
              <li>{{ menu.name }}</li>
            </NuxtLink>
          </div>
        </ul>
      </nav>
    </div>

    <!-- Mobile Menu -->
    <div class="container mx-auto">
      <nav
        :class="{ hidden: !isMenuOpen }"
        class="md:hidden w-full h-full px-4 py-4"
      >
        <ul class="flex flex-col space-y-4">
          <div v-for="menu in menus" :key="menu.name">
            <NuxtLink :to="menu.to" class="text-white hover:text-gray-300">
              <li>{{ menu.name }}</li>
            </NuxtLink>
          </div>
        </ul>
      </nav>
    </div>
  </header>
</template>
