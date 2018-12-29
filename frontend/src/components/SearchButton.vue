<template>
  <button class="default" :class="classes" type="button">Find me Restaurants</button>
</template>

<script>
export default {
  props: ["classes"],
  mounted() {}
};
</script>


<style lang="scss">
$red-color: #cc1f1a;
button {
  display: block;
  background: white;
  border: none;
  padding: 10px 55px 10px 20px;
  font-size: 48px;
  font-weight: 200;
  margin: 30px 0 0 0;
  box-shadow: inset 0px 0px 0px $red-color;
  position: relative;
  i {
    transition: 0s 0s ease-in-out;
  }
  &:after {
    content: "\f105";
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    height: 42px;
    width: 55px;
    font-family: FontAwesome;
    line-height: 85px;
    text-align: center;
    color: $red-color;
  }
  &:hover {
    box-shadow: inset 550px 0 0 $red-color;
    color: white;
    cursor: pointer;
    &:after {
      color: white;
    }
  }
}
</style>
