# pystartertemplate

Production-ready, modern ve öğretici bir FastAPI starter template.

Bu proje aşağıdaki hedeflerle hazırlanmıştır:

- strict typing
- temiz mimari
- yüksek kod kalitesi
- gelişime açık ama sade yapı

Amaç, yeni bir FastAPI projesine başlarken doğru kararları tekrar tekrar vermek zorunda kalmamaktır.

## İçindekiler

- Projenin Amacı
- Özellikler
- Mimari Yaklaşım
- Proje Yapısı
- Kurulum ve Çalıştırma
- Docker ve Docker Compose
- Konfigürasyon
- Testler
- API Endpoint Testleri
- Kod Kalitesi ve Standartlar
- Pre-commit
- Geliştirme Felsefesi
- Kimler İçin Uygun
- GitHub Template Kullanımı
- Lisans

## Projenin Amacı

Bu template, küçük projelerde sade kalabilen ancak büyüdüğünde doğal şekilde genişleyebilen bir FastAPI altyapısı sunar.

Overengineering yapılmaz, ancak production düşüncesi en baştan vardır.

## Özellikler

- FastAPI ile yüksek performanslı API
- Tek FastAPI uygulaması
- Service-based mimari
- Strict Mypy, Ruff ve Black
- Modern src layout
- GitHub Actions ile CI
- Pre-commit hook desteği
- Docker ve Docker Compose
- Typed pytest testleri
- Production farkındalığı olan logging
  
## Mimari Yaklaşım

Bu projede:

- Çoklu FastAPI app kullanılmaz
- Gereksiz katmanlar eklenmez
- Business logic servis katmanında yer alır
- API, service ve model katmanları ayrıdır

Akış şu şekildedir:

API → Service → Model

Bu yapı hem okunabilirliği hem de test edilebilirliği artırır.

## Proje Yapısı

```text
pystartertemplate/
├── src/
│   └── pystartertemplate/
│       ├── main.py
│       ├── api/
│       ├── services/
│       ├── models/
│       └── core/
│
├── tests/
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── Makefile
└── README.md
````

Docker Compose dosyası şu an tek servis içerir ancak ileride database, cache veya worker eklenmesine hazırdır.

## Kurulum ve Çalıştırma

### Sanal ortam oluşturma

```bash
python -m venv .venv
source .venv/bin/activate
```

### Geliştirme bağımlılıklarını kurma

```bash
make install-dev
```

### Uygulamayı çalıştırma

```bash
make run
```

Uygulama şu adreslerde erişilebilir olur:

- API root: [http://localhost:8000](http://localhost:8000)
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Docker ve Docker Compose

Docker Compose ile çalıştırmak için:

```bash
make up
```

Durdurmak için:

```bash
make down
```

Bu yapı şu an tek servis içerir ancak çoklu servisli mimariye geçişe hazırdır.

---

## Konfigürasyon

Konfigürasyon `pydantic-settings` ile yönetilir.

`.env` dosyasını oluşturmak için:

```bash
cp .env.example .env
```

Örnek `.env` içeriği:

```env
PROJECT_NAME=pystartertemplate
ENVIRONMENT=local
DEBUG=true
LOG_LEVEL=INFO
LOG_FILE_PATH=logs/app.log
```

## Testler

Bu projede tüm testler typed yazılır ve `mypy --strict` kurallarına tabidir.

Testleri çalıştırmak için:

```bash
make test
```

## API Endpoint Testleri

Makefile üzerinden curl yazmadan endpoint test edebilirsiniz:

```bash
make root
make health
make echo
make echo-invalid
```

Bu komutlar API kontratını hızlıca doğrulamak için tasarlanmıştır.

## Kod Kalitesi ve Standartlar

Kullanılan araçlar:

- Black: Kod formatlama
- Ruff: Lint ve import düzeni
- Mypy: Static type checking
- Pytest: Test runner
- Pre-commit: Commit öncesi kalite kapısı

Tüm kontrolleri tek komutta çalıştırmak için:

```bash
make test-all
```

## Pre-commit

Pre-commit hook’larını kurmak için:

```bash
pip install pre-commit
pre-commit install
```

Manuel çalıştırma:

```bash
pre-commit run --all-files
```

## Geliştirme Felsefesi

Bu template şu prensiplere dayanır:

- Sonra düzeltiriz yaklaşımı yoktur
- Hatalar yazarken yakalanır
- CI sürpriz yapmaz
- Okunabilirlik önceliklidir
- Production düşüncesi en baştan vardır

## Kimler İçin Uygun

- Junior geliştiriciler
- Mid-level geliştiriciler
- Senior geliştiriciler
- Ortak standartla başlamak isteyen ekipler

## GitHub Template Kullanımı

Bu repo GitHub üzerinde Template Repository olarak işaretlenmiştir.

Yeni bir proje başlatmak için:

1. GitHub’da Use this template butonuna tıklayın
2. Yeni repo adını belirleyin
3. Geliştirmeye başlayın

## Lisans

MIT License

## Son Not

Bu template’in amacı her şeyi eklemek değil, doğru ve sağlam bir zemin kurmaktır.

Üzerine güvenle ürün inşa edebilirsiniz.
