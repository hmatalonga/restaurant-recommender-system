<template>
  <input
    class="button"
    :class="{ 'text-centered': centerText }"
    type="text"
    :name="id"
    v-model="query"
    @keydown.esc="query = ''"
    :placeholder="placeholder"
    autocomplete="off"
  >
</template>

<script>
import { debounce } from "lodash";

export default {
  props: {
    id: String,
    value: String,
    placeholder: {
      type: String,
      default: "Tell us a restaurant name"
    },
    width: {
      type: Number,
      default: 420
    },
    centerText: {
      type: Boolean,
      default: false
    },
    classes: String
  },
  data() {
    return {
      query: this.value
    };
  },
  mounted() {
    this.$el.style.maxWidth = `${this.width}px`;
  },
  watch: {
    query: debounce(function() {
      this.$emit("input", this.query);
    }, 500)
  }
};
</script>


<style lang="scss" scoped>
input {
  display: inline-block;
  border: none;
  outline: none;
  margin: 0;
  padding: 6px;
  font-family: "Lato", sans-serif;
  font-weight: 200;
  font-size: 4rem;
  line-height: 1.5;
  color: #007a73;
  border-bottom: 1px dashed #007a73;
  background-color: #38a89d;
  &:hover {
    border-bottom: 1px dashed #004f4a;
    color: #004f4a;
    cursor: pointer;
  }
}
.text-centered {
  text-align: center;
}
</style>
