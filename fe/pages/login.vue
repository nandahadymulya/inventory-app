<script setup lang="ts">
import { useAuthStore } from "@/stores/auth.js";

definePageMeta({
  layout: "blank",
});

const authStore = useAuthStore();
const router = useRouter();

interface loginForm {
  username: string;
  password: string;
}

let loginForm: loginForm = {
  username: "",
  password: "",
};

const login = async () => {
  const formData = new FormData();
  formData.append("username", loginForm.username);
  formData.append("password", loginForm.password);
  try {
    await authStore.fetchAuth(formData);
  } catch (error) {}

  router.push("/");
};

const message = ref("");
// const showMessage = (msg) => {
//   message.value = msg;
//   setTimeout(() => {
//     message.value = "";
//   }, 1000);
// };

const passwordType = ref(true);
</script>
<template>
  <div class="flex flex-col h-screen justify-center items-center">
    <div class="text-center text-4xl font-bold pb-5">
      <h1>Login Inventory App</h1>
    </div>

    <div v-if="message" class="w-80 text-center p-3 bg-zinc-200 rounded">
      {{ message }}
    </div>

    <div class="bg-zinc-50 p-10 self-center rounded-md">
      <div class="flex flex-col items-center justify-center text-center">
        <form method="post" name="login">
          <div class="w-80">
            <label for="username" class="text-xl font-semibold w-full"
              >Username</label
            >
            <div class="w-80 3">
              <input
                v-model="loginForm.username"
                id="username"
                type="text"
                placeholder="Type your username"
                class="bg-zinc-100 p-3 rounded w-full"
              />
            </div>
          </div>
          <div class="w-80">
            <label for="password" class="text-xl font-semibold w-full"
              >Password</label
            >
            <div class="flex justify-between 3">
              <input
                v-model="loginForm.password"
                :type="passwordType ? 'password' : 'text'"
                id="password"
                placeholder="Type your password"
                class="bg-zinc-100 w-full p-3 rounded"
              />
              <!-- <div class="self-center ms-3"> -->
              <!-- <Eye v-if="passwordType" color="#aaa" /> -->
              <!-- <EyeSlash color="#aaa" /> -->
              <!-- </div> -->
            </div>
          </div>
        </form>
        <div class="3 w-80 rounded-md">
          <button
            @click="login()"
            class="text-zinc-100 font-bold text-center bg-zinc-400 text-center w-full rounded p-3"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
