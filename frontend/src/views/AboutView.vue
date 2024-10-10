<template>
  <div>
    <h1>About</h1>
    <p>This is the about page.</p>
  </div>


</template>

<script>
export default {
  data() {
    return {
      message: ''
    }
  },
  async created() {
    const response = await fetch('/api/ping')
    const data = await response.json()
    this.message = data.message
  }
}
</script>