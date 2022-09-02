# Python-Rfid-Flask
刷RFID之後驗證成功才亮LED燈且讓蜂鳴器發聲與顯示溫溼度感測值及時間在網頁上，並自動更新此溫溼度感測值及時間，且存於postgresql,mysql資料庫之中。


1.先將rfid、LED、蜂鳴器與溫度感測器分別接到Arduino

2.在arduino的程式中寫入，當rfid判斷到卡片後，先蜂鳴器先響，之後LED發亮，最後在取得溫濕度。

3.之後利用serial在python中取得溫濕度的值

4.最後用flask把溫濕度的直上傳到網頁中

