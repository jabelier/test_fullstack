<template>
    <div class="container">
      <!-- Header -->
      <div class="header-block">
        <div class="header-row">
          <div class="header-left">
            <img class="search-icon" src="/images/sidebar/Search.svg" alt="" />
            <h1 class="search-title">Business history</h1>
            <button class="btn-secondary">
              <img class="btn-icon-sm" src="/images/sidebar/Plus.svg" alt="" />
              <span>Добавить в радар</span>
              <img class="btn-icon-sm" src="/images/sidebar/Target.svg" alt="" />
            </button>
            <img class="icon-trailing" src="/images/analysis/Info.svg" alt="" />
          </div>
          <span class="loaded-count">Загружено: 12 видео</span>
        </div>

        <div class="info-banner">
          <p class="info-text">
            Ролики собираются напрямую из поиска соц. сети. Все видео из выдачи –
            актуальны и продвигаются прямо сейчас.
          </p>
          <button class="info-close">
            <img src="/images/sidebar/X.svg" alt="Close" />
          </button>
        </div>
      </div>

      <!-- Filters -->
      <div class="filters-row">
        <button class="btn-outline">
          <span>За все время</span>
          <img class="btn-icon-sm" src="/images/sidebar/CaretDown.svg" alt="" />
        </button>
        <button class="btn-outline">
          <span>По лайкам</span>
          <img class="btn-icon-sm" src="/images/sidebar/CaretDown.svg" alt="" />
        </button>
      </div>

      <!-- Video cards grid -->
      <div class="cards-grid">
        <VideoCart v-for="n in 12" :key="n" @analyze="showModal = true" />
      </div>

      <AnalysisModal :visible="showModal" @close="showModal = false" />

      <!-- Bottom overlay -->
      <div class="bottom-bar">
        <button class="btn-find">
          <img class="btn-find-icon" src="/images/sidebar/Lightning.svg" alt="" />
          <span>Найти еще ролики</span>
        </button>

        <div class="counter">
          <div class="counter-loader">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="9" stroke="rgba(255,255,255,0.25)" stroke-width="2.5" />
              <path
                d="M12 3 A9 9 0 0 1 21 12"
                stroke="white"
                stroke-width="2.5"
                stroke-linecap="round"
              />
            </svg>
          </div>
          <span class="counter-text">Видео: 24 из 3000</span>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import VideoCart from './VideoCart.vue'
import AnalysisModal from './AnalysisModal.vue'

const showModal = ref(false)
</script>

<style scoped>
.container {
  flex: 1;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
}

/* ── Header ── */
.header-block {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 16px;
}

.header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.search-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.search-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0.15px;
  color: #000000;
  white-space: nowrap;
  margin: 0;
}

.btn-secondary {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 12px;
  background: #f4f5f6;
  border-radius: 12px;
  border: none;
  cursor: pointer;
}

.btn-secondary span {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #171c1f;
  padding: 0 4px;
  white-space: nowrap;
}

.btn-icon-sm {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.icon-trailing {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.loaded-count {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  letter-spacing: 0.5px;
  color: #4e616b;
  white-space: nowrap;
}

/* ── Info banner ── */
.info-banner {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 16px;
  background: #d5d6f8;
  border-radius: 16px;
}

.info-text {
  flex: 1;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  color: #2b31b3;
  margin: 0;
}

.info-close {
  width: 20px;
  height: 20px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  flex-shrink: 0;
}

.info-close img {
  width: 100%;
  height: 100%;
}

/* ── Filters ── */
.filters-row {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 16px 0 20px;
}

.btn-outline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  padding: 12px;
  border: 1px solid #c6ced2;
  border-radius: 12px;
  background: transparent;
  cursor: pointer;
}

.btn-outline span {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #000000;
  padding: 0 4px;
  white-space: nowrap;
}

/* ── Cards grid ── */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  padding: 16px 16px;
  padding-bottom: 80px;
}

.cards-grid :deep(.video-cart) {
  width: 100%;
  max-width: none;
}

/* ── Bottom bar ── */
.bottom-bar {
  position: sticky;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px 24px;
  pointer-events: none;
  z-index: 10;
}

.btn-find {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  background: #2b31b3;
  border-radius: 16px;
  border: none;
  cursor: pointer;
  pointer-events: all;
  width: 240px;
  height: 48px;
}

.btn-find-icon {
  width: 24px;
  height: 24px;
}

.btn-find span {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  letter-spacing: 0.3px;
  color: #ffffff;
  white-space: nowrap;
}

.counter {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  padding: 16px 24px;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(12px);
  border-radius: 1000px;
  pointer-events: all;
  position: absolute;
  right: 24px;
  bottom: 16px;
}

.counter-loader {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
  animation: spin 1.2s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.counter-text {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  letter-spacing: 0.5px;
  color: #ffffff;
  white-space: nowrap;
}
</style>
