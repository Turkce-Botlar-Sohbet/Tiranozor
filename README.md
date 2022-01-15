## URL-Yükleyici
---

Bağlantıları Yüklemek için Telegram Botu.

**Özellikleri**:

👉 [YTDL Desteklenen Bağlantıları](https://ytdl-org.github.io/youtube-dl/supportedsites.html) Telegram'a yükler

👉 HTTP/HTTPS'yi Dosya/Video olarak Telegram'a yükler

👉 ZippyShare, HxFile ve AnonFiles

👉 Mesaj yayınla, yasakla, yasağı kaldır, toplam kullanıcıları kontrol et

👉 Eğer Konfig'inizi config.py dosyasından almak istiyorsanız WEBHOOK değerini True olarak ayarlayın

👉 Her restart'ta tüm python paketleri güncellenir

#### Heroku'da çalıştırın

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### VPS'nizde çalıştırın

```sh
git clone https://github.com/Turkce-Botlar-Sohbet/URL-Yukleyici
cd URL-Yukleyici
pip3 install -r requirements.txt
# <config.py'yi uygun şekilde yapılandırın>
python3 bot.py

```
## Komutlar
Komut                   | Açıklama
----------------------- | ----------------------------------------    
`/broadcast`            | Kullanıcılara toplu olarak mesaj gönderme.
`/help`                 | Yardım komutu.     
`/genthumb`             | Thumbnail eklemek için bir fotoğrafa yanıtlayın.
`/delthumb`             | Thumbnail silmek için.
`/total`                | Veritabanında kayıtlı toplam kullanıcı sayısını verir.
`/ban`                  | Kullanıcıyı bottan yasaklamak için.
`/unban`                | Kullanıcının yasağını kaldırmak için.
`/banned_users`         | Yasaklı kullanıcı sayısını verir.

## Kredi ve Teşekkürler

* [X-URL-Uploader](https://github.com/X-Gorn/X-URL-Uploader/tree/database) için [@X-Gorn](https://t.me/xgorn)
* [TG-URL-Uploader](https://github.com/TGExplore/TG-URL-Uploader) için [@TGExplore](https://t.me/ViruZs)
* [AnyDLBot](https://telegram.dog/AnyDLBot) için [@SpEcHlDe](https://t.me/ThankTelegram)
* [Pyrogram Library](https://github.com/pyrogram/pyrogram) için [Dan Tès](https://t.me/haskell)
* [UploaditBot](https://telegram.dog/UploaditBot) için [Yoily](https://t.me/YoilyL)
* [database.py](https://github.com/AbirHasan2005/VideoCompress/blob/main/bot/database/database.py) için [@AbirHasan2005](https://t.me/AbirHasan2005)

## License
<a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
<img src="https://www.gnu.org/graphics/gplv3-127x51.png" alt="GNU GPLv3 Image">
</a>
<br>
URL-Yükleyici is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the 
  <a href="https://www.gnu.org/licenses/gpl.html">GNU General Public License</a> 
  as published by the Free Software Foundation, either version 3 of the License, 
  or (at your option) any later version.
