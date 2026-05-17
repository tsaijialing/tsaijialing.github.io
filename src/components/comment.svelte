<script lang="ts">
  import { onMount } from 'svelte'

  let commentContainer: HTMLDivElement

  function loadGiscus() {
    if (!commentContainer) return
    
    // 清空舊的評論，避免切換頁面時重複渲染
    commentContainer.innerHTML = ''

    const script = document.createElement('script')
    script.src = 'https://giscus.app/client.js'
    script.setAttribute('data-repo', 'tsaijialing/tsaijialing.github.io')
    script.setAttribute('data-repo-id', 'R_kgDOSeKBJA')
    script.setAttribute('data-category', 'Announcements')
    script.setAttribute('data-category-id', 'DIC_kwDOSeKBJM4C9PNk')
    script.setAttribute('data-mapping', 'pathname')
    script.setAttribute('data-strict', '0')
    script.setAttribute('data-reactions-enabled', '1')
    script.setAttribute('data-emit-metadata', '0')
    script.setAttribute('data-input-position', 'top')
    script.setAttribute('data-theme', 'preferred_color_scheme')
    script.setAttribute('data-lang', 'zh-TW')
    script.setAttribute('crossorigin', 'anonymous')
    script.async = true

    commentContainer.appendChild(script)
  }

  onMount(() => {
    // 首次載入頁面時初始化
    loadGiscus()

    // 監聽 Fuwari 的 Swup 動態網頁切換事件，確保切換文章時評論會重新載入
    document.addEventListener('swup:page:next', loadGiscus)

    return () => {
      document.removeEventListener('swup:page:next', loadGiscus)
    }
  })
</script>

<div class="card-base p-6 mt-4">
  <div bind:this={commentContainer} id="giscus-comments"></div>
</div>