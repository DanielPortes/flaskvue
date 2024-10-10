<template>
  <div class="container">
    <h1>Whiskies</h1>
    <hr>
    <Alert :message="message" :type="alertType" v-if="showMessage"></Alert>
    <button type="button" class="btn btn-success btn-sm" @click="toggleAddWhiskyModal">
      Add Whisky
    </button>
    <WhiskyTable
        :whiskies="whiskies"
        @edit-whisky="toggleEditWhiskyModal"
        @delete-whisky="handleDeleteWhisky"
    ></WhiskyTable>
    <AddWhiskyModal
        :active="activeAddWhiskyModal"
        :form="addWhiskyForm"
        @close="toggleAddWhiskyModal"
        @submit="handleAddSubmit"
        @reset="handleAddReset"
    ></AddWhiskyModal>
    <EditWhiskyModal
        :active="activeEditWhiskyModal"
        :form="editWhiskyForm"
        @close="toggleEditWhiskyModal"
        @submit="handleEditSubmit"
        @cancel="handleEditCancel"
    ></EditWhiskyModal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from '@/components/Alert.vue';
import WhiskyTable from '@/components/WhiskyTable.vue';
import AddWhiskyModal from '@/components/AddWhiskyModal.vue';
import EditWhiskyModal from '@/components/EditWhiskyModal.vue';

export default {
  name: 'WhiskyView',
  components: {
    Alert,
    WhiskyTable,
    AddWhiskyModal,
    EditWhiskyModal
  },
  data() {
    return {
      activeAddWhiskyModal: false,
      activeEditWhiskyModal: false,
      addWhiskyForm: this.getInitialWhiskyForm(),
      whiskies: [],
      editWhiskyForm: this.getInitialWhiskyForm(),
      message: '',
      alertType: 'success',
      showMessage: false,
    };
  },
  methods: {
    getInitialWhiskyForm() {
      return {
        name: '',
        age: 0,
        distillery: '',
        region: '',
        tasted: false
      };
    },
    async getWhiskies() {
      try {
        const response = await axios.get('http://localhost:5000/whiskies');
        this.whiskies = response.data.whiskies;
      } catch (error) {
        console.error('Error fetching whiskies:', error);
        this.showAlert('Error fetching whiskies', 'danger');
      }
    },
    async addWhisky(payload) {
      try {
        await axios.post('http://localhost:5000/whiskies', payload);
        await this.getWhiskies();
        this.showAlert('Whisky added!', 'success');
      } catch (error) {
        console.error('Error adding whisky:', error);
        this.showAlert('Error adding whisky', 'danger');
      }
    },
    async updateWhisky(payload, whiskyId) {
      try {
        await axios.put(`http://localhost:5000/whiskies/${whiskyId}`, payload);
        await this.getWhiskies();
        this.showAlert('Whisky updated!', 'success');
      } catch (error) {
        console.error('Error updating whisky:', error);
        this.showAlert('Error updating whisky', 'danger');
      }
    },
    async removeWhisky(whiskyId) {
      try {
        await axios.delete(`http://localhost:5000/whiskies/${whiskyId}`);
        await this.getWhiskies();
        this.showAlert('Whisky removed!', 'success');
      } catch (error) {
        console.error('Error removing whisky:', error);
        this.showAlert('Error removing whisky', 'danger');
      }
    },
    showAlert(message, type = 'success') {
      this.message = message;
      this.alertType = type;
      this.showMessage = true;
    },
    toggleModal(modalType) {
      this[modalType] = !this[modalType];
      document.body.classList.toggle('modal-open', this[modalType]);
    },
    toggleAddWhiskyModal() {
      this.toggleModal('activeAddWhiskyModal');
    },
    toggleEditWhiskyModal(whisky = null) {
      if (whisky) {
        this.editWhiskyForm = {...whisky};
      }
      this.toggleModal('activeEditWhiskyModal');
    },
    handleAddSubmit() {
      if (!this.addWhiskyForm.name || !this.addWhiskyForm.distillery || !this.addWhiskyForm.region) {
        this.showAlert('Please fill in all required fields', 'warning');
        return;
      }
      this.toggleAddWhiskyModal();
      const payload = {
        ...this.addWhiskyForm,
        age: Number(this.addWhiskyForm.age) // Ensure age is sent as a number
      };
      this.addWhisky(payload);
      this.addWhiskyForm = this.getInitialWhiskyForm();
    },
    handleAddReset() {
      this.addWhiskyForm = this.getInitialWhiskyForm();
    },
    handleEditSubmit() {
      this.toggleEditWhiskyModal();
      const payload = {...this.editWhiskyForm};
      this.updateWhisky(payload, this.editWhiskyForm.id);
    },
    handleEditCancel() {
      this.toggleEditWhiskyModal();
      this.editWhiskyForm = this.getInitialWhiskyForm();
    },
    handleDeleteWhisky(whisky) {
      this.removeWhisky(whisky.id);
    },
  },
  created() {
    this.getWhiskies();
  },
};
</script>