# CLAUDE.md — wowmakeup.pl

## ⚠️ WAŻNE — zawsze przed zakończeniem pracy nad stroną
Za każdym razem, gdy ruszasz cokolwiek w `index.html` (albo w stylach/klasach), MUSISZ:
1. **Jeśli zmieniałeś klasy Tailwinda** — przebudować CSS: `npm run build:css` (i zacommitować `tailwind.css`; GitHub Pages nie robi buildu, więc na produkcję idzie ten plik z repo).
2. **Zweryfikować lokalnie w prawdziwej przeglądarce**, że strona wygląda i działa — nie zakładaj „na oko". Ścieżki do lokalnych zasobów (CSS, favicony, manifest) są **względne**, więc do szybkiego podglądu wystarczy otworzyć `index.html` dwuklikiem (`file://`) — style się załadują (uwaga: Google Analytics nie odpali się pod `file://`, to normalne). Dla pełnej zgodności z produkcją użyj serwera: `npm run serve` lub `python -m http.server 8080 --bind 127.0.0.1` → `http://127.0.0.1:8080/`. Do automatycznej weryfikacji użyj Playwright (sprawdź: renderowanie, brak błędów w konsoli, brak odwołań do `cdn.tailwindcss.com`). **Nie zmieniaj lokalnych ścieżek z powrotem na absolutne (`/...`)** — psuje to `file://`; pełne URL-e `https://` (OG, `canonical`, Schema.org) zostają absolutne.
3. Po weryfikacji **posprzątać pliki tymczasowe** (zrzuty ekranu, `.playwright-mcp/`) i zatrzymać serwer.
Użytkownik lubi móc sam obejrzeć efekt lokalnie — gdy kończysz zmianę wizualną, zaproponuj/uruchom podgląd.

## Czym jest ten projekt
Statyczny **landing page (jedna strona)** usług makijażu mobilnego Karoliny Kowalewicz (WOW Makeup) — makijaż ślubny, okolicznościowy, kolorowy z dojazdem do klientki. Obszar: Starogard Gdański, Tczew, Skarszewy, Gdańsk i okolice.

## Stack i hosting
- **Czysty HTML** — cała strona to jeden plik `index.html` (~1330 linii): struktura, style `<style>` i JS `<script>` w jednym pliku.
- **Tailwind CSS skompilowany statycznie** — plik `tailwind.css` (~20 KB, zminifikowany) podłączony przez `<link>`. NIE używamy już CDN (`cdn.tailwindcss.com`) — było render-blocking i niezalecane produkcyjnie.
  - Źródło: `src/input.css` (dyrektywy `@tailwind`) + `tailwind.config.js` (motyw: kolory `beige`/`rose`, `content: ['./index.html']`).
  - **Regeneracja po zmianie klas Tailwind w `index.html`**: `npm install` (raz), potem `npm run build:css`. Podgląd na żywo: `npm run watch:css`.
  - `tailwind.css` JEST commitowany do repo (to on jedzie na produkcję — GitHub Pages nie robi buildu). `node_modules/` jest ignorowany.
  - Weryfikacja lokalna: `npm run serve` (albo `python -m http.server`) i otwórz `localhost`.
  - **Kolejność kaskady (WAŻNE)**: `<link>` do `tailwind.css` jest w `<head>` PRZED blokiem `<style>`, więc reguły w inline `<style>` (przy równej specyficzności) **nadpisują** Tailwinda. Uwaga na klasy o tych samych nazwach co utility Tailwinda: NIE definiuj w `<style>` reguł jak `.container`, `.grid`, `.bg-white` w sposób kolidujący z Tailwindem (poprzednio `.container { max-width: 100% }` rozciągał nagłówek/stopkę na pełną szerokość — usunięte). Przy CDN było odwrotnie (Tailwind ładowany na końcu), więc taki kod bywał „martwy" i ożywa po przejściu na statyczny plik.
- **Font**: Montserrat z Google Fonts (`@import` w `<style>`).
- **Hosting**: GitHub Pages + custom domena (`CNAME` → `wowmakeup.pl`), `.nojekyll`.
- **Deploy**: commit i push na `master`. Pamiętaj, by najpierw przebudować `tailwind.css`, jeśli zmieniałeś klasy.
- Analytics: Google Analytics 4 (`G-4H3QQHY4KH`).

## Struktura sekcji `index.html`
Nawigacja → Hero (`#home`) → Obszar działania → O mnie (`#about`) → Usługi (`#services`) → Cennik (`#pricing`) → Portfolio (`#portfolio`) → Kontakt (`#contact`) → Stopka.

## Ważne miejsca do edycji
- **Ceny usług**: sekcja Cennik (`#pricing`) — karty z cenami + duplikat w Schema.org JSON-LD (`hasOfferCatalog`) w `<head>`. **Przy zmianie ceny trzeba zaktualizować OBA miejsca.**
- **Cena dojazdu**: sekcja „Informacje dodatkowe" w cenniku (blok „Dojazd gratis").
- **Obrazy**: `assets/` — WebP w 4 rozmiarach (`-small`/`-medium`/`-large` + oryginał) z `srcset`. Skrypt `optimize_images.py` do generowania rozmiarów.
- **Meta/SEO**: `<head>` — meta tags, Open Graph, Twitter Card, Schema.org, `geo.*`.
- **Kontakt**: formularz wysyła zgłoszenia przez **FormSubmit** (`https://formsubmit.co/ajax/kowalewicz.karolina1997@gmail.com`) – fetch/AJAX bez przeładowania, handler w `<script>` na dole `index.html`. Mail do Karoliny: polskie etykiety, dynamiczny temat, Reply-To z pola `email` (klik „Odpowiedz" pisze do klientki), widoczna kopia `_cc` na `kowalewicz.pawel@gmail.com`, honeypot `_honey`. Brak numeru telefonu na stronie.
  - **Uwaga – pole `email`**: musi nazywać się dokładnie `email` (z niego FormSubmit robi Reply-To). Zmiana nazwy psuje odpowiadanie.
  - **Uwaga – aktywacja per DOMENA**: FormSubmit aktywuje formularz osobno dla każdego origin. Pierwsze zgłoszenie z nowej domeny (np. produkcja `wowmakeup.pl` po testach z localhost) wysyła NOWY mail aktywacyjny na skrzynkę Karoliny – trzeba kliknąć link „Activate Form", inaczej wysyłka zwraca błąd.
  - **Uwaga – testowanie**: formularz robi `fetch` do zewnętrznego serwera, więc NIE działa spod `file://` (dwuklik `index.html`) – testuj przez serwer lokalny lub na produkcji.

## Konwencje
- Język treści: **polski**, pełna poprawność ortograficzna (diakrytyki).
- Nazwy plików obrazów bywają z polskimi znakami (np. `ślubny1.webp`).
- Marka pisana jako „WOW Makeup" (uwaga: miejscami w meta pojawia się „WowMakeup" — niespójność).

## Pliki pomocnicze
- `SEO_CHECKLIST.md` — pełna checklista SEO (co zrobione, co do zrobienia po wdrożeniu).
- `README.md` — opis projektu.
- `sitemap.xml`, `robots.txt` — dla botów.
