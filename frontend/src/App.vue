<template>
  <div id="app">
    <NLForm v-if="easyMode"/>
    <NLFormTextInput id="query" v-model="searchQuery" :width="700" :centerText="true" v-else/>
    <SearchButton :classes="['foo', 'bar']"/>
    <div class="helper-block">
      <span @click="easyMode = !easyMode">{{ helperMessage }}</span>
    </div>
  </div>
</template>

<script>
import NLForm from "./components/NLForm.vue";
import SearchButton from "./components/SearchButton.vue";
import NLFormTextInput from "./components/NLFormTextInput.vue";

export default {
  name: "app",
  components: {
    NLForm,
    SearchButton,
    NLFormTextInput
  },
  data() {
    return {
      easyMode: true,
      searchQuery: "The French Laundry"
    };
  },
  computed: {
    helperMessage() {
      return this.easyMode
        ? "I already know some awesome restaurant!"
        : "Let me choose some options...";
    }
  }
};
</script>

<style lang="scss">
*,
*:before,
*:after {
  box-sizing: border-box;
  transition: 0.25s ease-in-out;
}

*::selection {
  background: #cc1f1a;
  color: white;
}
body {
  background-color: #38a89d;
}
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 85vh;

  .helper-block {
    width: 700px;
    padding: 40px 0;
    text-align: center;
    span {
      font-family: "Lato", sans-serif;
      font-size: 1.4rem;
      line-height: 1.5;
      color: #007a73;
    }
    span:hover {
      cursor: pointer;
      color: #004f4a;
    }
  }
}
</style>
