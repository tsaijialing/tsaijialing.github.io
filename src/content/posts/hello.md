---
title: 'Hello World!'
slug: 'hello'
published: 2026-05-17
description: '使用 Hexo + github pages 架設個人網站'
image: ''
category: '指南'
draft: false
---

使用 Hexo + github pages 架設個人網站
 

## 1.安裝Node.js
前往[Node.js官網](https://nodejs.org/zh-tw/download "游標顯示")安裝。  
安裝完成後開啟終端機(terminal)輸入
```bash
npm
```
安裝成功會跳出相關資訊。
  

## 2.安裝Hexo
[Hexo官網](https://hexo.io/zh-tw/ "游標顯示")
複製指令貼上到終端機即可安裝
```bash
npm install hexo-cli -g
``` 


## 3.初始化Hexo網誌與啟動本地伺服器
在桌面新增資料夾「workspace」並在vscode中開啟資料夾
在vscode中按下 ctrl/command +  `  (位於esc下方) 開啟終端機。
在終端機中輸入[Hexo官網](https://hexo.io/zh-tw/ "游標顯示")中的
```bash
hexo init blog
cd blog
npm install
hexo server
```

若執行成功會看到vscode左側新增了資料夾「blog」，且終端機中顯示網址`http://localhost:4000/`，在瀏覽器中開啟此網址會看到建立的部落格。
 

## 4.撰寫文章
在blog > source > _posts 會看到預設文章`hello-world.md`。  
文章可用markdown語法撰寫。  
文章撰寫完成在終端機中輸入
```bash
hexo clean
hexo s
```
重新整理`http://localhost:4000/` 顯示網頁更新。
 
若要建立新文章，在blog下的終端機中輸入
```bash
hexo new filename # filename輸入檔名
``` 
 

## 5.使用github pages
註冊[github](https://github.com/ "游標顯示")帳號，點擊「create repository」，在 repository name 輸入 `使用者名稱.github.io`。


## 6.設定github SSH金鑰
在終端機輸入
```bash
# mac
ls -al ~/.ssh
ssh-keygen -t ed25519 -C "email@email.com"` # 改成你註冊github的email
pbcopy < ~/.ssh/id_ed25519.pub
```
```bash
# windows
ls -al ~/.ssh
ssh-keygen -t ed25519 -C "email@email.com"` # 改成你註冊github的email
Get-Content ~\.ssh\id_ed25519.pub | Set-Clipboard
```
開啟github > 個人頭像 > setting > SSH and GPG keys  
點擊New SSH key  
Title: 幫電腦取名  
Key: 直接貼上(ctrl/command + v)  
點擊Add SSH key，輸入GitHub密碼驗證  
回到終端機輸入
```bash
ssh -T git@github.com
```
若出現
`Are you sure you want to continue connecting (yes/no/[fingerprint])?`，輸入`yes`  
看到`Hi 你的帳號! You've successfully authenticated...`代表成功


## 7.設定自動部署
在blog下終端機輸入
```bash
npm install hexo-deployer-git --save
```

## 8.修改設定檔
打開blog > _config.yml找到`deploy: `修改成
```yaml
deploy:
  type: git
  repository: git@github.com:使用者名稱/使用者名稱.github.io.git
  branch: main
  # 每個冒號後皆有半型空格
  ```


## 9.Themes
前往[Hexo官網的Themes](https://hexo.io/themes/#single_page "游標顯示")選擇主題模板點擊名稱進入github。

在blog下的終端機輸入
```bash
git clone https://github.com/主題資料夾名稱-theme/hexo-theme-主題資料夾名稱 themes/主題資料夾名稱
```
打開blog > _config.yml修改成`theme: 主題資料夾名稱`

## 10.輸出網頁
在終端機輸入
```bash
hexo clean && hexo g && hexo d
```

## 11.建立完成
搜尋網頁`使用者名稱.github.io`，若頁面未更新按下 ctrl/command + shift + r 清除快取



參考資料:[十分鐘小魔法 - 不需要寫程式也不用花錢，10 分鐘架設出專屬於自己的部落格，建立個人品牌 | 使用 Hexo + GitHub](https://youtu.be/WJk765ztHUg?si=A2jDyXNRJ9Zr-hac "游標顯示")