<template>
  <Transition name="modal">
    <div v-if="visible" class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-panel">
        <!-- LEFT SIDEBAR -->
        <aside class="sidebar">
          <!-- Video preview -->
          <div class="video-preview">
            <img
              src="/images/video-cart/Container.png"
              alt=""
              class="video-preview__img"
            />
            <div class="video-preview__badges">
              <div class="vid-badge">
                <div class="vid-badge__icon-wrap">
                  <img class="vid-badge__icon" src="/images/video-cart/Social media Logos.svg" alt="" />
                </div>
                <span class="vid-badge__label">Reels</span>
              </div>
              <div class="vid-badge">
                <img class="vid-badge__fire" src="/images/video-cart/FireSimple.svg" alt="" />
                <span class="vid-badge__label">X10</span>
              </div>
            </div>
            <button class="play-btn" aria-label="Play">
              <img src="/images/analysis/Play.svg" alt="" class="play-btn__icon" />
            </button>
          </div>

          <!-- Date + Actions -->
          <div class="date-actions">
            <div class="date-cell">
              <span class="date-text">12.12.2025</span>
            </div>
            <div class="date-actions__icons">
              <button class="heart-btn">
                <img src="/images/analysis/Heart2.svg" alt="Like" />
              </button>
              <div class="ext-link-wrap">
                <img src="/images/analysis/System_External Link.svg" alt="" class="icon-20" />
              </div>
            </div>
          </div>

          <!-- Blogger Card -->
          <div class="blogger-card">
            <div class="blogger-left">
              <img src="/images/video-cart/Avatar.png" alt="" class="blogger-card__avatar" />
              <div class="blogger-card__body">
                <span class="blogger-card__name">@blogerich</span>
                <span class="blogger-card__subs">384.5K</span>
              </div>
            </div>
            <div class="blogger-card__icon-wrap">
              <img src="/images/analysis/Detective.svg" alt="" class="blogger-detective" />
              <img src="/images/analysis/Plus.svg" alt="" class="blogger-plus" />
            </div>
          </div>

          <!-- Description -->
          <div class="description-block">
            <p class="description-block__text">
              Чтобы выиграть в этой игре, нужно быть настоящим психопатом.
              Если ты создатель контента и хочешь стать вирусным, сделай что-то очень глупое, например, сжечь свою роскошную машину.
            </p>
            <button class="more-link">Ещё</button>
          </div>

          <!-- Stats -->
          <div class="stats-list">
            <div class="stats-item">
              <div class="stats-item__left">
                <img src="/images/analysis/Eye.svg" alt="" class="stats-icon" />
                <span class="stats-item__label">Просмотры</span>
              </div>
              <span class="stats-item__value">1,2 млн</span>
            </div>
            <div class="stats-item">
              <div class="stats-item__left">
                <img src="/images/analysis/Heart.svg" alt="" class="stats-icon" />
                <span class="stats-item__label">Лайки</span>
              </div>
              <span class="stats-item__value">1,2 млн</span>
            </div>
            <div class="stats-item">
              <div class="stats-item__left">
                <img src="/images/analysis/ChatCircle.svg" alt="" class="stats-icon" />
                <span class="stats-item__label">Комментарии</span>
              </div>
              <span class="stats-item__value">1,2 млн</span>
            </div>
            <div class="stats-item">
              <div class="stats-item__left">
                <img src="/images/analysis/PaperPlaneTilt.svg" alt="" class="stats-icon" />
                <span class="stats-item__label">Репосты</span>
              </div>
              <span class="stats-item__value">1,2 млн</span>
            </div>
            <div class="stats-item">
              <div class="stats-item__left">
                <img src="/images/analysis/ChartDonut.svg" alt="" class="stats-icon" />
                <span class="stats-item__label">ER</span>
              </div>
              <span class="stats-item__value">1,2 млн</span>
            </div>
          </div>
        </aside>

        <!-- RIGHT CONTENT AREA -->
        <div class="content">
          <!-- Video Info -->
          <section class="section video-info">
            <button class="close-btn" @click="$emit('close')" aria-label="Close">
              <img src="/images/analysis/X.svg" alt="Close" />
            </button>
            <span class="video-info__topic">Тема видео</span>
            <h2 class="video-info__title">
              Рассуждения на тему правильности и неправильности
            </h2>
            <div class="music-language-row">
              <div class="music-pill">
                <img
                  src="/images/analysis/Media_Music.svg"
                  alt=""
                  class="icon-16"
                />
                <span class="music-pill__text">Tyga – Pop it off</span>
              </div>
              <div class="language-row">
                <span class="language-row__label">Язык:</span>
                <img
                  src="/images/analysis/GB.svg"
                  alt="GB"
                  class="language-row__flag"
                />
                <span class="language-row__value">Английский</span>
              </div>
            </div>
            <div class="tags-row">
              <span class="tag tag--purple">Туториал</span>
              <span class="tag tag--green">Энергичное видео</span>
              <span class="tag tag--orange">Изи монтаж</span>
              <span class="tag tag--pink">Трендовый звук</span>
              <span class="tag tag--orange">Лид магнит</span>
              <span class="tag tag--purple">Красота и здоровье</span>
            </div>
          </section>

          <!-- Транскрибация -->
          <section class="section">
            <div class="section__header">
              <h3 class="section__title">Транскрибация</h3>
              <div class="section__header-actions">
                <button class="translated-btn">
                  <img src="/images/analysis/Translate.svg" alt="" class="icon-16" />
                  <span>Переведено</span>
                </button>
                <button class="copy-btn">
                  <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                </button>
              </div>
            </div>
            <div class="content-box transcription-box">
              <div class="transcription-box__content">
                <p>
                  SPF скатывается? Смотри — вот эти катышки. И нет, это не
                  всегда "плохой SPF".
                </p>
                <p>Скатывается по трём причинам.</p>
                <p>
                  Первая — ты намазал под SPF слишком много всего: сыворотка,
                  крем, база…
                </p>
                <p>
                  Вторая — ты наносишь толстым слоем и начинаешь тереть.
                </p>
              </div>
              <button class="show-more-btn">
                <span>Ещё</span>
                <img src="/images/analysis/CaretDown.svg" alt="" class="icon-16" />
              </button>
            </div>
          </section>

          <!-- Адаптировать -->
          <section class="section">
            <button class="adapt-btn">
              <img src="/images/analysis/MagicWand.svg" alt="" class="icon-20" />
              <span>Адаптировать</span>
            </button>
          </section>

          <!-- Суть -->
          <section class="section">
            <div class="section__header">
              <h3 class="section__title">Суть</h3>
              <div class="section__header-actions">
                <button class="copy-btn">
                  <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                </button>
              </div>
            </div>
            <div class="content-box essence-box">
              <p>
                Разбор состава/логики: он в человеческих словах переводит
                состав/механику ("что реально делает X"), называет 2–3
                работающих активных компонента и 2–3 маркетинговых "пустых"
                обещания.
              </p>
            </div>
          </section>

          <!-- Структура -->
          <section class="section">
            <h3 class="section__title">Структура</h3>
            <div class="timeline">
              <div class="timeline-step">
                <div class="timeline-step__time">
                  <img
                    src="/images/analysis/ClockCountdown.svg"
                    alt=""
                    class="icon-16"
                  />
                  <span>0–3 сек</span>
                </div>
                <div class="timeline-step__line">
                  <div class="timeline-connector timeline-connector--top"></div>
                  <img
                    src="/images/analysis/Ellipse1.svg"
                    alt=""
                    class="timeline-dot"
                  />
                  <div class="timeline-connector timeline-connector--bottom"></div>
                </div>
                <div class="timeline-step__content">
                  <strong>Шок-сравнение</strong>
                  <p>
                    Визуальный (Девушка с предметом) + Текст на экране:
                    "Это спасет вашу зиму"
                  </p>
                </div>
              </div>

              <div class="timeline-step">
                <div class="timeline-step__time">
                  <img
                    src="/images/analysis/ClockCountdown.svg"
                    alt=""
                    class="icon-16"
                  />
                  <span>3–15 сек</span>
                </div>
                <div class="timeline-step__line">
                  <div class="timeline-connector timeline-connector--top"></div>
                  <img
                    src="/images/analysis/Ellipse2.svg"
                    alt=""
                    class="timeline-dot"
                  />
                  <div class="timeline-connector timeline-connector--bottom"></div>
                </div>
                <div class="timeline-step__content">
                  <strong>Сюжет</strong>
                  <p>
                    [Герой] показывает проблему -> Резкая смена кадра ->
                    Решение
                  </p>
                </div>
              </div>

              <div class="timeline-step">
                <div class="timeline-step__time">
                  <img
                    src="/images/analysis/ClockCountdown.svg"
                    alt=""
                    class="icon-16"
                  />
                  <span>15–120 сек</span>
                </div>
                <div class="timeline-step__line">
                  <div class="timeline-connector timeline-connector--top"></div>
                  <img
                    src="/images/analysis/Ellipse3.svg"
                    alt=""
                    class="timeline-dot"
                  />
                  <div class="timeline-connector timeline-connector--bottom"></div>
                </div>
                <div class="timeline-step__content">
                  <strong>Финал / CTA</strong>
                  <p>
                    Призыв: "Пиши слово "ССЫЛКА" в комменты"
                  </p>
                </div>
              </div>
            </div>
          </section>

          <!-- Хуки -->
          <section class="section">
            <h3 class="section__title">Хуки</h3>
            <div class="content-box hooks-box">
              <div class="hook-item">
                <div class="hook-item__header">
                  <span class="hook-item__label">Хук фраза</span>
                  <button class="copy-btn copy-btn--inline">
                    <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                  </button>
                </div>
                <p>Одна из них — пустышка. Угадаешь какая?</p>
              </div>
              <div class="hook-item">
                <div class="hook-item__header">
                  <span class="hook-item__label">Визуальный хук</span>
                  <button class="copy-btn copy-btn--inline">
                    <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                  </button>
                </div>
                <p>Одна из них — пустышка. Угадаешь какая?</p>
              </div>
              <div class="hook-item">
                <div class="hook-item__header">
                  <span class="hook-item__label">Текстовый хук</span>
                  <button class="copy-btn copy-btn--inline">
                    <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                  </button>
                </div>
                <p>Одна из них — пустышка. Угадаешь какая?</p>
              </div>
            </div>
          </section>

          <!-- Рабочие приемы -->
          <section class="section">
            <div class="section__header">
              <h3 class="section__title">Рабочие приемы</h3>
              <div class="section__header-actions">
                <button class="copy-btn">
                  <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                </button>
              </div>
            </div>
            <div class="content-box techniques-box">
              <div class="technique">
                <strong>2. Суть видео</strong>
                <p>
                  Приём: "кому подходит / кому нет" двумя блоками.
                </p>
                <p>
                  Почему сработало: это формат "диагноз -> лечение ->
                  решение". Люди сохраняют не эмоции, а инструкцию. И это
                  "обзор", а не философия
                </p>
              </div>
              <div class="technique">
                <strong>3. Монтаж</strong>
                <p>
                  Приём: смена планов каждые 1-2 секунды: лицо -> продукт
                  крупно -> рука (демо) -> снова лицо.
                </p>
                <p>
                  Почему сработало: вертикалки смотрят на автопилоте. Частая
                  смена планов держит внимание даже без звука
                </p>
                <p>
                  Приём: все доказательства — через B-roll вставки на 0.3–0.8
                  сек (катышки, блеск, этикетка, нанесение).
                </p>
                <p>
                  Почему сработало: речь в кадре быстро утомляет. B-roll
                  делает ощущение "я реально тестировал".
                </p>
              </div>
              <div class="technique">
                <strong>4. Реплики</strong>
                <p>
                  Приём: "триггер доверия" одной фразой: "Я не продаю этот
                  SPF, мне пох, скажу как есть."
                </p>
                <p>
                  Почему сработало: снимает защиту "мне впаривают".
                </p>
                <p>
                  Приём: "вилка выбора" в середине: "Если кожа жирная — делай
                  так. Если сухая — так."
                </p>
                <p>
                  Почему сработало: персонализация без долгого объяснения =
                  удержание.
                </p>
              </div>
            </div>
          </section>

          <!-- Воронка / Маркетинг -->
          <section class="section">
            <div class="section__header">
              <h3 class="section__title">Воронка / Маркетинг</h3>
              <div class="section__header-actions">
                <button class="copy-btn">
                  <img src="/images/analysis/Copy.svg" alt="" class="icon-16" />
                </button>
              </div>
            </div>
            <div class="content-box marketing-box">
              <div class="funnel-item">
                <strong>CTA голос/визуал</strong>
                <p>
                  Почему сработало: зритель узнаёт свой баг мгновенно. Это не
                  "мнение", а физический факт в кадре, мозг цепляется.
                </p>
              </div>
              <div class="funnel-item">
                <strong>Тригер</strong>
                <p>
                  Почему сработало: зритель узнаёт свой баг мгновенно. Это не
                  "мнение", а физический факт в кадре, мозг цепляется.
                </p>
              </div>
              <div class="funnel-item">
                <strong>Куда ведет</strong>
                <p>
                  Почему сработало: зритель узнаёт свой баг мгновенно. Это не
                  "мнение", а физический факт в кадре, мозг цепляется.
                </p>
              </div>
              <div class="funnel-item">
                <strong>Лид-магнит</strong>
                <p>
                  Почему сработало: зритель узнаёт свой баг мгновенно. Это не
                  "мнение", а физический факт в кадре, мозг цепляется.
                </p>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
