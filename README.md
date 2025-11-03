# WowMakeup.pl 💄

Profesjonalna strona wizytówka dla WowMakeup - usługi makijażu mobilnego i kosmetologii.

## 🎨 O projekcie

Strona internetowa dla Karoliny Kowalewicz, profesjonalnej makijażystki i kosmetologa. Strona prezentuje ofertę makijażu mobilnego (ślubnego, okolicznościowego, kolorowego) oraz usług kosmetologicznych.

## 🚀 Technologie

- HTML5
- CSS3 (Tailwind CSS)
- JavaScript (Vanilla)
- Responsive Design
- SEO Optimized

## 📋 Funkcjonalności

- ✅ Responsywny design (mobile-first)
- ✅ Zoptymalizowana pod SEO
- ✅ Szybkie ładowanie strony
- ✅ Gallery portfolio z realizacjami
- ✅ Formularz kontaktowy
- ✅ Integracja z Google Analytics
- ✅ Schema.org structured data
- ✅ Open Graph meta tags
- ✅ Sitemap.xml i robots.txt
- ✅ PWA ready (site.webmanifest)

## 🌐 Hosting na GitHub Pages

### Krok 1: Push do repozytorium

```bash
git add .
git commit -m "Initial commit - wowmakeup.pl website"
git push origin main
```

### Krok 2: Włączenie GitHub Pages

1. Przejdź do ustawień repozytorium na GitHub
2. W sekcji "Pages" wybierz branch `main` i folder `/ (root)`
3. Kliknij "Save"
4. Strona będzie dostępna pod adresem: `https://[username].github.io/wowmakeup.pl`

### Krok 3: Konfiguracja domeny niestandardowej

1. W ustawieniach GitHub Pages dodaj domenę `wowmakeup.pl`
2. U swojego dostawcy domeny skonfiguruj rekordy DNS:
   - A record: `185.199.108.153`
   - A record: `185.199.109.153`
   - A record: `185.199.110.153`
   - A record: `185.199.111.153`
   - CNAME (www): `[username].github.io`

## 📊 Google Analytics

W pliku `index.html` zastąp `GA_MEASUREMENT_ID` swoim ID z Google Analytics:

```javascript
gtag('config', 'GA_MEASUREMENT_ID'); // Zamień na swój ID, np. 'G-XXXXXXXXXX'
```

### Jak uzyskać Google Analytics ID:

1. Przejdź na https://analytics.google.com
2. Utwórz nowe konto/właściwość dla wowmakeup.pl
3. Skopiuj Measurement ID (format: G-XXXXXXXXXX)
4. Wklej w dwóch miejscach w pliku index.html

## 🎨 Favicony

Obecnie w projekcie brakuje favicons. Aby je dodać:

1. Przejdź na https://realfavicongenerator.net/
2. Wgraj logo firmy (można stworzyć proste logo z literą "W")
3. Pobierz wygenerowane pliki
4. Umieść je w głównym katalogu projektu

Potrzebne pliki:
- `favicon.ico`
- `favicon-16x16.png`
- `favicon-32x32.png`
- `apple-touch-icon.png`
- `favicon-192x192.png`
- `favicon-512x512.png`

## 🖼️ Optymalizacja obrazów

Obrazy w folderze `assets/` są już w formacie WebP, co jest optymalne dla SEO. Jeśli chcesz dodatkowo zoptymalizować rozmiary:

### Opcja 1: Użyj online tools
- https://squoosh.app/
- https://tinypng.com/

### Opcja 2: Użyj narzędzi CLI (dla zaawansowanych)

Zainstaluj Sharp (Node.js):
```bash
npm install -g sharp-cli
```

Przekonwertuj i zmień rozmiar:
```bash
sharp -i assets/profilowe.webp -o assets/profilowe-500.webp resize 500
sharp -i assets/profilowe.webp -o assets/profilowe-800.webp resize 800
```

## 📱 Media społecznościowe

- Instagram: [@wowmakeup.kowalewicz](https://www.instagram.com/wowmakeup.kowalewicz)
- Facebook: [wowmakeupkowalewicz](https://www.facebook.com/wowmakeupkowalewicz)
- Email: kowalewicz.karolina1997@gmail.com

## 📝 Uwagi do dalszego rozwoju

1. **Favicony** - należy dodać zgodnie z sekcją powyżej
2. **Google Analytics ID** - należy zastąpić placeholder prawdziwym ID
3. **Optymalizacja obrazów** - opcjonalnie stworzyć wiele rozmiarów dla różnych urządzeń
4. **Blog** - w przyszłości można dodać sekcję z poradami makijażowymi
5. **Cennik** - gdy będzie gotowy, można dodać dedykowaną sekcję
6. **Opinie klientek** - sekcja z recenzjami i rekomendacjami

## 🔍 Checklist SEO

- ✅ Meta tags (title, description, keywords)
- ✅ Open Graph tags
- ✅ Twitter Card tags
- ✅ Canonical URL
- ✅ Schema.org structured data (BeautySalon)
- ✅ Semantic HTML5 tags
- ✅ Alt attributes dla wszystkich obrazów
- ✅ robots.txt
- ✅ sitemap.xml
- ✅ Responsive design
- ✅ Fast loading (Tailwind CDN)
- ✅ HTTPS ready
- ⏳ Favicons (do dodania)
- ⏳ Google Analytics (do skonfigurowania)

## 📄 Licencja

© 2025 WowMakeup - Karolina Kowalewicz. Wszelkie prawa zastrzeżone.
