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
            <h5 class="modal-title">Add a new whisky</h5>
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
                <label for="addWhiskyName" class="form-label">Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addWhiskyName"
                  v-model="form.name"
                  placeholder="Enter name">
              </div>
              <div class="mb-3">
                <label for="addWhiskyAge" class="form-label">Age:</label>
                <input
                  type="number"
                  class="form-control"
                  id="addWhiskyAge"
                  v-model="form.age"
                  placeholder="Enter age">
              </div>
              <div class="mb-3">
                <label for="addWhiskyDistillery" class="form-label">Distillery:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addWhiskyDistillery"
                  v-model="form.distillery"
                  placeholder="Enter distillery">
              </div>
              <div class="mb-3">
                <label for="addWhiskyRegion" class="form-label">Region:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addWhiskyRegion"
                  v-model="form.region"
                  placeholder="Enter region">
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="addWhiskyTasted"
                  v-model="form.tasted">
                <label class="form-check-label" for="addWhiskyTasted">Tasted</label>
              </div>
              <div class="btn-group" role="group">
                <button type="submit" class="btn btn-primary btn-sm">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="$emit('reset')">
                  Reset
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
  name: 'AddWhiskyModal',
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