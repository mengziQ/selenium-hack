# PV(Page View)稼ぎ  
## PV数と訪問数  
google analyticsとかで見られるPV数は、ブラウザを開かないとカウントされないことが分かりました(今更)  
最初、getメソッドでアクセスするだけのものを書いてしまったらPVは増えませんでした。  

このプログラムではブラウザを開いたり閉じたりを繰り返しますが、こうすることによって「訪問数」も増えました。cookieで識別してるのでしょうか。  
なので、ブラウザを一度開いたまま更新しまくるとPV数は増えても訪問数は増えないのでは？という仮説。  

## 実装でつまったところ  
## invisibleな要素はseleniumのclickメソッドではクリックできない  
このエラーに泣かされた。  
```
selenium.common.exceptions.ElementNotVisibleException: Message: element not visible
```
ページがちょっとオサレ仕様で、検索フォーム用の虫眼鏡マークを押すとニョキッとフォームが出てくる動きになっていた。  
このとき、フォームが出てくる前の虫眼鏡とフォームが出てきてからの虫眼鏡が違う要素になっていて、しかも後者がinvisibleな要素だった。。  

**解決方法**  
send_scriptメソッドを使ってjavascriptでクリックを行う。  
今回はCSSセレクタを使いたかったのでjQueryを使った。  
```
driver.execute_script("$('html > body > div.header > div.container > div.search-icon > form > div > button').click()")
```
