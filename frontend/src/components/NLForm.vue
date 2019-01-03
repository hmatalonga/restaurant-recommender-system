<template>
  <form>I feel like eating
    <NLFormAutoComplete
      id="cuisine"
      :width="260"
      placeholder="any food"
      :items="food.items"
      v-model="food.text"
    />in a
    <NLFormAutoComplete
      id="price"
      :width="260"
      placeholder="fancy"
      :items="price.items"
      v-model="price.text"
    />restaurant in
    <NLFormAutoComplete
      id="city"
      placeholder="London"
      :items="location.items"
      v-model="location.text"
    />.
  </form>
</template>

<script>
import NLFormAutoComplete from "./NLFormAutoComplete.vue";
import { cities, cuisines, prices } from "../data.js";

export default {
  components: {
    NLFormAutoComplete
  },
  data() {
    return {
      food: {
        text: "",
        items: cuisines
      },
      price: {
        text: "",
        items: prices
      },
      location: {
        text: "",
        items: cities
      }
    };
  }
};
</script>


<style lang="scss" scoped>
form {
  max-width: 720px;
  margin-top: 100px;

  font-family: "Lato", sans-serif;
  font-weight: 200;
  font-size: 4rem;
  line-height: 1.5;
  color: white;
}
</style>

