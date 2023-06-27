import { defineStore } from "pinia";

const baseUrl = "http://localhost:8000/auth";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    user: {
      username: "",
      role: "",
    },
    token: null,
    isAuthenticated: false,
  }),
  getters: {
    getUser(state) {
      return state.user;
    },
    getToken(state) {
      return state.token;
    },
    getIsAuthenticated(state) {
      return state.isAuthenticated;
    },
  },
  actions: {
    async fetchAuth(formData) {
      let requestOptions = {
        method: "POST",
        body: formData,
        redirect: "follow",
      };

      const res = await fetch(`${baseUrl}/login`, requestOptions);
      const data = await res.json();
      const { access_token } = data;
      this.isAuthenticated = true;
      this.token = data.access_token;
      localStorage.setItem("token", JSON.stringify(access_token));
    },
    async fetchUser() {
      let requestOptions = {
        method: "GET",
        redirect: "follow",
      };
      let access_token = localStorage.getItem("token");
      access_token = access_token.slice(1, -1);
      console.log(access_token);
      const res = await fetch(
        `${baseUrl}/me?token=${access_token}`,
        requestOptions
      );
      const data = await res.json();
      console.log(data);
      this.user.username = data.username;
      this.user.role = data.role;
    },
    async logout() {
      let requestOptions = {
        method: "POST",
        redirect: "follow",
        body: localStorage.getItem("token"),
      };
      const res = await fetch(`${baseUrl}/logout`, requestOptions);
      // const data = await res.json();
      this.isAuthenticated = false;
      localStorage.removeItem("token");
    },
  },
  persist: true,
});
