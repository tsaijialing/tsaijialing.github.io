---
title: '為Blog新增評論系統'
slug: 'giscus'
published: 2026-05-18
description: '使用 giscus 為 fuwari 新增評論系統'
image: ''
category: '教學'
draft: false
tags: '筆記'
---

使用 giscus 為 fuwari 新增評論系統


## 1.取得儲存庫連結
前往[giscus官網](https://giscus.app/zh-TW "游標顯示")下載giscus應用程式
啟用[discussions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/enabling-or-disabling-github-discussions-for-a-repository "游標顯示")


## 2.公開儲存庫
前往[github](https://github.com/ "游標顯示") > Repositories 若`使用者名稱.github.io`右邊顯示`Public`代表儲存庫已公開
未公開則點擊`使用者名稱.github.io` > Settings > Features > 打開 Discussions 
複製儲存庫連結(使用者名稱/使用者名稱.github.io)貼上至[giscus官網](https://giscus.app/zh-TW "游標顯示")


## 3.設定 discussion
開啟 Discussion 的標題包含頁面的路徑名稱
Discussion 分類選擇 公告 (announcements)
功能開啟 啟用主文上的反應功能 (reaction) 、 將留言框置於在留言上方


## 4.新增評論系統
打開 src > pages > posts > [...slug].astro
在 </MainGridLayout> 行上方加入
```Js
                <Icon name="material-symbols:chevron-right-rounded" class="text-[2rem] text-[var(--primary)]" />
            </div>}
        </a>
    </div>


<script src=""
    data-repo=""
    data-repo-id=""
    data-category=""
    data-category-id=""
    data-mapping=""
    data-strict=""
    data-reactions-enabled=""
    data-emit-metadata=""
    data-input-position=""
    data-theme=""
    data-lang=""
    crossorigin=""
    async>
</script>


</MainGridLayout>


<style is:global>
#post-container :nth-child(1) { animation-delay: calc(var(--content-delay) + 0ms) }
#post-container :nth-child(2) { animation-delay: calc(var(--content-delay) + 50ms) }
#post-container :nth-child(3) { animation-delay: calc(var(--content-delay) + 100ms) }
#post-container :nth-child(4) { animation-delay: calc(var(--content-delay) + 175ms) }
#post-container :nth-child(5) { animation-delay: calc(var(--content-delay) + 250ms) }
#post-container :nth-child(6) { animation-delay: calc(var(--content-delay) + 325ms) }
</style>
```
(空白處自行填入數據)


## 5.上架Blog
儲存檔案後在終端機輸入
```bash
git add .
git commit -m "任意取名"
git push origin main
```


## 6.成功架設評論系統
前往Blog重新整理


參考資料:[新一代静态博客框架Astro的部署优化指南与使用体验](https://www.lapis.cafe/posts/technicaltutorials/astro-deploy-and-optimization/ "游標顯示")