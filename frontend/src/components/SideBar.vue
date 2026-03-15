<template>
  <aside class="sidebar">
    <!-- Logo -->
    <div class="logo-area">
      <img class="logo-icon" src="/images/sidebar/Logo.svg" alt="" />
      <span class="logo-text">trendsee</span>
      <span class="badge-gray">Beta</span>
    </div>

    <button class="collapse-btn">
      <img src="/images/sidebar/ArrowSquareLeft.svg" alt="" />
    </button>

    <!-- Scrollable menu -->
    <div class="menu-scroll">
      <!-- Поиск контента -->
      <div class="menu-section">
        <div class="section-header">Поиск контента</div>
        <nav class="menu-list">
          <router-link class="menu-item" to="/feed">
            <img class="menu-icon" src="/images/sidebar/House.svg" alt="" />
            <span>Главная </span>
          </router-link>
          <router-link class="menu-item" to="/videos">
            <img class="menu-icon" src="/images/sidebar/Video.svg" alt="" />
            <span>Видео</span>
          </router-link>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/Detective.svg" alt="" />
            <span>Шпионаж</span>
          </a>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/Target.svg" alt="" />
            <span>Контент радар</span>
            <span class="badge-brand">712</span>
          </a>
        </nav>
      </div>

      <!-- Работа с соцсетями -->
      <div class="menu-section">
        <div class="section-header">Работа с соцсетями</div>
        <nav class="menu-list">
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/ShareNetwork.svg" alt="" />
            <span>Кросс-постинг</span>
          </a>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/Robot.svg" alt="" />
            <span>Чат боты</span>
          </a>
        </nav>
      </div>

      <!-- Инструменты -->
      <div class="menu-section">
        <div class="section-header">Инструменты</div>
        <nav class="menu-list">
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/MagicWand.svg" alt="" />
            <span>ИИ-сценарий</span>
          </a>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/Cards.svg" alt="" />
            <span>Карусели</span>
          </a>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/LinkSimple.svg" alt="" />
            <span>Анализ видео</span>
          </a>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/Notepad.svg" alt="" />
            <span>Анализ профиля</span>
          </a>
          <a class="menu-item" href="#">
            <img class="menu-icon" src="/images/sidebar/CalendarCheck.svg" alt="" />
            <span>Черновик</span>
            <span class="badge-soon">Скоро</span>
          </a>
        </nav>
      </div>
    </div>

    <!-- Bottom area -->
    <div class="bottom-area">
      <!-- Tarif -->
      <div class="tarif-card">
        <div class="tarif-row">
          <div class="tarif-label">
            <img class="tarif-fire" src="/images/sidebar/Fire.svg" alt="" />
            <span class="tarif-tokens-label">Токены</span>
          </div>
          <span class="tarif-value">1 245 / 4 497</span>
        </div>
        <div class="progress-bar">
          <div class="progress-track" style="width: 28%"></div>
        </div>
        <button class="creative-btn">
          <span>Creative +</span>
          <img class="caret-icon" src="/images/sidebar/CaretRight.svg" alt="" />
        </button>
      </div>

      <!-- User -->
      <div class="user-card">
        <img
          class="user-avatar"
          src="/images/video-cart/Avatar.png"
          alt=""
        />
        <div class="user-info">
          <span class="user-name">Александра</span>
          <span class="user-phone">+7 (999) 999-99-99</span>
        </div>
        <img class="signout-icon" src="/images/sidebar/SignOut.svg" alt="" />
      </div>

      <!-- Language -->
      <div class="lang-row">
        <img class="lang-flag" src="/images/sidebar/RU.svg" alt="" />
        <span class="lang-text">RU</span>
        <img class="caret-icon" src="/images/sidebar/CaretDown.svg" alt="" />
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
</script>

<style scoped>
.sidebar {
  width: 274px;
  min-height: 800px;
  height: 100%;
  background: #f4f5f6;
  border-radius: 16px;
  padding: 12px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  position: relative;
  flex-shrink: 0;
}

/* ── Logo ── */
.logo-area {
  display: flex;
  align-items: center;
  gap: 6.34px;
  height: 28px;
}

.logo-icon {
  width: 30px;
  height: 22.65px;
  flex-shrink: 0;
}

.logo-text {
  font-family: 'Unbounded', sans-serif;
  font-weight: 600;
  font-size: 23.34px;
  line-height: 1.2;
  color: #1b1a25;
  letter-spacing: -0.47px;
  white-space: nowrap;
}

.badge-gray {
  background: #e6e8ea;
  border-radius: 1000px;
  padding: 4px 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #4e616b;
  white-space: nowrap;
}

.collapse-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 20px;
  height: 20px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.collapse-btn img {
  width: 100%;
  height: 100%;
}

/* ── Menu scroll ── */
.menu-scroll {
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.menu-scroll::-webkit-scrollbar {
  display: none;
}

.menu-section {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.section-header {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.1px;
  color: #83939c;
  padding: 4px 0;
}

.menu-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 8px;
  border-radius: 12px;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.menu-item:hover {
  background: #eaecee;
}

.menu-item.router-link-active {
  background: #e6e8ea;
}

.menu-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.menu-item span {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  letter-spacing: 0.5px;
  color: #4e616b;
}

.badge-brand {
  background: #d5d6f8;
  border-radius: 1000px;
  padding: 4px 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #2b31b3;
  margin-left: auto;
}

.badge-soon {
  background: #e6e8ea;
  border-radius: 1000px;
  padding: 4px 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #4e616b;
  margin-left: auto;
}

/* ── Bottom area ── */
.bottom-area {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-top: auto;
}

/* ── Tarif card ── */
.tarif-card {
  background: #ffffff;
  border-radius: 12px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tarif-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.tarif-label {
  display: flex;
  align-items: center;
  gap: 4px;
}

.tarif-fire {
  width: 20px;
  height: 20px;
}

.tarif-tokens-label {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-style: italic;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  color: #000000;
}

.tarif-value {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  color: #000000;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #e6e8ea;
  border-radius: 200px;
  overflow: hidden;
}

.progress-track {
  height: 100%;
  background: #2b31b3;
  border-radius: 100px;
}

.creative-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.creative-btn span {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  color: #83939c;
}

.caret-icon {
  width: 20px;
  height: 20px;
}

/* ── User card ── */
.user-card {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 4px;
  border-radius: 12px;
  height: 48px;
}

.user-avatar {
  width: 32px;
  height: 32px;
  border-radius: 128px;
  object-fit: cover;
  flex-shrink: 0;
}

.user-info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.user-name {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  color: #4e616b;
}

.user-phone {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #a0adb4;
}

.signout-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

/* ── Language ── */
.lang-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 12px;
}

.lang-flag {
  width: 24px;
  height: 16px;
  flex-shrink: 0;
}

.lang-text {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #83939c;
}
</style>
