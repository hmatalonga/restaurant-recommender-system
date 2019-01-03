<template>
  <div id="app">
    <div v-if="showResults">
      <ol v-if="results.length > 0">
        <li v-for="item of results" :key="item.Name">
          <a :href="makeMapsLink(item)" target="_blank">{{ item.Name }}</a>
        </li>
      </ol>
      <p class="text-info" v-else>No results found...</p>
      <div class="helper-block">
        <span @click="showResults = false">Back to search</span>
      </div>
    </div>
    <div v-else>
      <NLForm v-if="simpleMode"/>
      <NLFormTextInput id="query" v-model="searchQuery" :width="700" :centerText="true" v-else/>
      <SearchButton @search="makeSearch"/>
    </div>
    <div class="helper-block">
      <span @click="simpleMode = !simpleMode; showResults = false">{{ helperMessage }}</span>
    </div>
  </div>
</template>

<script>
import NLForm from "./components/NLForm.vue";
import SearchButton from "./components/SearchButton.vue";
import NLFormTextInput from "./components/NLFormTextInput.vue";
import axios from "axios";

export default {
  name: "app",
  components: {
    NLForm,
    SearchButton,
    NLFormTextInput
  },
  data() {
    return {
      simpleMode: true,
      showResults: false,
      searchQuery: "Gartine",
      results: []
    };
  },
  computed: {
    helperMessage() {
      return this.simpleMode
        ? "I already know some awesome restaurant!"
        : "Let me choose some options...";
    }
  },
  methods: {
    makeSearch() {
      if (this.simpleMode) {
        const params = {
          cuisine: this.$el.querySelector("#cuisine").value,
          price: this.$el.querySelector("#price").value,
          city: this.$el.querySelector("#city").value
        };
        axios
          .get("http://localhost:9000/simple", {
            params
          })
          .then(({ data }) => {
            this.results = JSON.parse(data);
            this.showResults = true;
          });
      } else {
        const params = {
          name: this.searchQuery
        };
        axios
          .get("http://localhost:9000/keyword", {
            params
          })
          .then(({ data }) => {
            this.results = JSON.parse(data);
            this.showResults = true;
          });
      }
    },
    makeMapsLink(item) {
      return `http://maps.google.com/?q=${item.Name},${item.City}`;
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

  ol {
    max-width: 720px;

    font-family: "Lato", sans-serif;
    font-weight: 200;
    font-size: 3.2rem;
    line-height: 1.5;
    color: white;

    li a {
      color: white;
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
  }

  p.text-info {
    max-width: 720px;

    font-family: "Lato", sans-serif;
    font-weight: 200;
    font-size: 3.2rem;
    line-height: 1.5;
    color: white;
  }

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
