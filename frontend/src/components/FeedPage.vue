<template>
  <div class="feed-container" ref="scrollContainer">
    <!-- Search bar -->
    <div class="toolbar">
      <div class="search-form">
        <input
          v-model.number="userId"
          class="input"
          type="number"
          min="1"
          placeholder="ID пользователя"
          @keyup.enter="handleSearch"
        />
        <button
          class="btn-primary-sm"
          :disabled="!userId || loading"
          @click="handleSearch"
        >
          Получить публикации
        </button>
      </div>
    </div>

    <!-- Empty state — no user selected -->
    <div v-if="!activeUserId" class="empty-state">
      Введите ID пользователя и нажмите «Получить публикации»
    </div>

    <template v-else>
      <!-- Empty state — no publications -->
      <div v-if="publications.length === 0 && !loading" class="empty-state">
        Публикаций не найдено.
      </div>

      <!-- Cards list -->
      <div class="cards-list">
        <div
          v-for="pub in publications"
          :key="pub.id"
          class="pub-card"
          @click="selectedPub = pub"
        >
          <div class="pub-card__header">
            <h3 class="pub-card__title">{{ pub.title }}</h3>
            <span
              :class="[
                'source-badge',
                pub.source === 'cache' ? 'source-badge--hot' : 'source-badge--cold',
              ]"
            >
              {{ pub.source === 'cache' ? 'cache' : 'database' }}
            </span>
          </div>
          <p class="pub-card__text">{{ truncate(pub.text) }}</p>
          <div class="pub-card__footer">
            <span class="pub-card__date">{{ formatDate(pub.created_at) }}</span>
          </div>
        </div>
      </div>

      <!-- Loading indicator -->
      <div v-if="loading" class="loading-indicator">
        <div class="spinner"></div>
        <span>Загрузка...</span>
      </div>

      <!-- Sentinel for IntersectionObserver -->
      <div ref="sentinel" class="sentinel"></div>

      <!-- All loaded -->
      <div v-if="!hasMore && publications.length > 0" class="all-loaded">
        Все публикации загружены
      </div>
    </template>

    <!-- Publication detail modal -->
    <PublicationModal :publication="selectedPub" @close="selectedPub = null" />
  </div>
</template>

<script setup lang="ts">
import { ref, onUnmounted, nextTick } from 'vue'
import { getPublications, type Publication } from '../api/client'
import { formatDate } from '../utils/date'
import PublicationModal from './PublicationModal.vue'

const LIMIT = 10

const userId = ref<number | null>(null)
const activeUserId = ref<number | null>(null)

const publications = ref<Publication[]>([])
const loading = ref(false)
const hasMore = ref(true)
const offset = ref(0)

const selectedPub = ref<Publication | null>(null)

const scrollContainer = ref<HTMLElement | null>(null)
const sentinel = ref<HTMLElement | null>(null)
let observer: IntersectionObserver | null = null

function truncate(text: string, max = 150): string {
  return text.length > max ? text.slice(0, max) + '…' : text
}

async function handleSearch() {
  if (!userId.value) return

  activeUserId.value = userId.value
  publications.value = []
  offset.value = 0
  hasMore.value = true

  observer?.disconnect()

  await loadPage()
  await nextTick()
  setupObserver()
}

async function loadPage() {
  if (loading.value || !hasMore.value || !activeUserId.value) return
  loading.value = true
  try {
    const data = await getPublications(activeUserId.value, LIMIT, offset.value)
    publications.value.push(...data.items)
    offset.value += data.items.length
    hasMore.value = publications.value.length < data.total
  } catch (e: any) {
    console.error('Load error:', e)
  } finally {
    loading.value = false
  }
}

function setupObserver() {
  if (!sentinel.value) return
  observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        loadPage()
      }
    },
    {
      root: scrollContainer.value,
      rootMargin: '0px 0px 500px 0px',
    },
  )
  observer.observe(sentinel.value)
}

onUnmounted(() => {
  observer?.disconnect()
})
</script>

<style scoped>
.feed-container {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  padding: 24px;
  gap: 16px;
}

/* ── Toolbar ── */
.toolbar {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px;
  background: #f4f5f6;
  border-radius: 16px;
  flex-shrink: 0;
}

.search-form {
  display: flex;
  gap: 8px;
  align-items: center;
}

.input {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  padding: 10px 14px;
  border: 1px solid #c6ced2;
  border-radius: 12px;
  outline: none;
  background: #ffffff;
  color: #171c1f;
  min-width: 0;
  flex: 1;
}

.input:focus {
  border-color: #2b31b3;
}

/* Hide number input spinners */
.input[type='number']::-webkit-inner-spin-button,
.input[type='number']::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.input[type='number'] {
  -moz-appearance: textfield;
}

.btn-primary-sm {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #ffffff;
  background: #2b31b3;
  border: none;
  border-radius: 12px;
  padding: 10px 16px;
  cursor: pointer;
  white-space: nowrap;
  flex-shrink: 0;
}

.btn-primary-sm:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ── Empty state ── */
.empty-state {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  color: #83939c;
  text-align: center;
  padding: 40px;
}

/* ── Cards list ── */
.cards-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.pub-card {
  background: #ffffff;
  border: 1px solid #e6e8ea;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  cursor: pointer;
  transition: border-color 0.15s, box-shadow 0.15s;
}

.pub-card:hover {
  border-color: #c6ced2;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.pub-card__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.pub-card__title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  color: #000000;
  margin: 0;
}

.source-badge {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 11px;
  letter-spacing: 0.4px;
  padding: 3px 8px;
  border-radius: 1000px;
  white-space: nowrap;
  flex-shrink: 0;
  text-transform: uppercase;
}

.source-badge--hot {
  background: #e1f7d8;
  color: #1e6d00;
}

.source-badge--cold {
  background: #e6e8ea;
  color: #4e616b;
}

.pub-card__text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 21px;
  color: #4e616b;
  margin: 0;
}

.pub-card__footer {
  display: flex;
  align-items: center;
  margin-top: 4px;
}

.pub-card__date {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  color: #a0adb4;
}

/* ── Loading ── */
.loading-indicator {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 16px;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  color: #83939c;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2.5px solid #e6e8ea;
  border-top-color: #2b31b3;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.sentinel {
  height: 1px;
  flex-shrink: 0;
}

.all-loaded {
  text-align: center;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  color: #a0adb4;
  padding: 12px;
}

.feed-container::-webkit-scrollbar {
  width: 4px;
}

.feed-container::-webkit-scrollbar-track {
  background: transparent;
}

.feed-container::-webkit-scrollbar-thumb {
  background: #d0d5dd;
  border-radius: 4px;
}
</style>
