<template>
  <div>
    <h1>Ping</h1>
    <p>{{ message }}</p>
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