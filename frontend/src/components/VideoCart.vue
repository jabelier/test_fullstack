<template>
  <div class="video-cart">
    <div class="container">
      <img
        class="container-bg"
        src="/images/video-cart/Container.png"
        alt=""
      />

      <div class="header">
        <div class="badges">
          <div class="badge">
            <div class="badge-icon-wrap">
              <img
                class="badge-icon"
                src="/images/video-cart/Social media Logos.svg"
                alt=""
              />
            </div>
            <span class="badge-label">Reels</span>
          </div>
          <div class="badge">
            <img
              class="badge-icon-fire"
              src="/images/video-cart/FireSimple.svg"
              alt=""
            />
            <span class="badge-label">X10</span>
          </div>
        </div>

        <div class="actions">
          <button class="action-btn">
            <img
              class="action-icon"
              src="/images/video-cart/Heart2.svg"
              alt="Like"
            />
          </button>
          <button class="action-btn">
            <img
              class="action-icon"
              src="/images/video-cart/System_External Link.svg"
              alt="External link"
            />
          </button>
        </div>
      </div>

      <div class="stats-list">
        <div class="stat-item">
          <img class="stat-icon" src="/images/video-cart/Eye.svg" alt="" />
          <span class="stat-value">105k</span>
        </div>
        <div class="stat-item">
          <img class="stat-icon" src="/images/video-cart/Heart.svg" alt="" />
          <span class="stat-value">85k</span>
        </div>
        <div class="stat-item">
          <img
            class="stat-icon"
            src="/images/video-cart/ChatCircle.svg"
            alt=""
          />
          <span class="stat-value">15k</span>
        </div>
        <div class="stat-item">
          <img
            class="stat-icon stat-icon--share"
            src="/images/video-cart/PaperPlaneTilt.svg"
            alt=""
          />
          <span class="stat-value">485</span>
        </div>
      </div>
    </div>

    <div class="info">
      <div class="blogger-card">
        <div class="blogger">
          <img
            class="avatar"
            src="/images/video-cart/Avatar.png"
            alt="Avatar"
          />
          <div class="blogger-body">
            <span class="blogger-name">@blogerich</span>
            <span class="blogger-followers">384.5K </span>
          </div>
        </div>
        <div class="blogger-icon-wrap">
          <img
            class="blogger-detective"
            src="/images/video-cart/Detective.svg"
            alt=""
          />
          <img
            class="blogger-plus"
            src="/images/video-cart/Plus.svg"
            alt=""
          />
        </div>
      </div>

      <p class="description">
        500 000 лайков на ютубе делаем , бля буду скидываю 😂😂
      </p>

      <span class="date">12.12.2025</span>

      <button class="btn-primary" @click="emit('analyze')">Анализ</button>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits<{ analyze: [] }>()
</script>

<style scoped>
.video-cart {
  width: 100%;
  max-width: 262px;
  background: #ffffff;
  border-radius: 16px;
  padding: 4px 4px 8px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* ── Container (image area) ── */
.container {
  position: relative;
  width: 100%;
  aspect-ratio: 254 / 400;
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 12px;
}

.container-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 16px;
  pointer-events: none;
}

/* ── Header (badges + actions) ── */
.header {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.badges {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.badge {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  border-radius: 8px;
}

.badge-icon-wrap {
  display: flex;
  align-items: center;
  padding: 2px;
}

.badge-icon {
  width: 16px;
  height: 16px;
  display: block;
}

.badge-icon-fire {
  width: 20px;
  height: 20px;
  display: block;
}

.badge-label {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #ffffff;
  text-align: center;
  padding-right: 2px;
}

/* ── Actions (like, external link) ── */
.actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: flex-end;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  border-radius: 12px;
  border: none;
  cursor: pointer;
}

.action-icon {
  width: 20px;
  height: 20px;
  display: block;
}

/* ── Stats list ── */
.stats-list {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 4px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(4px);
  border-radius: 12px;
}

.stat-item {
  flex: 1 0 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
}

.stat-icon {
  width: 20px;
  height: 20px;
  display: block;
}

.stat-icon--share {
  width: 18px;
  height: 18px;
}

.stat-value {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #ffffff;
  text-align: center;
  white-space: nowrap;
}

/* ── Info block (below image) ── */
.info {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 0 4px;
}

/* ── Blogger card ── */
.blogger-card {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 12px;
  padding: 4px 0;
  background: #ffffff;
}

.blogger {
  flex: 1 0 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 128px;
  object-fit: cover;
  flex-shrink: 0;
}

.blogger-body {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.blogger-name {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.1px;
  color: #2b31b3;
  white-space: nowrap;
}

.blogger-followers {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #4e616b;
  white-space: nowrap;
}

.blogger-icon-wrap {
  position: relative;
  padding: 4px;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.blogger-detective {
  width: 24px;
  height: 24px;
  display: block;
}

.blogger-plus {
  width: 12px;
  height: 12px;
  position: absolute;
  left: -3px;
  top: 22px;
}

/* ── Description ── */
.description {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #4e616b;
  height: 44px;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ── Date ── */
.date {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #a0adb4;
}

/* ── Button Primary ── */
.btn-primary {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 12px;
  background: #2b31b3;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  width: 100%;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #ffffff;
  text-align: center;
}
</style>
