<template>
  <div class="input-container">
    <div class="autocomplete-input">{{ autocomplete }}</div>
    <input
      :class="{ 'text-centered': centerText }"
      type="text"
      :name="id"
      v-model="query"
      @keydown.esc="query = ''"
      @keydown.exact="selectValue"
      @input="suggestValue"
      :placeholder="placeholder"
      autocomplete="off"
    >
  </div>
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
    items: {
      type: Array,
      require: true
    }
  },
  data() {
    return {
      query: this.value,
      autocomplete: "",
      currentValue: ""
    };
  },
  mounted() {
    this.$el.style.width = `${this.width}px`;
  },
  methods: {
    suggestValue() {
      if (this.query === "") {
        this.autocomplete = "";
        return;
      }
      let find = false;
      for (let i = 0; i < this.items.length; i++) {
        this.currentValue = this.items[i];
        let filter =
          this.currentValue.toLowerCase().indexOf(this.query.toLowerCase()) ===
          0;
        if (filter) {
          find = true;
          break;
        } else {
          this.currentValue = "";
        }
      }
      this.autocomplete = find ? this.currentValue : "";
    },
    selectValue(e) {
      if (e.keyCode === 13 || e.keyCode === 9) {
        e.preventDefault();
        this.query = this.currentValue;
        this.autocomplete = "";
      }
    }
  },
  watch: {
    query: debounce(function() {
      this.$emit("input", this.query);
    }, 500)
  }
};
</script>


<style lang="scss" scoped>
.input-container {
  position: relative;
  display: inline-block;

  input,
  .autocomplete-input {
    max-width: 100%;
    position: absolute;
    padding: 6px;
    top: -4.8rem;
    left: 0;
    font-family: "Lato", sans-serif;
    font-weight: 200;
    font-size: 4rem;
    line-height: 1.5;
    color: #007a73;
  }

  input {
    border: none;
    outline: none;
    margin: 0;
    border-bottom: 1px dashed #007a73;
    background-color: transparent;
    &:hover {
      border-bottom: 1px dashed #004f4a;
      color: #004f4a;
      cursor: pointer;
    }
  }
  .autocomplete-input {
    color: #007a73;
  }
  .text-centered {
    text-align: center;
  }
}
</style>
