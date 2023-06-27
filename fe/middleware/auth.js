import { useAuthStore } from "@/stores/auth";

export default defineNuxtRouteMiddleware((to) => {
  const { isAuthenticated } = useAuthStore();

  if (!isAuthenticated) {
    return navigateTo("/login");
  }
  if (to.path === "/login") {
    return navigateTo("/");
  }
});
