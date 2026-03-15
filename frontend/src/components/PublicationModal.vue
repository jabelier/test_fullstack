<template>
  <Transition name="modal">
    <div v-if="publication" class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-content">
        <button class="modal-close" @click="$emit('close')">&times;</button>

        <h2 class="modal-title">{{ publication.title }}</h2>
        <p class="modal-text">{{ publication.text }}</p>

        <div class="modal-meta">
          <div class="modal-meta__row">
            <span class="modal-meta__label">User ID</span>
            <span class="modal-meta__value">{{ publication.user_id }}</span>
          </div>
          <div class="modal-meta__row">
            <span class="modal-meta__label">Создано</span>
            <span class="modal-meta__value">{{ formatDate(publication.created_at) }}</span>
          </div>
          <div class="modal-meta__row">
            <span class="modal-meta__label">Обновлено</span>
            <span class="modal-meta__value">{{ formatDate(publication.updated_at) }}</span>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
import type { Publication } from '../api/client'
import { formatDate } from '../utils/date'

defineProps<{
  publication: Publication | null
}>()

defineEmits<{
  close: []
}>()
</script>

<style scoped>
/* ── Transition ── */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.25s ease;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
.modal-enter-active .modal-content,
.modal-leave-active .modal-content {
  transition: transform 0.25s ease, opacity 0.25s ease;
}
.modal-enter-from .modal-content {
  transform: translateY(24px) scale(0.96);
  opacity: 0;
}
.modal-leave-to .modal-content {
  transform: translateY(24px) scale(0.96);
  opacity: 0;
}

/* ── Overlay ── */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.45);
  padding: 24px;
}

/* ── Content ── */
.modal-content {
  position: relative;
  background: #ffffff;
  border-radius: 20px;
  padding: 32px;
  max-width: 560px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #83939c;
  background: #f4f5f6;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: background 0.15s;
}

.modal-close:hover {
  background: #e6e8ea;
  color: #171c1f;
}

.modal-title {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 20px;
  line-height: 28px;
  color: #171c1f;
  margin: 0 0 12px;
  padding-right: 40px;
}

.modal-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 15px;
  line-height: 24px;
  color: #4e616b;
  margin: 0 0 24px;
  white-space: pre-wrap;
}

/* ── Meta ── */
.modal-meta {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 16px;
  border-top: 1px solid #e6e8ea;
}

.modal-meta__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-meta__label {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 13px;
  color: #83939c;
}

.modal-meta__value {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 13px;
  color: #171c1f;
}
</style>
