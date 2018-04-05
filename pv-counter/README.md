# PV(Page View)稼ぎ  
## 各指標  
Google Analyticsなのかなんなのか調査中。  

### PV数と訪問数  
google analyticsとかで見られるPV数は、ブラウザを開かないとカウントされないことが分かりました(今更)  
最初、getメソッドでアクセスするだけのものを書いてしまったらPVは増えませんでした。  

このプログラムではブラウザを開いたり閉じたりを繰り返しますが、こうすることによって「訪問数」も増えました。cookieで識別してるのでしょうか。  
なので、ブラウザを一度開いたまま更新しまくるとPV数は増えても訪問数は増えないのでは？という仮説。  

### 参照元  
(ブログ内の特定の記事なら)その記事の直前に訪問したページのことだと思われます。  

### 検索ワード  
chromeで検索されたワード。例えば、何かのサイト内で検索したとしてもそれは検索ワードには恐らく入らないです。  

最近はSSLでの通信がほとんどなので、検索ワードが取得できないことが多く、管理画面で確認すると「none」だとか出てきました。  

## 実装でつまったところ  
## invisibleな要素はseleniumのclickメソッドではクリックできない  
このエラーに泣かされた。  
```
selenium.common.exceptions.ElementNotVisibleException: Message: element not visible
```
ページがちょっとオサレ仕様で、検索フォーム用の虫眼鏡マークを押すとニョキッとフォームが出てくる動きになっていた。  
このとき、フォームが出てくる前の虫眼鏡とフォームが出てきてからの虫眼鏡が違う要素になっていて、しかも後者がinvisibleな要素だった。。  

**解決方法**  
send_scriptメソッドを使ってjavascriptでクリックを行う。今回はCSSセレクタを使いたかったのでjQueryを使った。  
```
driver.execute_script("$('html > body > div.header > div.container > div.search-icon > form > div > button').click()")
```
