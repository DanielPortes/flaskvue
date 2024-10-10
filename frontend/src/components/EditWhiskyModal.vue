<template>
  <div>
    <div
      class="modal fade"
      :class="{ show: active, 'd-block': active }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Update Whisky</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="$emit('close')">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="$emit('submit')">
              <div class="mb-3">
                <label for="editWhiskyName" class="form-label">Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editWhiskyName"
                  v-model="form.name"
                  placeholder="Enter name">
              </div>
              <div class="mb-3">
                <label for="editWhiskyOrigin" class="form-label">Origin:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editWhiskyOrigin"
                  v-model="form.origin"
                  placeholder="Enter origin">
              </div>
              <div class="mb-3">
                <label for="editWhiskyAge" class="form-label">Age:</label>
                <input
                  type="number"
                  class="form-control"
                  id="editWhiskyAge"
                  v-model="form.age"
                  placeholder="Enter age">
              </div>
              <div class="btn-group" role="group">
                <button type="submit" class="btn btn-primary btn-sm">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="$emit('cancel')">
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="active" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
export default {
  name: 'EditWhiskyModal',
  props: {
    active: {
      type: Boolean,
      required: true
    },
    form: {
      type: Object,
      required: true
    }
  }
}
</script>