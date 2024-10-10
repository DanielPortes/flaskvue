<template>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Origin</th>
        <th scope="col">Age</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="whisky in whiskies" :key="whisky.id">
        <td>{{ whisky.name }}</td>
        <td>{{ whisky.origin }}</td>
        <td>{{ whisky.age }} years</td>
        <td>
          <div class="btn-group" role="group">
            <button
              type="button"
              class="btn btn-warning btn-sm"
              @click="$emit('edit-whisky', whisky)">
              Update
            </button>
            <button
              type="button"
              class="btn btn-danger btn-sm"
              @click="$emit('delete-whisky', whisky)">
              Delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'WhiskyTable',
  props: {
    whiskies: {
      type: Array,
      required: true
    }
  }
}
</script>