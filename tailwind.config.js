/** @type {import('tailwindcss').Config} */
module.exports = {
  // Skanowane pliki - Tailwind wygeneruje CSS tylko dla klas realnie uzytych w tych plikach
  content: ['./index.html'],
  theme: {
    extend: {
      // Kolory identyczne jak w dotychczasowej konfiguracji CDN (nie zmieniac bez potrzeby)
      colors: {
        beige: {
          50: '#fdfbf7',
          100: '#f8f4ee',
          200: '#f0e8dc',
          300: '#e6d7c3',
          400: '#d4c0a4',
          500: '#c4a87c',
          600: '#b39463',
          700: '#9d7e50',
        },
        rose: {
          50: '#fff5f5',
          100: '#ffe8e8',
          200: '#ffd1d1',
        },
      },
    },
  },
  plugins: [],
};