defineProps<{
  visible: boolean;
}>();

defineEmits<{
  (e: 'close'): void;
}>();
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  background: rgba(0, 0, 0, 0.4);
}

.modal-panel {
  width: 920px;
  height: 800px;
  background: #fff;
  border-radius: 24px 0 0 24px;
  display: flex;
  gap: 32px;
  padding: 24px;
  font-family: 'Inter', sans-serif;
  position: relative;
  overflow: hidden;
}

/* ===== LEFT SIDEBAR ===== */

.sidebar {
  width: 216px;
  min-width: 216px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  overflow: hidden;
}

/* ── Video preview ── */
.video-preview {
  width: 100%;
  aspect-ratio: 254 / 400;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  flex-shrink: 0;
}

.video-preview__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
}

.video-preview__badges {
  position: absolute;
  top: 12px;
  left: 12px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.vid-badge {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  border-radius: 8px;
}

.vid-badge__icon-wrap {
  display: flex;
  align-items: center;
  padding: 2px;
}

.vid-badge__icon {
  width: 16px;
  height: 16px;
}

.vid-badge__fire {
  width: 20px;
  height: 20px;
}

.vid-badge__label {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #ffffff;
  padding-right: 2px;
}

.play-btn {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #f4f5f6;
  border: none;
  border-radius: 16px;
  padding: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.play-btn__icon {
  width: 16px;
  height: 16px;
}

/* ── Date + Actions ── */
.date-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.date-cell {
  flex: 1;
  display: flex;
  align-items: center;
}

.date-text {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #a0adb4;
}

.date-actions__icons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.heart-btn {
  display: block;
  width: 24px;
  height: 24px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
}

.heart-btn img {
  width: 100%;
  height: 100%;
}

.ext-link-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
}

.icon-16 {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.icon-20 {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

/* ── Blogger Card ── */
.blogger-card {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 12px;
  padding: 4px 0;
  background: #ffffff;
}

.blogger-left {
  flex: 1 0 0;
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.blogger-card__avatar {
  width: 40px;
  height: 40px;
  border-radius: 128px;
  object-fit: cover;
  flex-shrink: 0;
}

.blogger-card__body {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.blogger-card__name {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.1px;
  color: #2b31b3;
  white-space: nowrap;
}

.blogger-card__subs {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #4e616b;
  white-space: nowrap;
}

.blogger-card__icon-wrap {
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
}

.blogger-plus {
  width: 12px;
  height: 12px;
  position: absolute;
  left: -3px;
  top: 22px;
}

/* ── Description ── */
.description-block {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.description-block__text {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #343a40;
  height: 28px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: pre-wrap;
}

.more-link {
  background: none;
  border: none;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #171c1f;
  cursor: pointer;
  padding: 0;
  text-align: left;
}

/* ── Stats ── */
.stats-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stats-item {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #f4f5f6;
  border-radius: 12px;
  padding: 8px 12px;
}

.stats-item__left {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.stats-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.stats-item__label {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 14.5px;
  letter-spacing: 0.4px;
  color: #343a40;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.stats-item__value {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0.25px;
  color: #393c4c;
  white-space: nowrap;
}

/* ===== RIGHT CONTENT ===== */

.content {
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 24px;
  min-width: 0;
}

.section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.section__header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.section__title {
  font-size: 16px;
  font-weight: 600;
  color: #000;
  margin: 0;
}

.section__header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
}

/* Video Info */

.video-info {
  position: relative;
  gap: 16px;
}

.music-language-row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.video-info__topic {
  font-size: 14px;
  font-weight: 500;
  color: #4e616b;
}

.video-info__title {
  font-size: 24px;
  font-weight: 600;
  color: #000;
  line-height: 29px;
  margin: 0;
  padding-right: 56px;
}

.close-btn {
  position: absolute;
  top: 0;
  right: 0;
  background: #f4f5f6;
  border: none;
  border-radius: 16px;
  padding: 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn img {
  width: 16px;
  height: 16px;
}

.music-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #f1f3f5;
  border-radius: 24px;
  padding: 4px 12px 4px 8px;
  align-self: flex-start;
}

.music-pill__text {
  font-size: 12px;
  color: #343a40;
}

.language-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.language-row__label {
  font-size: 14px;
  color: #4e616b;
}

.language-row__flag {
  width: 20px;
  height: 14px;
}

.language-row__value {
  font-size: 14px;
  color: #4e616b;
}

.tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  border-radius: 1000px;
  padding: 4px 12px;
  font-size: 14px;
  font-weight: 500;
}

.tag--purple {
  background: #d5d6f8;
  color: #2b31b3;
}

.tag--green {
  background: #e1f7d8;
  color: #1e6d00;
}

.tag--orange {
  background: #fff0cb;
  color: #9e3f00;
}

.tag--pink {
  background: #ffecf1;
  color: #bf0031;
}

/* Transcription */

.translated-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  background: #f4f5f6;
  border: none;
  border-radius: 999px;
  min-height: 32px;
  padding: 8px 12px;
  cursor: pointer;
  flex-shrink: 0;
}

.translated-btn span {
  font-size: 12px;
  font-weight: 600;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #2b31b3;
}

.copy-btn {
  background: #f4f5f6;
  border: none;
  border-radius: 12px;
  width: 32px;
  height: 32px;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.copy-btn--inline {
  background: transparent;
}

.content-box {
  background: #f4f5f6;
  border-radius: 12px;
  padding: 16px;
  font-size: 14px;
  font-weight: 400;
  color: #4e616b;
  line-height: 21px;
  letter-spacing: 0.25px;
}

.content-box p {
  margin: 0 0 8px;
}

.content-box p:last-child {
  margin-bottom: 0;
}

.transcription-box {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 217px;
  border-radius: 12px;
}

.transcription-box__content {
  flex: 1;
  max-height: 149px;
  overflow: hidden;
}

.show-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: none;
  border: none;
  font-size: 12px;
  font-weight: 600;
  color: #171c1f;
  cursor: pointer;
  padding: 0;
  line-height: 16px;
  letter-spacing: 0.4px;
  align-self: flex-end;
  margin-top: auto;
}

/* Adapt Button */

.adapt-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: #2b31b3;
  border: none;
  border-radius: 12px;
  padding: 16px;
  width: 220px;
  cursor: pointer;
}

.adapt-btn span {
  font-size: 18px;
  font-weight: 600;
  color: #fff;
}

.adapt-btn img {
  filter: brightness(0) invert(1);
}

/* Timeline */

.timeline {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.timeline-step {
  display: flex;
  gap: 8px;
}

.timeline-step__time {
  width: 96px;
  min-width: 96px;
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
  gap: 4px;
  padding-top: 10px;
  font-size: 12px;
  font-weight: 500;
  color: #4e616b;
  line-height: 16px;
  letter-spacing: 0.4px;
  white-space: nowrap;
}

.timeline-step__line {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 24px;
  min-width: 24px;
  align-self: stretch;
}

.timeline-dot {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.timeline-connector {
  width: 1px;
  background: #aeb1f2;
}

.timeline-connector--top {
  height: 11px;
}

.timeline-connector--bottom {
  flex: 1;
  min-height: 39px;
}

.timeline-step__content {
  flex: 1;
  padding-top: 8px;
  padding-bottom: 24px;
  padding-left: 0;
}

.timeline-step__content strong {
  font-size: 14px;
  font-weight: 600;
  color: #000;
  display: block;
  line-height: 21px;
  letter-spacing: 0.15px;
  margin-bottom: 4px;
}

.timeline-step__content p {
  font-size: 14px;
  font-weight: 400;
  color: #4e616b;
  line-height: 21px;
  letter-spacing: 0.25px;
  margin: 0;
}

.timeline-step:last-child .timeline-step__content {
  padding-bottom: 0;
}

/* Hooks */

.hooks-box {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.hook-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.hook-item__header {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 32px;
}

.hook-item__label {
  flex: 1;
  font-size: 16px;
  font-weight: 600;
  color: #000;
  line-height: 24px;
  letter-spacing: 0.15px;
}

.hook-item p {
  font-size: 14px;
  font-weight: 400;
  color: #4e616b;
  line-height: 21px;
  letter-spacing: 0.25px;
  margin: 0;
}

/* Techniques */

.essence-box {
  min-height: 95px;
}

.techniques-box {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.technique {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.technique strong {
  font-size: 16px;
  font-weight: 600;
  color: #000;
  display: block;
  line-height: 24px;
  letter-spacing: 0.15px;
}

.technique p {
  margin: 0;
  line-height: 21px;
  letter-spacing: 0.25px;
}

/* Funnel */

.marketing-box {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.funnel-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.funnel-item strong {
  font-size: 16px;
  font-weight: 600;
  color: #000;
  display: block;
  line-height: 24px;
  letter-spacing: 0.15px;
}

.funnel-item p {
  margin: 0;
  line-height: 21px;
  letter-spacing: 0.25px;
}

/* ===== TRANSITIONS ===== */

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-active .modal-panel,
.modal-leave-active .modal-panel {
  transition: transform 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-panel {
  transform: translateX(100%);
}

.modal-leave-to .modal-panel {
  transform: translateX(100%);
}

/* Scrollbar styling */

.content {
  scrollbar-width: none; /* Firefox */
}

.content::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Edge */
}
</style>
