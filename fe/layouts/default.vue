<script setup></script>
<template>
  <div class="h-screen bg-zinc-50 w-full p-0 m-0">
    <div class="row">
      BOS
      <div class="brand"></div>
      <div class="topbar"></div>
    </div>
    <div class="row">
      <div class="sidebar"></div>
      <div class="content">
        <slot />
      </div>
    </div>
  </div>
</template>
